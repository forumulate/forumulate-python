from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class PreviewExchangeResource:
    """``client.preview_exchange`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def exchange(
        self,
        *,
        token: str,
        path: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        library: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Exchange a single-use preview token for a draft-reading credential

        ``POST /delivery/v1/preview/exchange``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/delivery/v1/preview/exchange",
            query=_query({}, extra_query),
            body=_body({"token": token, "path": path, "library": library}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
