from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class AssetLibraryResource:
    """``client.asset_library`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def update(
        self,
        org_id: str,
        space_id: str,
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
    ) -> AssetLibraryUpdateResponse:
        """Update an asset’s alt text, caption, focal point, folder or tags

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/assets/{assetId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/assets/{_path(asset_id)}",
            query=_query({}, extra_query),
            body=_body({"alt": alt, "caption": caption, "focalX": focal_x, "focalY": focal_y, "folderId": folder_id, "tags": tags}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_folders(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AssetLibraryListFoldersResponse:
        """List the media library’s folders

        ``GET /orgs/{orgId}/asset-folders``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/asset-folders",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_folders_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_folders`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/asset-folders",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create_folder(
        self,
        org_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AssetLibraryCreateFolderResponse:
        """Create a media library folder

        ``POST /orgs/{orgId}/asset-folders``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/asset-folders",
            query=_query({}, extra_query),
            body=_body({"name": name, "parentId": parent_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_folder(
        self,
        org_id: str,
        folder_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AssetLibraryUpdateFolderResponse:
        """Rename or move a media library folder

        ``PATCH /orgs/{orgId}/asset-folders/{folderId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/asset-folders/{_path(folder_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "parentId": parent_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_folder(
        self,
        org_id: str,
        folder_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AssetLibraryDeleteFolderResponse:
        """Delete a media library folder

        ``DELETE /orgs/{orgId}/asset-folders/{folderId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/asset-folders/{_path(folder_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
