from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventTicketsResource:
    """``client.event_tickets`` (8 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def tiers(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketsTiersResponse:
        """List tiers in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/events/{handle}/tiers``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/tiers",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def create_tier(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        name: str,
        price_cents: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        currency: Union[str, NotGiven] = NOT_GIVEN,
        capacity: Union[Optional[int], NotGiven] = NOT_GIVEN,
        max_per_order: Union[int, NotGiven] = NOT_GIVEN,
        sales_start: Union[Optional[str], NotGiven] = NOT_GIVEN,
        sales_end: Union[Optional[str], NotGiven] = NOT_GIVEN,
        position: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketsCreateTierResponse:
        """Create a tier in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/events/{handle}/tiers``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/tiers",
            query=_query({}, extra_query),
            body=_body({"name": name, "description": description, "priceCents": price_cents, "currency": currency, "capacity": capacity, "maxPerOrder": max_per_order, "salesStart": sales_start, "salesEnd": sales_end, "position": position}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_tier(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        tier: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        price_cents: Union[int, NotGiven] = NOT_GIVEN,
        currency: Union[str, NotGiven] = NOT_GIVEN,
        capacity: Union[Optional[int], NotGiven] = NOT_GIVEN,
        max_per_order: Union[int, NotGiven] = NOT_GIVEN,
        sales_start: Union[Optional[str], NotGiven] = NOT_GIVEN,
        sales_end: Union[Optional[str], NotGiven] = NOT_GIVEN,
        position: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketsUpdateTierResponse:
        """Update the tier

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/events/{handle}/tiers/{tier}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/tiers/{_path(tier)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "description": description, "priceCents": price_cents, "currency": currency, "capacity": capacity, "maxPerOrder": max_per_order, "salesStart": sales_start, "salesEnd": sales_end, "position": position}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_tier(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        tier: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketsDeleteTierResponse:
        """Delete the tier

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/events/{handle}/tiers/{tier}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/tiers/{_path(tier)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ticketing(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        refund_policy: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketsTicketingResponse:
        """Replace the ticketing in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/events/{handle}/ticketing``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/ticketing",
            query=_query({}, extra_query),
            body=_body({"refundPolicy": refund_policy}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def orders(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketsOrdersResponse:
        """List orders in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/events/{handle}/orders``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/orders",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def orders_all(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``orders`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/orders",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def refund(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        order: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketsRefundResponse:
        """Create the refund in a space (events orders)

        ``POST /orgs/{orgId}/spaces/{spaceId}/events/{handle}/orders/{order}/refund``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/orders/{_path(order)}/refund",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def checkout(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        tier_id: str,
        quantity: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        promo_code: Union[str, NotGiven] = NOT_GIVEN,
        email: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the checkout in a space (events tickets)

        ``POST /orgs/{orgId}/spaces/{spaceId}/events/{handle}/tickets/checkout``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/tickets/checkout",
            query=_query({}, extra_query),
            body=_body({"tierId": tier_id, "quantity": quantity, "promoCode": promo_code, "email": email, "name": name, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
