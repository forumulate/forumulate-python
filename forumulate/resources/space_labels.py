from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SpaceLabelsResource:
    """``client.space_labels`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def strings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OwnerStringsListing:
        """List strings in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/i18n/strings``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/i18n/strings",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def replace(
        self,
        org_id: str,
        space_id: str,
        *,
        labels: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace labels in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/i18n/labels``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/i18n/labels",
            query=_query({}, extra_query),
            body=_body({"labels": labels}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def merge(
        self,
        org_id: str,
        space_id: str,
        *,
        labels: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update labels in a space

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/i18n/labels``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/i18n/labels",
            query=_query({}, extra_query),
            body=_body({"labels": labels}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
