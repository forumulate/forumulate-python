from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EnvironmentsResource:
    """``client.environments`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EnvironmentsListResponse:
        """List a library's sandboxes

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/environments``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/environments",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def fork(
        self,
        org_id: str,
        library_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        include_content: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EnvironmentsForkResponse:
        """Fork a library into a sandbox

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/environments``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/environments",
            query=_query({}, extra_query),
            body=_body({"name": name, "slug": slug, "includeContent": include_content}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def compare(
        self,
        org_id: str,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EnvironmentsCompareResponse:
        """Compare a sandbox’s model with its source

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/environment/compare``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/environment/compare",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def promote(
        self,
        org_id: str,
        library_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EnvironmentsPromoteResponse:
        """Promote a sandbox’s model into its source

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/environment/promote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/environment/promote",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
