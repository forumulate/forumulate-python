from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class LibraryMediaResource:
    """``client.library_media`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        search: Union[str, NotGiven] = NOT_GIVEN,
        folder_id: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        missing_alt: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryAssetPage:
        """List a content library’s media

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/assets``

        :param limit: Assets per page.
        :param missing_alt: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param cursor: The `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/assets",
            query=_query({"limit": limit, "type": type, "search": search, "folderId": folder_id, "tag": tag, "missingAlt": missing_alt, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        search: Union[str, NotGiven] = NOT_GIVEN,
        folder_id: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        missing_alt: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/assets",
            query=_query({"limit": limit, "type": type, "search": search, "folderId": folder_id, "tag": tag, "missingAlt": missing_alt}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def upload(
        self,
        org_id: str,
        library_id: str,
        *,
        file: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryMediaUploadResponse:
        """Upload a file to a content library

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/assets``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/assets",
            query=_query({}, extra_query),
            body=_body({"file": file}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bulk_update(
        self,
        org_id: str,
        library_id: str,
        *,
        updates: List[LibraryMediaBulkUpdateParamsUpdate],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryMediaBulkUpdateResponse:
        """Update many of a content library’s assets at once

        ``PATCH /orgs/{orgId}/content/libraries/{libraryId}/assets``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/assets",
            query=_query({}, extra_query),
            body=_body({"updates": updates}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def suggest_alt_text(
        self,
        org_id: str,
        library_id: str,
        *,
        asset_ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryMediaSuggestAltTextResponse:
        """Suggest alt text for a content library’s pictures

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/assets/alt-text``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/assets/alt-text",
            query=_query({}, extra_query),
            body=_body({"assetIds": asset_ids, "locale": locale}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        library_id: str,
        asset_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        alt: Union[Optional[str], NotGiven] = NOT_GIVEN,
        caption: Union[Optional[str], NotGiven] = NOT_GIVEN,
        focal_x: Union[Optional[float], NotGiven] = NOT_GIVEN,
        focal_y: Union[Optional[float], NotGiven] = NOT_GIVEN,
        folder_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryMediaUpdateResponse:
        """Update one content library asset

        ``PATCH /orgs/{orgId}/content/libraries/{libraryId}/assets/{assetId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/assets/{_path(asset_id)}",
            query=_query({}, extra_query),
            body=_body({"alt": alt, "caption": caption, "focalX": focal_x, "focalY": focal_y, "folderId": folder_id, "tags": tags}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        library_id: str,
        asset_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryMediaRemoveResponse:
        """Delete a content library asset

        ``DELETE /orgs/{orgId}/content/libraries/{libraryId}/assets/{assetId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/assets/{_path(asset_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def used_in(
        self,
        org_id: str,
        library_id: str,
        asset_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryUsage:
        """List the entries that use a content library asset

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/assets/{assetId}/used-in``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/assets/{_path(asset_id)}/used-in",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
