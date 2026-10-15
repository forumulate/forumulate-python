from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class CareersAtsResource:
    """``client.careers_ats`` (4 operations)."""

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
    ) -> CareersAtsGetResponse:
        """List ats in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/careers/ats``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/ats",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        space_id: str,
        *,
        provider: str,
        board: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        sync_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersAtsSetResponse:
        """Replace ats in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/careers/ats``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/ats",
            query=_query({}, extra_query),
            body=_body({"provider": provider, "board": board, "syncEnabled": sync_enabled}, extra_body),
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
    ) -> CareersAtsRemoveResponse:
        """Delete ats in a space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/careers/ats``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/ats",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def sync(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Sync roles from the connected job board

        ``POST /orgs/{orgId}/spaces/{spaceId}/careers/ats/sync``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/ats/sync",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
