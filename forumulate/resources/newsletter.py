from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class NewsletterResource:
    """``client.newsletter`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def confirm(
        self,
        *,
        token: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NewsletterConfirmResponse:
        """Confirm the newsletter

        ``POST /newsletter/confirm``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/newsletter/confirm",
            query=_query({}, extra_query),
            body=_body({"token": token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unsubscribe(
        self,
        *,
        token: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NewsletterUnsubscribeResponse:
        """Unsubscribe the newsletter

        ``POST /newsletter/unsubscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/newsletter/unsubscribe",
            query=_query({}, extra_query),
            body=_body({"token": token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def one_click_unsubscribe_page(
        self,
        *,
        token: str,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Get the one click unsubscribe

        ``GET /newsletter/one-click-unsubscribe``
        """
        return self._client._request(
            "GET",
            f"/newsletter/one-click-unsubscribe",
            query=_query({"token": token}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def one_click_unsubscribe(
        self,
        *,
        token: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> NewsletterOneClickUnsubscribeResponse:
        """Create the one click unsubscribe

        ``POST /newsletter/one-click-unsubscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/newsletter/one-click-unsubscribe",
            query=_query({"token": token}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def open(
        self,
        token: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the open

        ``GET /newsletter/open/{token}``
        """
        return self._client._request(
            "GET",
            f"/newsletter/open/{_path(token)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def click(
        self,
        token: str,
        *,
        u: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Get the click

        ``GET /newsletter/click/{token}``
        """
        return self._client._request(
            "GET",
            f"/newsletter/click/{_path(token)}",
            query=_query({"u": u}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
