from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ApiActivityResource:
    """``client.api_activity`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def mine(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ApiActivityMineResponse:
        """Get the API activity in an organization

        ``GET /orgs/{orgId}/api-activity``

        :param limit: Calls listed, newest first.
        :param page: Which page of results to return, 1-based.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/api-activity",
            query=_query({"limit": limit, "cursor": cursor, "page": page}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def mine_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ApiCall]:
        """Iterate every item of ``mine`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/api-activity",
            query=_query({"limit": limit, "page": page}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="calls",
        )
