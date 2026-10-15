from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class MembersResource:
    """``client.members`` (12 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        external_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersListResponse:
        """List members in an organization

        ``GET /orgs/{orgId}/members``

        :param external_id: The subject this organization's IdP issued to a federated reader.
        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/members",
            query=_query({"externalId": external_id, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        external_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/members",
            query=_query({"externalId": external_id, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def invite(
        self,
        org_id: str,
        *,
        email: str,
        role: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        effect: Union[str, NotGiven] = NOT_GIVEN,
        group_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersInviteResponse:
        """Create a member in an organization

        ``POST /orgs/{orgId}/members``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/members",
            query=_query({}, extra_query),
            body=_body({"email": email, "role": role, "spaceId": space_id, "effect": effect, "groupId": group_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def invites(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersInvitesResponse:
        """List invites in an organization

        ``GET /orgs/{orgId}/members/invites``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/members/invites",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def invites_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``invites`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/members/invites",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def revoke_invite(
        self,
        org_id: str,
        invite_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersRevokeInviteResponse:
        """Delete the invite

        ``DELETE /orgs/{orgId}/members/invites/{inviteId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/members/invites/{_path(invite_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bulk_invite(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        emails: Union[List[str], NotGiven] = NOT_GIVEN,
        csv: Union[str, NotGiven] = NOT_GIVEN,
        role: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        effect: Union[str, NotGiven] = NOT_GIVEN,
        group_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the bulk in an organization (members)

        ``POST /orgs/{orgId}/members/bulk``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/members/bulk",
            query=_query({}, extra_query),
            body=_body({"emails": emails, "csv": csv, "role": role, "spaceId": space_id, "effect": effect, "groupId": group_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_invite_links(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersListInviteLinksResponse:
        """List invite links in an organization

        ``GET /orgs/{orgId}/members/invite-links``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/members/invite-links",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_invite_links_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_invite_links`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/members/invite-links",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create_invite_link(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        role: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        effect: Union[str, NotGiven] = NOT_GIVEN,
        group_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        email: Union[Optional[str], NotGiven] = NOT_GIVEN,
        max_uses: Union[Optional[int], NotGiven] = NOT_GIVEN,
        expires_in_days: Union[Optional[int], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersCreateInviteLinkResponse:
        """Create an invite link in an organization

        ``POST /orgs/{orgId}/members/invite-links``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/members/invite-links",
            query=_query({}, extra_query),
            body=_body({"role": role, "spaceId": space_id, "effect": effect, "groupId": group_id, "email": email, "maxUses": max_uses, "expiresInDays": expires_in_days}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke_invite_link(
        self,
        org_id: str,
        link_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersRevokeInviteLinkResponse:
        """Delete the invite link

        ``DELETE /orgs/{orgId}/members/invite-links/{linkId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/members/invite-links/{_path(link_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        user_id: str,
        *,
        role: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        effect: Union[str, NotGiven] = NOT_GIVEN,
        custom_role_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersUpdateResponse:
        """Update the member

        ``PATCH /orgs/{orgId}/members/{userId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/members/{_path(user_id)}",
            query=_query({}, extra_query),
            body=_body({"role": role, "spaceId": space_id, "effect": effect, "customRoleId": custom_role_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        user_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersRemoveResponse:
        """Delete the member

        ``DELETE /orgs/{orgId}/members/{userId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/members/{_path(user_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke_sessions(
        self,
        org_id: str,
        user_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersRevokeSessionsResponse:
        """Revoke the session

        ``POST /orgs/{orgId}/members/{userId}/sessions/revoke``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/members/{_path(user_id)}/sessions/revoke",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reassign_content(
        self,
        org_id: str,
        user_id: str,
        *,
        target_user_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MembersReassignContentResponse:
        """Create the reassign content in an organization

        ``POST /orgs/{orgId}/members/{userId}/reassign-content``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/members/{_path(user_id)}/reassign-content",
            query=_query({}, extra_query),
            body=_body({"targetUserId": target_user_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
