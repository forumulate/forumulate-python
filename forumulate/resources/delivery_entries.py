from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class DeliveryEntriesResource:
    """``client.delivery_entries`` (15 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def types0(
        self,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesTypes0Response:
        """List the content types (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/types``
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/types",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def types1(
        self,
        key_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesTypes1Response:
        """List the content types (k)

        ``GET /delivery/v1/k/{keyId}/types``
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/types",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list0(
        self,
        library_id: str,
        type: str,
        *,
        where: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        count: Union[bool, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesList0Response:
        """List entries of a content type (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/types/{type}/entries``

        :param where: `{field: {operator: value}}` with `and`/`or` lists, as JSON or bracket-encoded (`where[price][gt]=10`).
        :param sort: Comma-separated field paths, `-` first for descending.
        :param limit: Entries per window, 1–100 (default 20; above 100 is capped).
        :param cursor: `page.nextCursor` from the previous window.
        :param count: Ask for `page.total`; sent only where counting is cheap.
        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/types/{_path(type)}/entries",
            query=_query({"where": where, "sort": sort, "limit": limit, "cursor": cursor, "count": count, "locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list0_all(
        self,
        library_id: str,
        type: str,
        *,
        where: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        count: Union[bool, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[DeliveryEntriesList0ResponseDataItem]:
        """Iterate every item of ``list0`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/types/{_path(type)}/entries",
            query=_query({"where": where, "sort": sort, "limit": limit, "count": count, "locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="data",
        )

    def list1(
        self,
        key_id: str,
        type: str,
        *,
        where: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        count: Union[bool, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesList1Response:
        """List entries of a content type (k)

        ``GET /delivery/v1/k/{keyId}/types/{type}/entries``

        :param where: `{field: {operator: value}}` with `and`/`or` lists, as JSON or bracket-encoded (`where[price][gt]=10`).
        :param sort: Comma-separated field paths, `-` first for descending.
        :param limit: Entries per window, 1–100 (default 20; above 100 is capped).
        :param cursor: `page.nextCursor` from the previous window.
        :param count: Ask for `page.total`; sent only where counting is cheap.
        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/types/{_path(type)}/entries",
            query=_query({"where": where, "sort": sort, "limit": limit, "cursor": cursor, "count": count, "locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list1_all(
        self,
        key_id: str,
        type: str,
        *,
        where: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        count: Union[bool, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[DeliveryEntriesList1ResponseDataItem]:
        """Iterate every item of ``list1`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/types/{_path(type)}/entries",
            query=_query({"where": where, "sort": sort, "limit": limit, "count": count, "locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="data",
        )

    def query0(
        self,
        library_id: str,
        type: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        where: Union[Any, NotGiven] = NOT_GIVEN,
        sort: Union[Any, NotGiven] = NOT_GIVEN,
        body_select: Union[Any, NotGiven] = NOT_GIVEN,
        limit: Union[Any, NotGiven] = NOT_GIVEN,
        cursor: Union[Any, NotGiven] = NOT_GIVEN,
        count: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesQuery0Response:
        """Query entries of a content type (libraries)

        ``POST /delivery/v1/libraries/{libraryId}/types/{type}/entries/query``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/delivery/v1/libraries/{_path(library_id)}/types/{_path(type)}/entries/query",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            body=_body({"where": where, "sort": sort, "select": body_select, "limit": limit, "cursor": cursor, "count": count}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def query1(
        self,
        key_id: str,
        type: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        where: Union[Any, NotGiven] = NOT_GIVEN,
        sort: Union[Any, NotGiven] = NOT_GIVEN,
        body_select: Union[Any, NotGiven] = NOT_GIVEN,
        limit: Union[Any, NotGiven] = NOT_GIVEN,
        cursor: Union[Any, NotGiven] = NOT_GIVEN,
        count: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesQuery1Response:
        """Query entries of a content type (k)

        ``POST /delivery/v1/k/{keyId}/types/{type}/entries/query``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/delivery/v1/k/{_path(key_id)}/types/{_path(type)}/entries/query",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            body=_body({"where": where, "sort": sort, "select": body_select, "limit": limit, "cursor": cursor, "count": count}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def one0(
        self,
        library_id: str,
        type: str,
        id_or_slug: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesOne0Response:
        """Read one entry (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/types/{type}/entries/{idOrSlug}``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/types/{_path(type)}/entries/{_path(id_or_slug)}",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def one1(
        self,
        key_id: str,
        type: str,
        id_or_slug: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesOne1Response:
        """Read one entry (k)

        ``GET /delivery/v1/k/{keyId}/types/{type}/entries/{idOrSlug}``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/types/{_path(type)}/entries/{_path(id_or_slug)}",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def resolve(
        self,
        library_id: str,
        type: str,
        id: str,
        *,
        fields: Dict[str, Any],
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesResolveResponse:
        """Resolve an unsaved draft

        ``POST /delivery/v1/libraries/{libraryId}/types/{type}/entries/{id}/resolve``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/delivery/v1/libraries/{_path(library_id)}/types/{_path(type)}/entries/{_path(id)}/resolve",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            body=_body({"fields": fields}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def global0(
        self,
        library_id: str,
        key: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesGlobal0Response:
        """Read a global (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/globals/{key}``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/globals/{_path(key)}",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def global1(
        self,
        key_id: str,
        key: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[bool, NotGiven] = NOT_GIVEN,
        depth: Union[int, NotGiven] = NOT_GIVEN,
        populate: Union[str, NotGiven] = NOT_GIVEN,
        select: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryEntriesGlobal1Response:
        """Read a global (k)

        ``GET /delivery/v1/k/{keyId}/globals/{key}``

        :param locale: A locale code (the library’s source locale when omitted).
        :param fallback: Fall back through the declared locale chain, then the source (default `true`).
        :param depth: How far references are populated: 0 serves stubs `{kind, id, contentType, slug}`.
        :param populate: Per type, the fields to keep on a populated entry: `populate[author]=name,avatar`.
        :param select: Comma-separated field paths to keep in `fields`.
        :param draft: Accepted for a preview key, which always reads drafts; a delivery key asking for drafts is a 403.
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/globals/{_path(key)}",
            query=_query({"locale": locale, "fallback": fallback, "depth": depth, "populate": populate, "select": select, "draft": draft}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def schema0(
        self,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read the library’s JSON Schema (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/schema.json``
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/schema.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def schema1(
        self,
        key_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read the library’s JSON Schema (k)

        ``GET /delivery/v1/k/{keyId}/schema.json``
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/schema.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def openapi0(
        self,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read the library’s OpenAPI document (libraries)

        ``GET /delivery/v1/libraries/{libraryId}/openapi.json``
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/openapi.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def openapi1(
        self,
        key_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read the library’s OpenAPI document (k)

        ``GET /delivery/v1/k/{keyId}/openapi.json``
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/openapi.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
