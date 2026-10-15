from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SectionLibraryResource:
    """``client.section_library`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        *,
        family: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SectionLibraryListResponse:
        """Get the section library

        ``GET /section-library``
        """
        return self._client._request(
            "GET",
            f"/section-library",
            query=_query({"family": family}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def one(
        self,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SectionLibraryOneResponse:
        """Get one entry of the section library

        ``GET /section-library/{id}``
        """
        return self._client._request(
            "GET",
            f"/section-library/{_path(id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
