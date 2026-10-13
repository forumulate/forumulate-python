from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class StatusMonitorsResource:
    """``client.status.monitors`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def ping_get(
        self,
        monitor_id: str,
        token: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusMonitorsPingGetResponse:
        """Record a heartbeat for a monitor

        ``GET /status/ping/{monitorId}/{token}``
        """
        return self._client._request(
            "GET",
            f"/status/ping/{_path(monitor_id)}/{_path(token)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def ping_post(
        self,
        monitor_id: str,
        token: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusMonitorsPingPostResponse:
        """Record a heartbeat for a monitor, by POST

        ``POST /status/ping/{monitorId}/{token}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/status/ping/{_path(monitor_id)}/{_path(token)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def report(
        self,
        monitor_id: str,
        token: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        reason: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusMonitorsReportResponse:
        """Report that a monitored service restarted

        ``POST /status/restart/{monitorId}/{token}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/status/restart/{_path(monitor_id)}/{_path(token)}",
            query=_query({}, extra_query),
            body=_body({"reason": reason}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class StatusResource:
    """``client.status`` (13 operations; monitors)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.monitors = StatusMonitorsResource(client)

    def list_channels(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusListChannelsResponse:
        """List channels in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/status/channels``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/channels",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_channels_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[StatusChannel]:
        """Iterate every item of ``list_channels`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/channels",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="channels",
        )

    def add_channel(
        self,
        org_id: str,
        space_id: str,
        *,
        kind: str,
        url: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        label: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusAddChannelResponse:
        """Create a channel in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/status/channels``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/channels",
            query=_query({}, extra_query),
            body=_body({"kind": kind, "url": url, "label": label}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_channel(
        self,
        org_id: str,
        space_id: str,
        channel_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusRemoveChannelResponse:
        """Delete the channel

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/status/channels/{channelId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/channels/{_path(channel_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def monitors_status(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusMonitorsStatusResponse:
        """List monitors in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/status/monitors``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/monitors",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def monitors_status_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[MonitorSummary]:
        """Iterate every item of ``monitors_status`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/monitors",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="monitors",
        )

    def add_monitor(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        url: Union[str, NotGiven] = NOT_GIVEN,
        method: Union[str, NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        interval_seconds: Union[int, NotGiven] = NOT_GIVEN,
        visible: Union[bool, NotGiven] = NOT_GIVEN,
        alerts_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        failure_threshold: Union[int, NotGiven] = NOT_GIVEN,
        success_threshold: Union[int, NotGiven] = NOT_GIVEN,
        keyword: Union[Optional[str], NotGiven] = NOT_GIVEN,
        cert_expiry_days: Union[Optional[int], NotGiven] = NOT_GIVEN,
        expect_status: Union[Optional[int], NotGiven] = NOT_GIVEN,
        max_latency_ms: Union[Optional[int], NotGiven] = NOT_GIVEN,
        request_headers: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        request_body: Union[Optional[str], NotGiven] = NOT_GIVEN,
        body_path: Union[Optional[str], NotGiven] = NOT_GIVEN,
        body_expect: Union[Optional[str], NotGiven] = NOT_GIVEN,
        group: Union[Optional[str], NotGiven] = NOT_GIVEN,
        declared_state: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusAddMonitorResponse:
        """Add a status monitor

        ``POST /orgs/{orgId}/spaces/{spaceId}/status/monitors``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/monitors",
            query=_query({}, extra_query),
            body=_body({"name": name, "url": url, "method": method, "kind": kind, "intervalSeconds": interval_seconds, "visible": visible, "alertsEnabled": alerts_enabled, "failureThreshold": failure_threshold, "successThreshold": success_threshold, "keyword": keyword, "certExpiryDays": cert_expiry_days, "expectStatus": expect_status, "maxLatencyMs": max_latency_ms, "requestHeaders": request_headers, "requestBody": request_body, "bodyPath": body_path, "bodyExpect": body_expect, "group": group, "declaredState": declared_state}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_monitor(
        self,
        org_id: str,
        space_id: str,
        monitor_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        url: Union[str, NotGiven] = NOT_GIVEN,
        method: Union[str, NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        interval_seconds: Union[int, NotGiven] = NOT_GIVEN,
        visible: Union[bool, NotGiven] = NOT_GIVEN,
        alerts_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        failure_threshold: Union[int, NotGiven] = NOT_GIVEN,
        success_threshold: Union[int, NotGiven] = NOT_GIVEN,
        keyword: Union[Optional[str], NotGiven] = NOT_GIVEN,
        cert_expiry_days: Union[Optional[int], NotGiven] = NOT_GIVEN,
        expect_status: Union[Optional[int], NotGiven] = NOT_GIVEN,
        max_latency_ms: Union[Optional[int], NotGiven] = NOT_GIVEN,
        request_headers: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        request_body: Union[Optional[str], NotGiven] = NOT_GIVEN,
        body_path: Union[Optional[str], NotGiven] = NOT_GIVEN,
        body_expect: Union[Optional[str], NotGiven] = NOT_GIVEN,
        group: Union[Optional[str], NotGiven] = NOT_GIVEN,
        declared_state: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusUpdateMonitorResponse:
        """Update the monitor

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/status/monitors/{monitorId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/monitors/{_path(monitor_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "url": url, "method": method, "kind": kind, "intervalSeconds": interval_seconds, "visible": visible, "alertsEnabled": alerts_enabled, "failureThreshold": failure_threshold, "successThreshold": success_threshold, "keyword": keyword, "certExpiryDays": cert_expiry_days, "expectStatus": expect_status, "maxLatencyMs": max_latency_ms, "requestHeaders": request_headers, "requestBody": request_body, "bodyPath": body_path, "bodyExpect": body_expect, "group": group, "declaredState": declared_state}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_monitor(
        self,
        org_id: str,
        space_id: str,
        monitor_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusRemoveMonitorResponse:
        """Delete the monitor

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/status/monitors/{monitorId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/monitors/{_path(monitor_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusGetSettingsResponse:
        """List settings in a space (status)

        ``GET /orgs/{orgId}/spaces/{spaceId}/status/settings``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/settings",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        auto_incident: Union[bool, NotGiven] = NOT_GIVEN,
        notify_subscribers: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusSetSettingsResponse:
        """Replace settings in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/status/settings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/settings",
            query=_query({}, extra_query),
            body=_body({"autoIncident": auto_incident, "notifySubscribers": notify_subscribers}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def board(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusBoard:
        """Get the board in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/status/board``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/board",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def create_incident(
        self,
        org_id: str,
        space_id: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        state: Union[str, NotGiven] = NOT_GIVEN,
        severity: Union[str, NotGiven] = NOT_GIVEN,
        body: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        fields: Union[StatusCreateIncidentParamsFields, NotGiven] = NOT_GIVEN,
        scheduled_for: Union[Optional[str], NotGiven] = NOT_GIVEN,
        scheduled_until: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusCreateIncidentResponse:
        """Create an incident in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/status/incidents``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents",
            query=_query({}, extra_query),
            body=_body({"title": title, "state": state, "severity": severity, "body": body, "fields": fields, "scheduledFor": scheduled_for, "scheduledUntil": scheduled_until}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_incident(
        self,
        org_id: str,
        space_id: str,
        incident_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        state: Union[str, NotGiven] = NOT_GIVEN,
        severity: Union[str, NotGiven] = NOT_GIVEN,
        body: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        fields: Union[StatusUpdateIncidentParamsFields, NotGiven] = NOT_GIVEN,
        scheduled_for: Union[Optional[str], NotGiven] = NOT_GIVEN,
        scheduled_until: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusUpdateIncidentResponse:
        """Update the incident

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/status/incidents/{incidentId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents/{_path(incident_id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "state": state, "severity": severity, "body": body, "fields": fields, "scheduledFor": scheduled_for, "scheduledUntil": scheduled_until}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def add_incident_update(
        self,
        org_id: str,
        space_id: str,
        incident_id: str,
        *,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        state: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusAddIncidentUpdateResponse:
        """Create an update in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/status/incidents/{incidentId}/updates``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents/{_path(incident_id)}/updates",
            query=_query({}, extra_query),
            body=_body({"body": body, "state": state}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
