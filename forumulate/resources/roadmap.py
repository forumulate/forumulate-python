from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class RoadmapResource:
    """``client.roadmap`` (8 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def board(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> RoadmapBoardResponse:
        """Get the roadmap in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/roadmap``

        :param limit: Items per LANE — not lanes.
        :param page: Which page of results to return, 1-based.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap",
            query=_query({"limit": limit, "cursor": cursor, "page": page}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def board_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[RoadmapBoardResponseLane]:
        """Iterate every item of ``board`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap",
            query=_query({"limit": limit, "page": page}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="lanes",
        )

    def submit(
        self,
        org_id: str,
        space_id: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[RoadmapSubmitParamsContent, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[RoadmapSubmitParamsCustomization], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> RoadmapSubmitResponse:
        """Create the roadmap in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/roadmap``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "tags": tags, "customization": customization, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> RoadmapGetResponse:
        """Get the roadmap

        ``GET /orgs/{orgId}/spaces/{spaceId}/roadmap/{topicId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/{_path(topic_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[RoadmapUpdateParamsCustomization], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> RoadmapUpdateResponse:
        """Update the roadmap

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/roadmap/{topicId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/{_path(topic_id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "tags": tags, "customization": customization}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def vote(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> RoadmapVoteResponse:
        """Create the vote in a space (roadmap)

        ``POST /orgs/{orgId}/spaces/{spaceId}/roadmap/{topicId}/vote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/{_path(topic_id)}/vote",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def comment(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[RoadmapCommentParamsContent, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> RoadmapCommentResponse:
        """Create a comment in a space (roadmap)

        ``POST /orgs/{orgId}/spaces/{spaceId}/roadmap/{topicId}/comments``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/{_path(topic_id)}/comments",
            query=_query({}, extra_query),
            body=_body({"content": content, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def merge(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        canonical_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> RoadmapMergeResponse:
        """Merge the roadmap

        ``POST /orgs/{orgId}/spaces/{spaceId}/roadmap/{topicId}/merge``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/{_path(topic_id)}/merge",
            query=_query({}, extra_query),
            body=_body({"canonicalId": canonical_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_status(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        status: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> RoadmapSetStatusResponse:
        """Create the status in a space (roadmap)

        ``POST /orgs/{orgId}/spaces/{spaceId}/roadmap/{topicId}/status``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/{_path(topic_id)}/status",
            query=_query({}, extra_query),
            body=_body({"status": status}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
