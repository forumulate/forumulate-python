from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class IconsResource:
    """``client.icons`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        *,
        for_: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IconsListResponse:
        """List icons

        ``GET /icons``
        """
        return self._client._request(
            "GET",
            f"/icons",
            query=_query({"for": for_}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
