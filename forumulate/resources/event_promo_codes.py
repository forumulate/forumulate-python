from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventPromoCodesResource:
    """``client.event_promo_codes`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventPromoCodesListResponse:
        """List event promo codes in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/event-promo-codes``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-promo-codes",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-promo-codes",
            query=_query({"limit": limit}, extra_query),
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
        code: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        event_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        percent_off: Union[Optional[int], NotGiven] = NOT_GIVEN,
        amount_off_cents: Union[Optional[int], NotGiven] = NOT_GIVEN,
        max_redemptions: Union[Optional[int], NotGiven] = NOT_GIVEN,
        expires_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        tier_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventPromoCodesCreateResponse:
        """Create an event promo code in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/event-promo-codes``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-promo-codes",
            query=_query({}, extra_query),
            body=_body({"code": code, "eventId": event_id, "percentOff": percent_off, "amountOffCents": amount_off_cents, "maxRedemptions": max_redemptions, "expiresAt": expires_at, "tierIds": tier_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def replace(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        code: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        event_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        percent_off: Union[Optional[int], NotGiven] = NOT_GIVEN,
        amount_off_cents: Union[Optional[int], NotGiven] = NOT_GIVEN,
        max_redemptions: Union[Optional[int], NotGiven] = NOT_GIVEN,
        expires_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        tier_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventPromoCodesReplaceResponse:
        """Replace the event promo code

        ``PUT /orgs/{orgId}/spaces/{spaceId}/event-promo-codes/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-promo-codes/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"code": code, "eventId": event_id, "percentOff": percent_off, "amountOffCents": amount_off_cents, "maxRedemptions": max_redemptions, "expiresAt": expires_at, "tierIds": tier_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventPromoCodesRemoveResponse:
        """Delete the event promo code

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/event-promo-codes/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-promo-codes/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
