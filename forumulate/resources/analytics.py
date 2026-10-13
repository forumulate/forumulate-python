from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class AnalyticsGrowthResource:
    """``client.analytics.growth`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def reports(
        self,
        org_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        weeks: Union[int, NotGiven] = NOT_GIVEN,
        months: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GrowthReport:
        """List reports in an organization

        ``GET /orgs/{orgId}/growth/reports``

        :param days: Days of daily series.
        :param weeks: Weeks of weekly series.
        :param months: Months of monthly series.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/growth/reports",
            query=_query({"days": days, "weeks": weeks, "months": months}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def extra_reports(
        self,
        org_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        weeks: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GrowthExtraReport:
        """Get the extra in an organization

        ``GET /orgs/{orgId}/growth/reports/extra``

        :param days: Days of daily series.
        :param weeks: Weeks of weekly series.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/growth/reports/extra",
            query=_query({"days": days, "weeks": weeks}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class AnalyticsResource:
    """``client.analytics`` (2 operations; growth)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.growth = AnalyticsGrowthResource(client)

    def events(
        self,
        org_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgEventsReport:
        """List events in an organization (analytics)

        ``GET /orgs/{orgId}/analytics/events``

        :param days: Window length.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/analytics/events",
            query=_query({"days": days}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def referrers(
        self,
        org_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReferrersReport:
        """List referrers in an organization

        ``GET /orgs/{orgId}/analytics/referrers``

        :param days: Window length.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/analytics/referrers",
            query=_query({"days": days}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
