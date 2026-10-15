from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class MyActivityResource:
    """``client.my_activity`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MyActivityPage:
        """The signed-in reader's own activity in this organization

        ``GET /public/orgs/{orgId}/me/activity``

        :param limit: Rows per page.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/me/activity",
            query=_query({"limit": limit, "type": type, "spaceId": space_id, "q": q, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/me/activity",
            query=_query({"limit": limit, "type": type, "spaceId": space_id, "q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def bulk(
        self,
        org_id: str,
        *,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        ids: Union[List[str], NotGiven] = NOT_GIVEN,
        all: Union[bool, NotGiven] = NOT_GIVEN,
        in_posts: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Remove, unreact, unbookmark or unwatch several of your rows at once

        ``POST /public/orgs/{orgId}/me/activity/bulk``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/me/activity/bulk",
            query=_query({}, extra_query),
            body=_body({"action": action, "ids": ids, "all": all, "inPosts": in_posts}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def export_all(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MyActivityExportAllResponse:
        """Download your activity in this organization (JSON)

        ``GET /public/orgs/{orgId}/me/export``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/me/export",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
