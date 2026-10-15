from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class CourseLearnersResource:
    """``client.course_learners`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def roster(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseLearnersRosterResponse:
        """List learners in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/learners``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/learners",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def roster_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``roster`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/learners",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def roster_csv(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of learners

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/learners.csv``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/learners.csv",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def funnel(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseFunnel:
        """Get the funnel in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/funnel``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/funnel",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def revoke(
        self,
        org_id: str,
        space_id: str,
        user_id: str,
        *,
        revoked: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseLearnersRevokeResponse:
        """Replace the certificate in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/learners/{userId}/certificate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/learners/{_path(user_id)}/certificate",
            query=_query({}, extra_query),
            body=_body({"revoked": revoked}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def learning(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseLearnersLearningResponse:
        """Get the learning in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/authoring/learning``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/learning",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_learning(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        welcome_email: Union[bool, NotGiven] = NOT_GIVEN,
        completion_email: Union[bool, NotGiven] = NOT_GIVEN,
        nudge_after_days: Union[Optional[int], NotGiven] = NOT_GIVEN,
        xp_per_lesson: Union[int, NotGiven] = NOT_GIVEN,
        xp_per_course: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseLearnersSetLearningResponse:
        """Replace the learning in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/authoring/learning``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/learning",
            query=_query({}, extra_query),
            body=_body({"welcomeEmail": welcome_email, "completionEmail": completion_email, "nudgeAfterDays": nudge_after_days, "xpPerLesson": xp_per_lesson, "xpPerCourse": xp_per_course}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
