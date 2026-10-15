from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EmbedFeedsResource:
    """``client.embed_feeds`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EmbedFeedsListResponse:
        """List embed feeds in an organization

        ``GET /orgs/{orgId}/embed-feeds``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/embed-feeds",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/embed-feeds",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def add(
        self,
        org_id: str,
        *,
        space_id: str,
        feed_url: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        author: Union[Optional[str], NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        poll_interval_minutes: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EmbedFeedsAddResponse:
        """Create an embed feed in an organization

        ``POST /orgs/{orgId}/embed-feeds``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/embed-feeds",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "feedUrl": feed_url, "categoryId": category_id, "author": author, "enabled": enabled, "pollIntervalMinutes": poll_interval_minutes}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        feed_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        author: Union[Optional[str], NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        poll_interval_minutes: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EmbedFeedsUpdateResponse:
        """Update the embed feed

        ``PATCH /orgs/{orgId}/embed-feeds/{feedId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/embed-feeds/{_path(feed_id)}",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "categoryId": category_id, "author": author, "enabled": enabled, "pollIntervalMinutes": poll_interval_minutes}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        feed_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EmbedFeedsRemoveResponse:
        """Delete the embed feed

        ``DELETE /orgs/{orgId}/embed-feeds/{feedId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/embed-feeds/{_path(feed_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def poll_now(
        self,
        org_id: str,
        feed_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EmbedFeedsPollNowResponse:
        """Create the poll in an organization

        ``POST /orgs/{orgId}/embed-feeds/{feedId}/poll``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/embed-feeds/{_path(feed_id)}/poll",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
