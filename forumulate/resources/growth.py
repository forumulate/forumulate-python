from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class GrowthResource:
    """``client.growth`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def conversions(
        self,
        org_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        space: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConversionsReport:
        """List conversions in an organization

        ``GET /orgs/{orgId}/analytics/conversions``

        :param days: Window length.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/analytics/conversions",
            query=_query({"days": days, "space": space}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def settle(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        status: Union[str, NotGiven] = NOT_GIVEN,
        winner: Union[Optional[str], NotGiven] = NOT_GIVEN,
        auto_pick: Union[bool, NotGiven] = NOT_GIVEN,
        goal: Union[Optional[str], NotGiven] = NOT_GIVEN,
        min_visitors: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GrowthSettleResponse:
        """Replace the experiment

        ``PUT /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/experiments/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/experiments/{_path(key)}",
            query=_query({}, extra_query),
            body=_body({"status": status, "winner": winner, "autoPick": auto_pick, "goal": goal, "minVisitors": min_visitors}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
