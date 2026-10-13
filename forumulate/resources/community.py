from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class CommunityBadgeQueryGrantsResource:
    """``client.community.badge_query_grants`` (6 operations)."""

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
    ) -> CommunityBadgeQueryGrantsListResponse:
        """List badge query grants in an organization

        ``GET /orgs/{orgId}/admin/badge-query-grants``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/admin/badge-query-grants",
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
    ) -> Iterator[CommunityBadgeQueryGrantsListResponseRule]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/admin/badge-query-grants",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="rules",
        )

    def create(
        self,
        org_id: str,
        *,
        badge_slug: str,
        sql: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityBadgeQueryGrantsCreateResponse:
        """Create a badge query grant in an organization

        ``POST /orgs/{orgId}/admin/badge-query-grants``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/admin/badge-query-grants",
            query=_query({}, extra_query),
            body=_body({"badgeSlug": badge_slug, "sql": sql, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        rule_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        badge_slug: Union[str, NotGiven] = NOT_GIVEN,
        sql: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityBadgeQueryGrantsUpdateResponse:
        """Update the badge query grant

        ``PATCH /orgs/{orgId}/admin/badge-query-grants/{ruleId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/admin/badge-query-grants/{_path(rule_id)}",
            query=_query({}, extra_query),
            body=_body({"badgeSlug": badge_slug, "sql": sql, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        rule_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityBadgeQueryGrantsRemoveResponse:
        """Delete the badge query grant

        ``DELETE /orgs/{orgId}/admin/badge-query-grants/{ruleId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/admin/badge-query-grants/{_path(rule_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def run_one(
        self,
        org_id: str,
        rule_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityBadgeQueryGrantsRunOneResponse:
        """Run the badge query grant

        ``POST /orgs/{orgId}/admin/badge-query-grants/{ruleId}/run``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/admin/badge-query-grants/{_path(rule_id)}/run",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def run_all(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityBadgeQueryGrantsRunAllResponse:
        """Run the badge query grant (create)

        ``POST /orgs/{orgId}/admin/badge-query-grants/run``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/admin/badge-query-grants/run",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class CommunityCannedRepliesResource:
    """``client.community.canned_replies`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityCannedRepliesListResponse:
        """List canned replies in an organization

        ``GET /orgs/{orgId}/community/canned-replies``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/canned-replies",
            query=_query({"spaceId": space_id, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CannedReplyRow]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/canned-replies",
            query=_query({"spaceId": space_id, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="cannedReplies",
        )

    def create(
        self,
        org_id: str,
        *,
        title: str,
        body: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityCannedRepliesCreateResponse:
        """Create a canned reply in an organization

        ``POST /orgs/{orgId}/community/canned-replies``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/canned-replies",
            query=_query({}, extra_query),
            body=_body({"title": title, "body": body, "spaceId": space_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        body: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityCannedRepliesUpdateResponse:
        """Update the canned reply

        ``PATCH /orgs/{orgId}/community/canned-replies/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/community/canned-replies/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityCannedRepliesRemoveResponse:
        """Delete the canned reply

        ``DELETE /orgs/{orgId}/community/canned-replies/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/canned-replies/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def use(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityCannedRepliesUseResponse:
        """Create the use in an organization

        ``POST /orgs/{orgId}/community/canned-replies/{id}/use``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/canned-replies/{_path(id)}/use",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class CommunityExtrasResource:
    """``client.community.extras`` (18 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list_saved(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasListSavedResponse:
        """List saved searches in an organization

        ``GET /orgs/{orgId}/community/saved-searches``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/saved-searches",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_saved_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[SavedSearchRow]:
        """Iterate every item of ``list_saved`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/saved-searches",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="searches",
        )

    def save(
        self,
        org_id: str,
        *,
        name: str,
        query: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        notify: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasSaveResponse:
        """Create a saved search in an organization

        ``POST /orgs/{orgId}/community/saved-searches``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/saved-searches",
            query=_query({}, extra_query),
            body=_body({"name": name, "query": query, "notify": notify}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_saved_notify(
        self,
        org_id: str,
        id: str,
        *,
        notify: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasSetSavedNotifyResponse:
        """Create the notify in an organization

        ``POST /orgs/{orgId}/community/saved-searches/{id}/notify``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/saved-searches/{_path(id)}/notify",
            query=_query({}, extra_query),
            body=_body({"notify": notify}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_saved(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasRemoveSavedResponse:
        """Delete the saved search

        ``DELETE /orgs/{orgId}/community/saved-searches/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/saved-searches/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def cakeday(
        self,
        org_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasCakedayResponse:
        """Get the cakeday in an organization

        ``GET /orgs/{orgId}/community/cakeday``

        :param days: Window length.
        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/cakeday",
            query=_query({"days": days, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def cakeday_all(
        self,
        org_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CakedayRow]:
        """Iterate every item of ``cakeday`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/cakeday",
            query=_query({"days": days, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="cakedays",
        )

    def list_notes(
        self,
        org_id: str,
        user_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasListNotesResponse:
        """List notes in an organization

        ``GET /orgs/{orgId}/community/members/{userId}/notes``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/members/{_path(user_id)}/notes",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_notes_all(
        self,
        org_id: str,
        user_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[UserNoteRow]:
        """Iterate every item of ``list_notes`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/members/{_path(user_id)}/notes",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="notes",
        )

    def add_note(
        self,
        org_id: str,
        user_id: str,
        *,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasAddNoteResponse:
        """Create a note in an organization

        ``POST /orgs/{orgId}/community/members/{userId}/notes``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/members/{_path(user_id)}/notes",
            query=_query({}, extra_query),
            body=_body({"body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_note(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasRemoveNoteResponse:
        """Delete the note

        ``DELETE /orgs/{orgId}/community/notes/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/notes/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ack_status(
        self,
        org_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasAckStatusResponse:
        """Get the ack status in an organization

        ``GET /orgs/{orgId}/community/topics/{topicId}/ack-status``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/topics/{_path(topic_id)}/ack-status",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def acknowledge(
        self,
        org_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasAcknowledgeResponse:
        """Create the acknowledge in an organization

        ``POST /orgs/{orgId}/community/topics/{topicId}/acknowledge``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/topics/{_path(topic_id)}/acknowledge",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_policy(
        self,
        org_id: str,
        topic_id: str,
        *,
        requires_ack: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasSetPolicyResponse:
        """Create the policy in an organization

        ``POST /orgs/{orgId}/community/topics/{topicId}/policy``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/topics/{_path(topic_id)}/policy",
            query=_query({}, extra_query),
            body=_body({"requiresAck": requires_ack}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def assign(
        self,
        org_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        assignee_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        assigned_group_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasAssignResponse:
        """Assign the topic

        ``POST /orgs/{orgId}/community/topics/{topicId}/assign``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/topics/{_path(topic_id)}/assign",
            query=_query({}, extra_query),
            body=_body({"assigneeId": assignee_id, "assignedGroupId": assigned_group_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_event(
        self,
        org_id: str,
        topic_id: str,
        *,
        event_at: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasSetEventResponse:
        """Create the event in an organization

        ``POST /orgs/{orgId}/community/topics/{topicId}/event``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/topics/{_path(topic_id)}/event",
            query=_query({}, extra_query),
            body=_body({"eventAt": event_at}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def events(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasEventsResponse:
        """List events in a space (community)

        ``GET /orgs/{orgId}/community/spaces/{spaceId}/events``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def events_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CommunityExtrasEventsResponseEvent]:
        """Iterate every item of ``events`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="events",
        )

    def rsvp_state(
        self,
        org_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasRsvpStateResponse:
        """Get the rsvp in an organization

        ``GET /orgs/{orgId}/community/topics/{topicId}/rsvp``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/topics/{_path(topic_id)}/rsvp",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def rsvp(
        self,
        org_id: str,
        topic_id: str,
        *,
        status: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasRsvpResponse:
        """Create the rsvp in an organization

        ``POST /orgs/{orgId}/community/topics/{topicId}/rsvp``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/topics/{_path(topic_id)}/rsvp",
            query=_query({}, extra_query),
            body=_body({"status": status}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def preview(
        self,
        org_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasPreviewResponse:
        """Preview the topic

        ``GET /orgs/{orgId}/community/topics/{topicId}/preview``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/topics/{_path(topic_id)}/preview",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def yearly_review(
        self,
        org_id: str,
        *,
        year: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityExtrasYearlyReviewResponse:
        """Get the yearly review in an organization

        ``GET /orgs/{orgId}/community/me/yearly-review``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/me/yearly-review",
            query=_query({"year": year}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class CommunityRelationshipsResource:
    """``client.community.relationships`` (8 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def set_status(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        emoji: Union[Optional[str], NotGiven] = NOT_GIVEN,
        message: Union[Optional[str], NotGiven] = NOT_GIVEN,
        until: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityRelationshipsSetStatusResponse:
        """Create the status in an organization

        ``POST /orgs/{orgId}/community/status``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/status",
            query=_query({}, extra_query),
            body=_body({"emoji": emoji, "message": message, "until": until}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def clear_status(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityRelationshipsClearStatusResponse:
        """Delete the status in an organization

        ``DELETE /orgs/{orgId}/community/status``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/status",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityRelationshipsListResponse:
        """Get the ignored in an organization

        ``GET /orgs/{orgId}/community/ignored``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/ignored",
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
    ) -> Iterator[RelationshipRow]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/ignored",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="relationships",
        )

    def mute(
        self,
        org_id: str,
        target_user_id: str,
        *,
        mode: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        expires_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityRelationshipsMuteResponse:
        """Mute the member

        ``POST /orgs/{orgId}/community/members/{targetUserId}/mute``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/members/{_path(target_user_id)}/mute",
            query=_query({}, extra_query),
            body=_body({"mode": mode, "expiresAt": expires_at}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unmute(
        self,
        org_id: str,
        target_user_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityRelationshipsUnmuteResponse:
        """Mute the member (delete)

        ``DELETE /orgs/{orgId}/community/members/{targetUserId}/mute``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/members/{_path(target_user_id)}/mute",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def follow(
        self,
        org_id: str,
        target_user_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityRelationshipsFollowResponse:
        """Follow the member

        ``POST /orgs/{orgId}/community/members/{targetUserId}/follow``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/members/{_path(target_user_id)}/follow",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unfollow(
        self,
        org_id: str,
        target_user_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityRelationshipsUnfollowResponse:
        """Follow the member (delete)

        ``DELETE /orgs/{orgId}/community/members/{targetUserId}/follow``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/members/{_path(target_user_id)}/follow",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def card(
        self,
        org_id: str,
        target_user_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityRelationshipsCardResponse:
        """Get the card in an organization

        ``GET /orgs/{orgId}/community/members/{targetUserId}/card``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/members/{_path(target_user_id)}/card",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class CommunityReputationResource:
    """``client.community.reputation`` (22 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def profile(
        self,
        org_id: str,
        user_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationProfileResponse:
        """Get the profile in an organization

        ``GET /orgs/{orgId}/community/members/{userId}/profile``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/members/{_path(user_id)}/profile",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def catalog(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationCatalogResponse:
        """Get the catalog in an organization (community reputation)

        ``GET /orgs/{orgId}/community/reputation/catalog``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/reputation/catalog",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def create_badge(
        self,
        org_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        icon: Union[str, NotGiven] = NOT_GIVEN,
        tier: Union[str, NotGiven] = NOT_GIVEN,
        grouping: Union[Optional[str], NotGiven] = NOT_GIVEN,
        counter: Union[Optional[str], NotGiven] = NOT_GIVEN,
        threshold: Union[Optional[int], NotGiven] = NOT_GIVEN,
        allow_title: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationCreateBadgeResponse:
        """Create a badge in an organization

        ``POST /orgs/{orgId}/community/reputation/badges``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/reputation/badges",
            query=_query({}, extra_query),
            body=_body({"slug": slug, "name": name, "description": description, "icon": icon, "tier": tier, "grouping": grouping, "counter": counter, "threshold": threshold, "allowTitle": allow_title}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_badge(
        self,
        org_id: str,
        badge_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        icon: Union[str, NotGiven] = NOT_GIVEN,
        tier: Union[str, NotGiven] = NOT_GIVEN,
        grouping: Union[Optional[str], NotGiven] = NOT_GIVEN,
        counter: Union[Optional[str], NotGiven] = NOT_GIVEN,
        threshold: Union[Optional[int], NotGiven] = NOT_GIVEN,
        allow_title: Union[bool, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationUpdateBadgeResponse:
        """Create the badge

        ``POST /orgs/{orgId}/community/reputation/badges/{badgeId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/reputation/badges/{_path(badge_id)}",
            query=_query({}, extra_query),
            body=_body({"slug": slug, "name": name, "description": description, "icon": icon, "tier": tier, "grouping": grouping, "counter": counter, "threshold": threshold, "allowTitle": allow_title, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_badge(
        self,
        org_id: str,
        badge_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationDeleteBadgeResponse:
        """Delete the badge

        ``DELETE /orgs/{orgId}/community/reputation/badges/{badgeId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/reputation/badges/{_path(badge_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def grant_badge(
        self,
        org_id: str,
        user_id: str,
        *,
        slug: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationGrantBadgeResponse:
        """Create a badge in an organization (for a user)

        ``POST /orgs/{orgId}/community/reputation/{userId}/badges``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/reputation/{_path(user_id)}/badges",
            query=_query({}, extra_query),
            body=_body({"slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke_badge(
        self,
        org_id: str,
        user_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationRevokeBadgeResponse:
        """Delete the badge (for a user and a named one)

        ``DELETE /orgs/{orgId}/community/reputation/{userId}/badges/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/reputation/{_path(user_id)}/badges/{_path(slug)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def recompute(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationRecomputeResponse:
        """Create the recompute in an organization

        ``POST /orgs/{orgId}/community/reputation/recompute``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/reputation/recompute",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def me(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationMeResponse:
        """Your reputation in an organization

        ``GET /orgs/{orgId}/community/reputation/me``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/reputation/me",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_external(
        self,
        org_id: str,
        user_id: str,
        *,
        source: str,
        label: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        value: Union[Optional[int], NotGiven] = NOT_GIVEN,
        tier: Union[Optional[str], NotGiven] = NOT_GIVEN,
        profile_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        icon: Union[Optional[str], NotGiven] = NOT_GIVEN,
        icon_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationSetExternalResponse:
        """Replace the external in an organization

        ``PUT /orgs/{orgId}/community/reputation/{userId}/external``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/community/reputation/{_path(user_id)}/external",
            query=_query({}, extra_query),
            body=_body({"source": source, "label": label, "value": value, "tier": tier, "profileUrl": profile_url, "icon": icon, "iconUrl": icon_url}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_external(
        self,
        org_id: str,
        user_id: str,
        source: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationRemoveExternalResponse:
        """Delete the external

        ``DELETE /orgs/{orgId}/community/reputation/{userId}/external/{source}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/reputation/{_path(user_id)}/external/{_path(source)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def external_leaderboard(
        self,
        org_id: str,
        source: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExternalLeaderboardDto:
        """Get the leaderboard in an organization (external)

        ``GET /orgs/{orgId}/community/reputation/external/{source}/leaderboard``

        :param limit: Members on the board.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/reputation/external/{_path(source)}/leaderboard",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get_featured(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationGetFeaturedResponse:
        """Get the featured in an organization

        ``GET /orgs/{orgId}/community/reputation/me/featured``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/reputation/me/featured",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_featured(
        self,
        org_id: str,
        *,
        slugs: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationSetFeaturedResponse:
        """Replace the featured in an organization

        ``PUT /orgs/{orgId}/community/reputation/me/featured``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/community/reputation/me/featured",
            query=_query({}, extra_query),
            body=_body({"slugs": slugs}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_featured_topic(
        self,
        org_id: str,
        *,
        topic_id: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationSetFeaturedTopicResponse:
        """Replace the featured topic in an organization

        ``PUT /orgs/{orgId}/community/reputation/me/featured-topic``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/community/reputation/me/featured-topic",
            query=_query({}, extra_query),
            body=_body({"topicId": topic_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_backgrounds(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        profile_background_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        card_background_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationSetBackgroundsResponse:
        """Replace backgrounds in an organization

        ``PUT /orgs/{orgId}/community/reputation/me/backgrounds``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/community/reputation/me/backgrounds",
            query=_query({}, extra_query),
            body=_body({"profileBackgroundUrl": profile_background_url, "cardBackgroundUrl": card_background_url}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def leaderboard(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationLeaderboardResponse:
        """Get the leaderboard in an organization

        ``GET /orgs/{orgId}/community/reputation/leaderboard``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/reputation/leaderboard",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def leaderboard_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CommunityReputationLeaderboardResponseLeader]:
        """Iterate every item of ``leaderboard`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/reputation/leaderboard",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="leaders",
        )

    def points_leaderboard(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationPointsLeaderboardResponse:
        """List points in an organization

        ``GET /orgs/{orgId}/community/reputation/points``

        :param limit: Members on the board.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/reputation/points",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def directory(
        self,
        org_id: str,
        *,
        page_size: Union[int, NotGiven] = NOT_GIVEN,
        search: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        period: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationDirectoryResponse:
        """Get the directory in an organization

        ``GET /orgs/{orgId}/community/directory``

        :param page_size: Members per page.
        :param page: Which page of results to return, 1-based.
        :param limit: Rows per page — the spelling used everywhere else in this API.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/directory",
            query=_query({"pageSize": page_size, "search": search, "page": page, "period": period, "cursor": cursor, "limit": limit, "order": order, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def directory_all(
        self,
        org_id: str,
        *,
        page_size: Union[int, NotGiven] = NOT_GIVEN,
        search: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        period: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``directory`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/directory",
            query=_query({"pageSize": page_size, "search": search, "page": page, "period": period, "limit": limit, "order": order, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="members",
        )

    def for_user(
        self,
        org_id: str,
        user_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationForUserResponse:
        """Get the reputation

        ``GET /orgs/{orgId}/community/reputation/{userId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/reputation/{_path(user_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_level(
        self,
        org_id: str,
        user_id: str,
        *,
        level: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationSetLevelResponse:
        """Create the level in an organization

        ``POST /orgs/{orgId}/community/reputation/{userId}/level``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/reputation/{_path(user_id)}/level",
            query=_query({}, extra_query),
            body=_body({"level": level}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unfurl_link(
        self,
        org_id: str,
        *,
        url: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReputationUnfurlLinkResponse:
        """Get the unfurl in an organization

        ``GET /orgs/{orgId}/community/unfurl``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/unfurl",
            query=_query({"url": url}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class CommunityResource:
    """``client.community`` (9 operations; badge_query_grants, canned_replies, extras, relationships, reputation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.badge_query_grants = CommunityBadgeQueryGrantsResource(client)
        self.canned_replies = CommunityCannedRepliesResource(client)
        self.extras = CommunityExtrasResource(client)
        self.relationships = CommunityRelationshipsResource(client)
        self.reputation = CommunityReputationResource(client)

    def analytics_summary(
        self,
        org_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        contributors: Union[int, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityAnalytics:
        """List analytics in an organization

        ``GET /orgs/{orgId}/community/analytics``

        :param days: Window length.
        :param contributors: Top contributors returned.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/analytics",
            query=_query({"days": days, "contributors": contributors, "spaceId": space_id}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def reactions(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityReactionsResponse:
        """List reactions in an organization

        ``GET /orgs/{orgId}/community/reactions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/reactions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def reactions_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``reactions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/reactions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="emojis",
        )

    def set_reactions(
        self,
        org_id: str,
        *,
        emojis: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunitySetReactionsResponse:
        """Create a reaction in an organization

        ``POST /orgs/{orgId}/community/reactions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/reactions",
            query=_query({}, extra_query),
            body=_body({"emojis": emojis}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_custom_reactions(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityListCustomReactionsResponse:
        """Get the custom in an organization

        ``GET /orgs/{orgId}/community/reactions/custom``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/reactions/custom",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_custom_reactions_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CustomReaction]:
        """Iterate every item of ``list_custom_reactions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/reactions/custom",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="reactions",
        )

    def upload_custom_reaction(
        self,
        org_id: str,
        *,
        file: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityUploadCustomReactionResponse:
        """Create the custom in an organization

        ``POST /orgs/{orgId}/community/reactions/custom``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/community/reactions/custom",
            query=_query({}, extra_query),
            body=_body({"file": file}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_custom_reaction(
        self,
        org_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityDeleteCustomReactionResponse:
        """Delete the custom

        ``DELETE /orgs/{orgId}/community/reactions/custom/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/community/reactions/custom/{_path(slug)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def tag_feed(
        self,
        org_id: str,
        tag: str,
        *,
        page_size: Union[int, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityTagFeedResponse:
        """Get the tag (community)

        ``GET /orgs/{orgId}/community/tags/{tag}``

        :param page_size: Items per page.
        :param page: Which page of results to return, 1-based.
        :param limit: Rows per page — the spelling used everywhere else in this API.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/tags/{_path(tag)}",
            query=_query({"pageSize": page_size, "page": page, "cursor": cursor, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def tag_feed_all(
        self,
        org_id: str,
        tag: str,
        *,
        page_size: Union[int, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ArticleSummary]:
        """Iterate every item of ``tag_feed`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/tags/{_path(tag)}",
            query=_query({"pageSize": page_size, "page": page, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="items",
        )

    def search(
        self,
        org_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunitySearchResponse:
        """Get the search in an organization (community)

        ``GET /orgs/{orgId}/community/search``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/search",
            query=_query({"q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def bookmarks(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CommunityBookmarksResponse:
        """List bookmarks in an organization (community)

        ``GET /orgs/{orgId}/community/bookmarks``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/community/bookmarks",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def bookmarks_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ArticleSummary]:
        """Iterate every item of ``bookmarks`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/community/bookmarks",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="articles",
        )
