import json
import random
import time
from typing import Any, Dict, Iterator, List, Mapping, Optional
from urllib.parse import quote

import requests

__version__ = "1.1.0"

# Named environments -> base URL. Pass environment="name" to the client.
ENVIRONMENTS: Dict[str, str] = {}

# Sent on every request. A library's default User-Agent (python-requests/…) is
# exactly what edge firewalls challenge, so a first call would fail with an
# HTML block page instead of JSON; an identifying UA passes.
USER_AGENT = "forumulate-sdk-python/1.1.0"
DEFAULT_HEADERS: Dict[str, str] = {"Forumulate-Version":"2026-11-01"}


class NotGiven:
    """Marks an argument the caller did not pass (distinct from passing None)."""

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()


class ForumulateError(Exception):
    """Base class for every error this SDK raises."""


class APIConnectionError(ForumulateError):
    """The request never got an HTTP answer (DNS, refused, reset, TLS)."""


class APITimeoutError(APIConnectionError):
    """The request timed out."""


class APIStatusError(ForumulateError):
    """The API answered with a 4xx/5xx status.

    ``status`` is the HTTP status, ``code`` the API's machine-readable error code
    (when it sent one), ``message`` its human-readable message, ``body`` the
    decoded response and ``request_id`` the id to quote to support.
    """

    def __init__(self, status: int, body: Any, headers: Mapping[str, str]):
        err = body.get("error") if isinstance(body, dict) else None
        if not isinstance(err, dict):
            err = body if isinstance(body, dict) else {}
        self.status = status
        self.status_code = status
        self.code: Optional[str] = err.get("code") if isinstance(err.get("code"), str) else None
        msg = err.get("message")
        self.message: str = msg if isinstance(msg, str) else "HTTP %d" % status
        self.body = body
        self.headers = dict(headers)
        rid = body.get("requestId") if isinstance(body, dict) else None
        self.request_id: Optional[str] = rid or headers.get("x-request-id")
        super().__init__("%d %s: %s" % (status, self.code or "error", self.message))


# Backwards-friendly alias: the flat clients call it ApiError.
ApiError = APIStatusError


class BadRequestError(APIStatusError):
    """400: the request was malformed."""


class AuthenticationError(APIStatusError):
    """401: no credential, or the credential is not valid."""


class PermissionDeniedError(APIStatusError):
    """403: authenticated, but not allowed to do this."""


class NotFoundError(APIStatusError):
    """404: no such resource (or not one you can see)."""


class ConflictError(APIStatusError):
    """409: the request conflicts with the current state."""


class UnprocessableEntityError(APIStatusError):
    """422: the request was well-formed but semantically invalid."""


class RateLimitError(APIStatusError):
    """429: too many requests; retried automatically before this is raised."""


class InternalServerError(APIStatusError):
    """5xx: the server failed; retried automatically before this is raised."""


_STATUS_ERRORS = {
    400: BadRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    422: UnprocessableEntityError,
    429: RateLimitError,
}


def _error_for(status: int, body: Any, headers: Mapping[str, str]) -> APIStatusError:
    cls = _STATUS_ERRORS.get(status) or (InternalServerError if status >= 500 else APIStatusError)
    return cls(status, body, headers)


def _path(value: Any) -> str:
    """Encode one path segment, so an id with a '/' or '?' cannot change the route."""
    return quote(str(value), safe="")


def _wire(value: Any) -> Any:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (list, tuple)):
        return [_wire(v) for v in value]
    return value


