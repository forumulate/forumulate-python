from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ChangelogResource:
    """``client.changelog`` (9 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        offset: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogListResponse:
        """Get the changelog in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/changelog``

        :param limit: Releases per page, newest first.
        :param offset: Where in the archive to start.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog",
            query=_query({"limit": limit, "offset": offset, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        offset: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ArticleDetail]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog",
            query=_query({"limit": limit, "offset": offset}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="releases",
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ChangelogCreateParamsContent, NotGiven] = NOT_GIVEN,
        version: Union[Optional[str], NotGiven] = NOT_GIVEN,
        published_at: Union[str, NotGiven] = NOT_GIVEN,
        shipped_topic_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        fields: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        on_this_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[ChangelogCreateParamsCustomization], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogCreateResponse:
        """Create the changelog in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/changelog``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "version": version, "publishedAt": published_at, "shippedTopicIds": shipped_topic_ids, "tags": tags, "fields": fields, "onThisPage": on_this_page, "customization": customization, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def compile(
        self,
        org_id: str,
        space_id: str,
        *,
        since: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CompiledRelease:
        """Get the compile in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/changelog/compile``

        :param since: Use an ISO date (2026-01-31) or date-time (2026-01-31T09:00:00Z).
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/compile",
            query=_query({"since": since}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def publish(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogPublishResponse:
        """Publish the changelog

        ``POST /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/publish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/publish",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogGetResponse:
        """Get the changelog

        ``GET /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ChangelogUpdateParamsContent, NotGiven] = NOT_GIVEN,
        version: Union[Optional[str], NotGiven] = NOT_GIVEN,
        published_at: Union[str, NotGiven] = NOT_GIVEN,
        shipped_topic_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        fields: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        on_this_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[ChangelogUpdateParamsCustomization], NotGiven] = NOT_GIVEN,
        edit_reason: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogUpdateResponse:
        """Update the changelog

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "version": version, "publishedAt": published_at, "shippedTopicIds": shipped_topic_ids, "tags": tags, "fields": fields, "onThisPage": on_this_page, "customization": customization, "editReason": edit_reason, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogRemoveResponse:
        """Delete the changelog

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def schedule(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        publish_at: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogScheduleResponse:
        """Create the schedule in a space (changelog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/schedule``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/schedule",
            query=_query({}, extra_query),
            body=_body({"publishAt": publish_at}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unschedule(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogUnscheduleResponse:
        """Delete the schedule in a space (changelog)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/schedule``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/schedule",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
