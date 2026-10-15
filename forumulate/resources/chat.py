from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ChatIncomingWebhooksResource:
    """``client.chat.incoming_webhooks`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def post(
        self,
        webhook_id: str,
        *,
        secret: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        text: Union[str, NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatIncomingWebhooksPostResponse:
        """Create the incoming

        ``POST /chat/incoming/{webhookId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/chat/incoming/{_path(webhook_id)}",
            query=_query({"secret": secret}, extra_query),
            body=_body({"text": text, "body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ChatMessagesResource:
    """``client.chat.messages`` (14 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def thread(
        self,
        org_id: str,
        message_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesThreadResponse:
        """Get the thread in an organization

        ``GET /orgs/{orgId}/chat/messages/{messageId}/thread``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}/thread",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def thread_all(
        self,
        org_id: str,
        message_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``thread`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}/thread",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def edit(
        self,
        org_id: str,
        message_id: str,
        *,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesEditResponse:
        """Update the message

        ``PATCH /orgs/{orgId}/chat/messages/{messageId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}",
            query=_query({}, extra_query),
            body=_body({"body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        message_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesRemoveResponse:
        """Delete the message

        ``DELETE /orgs/{orgId}/chat/messages/{messageId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def react(
        self,
        org_id: str,
        message_id: str,
        *,
        emoji: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesReactResponse:
        """Create the react in an organization

        ``POST /orgs/{orgId}/chat/messages/{messageId}/react``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}/react",
            query=_query({}, extra_query),
            body=_body({"emoji": emoji}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def dm(
        self,
        org_id: str,
        *,
        user_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesDmResponse:
        """Open a direct message

        ``POST /orgs/{orgId}/chat/dm``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/dm",
            query=_query({}, extra_query),
            body=_body({"userId": user_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def group_dm(
        self,
        org_id: str,
        *,
        user_ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesGroupDmResponse:
        """Open a group direct message

        ``POST /orgs/{orgId}/chat/dm/group``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/dm/group",
            query=_query({}, extra_query),
            body=_body({"userIds": user_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def message_link(
        self,
        org_id: str,
        message_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesMessageLinkResponse:
        """Get the link in an organization

        ``GET /orgs/{orgId}/chat/messages/{messageId}/link``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}/link",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def quote_to_topic(
        self,
        org_id: str,
        message_id: str,
        *,
        space_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesQuoteToTopicResponse:
        """Create the quote to topic in an organization

        ``POST /orgs/{orgId}/chat/messages/{messageId}/quote-to-topic``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}/quote-to-topic",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "title": title}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def flag(
        self,
        org_id: str,
        message_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        reason: Union[str, NotGiven] = NOT_GIVEN,
        flag_type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesFlagResponse:
        """Flag the message

        ``POST /orgs/{orgId}/chat/messages/{messageId}/flag``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}/flag",
            query=_query({}, extra_query),
            body=_body({"reason": reason, "flagType": flag_type}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bookmark(
        self,
        org_id: str,
        message_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesBookmarkResponse:
        """Create the bookmark in an organization

        ``POST /orgs/{orgId}/chat/messages/{messageId}/bookmark``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}/bookmark",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_bookmark(
        self,
        org_id: str,
        message_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesRemoveBookmarkResponse:
        """Delete the bookmark in an organization

        ``DELETE /orgs/{orgId}/chat/messages/{messageId}/bookmark``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}/bookmark",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bookmark_reminder(
        self,
        org_id: str,
        message_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        preset: Union[str, NotGiven] = NOT_GIVEN,
        remind_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        note: Union[Optional[str], NotGiven] = NOT_GIVEN,
        name: Union[Optional[str], NotGiven] = NOT_GIVEN,
        auto_delete: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesBookmarkReminderResponse:
        """Update the reminder in an organization

        ``PATCH /orgs/{orgId}/chat/messages/{messageId}/bookmark/reminder``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/chat/messages/{_path(message_id)}/bookmark/reminder",
            query=_query({}, extra_query),
            body=_body({"preset": preset, "remindAt": remind_at, "note": note, "name": name, "autoDelete": auto_delete}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_bookmarks(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesListBookmarksResponse:
        """List bookmarks in an organization (chat)

        ``GET /orgs/{orgId}/chat/bookmarks``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/bookmarks",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_bookmarks_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_bookmarks`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/chat/bookmarks",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def move(
        self,
        org_id: str,
        *,
        message_ids: List[str],
        target_channel_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        thread_parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatMessagesMoveResponse:
        """Move the message

        ``POST /orgs/{orgId}/chat/messages/move``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/messages/move",
            query=_query({}, extra_query),
            body=_body({"messageIds": message_ids, "targetChannelId": target_channel_id, "threadParentId": thread_parent_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ChatProvidersResource:
    """``client.chat.providers`` (4 operations)."""

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
    ) -> ChatProvidersListResponse:
        """List custom chat providers in an organization

        ``GET /orgs/{orgId}/custom-chat-providers``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/custom-chat-providers",
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
            f"/orgs/{_path(org_id)}/custom-chat-providers",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        *,
        id: str,
        name: str,
        description: str,
        icon: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        docs_url: Union[str, NotGiven] = NOT_GIVEN,
        fields: Union[List[ChatProvidersCreateParamsField], NotGiven] = NOT_GIVEN,
        embed: Union[ChatProvidersCreateParamsEmbed, NotGiven] = NOT_GIVEN,
        knowledge: Union[ChatProvidersCreateParamsKnowledge, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatProvidersCreateResponse:
        """Create a custom chat provider in an organization

        ``POST /orgs/{orgId}/custom-chat-providers``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/custom-chat-providers",
            query=_query({}, extra_query),
            body=_body({"id": id, "name": name, "description": description, "icon": icon, "docsUrl": docs_url, "fields": fields, "embed": embed, "knowledge": knowledge}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        slug: str,
        *,
        id: str,
        name: str,
        description: str,
        icon: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        docs_url: Union[str, NotGiven] = NOT_GIVEN,
        fields: Union[List[ChatProvidersUpdateParamsField], NotGiven] = NOT_GIVEN,
        embed: Union[ChatProvidersUpdateParamsEmbed, NotGiven] = NOT_GIVEN,
        knowledge: Union[ChatProvidersUpdateParamsKnowledge, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatProvidersUpdateResponse:
        """Replace the custom chat provider

        ``PUT /orgs/{orgId}/custom-chat-providers/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/custom-chat-providers/{_path(slug)}",
            query=_query({}, extra_query),
            body=_body({"id": id, "name": name, "description": description, "icon": icon, "docsUrl": docs_url, "fields": fields, "embed": embed, "knowledge": knowledge}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatProvidersRemoveResponse:
        """Delete the custom chat provider

        ``DELETE /orgs/{orgId}/custom-chat-providers/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/custom-chat-providers/{_path(slug)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ChatResource:
    """``client.chat`` (25 operations; incoming_webhooks, messages, providers)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.incoming_webhooks = ChatIncomingWebhooksResource(client)
        self.messages = ChatMessagesResource(client)
        self.providers = ChatProvidersResource(client)

    def channels(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatChannelsResponse:
        """List channels in an organization

        ``GET /orgs/{orgId}/chat/channels``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def channels_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``channels`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create_channel(
        self,
        org_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        visibility: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatCreateChannelResponse:
        """Create a channel in an organization

        ``POST /orgs/{orgId}/chat/channels``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels",
            query=_query({}, extra_query),
            body=_body({"name": name, "spaceId": space_id, "visibility": visibility}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def search(
        self,
        org_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatSearchResult:
        """Get the search in an organization (chat)

        ``GET /orgs/{orgId}/chat/search``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/search",
            query=_query({"q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def archive(
        self,
        org_id: str,
        channel_id: str,
        *,
        archived: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatArchiveResponse:
        """Archive the channel

        ``POST /orgs/{orgId}/chat/channels/{channelId}/archive``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/archive",
            query=_query({}, extra_query),
            body=_body({"archived": archived}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def close(
        self,
        org_id: str,
        channel_id: str,
        *,
        closed: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatCloseResponse:
        """Close the channel

        ``POST /orgs/{orgId}/chat/channels/{channelId}/close``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/close",
            query=_query({}, extra_query),
            body=_body({"closed": closed}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def archive_to_topic(
        self,
        org_id: str,
        channel_id: str,
        *,
        space_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatArchiveToTopicResponse:
        """Archive to topic in an organization

        ``POST /orgs/{orgId}/chat/channels/{channelId}/archive-to-topic``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/archive-to-topic",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "title": title}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_notification(
        self,
        org_id: str,
        channel_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        level: Union[str, NotGiven] = NOT_GIVEN,
        muted: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatSetNotificationResponse:
        """Update notifications in an organization

        ``PATCH /orgs/{orgId}/chat/channels/{channelId}/notifications``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/notifications",
            query=_query({}, extra_query),
            body=_body({"level": level, "muted": muted}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def join(
        self,
        org_id: str,
        channel_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatJoinResponse:
        """Join the channel

        ``POST /orgs/{orgId}/chat/channels/{channelId}/join``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/join",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def add_member(
        self,
        org_id: str,
        channel_id: str,
        *,
        user_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatAddMemberResponse:
        """Create a member in an organization (chat channels)

        ``POST /orgs/{orgId}/chat/channels/{channelId}/members``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/members",
            query=_query({}, extra_query),
            body=_body({"userId": user_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_messages(
        self,
        org_id: str,
        channel_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        before: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatListMessagesResponse:
        """List messages in an organization (chat channels)

        ``GET /orgs/{orgId}/chat/channels/{channelId}/messages``

        :param limit: Messages per page.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/messages",
            query=_query({"limit": limit, "before": before, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_messages_all(
        self,
        org_id: str,
        channel_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        before: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_messages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/messages",
            query=_query({"limit": limit, "before": before}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def send(
        self,
        org_id: str,
        channel_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        attachments: Union[List[ChatSendParamsAttachment], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatSendResponse:
        """Create a message in an organization (chat channels)

        ``POST /orgs/{orgId}/chat/channels/{channelId}/messages``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/messages",
            query=_query({}, extra_query),
            body=_body({"body": body, "parentId": parent_id, "attachments": attachments}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_settings(
        self,
        org_id: str,
        channel_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slow_mode_seconds: Union[int, NotGiven] = NOT_GIVEN,
        auto_join: Union[bool, NotGiven] = NOT_GIVEN,
        retention_days: Union[Optional[int], NotGiven] = NOT_GIVEN,
        allowed_group_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatUpdateSettingsResponse:
        """Update settings in an organization

        ``PATCH /orgs/{orgId}/chat/channels/{channelId}/settings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/settings",
            query=_query({}, extra_query),
            body=_body({"slowModeSeconds": slow_mode_seconds, "autoJoin": auto_join, "retentionDays": retention_days, "allowedGroupId": allowed_group_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_incoming_webhooks(
        self,
        org_id: str,
        channel_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatListIncomingWebhooksResponse:
        """List incoming webhooks in an organization

        ``GET /orgs/{orgId}/chat/channels/{channelId}/incoming-webhooks``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/incoming-webhooks",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_incoming_webhooks_all(
        self,
        org_id: str,
        channel_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_incoming_webhooks`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/incoming-webhooks",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create_incoming_webhook(
        self,
        org_id: str,
        channel_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create an incoming webhook in an organization

        ``POST /orgs/{orgId}/chat/channels/{channelId}/incoming-webhooks``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/incoming-webhooks",
            query=_query({}, extra_query),
            body=_body({"name": name}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke_incoming_webhook(
        self,
        org_id: str,
        webhook_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatRevokeIncomingWebhookResponse:
        """Delete the incoming webhook

        ``DELETE /orgs/{orgId}/chat/incoming-webhooks/{webhookId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/chat/incoming-webhooks/{_path(webhook_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def receipts(
        self,
        org_id: str,
        channel_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatReceiptsResponse:
        """List receipts in an organization

        ``GET /orgs/{orgId}/chat/channels/{channelId}/receipts``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/receipts",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def receipts_all(
        self,
        org_id: str,
        channel_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``receipts`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/receipts",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def pins(
        self,
        org_id: str,
        channel_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatPinsResponse:
        """List pins in an organization

        ``GET /orgs/{orgId}/chat/channels/{channelId}/pins``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/pins",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def pins_all(
        self,
        org_id: str,
        channel_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``pins`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/pins",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def pin(
        self,
        org_id: str,
        channel_id: str,
        message_id: str,
        *,
        pinned: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatPinResponse:
        """Pin the message

        ``POST /orgs/{orgId}/chat/channels/{channelId}/messages/{messageId}/pin``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/messages/{_path(message_id)}/pin",
            query=_query({}, extra_query),
            body=_body({"pinned": pinned}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def read(
        self,
        org_id: str,
        channel_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatReadResponse:
        """Create the read in an organization (chat channels)

        ``POST /orgs/{orgId}/chat/channels/{channelId}/read``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/read",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_draft(
        self,
        org_id: str,
        channel_id: str,
        *,
        parent_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatGetDraftResponse:
        """List draft channels in an organization

        ``GET /orgs/{orgId}/chat/channels/{channelId}/draft``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/draft",
            query=_query({"parentId": parent_id}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def put_draft(
        self,
        org_id: str,
        channel_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatPutDraftResponse:
        """List draft channels in an organization (replace)

        ``PUT /orgs/{orgId}/chat/channels/{channelId}/draft``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/draft",
            query=_query({}, extra_query),
            body=_body({"body": body, "parentId": parent_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_draft(
        self,
        org_id: str,
        channel_id: str,
        *,
        parent_id: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatDeleteDraftResponse:
        """List draft channels in an organization (delete)

        ``DELETE /orgs/{orgId}/chat/channels/{channelId}/draft``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/draft",
            query=_query({"parentId": parent_id}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def heartbeat(
        self,
        org_id: str,
        channel_id: str,
        *,
        viewer_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        typing: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatHeartbeatResponse:
        """Create the heartbeat in an organization

        ``POST /orgs/{orgId}/chat/channels/{channelId}/heartbeat``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/heartbeat",
            query=_query({}, extra_query),
            body=_body({"viewerId": viewer_id, "typing": typing}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def online(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChatOnlineResponse:
        """Get the online in an organization

        ``GET /orgs/{orgId}/chat/presence/online``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/presence/online",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def online_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``online`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/chat/presence/online",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def stream(
        self,
        org_id: str,
        channel_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the stream in an organization (chat channels)

        ``GET /orgs/{orgId}/chat/channels/{channelId}/stream``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/stream",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def stream_stream(
        self,
        org_id: str,
        channel_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Stream ``stream`` as server-sent events, yielding each decoded event."""
        yield from self._client._stream(
            "GET",
            f"/orgs/{_path(org_id)}/chat/channels/{_path(channel_id)}/stream",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
