from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class LibraryDomainResource:
    """``client.library_domain`` (11 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DomainListDtoPaged:
        """List a content library’s custom domains

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/domains``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def add(
        self,
        org_id: str,
        library_id: str,
        *,
        hostname: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        base_path: Union[str, NotGiven] = NOT_GIVEN,
        also_redirect_www: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Publish a content library’s hosted output at a custom domain

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/domains``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains",
            query=_query({}, extra_query),
            body=_body({"hostname": hostname, "basePath": base_path, "alsoRedirectWww": also_redirect_www}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def allocate_subdomain(
        self,
        org_id: str,
        library_id: str,
        *,
        subdomain: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Give a content library’s hosted output a first-party subdomain

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/domains/subdomain``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains/subdomain",
            query=_query({}, extra_query),
            body=_body({"subdomain": subdomain}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def preview(
        self,
        org_id: str,
        library_id: str,
        *,
        hostname: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        base_path: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DomainPreview:
        """Dry-run a custom domain for a content library

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/domains/preview``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains/preview",
            query=_query({}, extra_query),
            body=_body({"hostname": hostname, "basePath": base_path}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def verify(
        self,
        org_id: str,
        library_id: str,
        domain_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        activate: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Verify a content library’s custom domain

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/domains/{domainId}/verify``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains/{_path(domain_id)}/verify",
            query=_query({}, extra_query),
            body=_body({"activate": activate}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def activate(
        self,
        org_id: str,
        library_id: str,
        domain_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DomainResponseDto:
        """Take a content library’s verified domain live

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/domains/{domainId}/activate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains/{_path(domain_id)}/activate",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def setup(
        self,
        org_id: str,
        library_id: str,
        domain_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DomainSetupDto:
        """What to configure for a content library’s domain

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/domains/{domainId}/setup``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains/{_path(domain_id)}/setup",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        library_id: str,
        domain_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryDomainRemoveResponse:
        """Remove a content library’s custom domain

        ``DELETE /orgs/{orgId}/content/libraries/{libraryId}/domains/{domainId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains/{_path(domain_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_www(
        self,
        org_id: str,
        library_id: str,
        domain_id: str,
        *,
        also_redirect_www: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Also redirect www.

        ``PUT /orgs/{orgId}/content/libraries/{libraryId}/domains/{domainId}/www``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains/{_path(domain_id)}/www",
            query=_query({}, extra_query),
            body=_body({"alsoRedirectWww": also_redirect_www}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_ip_allow_list(
        self,
        org_id: str,
        library_id: str,
        domain_id: str,
        *,
        ip_allow_list: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryDomainSetIpAllowListResponse:
        """Restrict who may read a content library’s domain

        ``PUT /orgs/{orgId}/content/libraries/{libraryId}/domains/{domainId}/ip-allow-list``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains/{_path(domain_id)}/ip-allow-list",
            query=_query({}, extra_query),
            body=_body({"ipAllowList": ip_allow_list}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_redirect(
        self,
        org_id: str,
        library_id: str,
        domain_id: str,
        *,
        redirect_to: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryDomainSetRedirectResponse:
        """Retire a content library’s domain with a 301 to a new home

        ``PUT /orgs/{orgId}/content/libraries/{libraryId}/domains/{domainId}/redirect``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/domains/{_path(domain_id)}/redirect",
            query=_query({}, extra_query),
            body=_body({"redirectTo": redirect_to}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
