from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class WebhooksResource:
    """``client.webhooks`` (9 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def events(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> WebhooksEventsResponse:
        """List events in an organization (webhooks)

        ``GET /orgs/{orgId}/webhooks/events``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/webhooks/events",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> WebhooksListResponse:
        """List webhooks in an organization

        ``GET /orgs/{orgId}/webhooks``

        :param limit: Webhooks per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/webhooks",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/webhooks",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        *,
        url: str,
        events: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        format: Union[str, NotGiven] = NOT_GIVEN,
        category_ids: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        tag_ids: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        group_ids: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        body_encoding: Union[str, NotGiven] = NOT_GIVEN,
        signature_version: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> WebhooksCreateResponse:
        """Create a webhook in an organization

        ``POST /orgs/{orgId}/webhooks``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/webhooks",
            query=_query({}, extra_query),
            body=_body({"url": url, "events": events, "spaceId": space_id, "format": format, "categoryIds": category_ids, "tagIds": tag_ids, "groupIds": group_ids, "bodyEncoding": body_encoding, "signatureVersion": signature_version}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        webhook_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        url: Union[str, NotGiven] = NOT_GIVEN,
        events: Union[List[str], NotGiven] = NOT_GIVEN,
        active: Union[bool, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        category_ids: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        tag_ids: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        group_ids: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        body_encoding: Union[str, NotGiven] = NOT_GIVEN,
        signature_version: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> WebhooksUpdateResponse:
        """Update the webhook

        ``PATCH /orgs/{orgId}/webhooks/{webhookId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/webhooks/{_path(webhook_id)}",
            query=_query({}, extra_query),
            body=_body({"url": url, "events": events, "active": active, "spaceId": space_id, "categoryIds": category_ids, "tagIds": tag_ids, "groupIds": group_ids, "bodyEncoding": body_encoding, "signatureVersion": signature_version}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        webhook_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> WebhooksRemoveResponse:
        """Delete the webhook

        ``DELETE /orgs/{orgId}/webhooks/{webhookId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/webhooks/{_path(webhook_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def deliveries(
        self,
        org_id: str,
        webhook_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> WebhooksDeliveriesResponse:
        """List deliveries in an organization (webhooks)

        ``GET /orgs/{orgId}/webhooks/{webhookId}/deliveries``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/webhooks/{_path(webhook_id)}/deliveries",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def deliveries_all(
        self,
        org_id: str,
        webhook_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``deliveries`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/webhooks/{_path(webhook_id)}/deliveries",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def replay(
        self,
        org_id: str,
        webhook_id: str,
        delivery_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Replay the delivery

        ``POST /orgs/{orgId}/webhooks/{webhookId}/deliveries/{deliveryId}/replay``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/webhooks/{_path(webhook_id)}/deliveries/{_path(delivery_id)}/replay",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rotate(
        self,
        org_id: str,
        webhook_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        overlap_hours: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> WebhooksRotateResponse:
        """Rotate secret in an organization (webhooks)

        ``POST /orgs/{orgId}/webhooks/{webhookId}/rotate-secret``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/webhooks/{_path(webhook_id)}/rotate-secret",
            query=_query({}, extra_query),
            body=_body({"overlapHours": overlap_hours}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ping(
        self,
        org_id: str,
        webhook_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Create the ping in an organization

        ``POST /orgs/{orgId}/webhooks/{webhookId}/ping``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/webhooks/{_path(webhook_id)}/ping",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
