from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class LibrarySdkResource:
    """``client.library_sdk`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentSdkStatus:
        """The library's client SDKs

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/sdk``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/sdk",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def publish(
        self,
        org_id: str,
        library_id: str,
        language: str,
        *,
        target: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        package_name: Union[str, NotGiven] = NOT_GIVEN,
        go_module_prefix: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibrarySdkPublishResponse:
        """Publish the library client to a connected registry

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/sdk/{language}/publish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/sdk/{_path(language)}/publish",
            query=_query({}, extra_query),
            body=_body({"target": target, "packageName": package_name, "goModulePrefix": go_module_prefix}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def download(
        self,
        org_id: str,
        library_id: str,
        language: str,
        *,
        go_module_prefix: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Download the library client as a .tar.gz

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/sdk/{language}/download``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/sdk/{_path(language)}/download",
            query=_query({"goModulePrefix": go_module_prefix}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
