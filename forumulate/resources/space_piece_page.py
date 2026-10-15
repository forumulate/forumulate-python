from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SpacePiecePageResource:
    """``client.space_piece_page`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacePiecePageGetResponse:
        """Get the piece page in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/piece-page``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/piece-page",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        sidebar: Union[Optional[SpacePiecePageSetParamsSidebar], NotGiven] = NOT_GIVEN,
        after: Union[Optional[SpacePiecePageSetParamsAfter], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacePiecePageSetResponse:
        """Replace the piece page in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/piece-page``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/piece-page",
            query=_query({}, extra_query),
            body=_body({"sidebar": sidebar, "after": after}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacePiecePageRemoveResponse:
        """Delete the piece page in a space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/piece-page``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/piece-page",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
