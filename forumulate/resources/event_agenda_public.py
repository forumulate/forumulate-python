from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventAgendaPublicResource:
    """``client.event_agenda_public`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def agenda(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventAgenda:
        """Get the agenda in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/agenda``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/agenda",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def ics(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        session: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of calendar (sessions)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/sessions/{session}/calendar.ics``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/sessions/{_path(session)}/calendar.ics",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
