from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class UsersAvatarResource:
    """``client.users.avatar`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def upload(
        self,
        *,
        file: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UsersAvatarUploadResponse:
        """Upload your avatar

        ``PUT /users/me/avatar``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/users/me/avatar",
            query=_query({}, extra_query),
            body=_body({"file": file}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def clear(
        self,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UsersAvatarClearResponse:
        """Remove your avatar

        ``DELETE /users/me/avatar``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/users/me/avatar",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def gravatar(
        self,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UsersAvatarGravatarResponse:
        """Use your Gravatar as your avatar

        ``POST /users/me/avatar/gravatar``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/users/me/avatar/gravatar",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def serve(
        self,
        user_id: str,
        blob_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the avatar

        ``GET /users/{userId}/avatar/{blobId}``
        """
        return self._client._request(
            "GET",
            f"/users/{_path(user_id)}/avatar/{_path(blob_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class UsersProgressionResource:
    """``client.users.progression`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def state(
        self,
        org_id: str,
        user_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UserStateDto:
        """Get the state in an organization

        ``GET /orgs/{orgId}/users/{userId}/progression/state``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/users/{_path(user_id)}/progression/state",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def signal(
        self,
        org_id: str,
        user_id: str,
        *,
        amount: int,
        body_idempotency_key: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        track: Union[str, NotGiven] = NOT_GIVEN,
        reason: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a signal in an organization

        ``POST /orgs/{orgId}/users/{userId}/progression/signals``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/users/{_path(user_id)}/progression/signals",
            query=_query({}, extra_query),
            body=_body({"track": track, "amount": amount, "reason": reason, "idempotencyKey": body_idempotency_key}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class UsersWalletResource:
    """``client.users.wallet`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def summary(
        self,
        org_id: str,
        user_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> WalletSummaryDto:
        """Get the wallet in an organization

        ``GET /orgs/{orgId}/users/{userId}/wallet``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/users/{_path(user_id)}/wallet",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def credit(
        self,
        org_id: str,
        user_id: str,
        *,
        currency: str,
        amount: int,
        body_idempotency_key: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        reason: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the credit in an organization

        ``POST /orgs/{orgId}/users/{userId}/wallet/credit``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/users/{_path(user_id)}/wallet/credit",
            query=_query({}, extra_query),
            body=_body({"currency": currency, "amount": amount, "reason": reason, "idempotencyKey": body_idempotency_key}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def debit(
        self,
        org_id: str,
        user_id: str,
        *,
        currency: str,
        amount: int,
        body_idempotency_key: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        reason: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the debit in an organization

        ``POST /orgs/{orgId}/users/{userId}/wallet/debit``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/users/{_path(user_id)}/wallet/debit",
            query=_query({}, extra_query),
            body=_body({"currency": currency, "amount": amount, "reason": reason, "idempotencyKey": body_idempotency_key}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def grant_item(
        self,
        org_id: str,
        user_id: str,
        *,
        item_key: str,
        quantity: int,
        body_idempotency_key: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        reason: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the grant in an organization

        ``POST /orgs/{orgId}/users/{userId}/wallet/items/grant``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/users/{_path(user_id)}/wallet/items/grant",
            query=_query({}, extra_query),
            body=_body({"itemKey": item_key, "quantity": quantity, "name": name, "reason": reason, "idempotencyKey": body_idempotency_key}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def consume_item(
        self,
        org_id: str,
        user_id: str,
        *,
        item_key: str,
        quantity: int,
        body_idempotency_key: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        reason: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the consume in an organization

        ``POST /orgs/{orgId}/users/{userId}/wallet/items/consume``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/users/{_path(user_id)}/wallet/items/consume",
            query=_query({}, extra_query),
            body=_body({"itemKey": item_key, "quantity": quantity, "name": name, "reason": reason, "idempotencyKey": body_idempotency_key}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class UsersResource:
    """``client.users`` (7 operations; avatar, progression, wallet)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.avatar = UsersAvatarResource(client)
        self.progression = UsersProgressionResource(client)
        self.wallet = UsersWalletResource(client)

    def me(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UsersMeResponse:
        """Your account

        ``GET /users/me``
        """
        return self._client._request(
            "GET",
            f"/users/me",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        avatar_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        bio: Union[Optional[str], NotGiven] = NOT_GIVEN,
        location: Union[Optional[str], NotGiven] = NOT_GIVEN,
        website_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UsersUpdateResponse:
        """Update your account

        ``PATCH /users/me``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/users/me",
            query=_query({}, extra_query),
            body=_body({"name": name, "avatarUrl": avatar_url, "bio": bio, "location": location, "websiteUrl": website_url}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_locale(
        self,
        *,
        locale: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UsersSetLocaleResponse:
        """Set your interface language

        ``PUT /users/me/locale``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/users/me/locale",
            query=_query({}, extra_query),
            body=_body({"locale": locale}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def change_username(
        self,
        *,
        username: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UsersChangeUsernameResponse:
        """Change your @handle

        ``PATCH /users/me/username``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/users/me/username",
            query=_query({}, extra_query),
            body=_body({"username": username}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_profile_visibility(
        self,
        *,
        hidden: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UsersSetProfileVisibilityResponse:
        """Hide or show your public profile

        ``PUT /users/me/profile-visibility``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/users/me/profile-visibility",
            query=_query({}, extra_query),
            body=_body({"hidden": hidden}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def export_data(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Export this account’s personal data (GDPR Article 15)

        ``GET /users/me/export``
        """
        return self._client._request(
            "GET",
            f"/users/me/export",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def delete_account(
        self,
        *,
        confirm: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UsersDeleteAccountResponse:
        """Erase this account (GDPR Article 17)

        ``POST /users/me/delete``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/users/me/delete",
            query=_query({}, extra_query),
            body=_body({"confirm": confirm}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
