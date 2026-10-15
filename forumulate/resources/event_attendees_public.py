from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventAttendeesPublicResource:
    """``client.event_attendees_public`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def settings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventAttendeesPublicSettingsResponse:
        """Get the event attendance in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/event-attendance``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-attendance",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventPublicAttendees:
        """List attendees in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/attendees``

        :param limit: Faces shown, at most.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/attendees",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def request(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        email: str,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        guests: Union[int, NotGiven] = NOT_GIVEN,
        answers: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        show_publicly: Union[bool, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Create the rsvp in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/rsvp``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/rsvp",
            query=_query({}, extra_query),
            body=_body({"email": email, "name": name, "guests": guests, "answers": answers, "showPublicly": show_publicly, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def confirm(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        token: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Confirm the rsvp

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/rsvp/confirm``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/rsvp/confirm",
            query=_query({}, extra_query),
            body=_body({"token": token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def cancel(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        token: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Cancel the rsvp

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/rsvp/cancel``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/rsvp/cancel",
            query=_query({}, extra_query),
            body=_body({"token": token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
