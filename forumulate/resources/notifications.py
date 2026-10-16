from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class NotificationsPushResource:
    """``client.notifications.push`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def public_key(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsPushPublicKeyResponse:
        """Get the vapid public key

        ``GET /push/vapid-public-key``
        """
        return self._client._request(
            "GET",
            f"/push/vapid-public-key",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def status(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsPushStatusResponse:
        """Get the status

        ``GET /push/status``
        """
        return self._client._request(
            "GET",
            f"/push/status",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def subscribe(
        self,
        *,
        endpoint: str,
        keys: NotificationsPushSubscribeParamsKeys,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsPushSubscribeResponse:
        """Subscribe the push

        ``POST /push/subscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/push/subscribe",
            query=_query({}, extra_query),
            body=_body({"endpoint": endpoint, "keys": keys}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unsubscribe(
        self,
        *,
        endpoint: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsPushUnsubscribeResponse:
        """Unsubscribe the push

        ``POST /push/unsubscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/push/unsubscribe",
            query=_query({}, extra_query),
            body=_body({"endpoint": endpoint}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class NotificationsResource:
    """``client.notifications`` (13 operations; push)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.push = NotificationsPushResource(client)

    def get_dnd(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsGetDndResponse:
        """Get the dnd in an organization

        ``GET /orgs/{orgId}/notifications/dnd``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/notifications/dnd",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_dnd(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        ends_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        daily_start: Union[Optional[int], NotGiven] = NOT_GIVEN,
        daily_end: Union[Optional[int], NotGiven] = NOT_GIVEN,
        timezone: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsSetDndResponse:
        """Replace the dnd in an organization

        ``PUT /orgs/{orgId}/notifications/dnd``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/notifications/dnd",
            query=_query({}, extra_query),
            body=_body({"endsAt": ends_at, "dailyStart": daily_start, "dailyEnd": daily_end, "timezone": timezone}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def snooze_dnd(
        self,
        org_id: str,
        *,
        minutes: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsSnoozeDndResponse:
        """Create the snooze in an organization

        ``POST /orgs/{orgId}/notifications/dnd/snooze``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/notifications/dnd/snooze",
            query=_query({}, extra_query),
            body=_body({"minutes": minutes}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_schedule(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsGetScheduleResponse:
        """Get the schedule in an organization (notifications)

        ``GET /orgs/{orgId}/notifications/schedule``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/notifications/schedule",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_schedule(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        timezone: Union[str, NotGiven] = NOT_GIVEN,
        days: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsSetScheduleResponse:
        """Replace the schedule in an organization

        ``PUT /orgs/{orgId}/notifications/schedule``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/notifications/schedule",
            query=_query({}, extra_query),
            body=_body({"enabled": enabled, "timezone": timezone, "days": days}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_type_preferences(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> TypePrefsMatrix:
        """List type preferences in an organization

        ``GET /orgs/{orgId}/notifications/type-preferences``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/notifications/type-preferences",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_type_preferences(
        self,
        org_id: str,
        *,
        preferences: List[NotificationsSetTypePreferencesParamsPreference],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace type preferences in an organization

        ``PUT /orgs/{orgId}/notifications/type-preferences``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/notifications/type-preferences",
            query=_query({}, extra_query),
            body=_body({"preferences": preferences}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def stream(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the stream in an organization (notifications)

        ``GET /orgs/{orgId}/notifications/stream``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/notifications/stream",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def stream_stream(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Stream ``stream`` as server-sent events, yielding each decoded event."""
        yield from self._client._stream(
            "GET",
            f"/orgs/{_path(org_id)}/notifications/stream",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get_preferences(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsGetPreferencesResponse:
        """List preferences in an organization

        ``GET /orgs/{orgId}/notifications/preferences``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/notifications/preferences",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_preferences(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        deliver_email: Union[str, NotGiven] = NOT_GIVEN,
        muted_types: Union[List[str], NotGiven] = NOT_GIVEN,
        deliver_push: Union[str, NotGiven] = NOT_GIVEN,
        push_muted_types: Union[List[str], NotGiven] = NOT_GIVEN,
        quiet_start: Union[Optional[int], NotGiven] = NOT_GIVEN,
        quiet_end: Union[Optional[int], NotGiven] = NOT_GIVEN,
        timezone: Union[str, NotGiven] = NOT_GIVEN,
        digest_hour: Union[int, NotGiven] = NOT_GIVEN,
        community_summary: Union[bool, NotGiven] = NOT_GIVEN,
        mailing_list_mode: Union[str, NotGiven] = NOT_GIVEN,
        messages_from: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsSetPreferencesResponse:
        """Update preferences in an organization

        ``PATCH /orgs/{orgId}/notifications/preferences``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/notifications/preferences",
            query=_query({}, extra_query),
            body=_body({"deliverEmail": deliver_email, "mutedTypes": muted_types, "deliverPush": deliver_push, "pushMutedTypes": push_muted_types, "quietStart": quiet_start, "quietEnd": quiet_end, "timezone": timezone, "digestHour": digest_hour, "communitySummary": community_summary, "mailingListMode": mailing_list_mode, "messagesFrom": messages_from}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        unread: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsListResponse:
        """List notifications in an organization

        ``GET /orgs/{orgId}/notifications``

        :param limit: Notifications per page, once a version is stated.
        :param unread: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/notifications",
            query=_query({"limit": limit, "unread": unread, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        unread: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/notifications",
            query=_query({"limit": limit, "unread": unread}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def read(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsReadResponse:
        """Create the read in an organization (notifications)

        ``POST /orgs/{orgId}/notifications/{id}/read``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/notifications/{_path(id)}/read",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def read_all(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NotificationsReadAllResponse:
        """Create the read all in an organization

        ``POST /orgs/{orgId}/notifications/read-all``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/notifications/read-all",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
