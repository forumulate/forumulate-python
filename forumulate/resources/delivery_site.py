from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class DeliverySiteResource:
    """``client.delivery_site`` (10 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def routes0(
        self,
        library_id: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteRoutes0Response:
        """List routes (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/routes``

        :param locale: A locale code (the source locale when omitted).
        :param cursor: `page.nextCursor` from the previous window.
        :param limit: Routes per window, 1–100 (default 20).
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/routes",
            query=_query({"locale": locale, "cursor": cursor, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def routes0_all(
        self,
        library_id: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[DeliverySiteRoutes0ResponseDataItem]:
        """Iterate every item of ``routes0`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/routes",
            query=_query({"locale": locale, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="data",
        )

    def routes1(
        self,
        key_id: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteRoutes1Response:
        """List routes (k)

        ``GET /delivery/v1/k/{keyId}/routes``

        :param locale: A locale code (the source locale when omitted).
        :param cursor: `page.nextCursor` from the previous window.
        :param limit: Routes per window, 1–100 (default 20).
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/routes",
            query=_query({"locale": locale, "cursor": cursor, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def routes1_all(
        self,
        key_id: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[DeliverySiteRoutes1ResponseDataItem]:
        """Iterate every item of ``routes1`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/routes",
            query=_query({"locale": locale, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="data",
        )

    def resolve0(
        self,
        library_id: str,
        *,
        path: str,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteResolve0Response:
        """Resolve a site path (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/routes/resolve``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        :param path: The site path, e.g.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/routes/resolve",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft, "path": path}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def resolve1(
        self,
        key_id: str,
        *,
        path: str,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteResolve1Response:
        """Resolve a site path (k)

        ``GET /delivery/v1/k/{keyId}/routes/resolve``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        :param path: The site path, e.g.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/routes/resolve",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft, "path": path}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def redirects0(
        self,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteRedirects0Response:
        """List redirects (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/redirects``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/redirects",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def redirects0_all(
        self,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``redirects0`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/redirects",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def redirects1(
        self,
        key_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteRedirects1Response:
        """List redirects (k)

        ``GET /delivery/v1/k/{keyId}/redirects``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/redirects",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def redirects1_all(
        self,
        key_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``redirects1`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/redirects",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def sitemap0(
        self,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteSitemap0Response:
        """Read the sitemap (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/sitemap.json``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/sitemap.json",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def sitemap0_all(
        self,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``sitemap0`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/sitemap.json",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def sitemap1(
        self,
        key_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteSitemap1Response:
        """Read the sitemap (k)

        ``GET /delivery/v1/k/{keyId}/sitemap.json``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/sitemap.json",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def sitemap1_all(
        self,
        key_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``sitemap1`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/sitemap.json",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def search0(
        self,
        library_id: str,
        *,
        q: str,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteSearch0Response:
        """Search entries (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/search``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        :param cursor: `page.nextCursor` from the previous window of the same search.
        :param limit: Hits per window, 1–100 (default 20).
        :param type: Comma-separated content types to search (default: every type with searchable fields).
        :param q: The text to search for (2–200 characters).
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/search",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft, "cursor": cursor, "limit": limit, "type": type, "q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def search0_all(
        self,
        library_id: str,
        *,
        q: str,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[DeliverySiteSearch0ResponseDataItem]:
        """Iterate every item of ``search0`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/search",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft, "limit": limit, "type": type, "q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="data",
        )

    def search1(
        self,
        key_id: str,
        *,
        q: str,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliverySiteSearch1Response:
        """Search entries (k)

        ``GET /delivery/v1/k/{keyId}/search``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        :param cursor: `page.nextCursor` from the previous window of the same search.
        :param limit: Hits per window, 1–100 (default 20).
        :param type: Comma-separated content types to search (default: every type with searchable fields).
        :param q: The text to search for (2–200 characters).
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/search",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft, "cursor": cursor, "limit": limit, "type": type, "q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def search1_all(
        self,
        key_id: str,
        *,
        q: str,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[DeliverySiteSearch1ResponseDataItem]:
        """Iterate every item of ``search1`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/search",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft, "limit": limit, "type": type, "q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="data",
        )
