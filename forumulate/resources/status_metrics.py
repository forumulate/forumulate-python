from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class StatusMetricsResource:
    """``client.status_metrics`` (4 operations)."""

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
    ) -> StatusMetricsListResponse:
        """A status page's custom metrics, hidden ones included

        ``GET /orgs/{orgId}/spaces/{spaceId}/status/metrics``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/metrics",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/metrics",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def upsert(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        unit: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[Optional[str], NotGiven] = NOT_GIVEN,
        decimals: Union[int, NotGiven] = NOT_GIVEN,
        aggregate: Union[str, NotGiven] = NOT_GIVEN,
        visible: Union[bool, NotGiven] = NOT_GIVEN,
        sort_key: Union[int, NotGiven] = NOT_GIVEN,
        component: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusMetricsUpsertResponse:
        """Create a custom metric, or change what it says about itself

        ``PUT /orgs/{orgId}/spaces/{spaceId}/status/metrics/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/metrics/{_path(key)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "unit": unit, "description": description, "decimals": decimals, "aggregate": aggregate, "visible": visible, "sortKey": sort_key, "component": component}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusMetricsRemoveResponse:
        """Delete a custom metric and every point of it

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/status/metrics/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/metrics/{_path(key)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def push(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        value: Union[float, NotGiven] = NOT_GIVEN,
        at: Union[str, NotGiven] = NOT_GIVEN,
        points: Union[List[StatusMetricsPushParamsPoint], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Push points to a custom metric

        ``POST /orgs/{orgId}/spaces/{spaceId}/status/metrics/{key}/points``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/metrics/{_path(key)}/points",
            query=_query({}, extra_query),
            body=_body({"value": value, "at": at, "points": points}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
