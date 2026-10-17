from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventsResource:
    """``client.events`` (10 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        scope: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventsListResponse:
        """List events in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/events``

        :param limit: Events per page, once a version is stated.
        :param from_: Use an ISO date (2026-01-31) or date-time (2026-01-31T09:00:00Z).
        :param to: Use an ISO date (2026-01-31) or date-time (2026-01-31T09:00:00Z).
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit, "tag": tag, "from": from_, "to": to, "cursor": cursor, "mode": mode, "scope": scope}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        scope: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit, "tag": tag, "from": from_, "to": to, "mode": mode, "scope": scope}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        title: str,
        starts_at: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        location: Union[Optional[str], NotGiven] = NOT_GIVEN,
        url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        ends_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        timezone: Union[str, NotGiven] = NOT_GIVEN,
        capacity: Union[Optional[int], NotGiven] = NOT_GIVEN,
        cover_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        cover_alt: Union[Optional[str], NotGiven] = NOT_GIVEN,
        state: Union[str, NotGiven] = NOT_GIVEN,
        state_reason: Union[Optional[str], NotGiven] = NOT_GIVEN,
        topic_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        attendance_mode: Union[Optional[str], NotGiven] = NOT_GIVEN,
        venue: Union[Optional[EventsCreateParamsVenue], NotGiven] = NOT_GIVEN,
        join_link_visibility: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        hosts: Union[Optional[List[EventsCreateParamsHost]], NotGiven] = NOT_GIVEN,
        recording_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        slides_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[EventsCreateParamsCustomization], NotGiven] = NOT_GIVEN,
        rsvp_approval: Union[bool, NotGiven] = NOT_GIVEN,
        guests_max: Union[int, NotGiven] = NOT_GIVEN,
        questions: Union[Optional[List[EventsCreateParamsQuestion]], NotGiven] = NOT_GIVEN,
        recurrence: Union[Optional[EventsCreateParamsRecurrence], NotGiven] = NOT_GIVEN,
        series_scope: Union[str, NotGiven] = NOT_GIVEN,
        gallery: Union[Optional[List[EventsCreateParamsGalleryItem]], NotGiven] = NOT_GIVEN,
        recap_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        feedback_form_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventsCreateResponse:
        """Create an event in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/events``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events",
            query=_query({}, extra_query),
            body=_body({"title": title, "description": description, "location": location, "url": url, "startsAt": starts_at, "endsAt": ends_at, "timezone": timezone, "capacity": capacity, "coverUrl": cover_url, "coverAlt": cover_alt, "state": state, "stateReason": state_reason, "topicId": topic_id, "attendanceMode": attendance_mode, "venue": venue, "joinLinkVisibility": join_link_visibility, "tags": tags, "hosts": hosts, "recordingUrl": recording_url, "slidesUrl": slides_url, "customization": customization, "rsvpApproval": rsvp_approval, "guestsMax": guests_max, "questions": questions, "recurrence": recurrence, "seriesScope": series_scope, "gallery": gallery, "recapUrl": recap_url, "feedbackFormId": feedback_form_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_all_events(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventsListAllEventsResponse:
        """Get the manage in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/events/manage``

        :param limit: Events per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/manage",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all_events_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_all_events`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/manage",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventSummary:
        """Get the event

        ``GET /orgs/{orgId}/spaces/{spaceId}/events/{handle}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        location: Union[Optional[str], NotGiven] = NOT_GIVEN,
        url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        starts_at: Union[str, NotGiven] = NOT_GIVEN,
        ends_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        timezone: Union[str, NotGiven] = NOT_GIVEN,
        capacity: Union[Optional[int], NotGiven] = NOT_GIVEN,
        cover_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        cover_alt: Union[Optional[str], NotGiven] = NOT_GIVEN,
        state: Union[str, NotGiven] = NOT_GIVEN,
        state_reason: Union[Optional[str], NotGiven] = NOT_GIVEN,
        topic_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        attendance_mode: Union[Optional[str], NotGiven] = NOT_GIVEN,
        venue: Union[Optional[EventsUpdateParamsVenue], NotGiven] = NOT_GIVEN,
        join_link_visibility: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        hosts: Union[Optional[List[EventsUpdateParamsHost]], NotGiven] = NOT_GIVEN,
        recording_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        slides_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[EventsUpdateParamsCustomization], NotGiven] = NOT_GIVEN,
        rsvp_approval: Union[bool, NotGiven] = NOT_GIVEN,
        guests_max: Union[int, NotGiven] = NOT_GIVEN,
        questions: Union[Optional[List[EventsUpdateParamsQuestion]], NotGiven] = NOT_GIVEN,
        recurrence: Union[Optional[EventsUpdateParamsRecurrence], NotGiven] = NOT_GIVEN,
        series_scope: Union[str, NotGiven] = NOT_GIVEN,
        gallery: Union[Optional[List[EventsUpdateParamsGalleryItem]], NotGiven] = NOT_GIVEN,
        recap_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        feedback_form_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update the event

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/events/{handle}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "description": description, "location": location, "url": url, "startsAt": starts_at, "endsAt": ends_at, "timezone": timezone, "capacity": capacity, "coverUrl": cover_url, "coverAlt": cover_alt, "state": state, "stateReason": state_reason, "topicId": topic_id, "attendanceMode": attendance_mode, "venue": venue, "joinLinkVisibility": join_link_visibility, "tags": tags, "hosts": hosts, "recordingUrl": recording_url, "slidesUrl": slides_url, "customization": customization, "rsvpApproval": rsvp_approval, "guestsMax": guests_max, "questions": questions, "recurrence": recurrence, "seriesScope": series_scope, "gallery": gallery, "recapUrl": recap_url, "feedbackFormId": feedback_form_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Delete the event

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/events/{handle}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def duplicate(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        starts_at: Union[str, NotGiven] = NOT_GIVEN,
        ends_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventsDuplicateResponse:
        """Duplicate the event

        ``POST /orgs/{orgId}/spaces/{spaceId}/events/{handle}/duplicate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/duplicate",
            query=_query({}, extra_query),
            body=_body({"title": title, "startsAt": starts_at, "endsAt": ends_at}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def my_rsvp(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventMyRsvp:
        """Get the rsvp in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/events/{handle}/rsvp``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/rsvp",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def rsvp(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        status: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        guests: Union[int, NotGiven] = NOT_GIVEN,
        answers: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        show_publicly: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the rsvp in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/events/{handle}/rsvp``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/rsvp",
            query=_query({}, extra_query),
            body=_body({"status": status, "guests": guests, "answers": answers, "showPublicly": show_publicly}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def clear_rsvp(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventRsvpCleared:
        """Delete the rsvp in a space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/events/{handle}/rsvp``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/rsvp",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
