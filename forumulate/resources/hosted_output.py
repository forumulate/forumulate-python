from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class HostedOutputResource:
    """``client.hosted_output`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def resolve(
        self,
        org_id: str,
        library_id: str,
        *,
        path: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> HostedOutputResolveResponse:
        """Resolve a hosted-output path

        ``GET /public/content/{orgId}/libraries/{libraryId}/hosted/resolve``

        :param path: The hosted path below the library, e.g.
        """
        return self._client._request(
            "GET",
            f"/public/content/{_path(org_id)}/libraries/{_path(library_id)}/hosted/resolve",
            query=_query({"path": path}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def sitemap(
        self,
        org_id: str,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> HostedSitemap:
        """Read a hosted site’s sitemap

        ``GET /public/content/{orgId}/libraries/{libraryId}/hosted/sitemap``
        """
        return self._client._request(
            "GET",
            f"/public/content/{_path(org_id)}/libraries/{_path(library_id)}/hosted/sitemap",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
