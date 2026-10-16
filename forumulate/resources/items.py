from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ItemsResource:
    """``client.items`` (13 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        updated_since: Union[str, NotGiven] = NOT_GIVEN,
        include_deleted: Union[str, NotGiven] = NOT_GIVEN,
        include: Union[List[str], NotGiven] = NOT_GIVEN,
        fields: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemPageDto:
        """List items in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/items``

        :param limit: Rows per page.
        :param cursor: The `page.next_cursor` of the previous response.
        :param updated_since: Only pieces changed after this instant.
        :param include_deleted: Carry tombstones (`deleted: true`) for pieces removed in the last 30 days, so a removal is discoverable without a full list.
        :param include: Comma-separated relations to fold in: `sections` (markdown per named slot) and `body` (the whole piece as markdown).
        :param fields: Comma-separated fields to return; everything else is left out.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items",
            query=_query({"limit": limit, "cursor": cursor, "updated_since": updated_since, "include_deleted": include_deleted, "include": include, "fields": fields}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        updated_since: Union[str, NotGiven] = NOT_GIVEN,
        include_deleted: Union[str, NotGiven] = NOT_GIVEN,
        include: Union[List[str], NotGiven] = NOT_GIVEN,
        fields: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items",
            query=_query({"limit": limit, "updated_since": updated_since, "include_deleted": include_deleted, "include": include, "fields": fields}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        preset: Union[Optional[str], NotGiven] = NOT_GIVEN,
        sections: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ItemsCreateParamsContent, NotGiven] = NOT_GIVEN,
        params: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsCreateResponse:
        """Create an item in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/items``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items",
            query=_query({}, extra_query),
            body=_body({"title": title, "slug": slug, "preset": preset, "sections": sections, "body": body, "content": content, "params": params}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def read(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the item (spaces)

        ``GET /orgs/{orgId}/spaces/{spaceId}/items/{itemId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def patch(
        self,
        org_id: str,
        space_id: str,
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
    ) -> ItemsPatchResponse:
        """Update the item (spaces)

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/items/{itemId}``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "slug": slug, "params": params}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsRemoveResponse:
        """Delete the item (spaces)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/items/{itemId}``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_content(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsGetContentResponse:
        """Get the content in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/content``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/content",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def put_content(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ItemsPutContentParamsContent, NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsPutContentResponse:
        """Replace the content in a space (items)

        ``PUT /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/content``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/content",
            query=_query({}, extra_query),
            body=_body({"content": content, "body": body}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def chunks(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsChunksResponse:
        """List chunks in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/chunks``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/chunks",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def verify(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsVerifyResponse:
        """Verify the item

        ``POST /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/verify``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/verify",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def publish(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsPublishResponse:
        """Publish the item (spaces)

        ``POST /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/publish``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/publish",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def fields(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsFieldsResponse:
        """List fields in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/fields``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/fields",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_fields(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        fields: Dict[str, Any],
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsSetFieldsResponse:
        """Update fields in a space

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/fields``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/fields",
            query=_query({}, extra_query),
            body=_body({"fields": fields}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def put_section(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        key: str,
        *,
        markdown: str,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ItemsPutSectionResponse:
        """Replace the section (items)

        ``PUT /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/sections/{key}``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/sections/{_path(key)}",
            query=_query({}, extra_query),
            body=_body({"markdown": markdown}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
