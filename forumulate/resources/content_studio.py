from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ContentStudioResource:
    """``client.content_studio`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def types(
        self,
        org_id: str,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StudioModel:
        """Read the library's content types, resolved

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/types``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/types",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        library_id: str,
        type: str,
        *,
        where: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        count: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StudioEntryListBody:
        """List a content type’s entries for the studio

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/types/{type}/entries``

        :param where: `{field: {operator: value}}` with `and`/`or` lists, as JSON or bracket-encoded (`where[price][gt]=10`).
        :param sort: Comma-separated field paths, `-` first for descending.
        :param limit: Entries per window, 1–100 (default 20; above 100 is capped).
        :param cursor: `page.nextCursor` from the previous window.
        :param count: Ask for `page.total`; sent only where counting is cheap.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/types/{_path(type)}/entries",
            query=_query({"where": where, "sort": sort, "limit": limit, "cursor": cursor, "count": count}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        library_id: str,
        type: str,
        *,
        where: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        count: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[StudioEntryRow]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/types/{_path(type)}/entries",
            query=_query({"where": where, "sort": sort, "limit": limit, "count": count}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="data",
        )

    def run_bulk(
        self,
        org_id: str,
        library_id: str,
        *,
        action: str,
        entry_ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        overwrite: Union[bool, NotGiven] = NOT_GIVEN,
        force: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Publish, unpublish, delete or copy many entries

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/bulk``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/bulk",
            query=_query({}, extra_query),
            body=_body({"action": action, "entryIds": entry_ids, "locale": locale, "overwrite": overwrite, "force": force}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
