from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class DeliveryKeyResource:
    """``client.delivery_key`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def key(
        self,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryKeyKeyResponse:
        """Describe the calling delivery key

        ``GET /delivery/v1/libraries/{libraryId}/key``
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/libraries/{_path(library_id)}/key",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def key_by_key_id(
        self,
        key_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DeliveryKeyKeyByKeyIdResponse:
        """Describe the calling publishable key by its id

        ``GET /delivery/v1/k/{keyId}/key``
        """
        return self._client._request(
            "GET",
            f"/delivery/v1/k/{_path(key_id)}/key",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
