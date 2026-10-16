from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class DeliveryKeysResource:
    """``client.delivery_keys`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryKeysListResponse:
        """List a content library’s delivery keys

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/keys``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/keys",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/keys",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        library_id: str,
        *,
        name: str,
        kind: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        origins: Union[List[str], NotGiven] = NOT_GIVEN,
        content_types: Union[List[str], NotGiven] = NOT_GIVEN,
        locales: Union[List[str], NotGiven] = NOT_GIVEN,
        expires_in_days: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a delivery key for a content library

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/keys``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/keys",
            query=_query({}, extra_query),
            body=_body({"name": name, "kind": kind, "origins": origins, "contentTypes": content_types, "locales": locales, "expiresInDays": expires_in_days}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        library_id: str,
        key_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        content_types: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        locales: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryKeysUpdateResponse:
        """Update a delivery key

        ``PATCH /orgs/{orgId}/content/libraries/{libraryId}/keys/{keyId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/keys/{_path(key_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "origins": origins, "contentTypes": content_types, "locales": locales}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke(
        self,
        org_id: str,
        library_id: str,
        key_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryKeysRevokeResponse:
        """Revoke a delivery key

        ``DELETE /orgs/{orgId}/content/libraries/{libraryId}/keys/{keyId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/keys/{_path(key_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rotate(
        self,
        org_id: str,
        library_id: str,
        key_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        grace_minutes: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Rotate a delivery key

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/keys/{keyId}/rotate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/keys/{_path(key_id)}/rotate",
            query=_query({}, extra_query),
            body=_body({"graceMinutes": grace_minutes}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
