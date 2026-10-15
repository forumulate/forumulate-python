from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class CourseCommerceResource:
    """``client.course_commerce`` (10 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def terms(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseCommerceTermsResponse:
        """Get the commerce in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/authoring/commerce``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/commerce",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_terms(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        price_cents: Union[int, NotGiven] = NOT_GIVEN,
        currency: Union[str, NotGiven] = NOT_GIVEN,
        refund_days: Union[int, NotGiven] = NOT_GIVEN,
        refund_text: Union[str, NotGiven] = NOT_GIVEN,
        coupons: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseCommerceSetTermsResponse:
        """Replace the commerce in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/authoring/commerce``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/commerce",
            query=_query({}, extra_query),
            body=_body({"enabled": enabled, "priceCents": price_cents, "currency": currency, "refundDays": refund_days, "refundText": refund_text, "coupons": coupons}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def coupons(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseCommerceCouponsResponse:
        """List coupons in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/coupons``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/coupons",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def coupons_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``coupons`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/coupons",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create_coupon(
        self,
        org_id: str,
        space_id: str,
        *,
        code: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        percent_off: Union[int, NotGiven] = NOT_GIVEN,
        amount_off_cents: Union[int, NotGiven] = NOT_GIVEN,
        max_redemptions: Union[Optional[int], NotGiven] = NOT_GIVEN,
        expires_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        active: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseCommerceCreateCouponResponse:
        """Create a coupon in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/course/coupons``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/coupons",
            query=_query({}, extra_query),
            body=_body({"code": code, "percentOff": percent_off, "amountOffCents": amount_off_cents, "maxRedemptions": max_redemptions, "expiresAt": expires_at, "active": active}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def patch_coupon(
        self,
        org_id: str,
        space_id: str,
        coupon_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        max_redemptions: Union[Optional[int], NotGiven] = NOT_GIVEN,
        expires_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        active: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the coupon

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/coupons/{couponId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/coupons/{_path(coupon_id)}",
            query=_query({}, extra_query),
            body=_body({"maxRedemptions": max_redemptions, "expiresAt": expires_at, "active": active}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_coupon(
        self,
        org_id: str,
        space_id: str,
        coupon_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseCommerceDeleteCouponResponse:
        """Delete the coupon

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/course/coupons/{couponId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/coupons/{_path(coupon_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def purchases(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseCommercePurchasesResponse:
        """List purchases in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/purchases``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/purchases",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def purchases_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``purchases`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/purchases",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def grant(
        self,
        org_id: str,
        space_id: str,
        *,
        user_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the grant in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/purchases/grant``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/purchases/grant",
            query=_query({}, extra_query),
            body=_body({"userId": user_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke(
        self,
        org_id: str,
        space_id: str,
        purchase_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseCommerceRevokeResponse:
        """Delete the purchase

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/course/purchases/{purchaseId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/purchases/{_path(purchase_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def refund(
        self,
        org_id: str,
        space_id: str,
        purchase_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CoursePurchaseView:
        """Create the refund in a space (course purchases)

        ``POST /orgs/{orgId}/spaces/{spaceId}/course/purchases/{purchaseId}/refund``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/purchases/{_path(purchase_id)}/refund",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
