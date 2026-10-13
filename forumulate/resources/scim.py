from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ScimGroupsResource:
    """``client.scim.groups`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        *,
        filter: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ScimGroupsListResponse:
        """List groups

        ``GET /scim/v2/Groups``
        """
        return self._client._request(
            "GET",
            f"/scim/v2/Groups",
            query=_query({"filter": filter}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def create(
        self,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        display_name: Union[str, NotGiven] = NOT_GIVEN,
        members: Union[List[ScimGroupsCreateParamsMember], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a group

        ``POST /scim/v2/Groups``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/scim/v2/Groups",
            query=_query({}, extra_query),
            body=_body({"displayName": display_name, "members": members}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ScimGroup:
        """Get the group (SCIM v2 groups)

        ``GET /scim/v2/Groups/{id}``
        """
        return self._client._request(
            "GET",
            f"/scim/v2/Groups/{_path(id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def replace(
        self,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        display_name: Union[str, NotGiven] = NOT_GIVEN,
        members: Union[List[ScimGroupsReplaceParamsMember], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the group

        ``PUT /scim/v2/Groups/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/scim/v2/Groups/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"displayName": display_name, "members": members}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def patch(
        self,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        operations: Union[List[ScimGroupsPatchParamsOperation], NotGiven] = NOT_GIVEN,
        active: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update the group (SCIM v2 groups)

        ``PATCH /scim/v2/Groups/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/scim/v2/Groups/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"Operations": operations, "active": active}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Delete the group (SCIM v2 groups)

        ``DELETE /scim/v2/Groups/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/scim/v2/Groups/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ScimUsersResource:
    """``client.scim.users`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        *,
        filter: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ScimUsersListResponse:
        """List users

        ``GET /scim/v2/Users``
        """
        return self._client._request(
            "GET",
            f"/scim/v2/Users",
            query=_query({"filter": filter}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def create(
        self,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        user_name: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[ScimUsersCreateParamsName, NotGiven] = NOT_GIVEN,
        active: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create an user

        ``POST /scim/v2/Users``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/scim/v2/Users",
            query=_query({}, extra_query),
            body=_body({"userName": user_name, "name": name, "active": active}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ScimUser:
        """Get the user

        ``GET /scim/v2/Users/{id}``
        """
        return self._client._request(
            "GET",
            f"/scim/v2/Users/{_path(id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def patch(
        self,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        operations: Union[List[ScimUsersPatchParamsOperation], NotGiven] = NOT_GIVEN,
        active: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update the user

        ``PATCH /scim/v2/Users/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/scim/v2/Users/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"Operations": operations, "active": active}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Delete the user

        ``DELETE /scim/v2/Users/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/scim/v2/Users/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ScimResource:
    """``client.scim`` (0 operations; groups, users)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.groups = ScimGroupsResource(client)
        self.users = ScimUsersResource(client)
