from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class TokensResource:
    """``client.tokens`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PatListDto:
        """List personal access tokens

        ``GET /pats``

        :param limit: Tokens per page, newest first.
        """
        return self._client._request(
            "GET",
            f"/pats",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/pats",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        *,
        name: str,
        scopes: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        expires_in_days: Union[int, NotGiven] = NOT_GIVEN,
        space_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        capabilities: Union[List[str], NotGiven] = NOT_GIVEN,
        scope_grants: Union[List[str], NotGiven] = NOT_GIVEN,
        constraints: Union[Any, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a personal access token

        ``POST /pats``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/pats",
            query=_query({}, extra_query),
            body=_body({"name": name, "scopes": scopes, "expiresInDays": expires_in_days, "spaceIds": space_ids, "capabilities": capabilities, "scopeGrants": scope_grants, "constraints": constraints}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def scopes(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PatScopeCatalogDto:
        """List scopes

        ``GET /pats/scopes``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/pats/scopes",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def scopes_all(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``scopes`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/pats/scopes",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def rename(
        self,
        id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Rename a token

        ``PATCH /pats/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/pats/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"name": name}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke(
        self,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> TokensRevokeResponse:
        """Delete the personal access token

        ``DELETE /pats/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/pats/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rotate(
        self,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        grace_minutes: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Rotate the personal access token

        ``POST /pats/{id}/rotate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/pats/{_path(id)}/rotate",
            query=_query({}, extra_query),
            body=_body({"graceMinutes": grace_minutes}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
