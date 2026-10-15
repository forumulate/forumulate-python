from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class CourseLearnerExtrasResource:
    """``client.course_learner_extras`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def positions(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseLearnerExtrasPositionsResponse:
        """Get the media in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/lessons/{slug}/media``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/lessons/{_path(slug)}/media",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def positions_all(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``positions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/lessons/{_path(slug)}/media",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def save_position(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        key: str,
        position: float,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        duration: Union[float, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseLearnerExtrasSavePositionResponse:
        """Replace the media in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/lessons/{slug}/media``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/lessons/{_path(slug)}/media",
            query=_query({}, extra_query),
            body=_body({"key": key, "position": position, "duration": duration}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def stats(
        self,
        org_id: str,
        space_id: str,
        *,
        tz: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseLearnerStats:
        """List stats in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/me/stats``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/me/stats",
            query=_query({"tz": tz}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def mine(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MyCoursePurchase:
        """Get the purchase in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/purchase``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/purchase",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def checkout(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        coupon: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the checkout in a space (course)

        ``POST /orgs/{orgId}/spaces/{spaceId}/course/checkout``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/checkout",
            query=_query({}, extra_query),
            body=_body({"coupon": coupon}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def confirm(
        self,
        org_id: str,
        space_id: str,
        *,
        session_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Confirm the checkout

        ``POST /orgs/{orgId}/spaces/{spaceId}/course/checkout/confirm``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/checkout/confirm",
            query=_query({}, extra_query),
            body=_body({"sessionId": session_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def refund(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MyCoursePurchase:
        """Create the refund in a space (course purchase)

        ``POST /orgs/{orgId}/spaces/{spaceId}/course/purchase/refund``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/purchase/refund",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
