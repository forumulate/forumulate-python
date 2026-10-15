from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventNoticesResource:
    """``client.event_notices`` (2 operations)."""

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
    ) -> EventNoticeSettingsView:
        """List event notices in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/event-notices``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-notices",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def put(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        confirmations: Union[bool, NotGiven] = NOT_GIVEN,
        reminders: Union[List[str], NotGiven] = NOT_GIVEN,
        reminder_note: Union[str, NotGiven] = NOT_GIVEN,
        organizer_digest: Union[bool, NotGiven] = NOT_GIVEN,
        announce: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace event notices in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/event-notices``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-notices",
            query=_query({}, extra_query),
            body=_body({"confirmations": confirmations, "reminders": reminders, "reminderNote": reminder_note, "organizerDigest": organizer_digest, "announce": announce}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
