from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class AuthResource:
    """``client.auth`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def logout(
        self,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AuthLogoutResponse:
        """Sign out

        ``POST /auth/logout``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/auth/logout",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def me(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AuthMeResponse:
        """The signed-in account

        ``GET /auth/me``
        """
        return self._client._request(
            "GET",
            f"/auth/me",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
