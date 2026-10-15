from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventTicketsPublicResource:
    """``client.event_tickets_public`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def view(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketsView:
        """List tickets in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/tickets``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/tickets",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def quote(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        tier_id: str,
        quantity: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        promo_code: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the quote in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/tickets/quote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/tickets/quote",
            query=_query({}, extra_query),
            body=_body({"tierId": tier_id, "quantity": quantity, "promoCode": promo_code}, extra_body),
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
        """Create the checkout in a space (public reader events tickets)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/tickets/checkout``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/tickets/checkout",
            query=_query({}, extra_query),
            body=_body({"tierId": tier_id, "quantity": quantity, "promoCode": promo_code, "email": email, "name": name, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def confirm(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        session_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketsPublicConfirmResponse:
        """Confirm the ticket

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/tickets/confirm``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/tickets/confirm",
            query=_query({}, extra_query),
            body=_body({"sessionId": session_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
