from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class GoogleIndexingResource:
    """``client.google_indexing`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GoogleIndexingStatus:
        """Get the google indexing in an organization

        ``GET /orgs/{orgId}/google-indexing``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/google-indexing",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def configure(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        service_account: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the google indexing in an organization

        ``PUT /orgs/{orgId}/google-indexing``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/google-indexing",
            query=_query({}, extra_query),
            body=_body({"serviceAccount": service_account, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def clear(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> GoogleIndexingClearResponse:
        """Delete the google indexing in an organization

        ``DELETE /orgs/{orgId}/google-indexing``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/google-indexing",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
