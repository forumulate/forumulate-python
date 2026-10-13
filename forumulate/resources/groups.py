from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class GroupsGrantsResource:
    """``client.groups.grants`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        group_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsGrantsListResponse:
        """List group grants in an organization

        ``GET /orgs/{orgId}/group-grants``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/group-grants",
            query=_query({"spaceId": space_id, "groupId": group_id, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        group_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[GroupGrantRow]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/group-grants",
            query=_query({"spaceId": space_id, "groupId": group_id, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="grants",
        )

    def grant(
        self,
        org_id: str,
        *,
        group_id: str,
        role: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        effect: Union[str, NotGiven] = NOT_GIVEN,
        custom_role_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsGrantsGrantResponse:
        """Create a group grant in an organization

        ``POST /orgs/{orgId}/group-grants``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/group-grants",
            query=_query({}, extra_query),
            body=_body({"groupId": group_id, "role": role, "spaceId": space_id, "effect": effect, "customRoleId": custom_role_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsGrantsRevokeResponse:
        """Delete the group grant

        ``DELETE /orgs/{orgId}/group-grants/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/group-grants/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class GroupsIdentityResource:
    """``client.groups.identity`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def options(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IdentityOptions:
        """Get the group identity in an organization

        ``GET /orgs/{orgId}/group-identity``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/group-identity",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[Optional[str], NotGiven] = NOT_GIVEN,
        primary_group_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the group identity in an organization

        ``PUT /orgs/{orgId}/group-identity``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/group-identity",
            query=_query({}, extra_query),
            body=_body({"title": title, "primaryGroupId": primary_group_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class GroupsMailboxResource:
    """``client.groups.mailbox`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        group_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsMailboxGetResponse:
        """Get the mailbox in an organization

        ``GET /orgs/{orgId}/groups/{groupId}/mailbox``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/mailbox",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        group_id: str,
        *,
        from_email: str,
        config: GroupsMailboxSetParamsConfig,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsMailboxSetResponse:
        """Replace the mailbox in an organization

        ``PUT /orgs/{orgId}/groups/{groupId}/mailbox``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/mailbox",
            query=_query({}, extra_query),
            body=_body({"fromEmail": from_email, "enabled": enabled, "config": config}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def clear(
        self,
        org_id: str,
        group_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsMailboxClearResponse:
        """Delete the mailbox in an organization

        ``DELETE /orgs/{orgId}/groups/{groupId}/mailbox``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/mailbox",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class GroupsMessagesResource:
    """``client.groups.messages`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def message(
        self,
        org_id: str,
        group_id: str,
        *,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsMessagesMessageResponse:
        """Create the message in an organization

        ``POST /orgs/{orgId}/groups/{groupId}/message``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/message",
            query=_query({}, extra_query),
            body=_body({"body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def inbox(
        self,
        org_id: str,
        group_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsMessagesInboxResponse:
        """Get the inbox in an organization

        ``GET /orgs/{orgId}/groups/{groupId}/inbox``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/inbox",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def inbox_all(
        self,
        org_id: str,
        group_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ChannelSummary]:
        """Iterate every item of ``inbox`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/inbox",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="threads",
        )


class GroupsResource:
    """``client.groups`` (11 operations; grants, identity, mailbox, messages)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.grants = GroupsGrantsResource(client)
        self.identity = GroupsIdentityResource(client)
        self.mailbox = GroupsMailboxResource(client)
        self.messages = GroupsMessagesResource(client)

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsListResponse:
        """List groups in an organization

        ``GET /orgs/{orgId}/groups``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/groups",
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
    ) -> Iterator[GroupSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/groups",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="groups",
        )

    def create(
        self,
        org_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        visibility: Union[str, NotGiven] = NOT_GIVEN,
        join_policy: Union[str, NotGiven] = NOT_GIVEN,
        flair: Union[Optional[str], NotGiven] = NOT_GIVEN,
        title: Union[Optional[str], NotGiven] = NOT_GIVEN,
        flair_icon: Union[Optional[str], NotGiven] = NOT_GIVEN,
        flair_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        flair_bg_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        bio: Union[Optional[str], NotGiven] = NOT_GIVEN,
        grant_trust_level: Union[Optional[int], NotGiven] = NOT_GIVEN,
        auto_join_domains: Union[Optional[str], NotGiven] = NOT_GIVEN,
        members_visibility: Union[str, NotGiven] = NOT_GIVEN,
        mentionable_level: Union[str, NotGiven] = NOT_GIVEN,
        messageable_level: Union[str, NotGiven] = NOT_GIVEN,
        default_notification_level: Union[str, NotGiven] = NOT_GIVEN,
        watched_category_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        watched_tag_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        category_notification_defaults: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        tag_notification_defaults: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsCreateResponse:
        """Create a group in an organization

        ``POST /orgs/{orgId}/groups``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/groups",
            query=_query({}, extra_query),
            body=_body({"name": name, "description": description, "visibility": visibility, "joinPolicy": join_policy, "flair": flair, "title": title, "flairIcon": flair_icon, "flairColor": flair_color, "flairBgColor": flair_bg_color, "bio": bio, "grantTrustLevel": grant_trust_level, "autoJoinDomains": auto_join_domains, "membersVisibility": members_visibility, "mentionableLevel": mentionable_level, "messageableLevel": messageable_level, "defaultNotificationLevel": default_notification_level, "watchedCategoryIds": watched_category_ids, "watchedTagIds": watched_tag_ids, "categoryNotificationDefaults": category_notification_defaults, "tagNotificationDefaults": tag_notification_defaults}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        group_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsGetResponse:
        """Get the group (orgs groups)

        ``GET /orgs/{orgId}/groups/{groupId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        group_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        visibility: Union[str, NotGiven] = NOT_GIVEN,
        join_policy: Union[str, NotGiven] = NOT_GIVEN,
        flair: Union[Optional[str], NotGiven] = NOT_GIVEN,
        title: Union[Optional[str], NotGiven] = NOT_GIVEN,
        flair_icon: Union[Optional[str], NotGiven] = NOT_GIVEN,
        flair_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        flair_bg_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        bio: Union[Optional[str], NotGiven] = NOT_GIVEN,
        grant_trust_level: Union[Optional[int], NotGiven] = NOT_GIVEN,
        auto_join_domains: Union[Optional[str], NotGiven] = NOT_GIVEN,
        members_visibility: Union[str, NotGiven] = NOT_GIVEN,
        mentionable_level: Union[str, NotGiven] = NOT_GIVEN,
        messageable_level: Union[str, NotGiven] = NOT_GIVEN,
        default_notification_level: Union[str, NotGiven] = NOT_GIVEN,
        watched_category_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        watched_tag_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        category_notification_defaults: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        tag_notification_defaults: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        inbox_email: Union[Optional[str], NotGiven] = NOT_GIVEN,
        inbox_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsUpdateResponse:
        """Update the group (orgs groups)

        ``PATCH /orgs/{orgId}/groups/{groupId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "description": description, "visibility": visibility, "joinPolicy": join_policy, "flair": flair, "title": title, "flairIcon": flair_icon, "flairColor": flair_color, "flairBgColor": flair_bg_color, "bio": bio, "grantTrustLevel": grant_trust_level, "autoJoinDomains": auto_join_domains, "membersVisibility": members_visibility, "mentionableLevel": mentionable_level, "messageableLevel": messageable_level, "defaultNotificationLevel": default_notification_level, "watchedCategoryIds": watched_category_ids, "watchedTagIds": watched_tag_ids, "categoryNotificationDefaults": category_notification_defaults, "tagNotificationDefaults": tag_notification_defaults, "inboxEmail": inbox_email, "inboxEnabled": inbox_enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        group_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsRemoveResponse:
        """Delete the group (orgs groups)

        ``DELETE /orgs/{orgId}/groups/{groupId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def add_member(
        self,
        org_id: str,
        group_id: str,
        *,
        user_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        is_manager: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsAddMemberResponse:
        """Create a member in an organization (groups)

        ``POST /orgs/{orgId}/groups/{groupId}/members``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/members",
            query=_query({}, extra_query),
            body=_body({"userId": user_id, "isManager": is_manager}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_member(
        self,
        org_id: str,
        group_id: str,
        user_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsRemoveMemberResponse:
        """Delete the member (groups)

        ``DELETE /orgs/{orgId}/groups/{groupId}/members/{userId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/members/{_path(user_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def join(
        self,
        org_id: str,
        group_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsJoinResponse:
        """Join the group

        ``POST /orgs/{orgId}/groups/{groupId}/join``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/join",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def leave(
        self,
        org_id: str,
        group_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsLeaveResponse:
        """Leave the group

        ``POST /orgs/{orgId}/groups/{groupId}/leave``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/leave",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def requests(
        self,
        org_id: str,
        group_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsRequestsResponse:
        """List requests in an organization

        ``GET /orgs/{orgId}/groups/{groupId}/requests``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/requests",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def requests_all(
        self,
        org_id: str,
        group_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[JoinRequestRow]:
        """Iterate every item of ``requests`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/requests",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="requests",
        )

    def review(
        self,
        org_id: str,
        group_id: str,
        request_id: str,
        *,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GroupsReviewResponse:
        """Create the request

        ``POST /orgs/{orgId}/groups/{groupId}/requests/{requestId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/groups/{_path(group_id)}/requests/{_path(request_id)}",
            query=_query({}, extra_query),
            body=_body({"action": action}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