def _query(params: Dict[str, Any], extra: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
    out = {k: _wire(v) for k, v in params.items() if v is not NOT_GIVEN and v is not None}
    if extra:
        out.update({k: _wire(v) for k, v in extra.items()})
    return out


def _body(fields: Dict[str, Any], extra: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
    out = {k: v for k, v in fields.items() if v is not NOT_GIVEN}
    if extra:
        out.update(extra)
    return out


def _base_url_from_env(env: Mapping[str, str]) -> str:
    """Resolve the API base the way every other Forumulate tool does."""
    api = (env.get("FORUMULATE_API_URL") or "").strip().rstrip("/")
    if api:
        return api
    site = (env.get("FORUMULATE_URL") or "").strip().rstrip("/") or "https://forumulate.com"
    suffix = "/api"
    if suffix and not site.lower().endswith(suffix.lower()):
        return site + suffix
    return site


def _token_from_env(env: Mapping[str, str]) -> Optional[str]:
    return (env.get("FORUMULATE_TOKEN") or "").strip() or None


def _cursor_of(page: Any) -> Optional[str]:
    """The next-page cursor, wherever the API put it (top level or in an envelope)."""
    if not isinstance(page, dict):
        return None
    for holder in (page, page.get("page"), page.get("pagination"), page.get("pageInfo"), page.get("meta")):
        if not isinstance(holder, dict):
            continue
        if holder.get("hasMore") is False or holder.get("hasNextPage") is False:
            return None
        for key in ("nextCursor", "endCursor", "next_cursor", "cursor"):
            value = holder.get(key)
            if isinstance(value, str) and value:
                return value
    return None


def _items_of(page: Any, key: Optional[str]) -> List[Any]:
    if isinstance(page, list):
        return page
    if not isinstance(page, dict):
        return []
    if key and isinstance(page.get(key), list):
        return page[key]
    for k in ("items", "data", "results"):
        if isinstance(page.get(k), list):
            return page[k]
    # The API names a list after what it holds ({"spaces": [...]}): take the one list.
    lists = [v for v in page.values() if isinstance(v, list)]
    return lists[0] if len(lists) == 1 else []


class BaseClient:
    """HTTP transport shared by every resource: auth, retries, errors, paging."""

    def __init__(
        self,
        *,
        base_url: str,
        token: Optional[str],
        timeout: float,
        max_retries: int,
        default_headers: Optional[Mapping[str, str]],
        http_session: Optional[requests.Session],
    ):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout
        self.max_retries = max_retries
        self.default_headers: Dict[str, str] = {"User-Agent": USER_AGENT, **DEFAULT_HEADERS, **(default_headers or {})}
        # One pooled session for every call; close() (or a with-block) releases it.
        self._session = http_session or requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False

    def close(self) -> None:
        """Close the underlying HTTP session and release pooled connections."""
        self._session.close()

    def _headers(self, extra: Optional[Mapping[str, Any]]) -> Dict[str, str]:
        headers = {"Accept": "application/json", **self.default_headers}
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        for k, v in (extra or {}).items():
            if v is not NOT_GIVEN and v is not None:
                headers[k] = str(v)
        return headers

    def _send(self, method: str, path: str, query, body, headers, timeout, stream: bool = False) -> requests.Response:
        url = self.base_url + path
        h = self._headers(headers)
        data = None
        if body is not None and body is not NOT_GIVEN:
            h["Content-Type"] = "application/json"
            data = json.dumps(body)
        attempt = 0
        while True:
            try:
                res = self._session.request(
                    method, url, params=query or None, data=data, headers=h,
                    timeout=timeout if timeout is not None else self.timeout, stream=stream,
                )
            except requests.Timeout as e:
                if attempt < self.max_retries:
                    attempt += 1
                    time.sleep(min(0.5 * 2 ** attempt, 8))
                    continue
                raise APITimeoutError(str(e)) from e
            except requests.RequestException as e:
                if attempt < self.max_retries:
                    attempt += 1
                    time.sleep(min(0.5 * 2 ** attempt, 8))
                    continue
                raise APIConnectionError(str(e)) from e
            # Retry rate limits and transient server errors, honouring Retry-After.
            if (res.status_code == 429 or res.status_code >= 500) and attempt < self.max_retries:
                ra = res.headers.get("Retry-After")
                delay = float(ra) if ra and ra.isdigit() else min(0.5 * 2 ** attempt, 8) + random.random() * 0.25
                res.close()
                time.sleep(delay)
                attempt += 1
                continue
            if res.status_code >= 400:
                try:
                    payload: Any = res.json()
                except ValueError:
                    payload = res.text
                raise _error_for(res.status_code, payload, res.headers)
            return res

    def _request(self, method: str, path: str, *, query=None, body=None, headers=None, timeout=None) -> Any:
        res = self._send(method, path, query, body, headers, timeout)
        if not res.content:
            return None
        if "json" in res.headers.get("Content-Type", ""):
            return res.json()
        return res.text

    def _paginate(self, method: str, path: str, *, query=None, page_param: str = "cursor", items_key=None, headers=None, timeout=None) -> Iterator[Any]:
        q = dict(query or {})
        while True:
            page = self._request(method, path, query=q, headers=headers, timeout=timeout)
            items = _items_of(page, items_key)
            for item in items:
                yield item
            if page_param in ("page", "offset"):
                if not items:
                    return
                q[page_param] = int(q.get(page_param) or (1 if page_param == "page" else 0)) + (1 if page_param == "page" else len(items))
                continue
            cursor = _cursor_of(page)
            if not cursor or not items:
                return
            q[page_param] = cursor

    def _stream(self, method: str, path: str, *, query=None, body=None, headers=None, timeout=None) -> Iterator[Any]:
        h = dict(headers or {})
        h["Accept"] = "text/event-stream"
        res = self._send(method, path, query, body, h, timeout, stream=True)
        data_lines: List[str] = []
        try:
            for line in res.iter_lines(decode_unicode=True):
                if not line:
                    if data_lines:
                        data = "\n".join(data_lines)
                        data_lines = []
                        try:
                            yield json.loads(data)
                        except ValueError:
                            yield data
                    continue
                if line.startswith("data:"):
                    data_lines.append(line[5:].strip())
        finally:
            res.close()


__all__ = [
    "NOT_GIVEN", "NotGiven", "ENVIRONMENTS", "USER_AGENT",
    "ForumulateError", "APIConnectionError", "APITimeoutError", "APIStatusError", "ApiError",
    "BadRequestError", "AuthenticationError", "PermissionDeniedError", "NotFoundError",
    "ConflictError", "UnprocessableEntityError", "RateLimitError", "InternalServerError",
]
