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
    """``client.analytics`` (4 operations; growth)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.growth = AnalyticsGrowthResource(client)

    def get(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgAnalytics:
        """List analytics tags in an organization

        ``GET /orgs/{orgId}/analytics-tags``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/analytics-tags",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        ga4: Union[Any, NotGiven] = NOT_GIVEN,
        gtm: Union[Any, NotGiven] = NOT_GIVEN,
        segment: Union[Any, NotGiven] = NOT_GIVEN,
        intercom: Union[Any, NotGiven] = NOT_GIVEN,
        plausible: Union[Any, NotGiven] = NOT_GIVEN,
        plausible_host: Union[Any, NotGiven] = NOT_GIVEN,
        fathom: Union[Any, NotGiven] = NOT_GIVEN,
        umami: Union[Any, NotGiven] = NOT_GIVEN,
        umami_host: Union[Any, NotGiven] = NOT_GIVEN,
        matomo: Union[Any, NotGiven] = NOT_GIVEN,
        matomo_host: Union[Any, NotGiven] = NOT_GIVEN,
        simple_analytics: Union[Any, NotGiven] = NOT_GIVEN,
        posthog: Union[Any, NotGiven] = NOT_GIVEN,
        posthog_host: Union[Any, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace analytics tags in an organization

        ``PUT /orgs/{orgId}/analytics-tags``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/analytics-tags",
            query=_query({}, extra_query),
            body=_body({"ga4": ga4, "gtm": gtm, "segment": segment, "intercom": intercom, "plausible": plausible, "plausibleHost": plausible_host, "fathom": fathom, "umami": umami, "umamiHost": umami_host, "matomo": matomo, "matomoHost": matomo_host, "simpleAnalytics": simple_analytics, "posthog": posthog, "posthogHost": posthog_host}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

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
