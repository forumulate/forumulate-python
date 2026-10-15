from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventAttendeesResource:
    """``client.event_attendees`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        status: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventAttendeeList:
        """List attendees in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/events/{handle}/attendees``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/attendees",
            query=_query({"status": status}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def csv(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of attendees

        ``GET /orgs/{orgId}/spaces/{spaceId}/events/{handle}/attendees.csv``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/attendees.csv",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def patch(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        rsvp_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        status: Union[str, NotGiven] = NOT_GIVEN,
        checked_in: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update the attendee

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/events/{handle}/attendees/{rsvpId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/attendees/{_path(rsvp_id)}",
            query=_query({}, extra_query),
            body=_body({"status": status, "checkedIn": checked_in}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def message(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        subject: str,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        statuses: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Create the message in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/events/{handle}/attendees/message``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/attendees/message",
            query=_query({}, extra_query),
            body=_body({"subject": subject, "body": body, "statuses": statuses}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def settings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventAttendeesSettingsResponse:
        """Get the event attendance in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/event-attendance``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-attendance",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def save_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        public_attendees: Union[bool, NotGiven] = NOT_GIVEN,
        email_rsvp: Union[bool, NotGiven] = NOT_GIVEN,
        searchable: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventAttendeesSaveSettingsResponse:
        """Replace the event attendance in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/event-attendance``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-attendance",
            query=_query({}, extra_query),
            body=_body({"publicAttendees": public_attendees, "emailRsvp": email_rsvp, "searchable": searchable}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
