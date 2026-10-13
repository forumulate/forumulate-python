from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventsResource:
    """``client.events`` (9 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        scope: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventsListResponse:
        """List events in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/events``

        :param limit: Events per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit, "scope": scope, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        scope: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[EventSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit, "scope": scope}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="events",
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
        state: Union[str, NotGiven] = NOT_GIVEN,
        topic_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[EventsCreateParamsCustomization], NotGiven] = NOT_GIVEN,
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
            body=_body({"title": title, "description": description, "location": location, "url": url, "startsAt": starts_at, "endsAt": ends_at, "timezone": timezone, "capacity": capacity, "coverUrl": cover_url, "state": state, "topicId": topic_id, "customization": customization}, extra_body),
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
    ) -> Iterator[EventSummary]:
        """Iterate every item of ``list_all_events`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/manage",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="events",
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
        state: Union[str, NotGiven] = NOT_GIVEN,
        topic_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[EventsUpdateParamsCustomization], NotGiven] = NOT_GIVEN,
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
            body=_body({"title": title, "description": description, "location": location, "url": url, "startsAt": starts_at, "endsAt": ends_at, "timezone": timezone, "capacity": capacity, "coverUrl": cover_url, "state": state, "topicId": topic_id, "customization": customization}, extra_body),
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

    def my_rsvp(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventsMyRsvpResponse:
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
            body=_body({"status": status}, extra_body),
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
