from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class LibraryItemResource:
    """``client.library_item`` (10 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def create(
        self,
        org_id: str,
        library_id: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        preset: Union[Optional[str], NotGiven] = NOT_GIVEN,
        sections: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[LibraryItemCreateParamsContent, NotGiven] = NOT_GIVEN,
        params: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryItemCreateResponse:
        """Create an item in an organization

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/items``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/items",
            query=_query({}, extra_query),
            body=_body({"title": title, "slug": slug, "preset": preset, "sections": sections, "body": body, "content": content, "params": params}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def lookup(
        self,
        org_id: str,
        library_id: str,
        *,
        keys: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryItemLookupResponse:
        """Create the lookup in an organization

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/items/lookup``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/items/lookup",
            query=_query({}, extra_query),
            body=_body({"keys": keys}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def read(
        self,
        org_id: str,
        library_id: str,
        item_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the item (content libraries)

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/items/{itemId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/items/{_path(item_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def patch(
        self,
        org_id: str,
        library_id: str,
        item_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        params: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryItemPatchResponse:
        """Update the item (content libraries)

        ``PATCH /orgs/{orgId}/content/libraries/{libraryId}/items/{itemId}``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/items/{_path(item_id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "slug": slug, "params": params}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        library_id: str,
        item_id: str,
        *,
        force: Union[str, NotGiven] = NOT_GIVEN,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryItemRemoveResponse:
        """Delete the item (content libraries)

        ``DELETE /orgs/{orgId}/content/libraries/{libraryId}/items/{itemId}``

        :param force: Delete even though other entries reference this one.
        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/items/{_path(item_id)}",
            query=_query({"force": force}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def fields(
        self,
        org_id: str,
        library_id: str,
        item_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryItemFieldsResponse:
        """List fields in an organization (items)

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/items/{itemId}/fields``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/items/{_path(item_id)}/fields",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_fields(
        self,
        org_id: str,
        library_id: str,
        item_id: str,
        *,
        fields: Dict[str, Any],
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryItemSetFieldsResponse:
        """Update fields in an organization (items)

        ``PATCH /orgs/{orgId}/content/libraries/{libraryId}/items/{itemId}/fields``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/items/{_path(item_id)}/fields",
            query=_query({}, extra_query),
            body=_body({"fields": fields}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def publish(
        self,
        org_id: str,
        library_id: str,
        item_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryItemPublishResponse:
        """Publish the item (content libraries)

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/items/{itemId}/publish``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/items/{_path(item_id)}/publish",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def trash(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryItemTrashResponse:
        """List trash libraries in an organization

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/trash``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/trash",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def trash_all(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``trash`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/trash",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def restore(
        self,
        org_id: str,
        library_id: str,
        item_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryItemRestoreResponse:
        """Restore the trash

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/trash/{itemId}/restore``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/trash/{_path(item_id)}/restore",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
