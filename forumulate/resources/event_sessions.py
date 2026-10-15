from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventSessionsResource:
    """``client.event_sessions`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
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
    ) -> EventSessionsListResponse:
        """List sessions in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/events/{handle}/sessions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/sessions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
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
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/sessions",
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
        handle: str,
        *,
        title: str,
        starts_at: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        ends_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        track: Union[Optional[str], NotGiven] = NOT_GIVEN,
        stage: Union[Optional[str], NotGiven] = NOT_GIVEN,
        level: Union[Optional[str], NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        speaker_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        recording_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        slides_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventSessionsCreateResponse:
        """Create a session in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/events/{handle}/sessions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/sessions",
            query=_query({}, extra_query),
            body=_body({"title": title, "description": description, "startsAt": starts_at, "endsAt": ends_at, "track": track, "stage": stage, "level": level, "tags": tags, "speakerIds": speaker_ids, "recordingUrl": recording_url, "slidesUrl": slides_url, "slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        session: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        starts_at: Union[str, NotGiven] = NOT_GIVEN,
        ends_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        track: Union[Optional[str], NotGiven] = NOT_GIVEN,
        stage: Union[Optional[str], NotGiven] = NOT_GIVEN,
        level: Union[Optional[str], NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        speaker_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        recording_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        slides_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update the session

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/events/{handle}/sessions/{session}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/sessions/{_path(session)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "description": description, "startsAt": starts_at, "endsAt": ends_at, "track": track, "stage": stage, "level": level, "tags": tags, "speakerIds": speaker_ids, "recordingUrl": recording_url, "slidesUrl": slides_url, "slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        session: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventSessionsRemoveResponse:
        """Delete the session (orgs spaces events)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/events/{handle}/sessions/{session}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/sessions/{_path(session)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
