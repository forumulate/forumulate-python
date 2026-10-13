from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class BillingResource:
    """``client.billing`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def view(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BillingView:
        """Get the billing in an organization

        ``GET /orgs/{orgId}/billing``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/billing",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def checkout(
        self,
        org_id: str,
        *,
        plan: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BillingCheckoutResponse:
        """Create the checkout in an organization

        ``POST /orgs/{orgId}/billing/checkout``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/billing/checkout",
            query=_query({}, extra_query),
            body=_body({"plan": plan}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def portal(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BillingPortalResponse:
        """Create the portal in an organization

        ``POST /orgs/{orgId}/billing/portal``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/billing/portal",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
