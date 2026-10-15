from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class CourseAccessResource:
    """``client.course_access`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseAccessGetResponse:
        """Get the access in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/course/authoring/access``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/access",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        order: Union[str, NotGiven] = NOT_GIVEN,
        require_prerequisites: Union[bool, NotGiven] = NOT_GIVEN,
        drip: Union[List[CourseAccessSetParamsDripItem], NotGiven] = NOT_GIVEN,
        audience: Union[str, NotGiven] = NOT_GIVEN,
        groups: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseAccessSetResponse:
        """Replace the access in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/course/authoring/access``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/authoring/access",
            query=_query({}, extra_query),
            body=_body({"order": order, "requirePrerequisites": require_prerequisites, "drip": drip, "audience": audience, "groups": groups}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
