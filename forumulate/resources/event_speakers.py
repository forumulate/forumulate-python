from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventSpeakersResource:
    """``client.event_speakers`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventSpeakersListResponse:
        """List event speakers in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/event-speakers``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-speakers",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-speakers",
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
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        pronouns: Union[Optional[str], NotGiven] = NOT_GIVEN,
        title: Union[Optional[str], NotGiven] = NOT_GIVEN,
        company: Union[Optional[str], NotGiven] = NOT_GIVEN,
        avatar_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        bio: Union[str, NotGiven] = NOT_GIVEN,
        socials: Union[List[EventSpeakersCreateParamsSocial], NotGiven] = NOT_GIVEN,
        position: Union[int, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventSpeakersCreateResponse:
        """Create an event speaker in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/event-speakers``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-speakers",
            query=_query({}, extra_query),
            body=_body({"name": name, "pronouns": pronouns, "title": title, "company": company, "avatarUrl": avatar_url, "bio": bio, "socials": socials, "position": position, "slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        speaker: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        pronouns: Union[Optional[str], NotGiven] = NOT_GIVEN,
        title: Union[Optional[str], NotGiven] = NOT_GIVEN,
        company: Union[Optional[str], NotGiven] = NOT_GIVEN,
        avatar_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        bio: Union[str, NotGiven] = NOT_GIVEN,
        socials: Union[List[EventSpeakersUpdateParamsSocial], NotGiven] = NOT_GIVEN,
        position: Union[int, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update the event speaker

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/event-speakers/{speaker}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-speakers/{_path(speaker)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "pronouns": pronouns, "title": title, "company": company, "avatarUrl": avatar_url, "bio": bio, "socials": socials, "position": position, "slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        speaker: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventSpeakersRemoveResponse:
        """Delete the event speaker

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/event-speakers/{speaker}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-speakers/{_path(speaker)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
