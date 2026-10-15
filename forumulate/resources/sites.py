from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SitesResource:
    """``client.sites`` (15 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesListResponse:
        """List sites in an organization

        ``GET /orgs/{orgId}/sites``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sites",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/sites",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        *,
        slug: str,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        config: Union[SitesCreateParamsConfig, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesCreateResponse:
        """Create a site in an organization

        ``POST /orgs/{orgId}/sites``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/sites",
            query=_query({}, extra_query),
            body=_body({"slug": slug, "name": name, "spaceIds": space_ids, "config": config}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        site_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesGetResponse:
        """Get the site

        ``GET /orgs/{orgId}/sites/{siteId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def replace(
        self,
        org_id: str,
        site_id: str,
        *,
        name: str,
        config: SitesReplaceParamsConfig,
        dry_run: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the site

        ``PUT /orgs/{orgId}/sites/{siteId}``

        :param dry_run: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}",
            query=_query({"dryRun": dry_run}, extra_query),
            body=_body({"name": name, "spaceIds": space_ids, "config": config}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        site_id: str,
        *,
        dry_run: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        space_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        config: Union[SitesUpdateParamsConfig, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update the site

        ``PATCH /orgs/{orgId}/sites/{siteId}``

        :param dry_run: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}",
            query=_query({"dryRun": dry_run}, extra_query),
            body=_body({"name": name, "spaceIds": space_ids, "config": config}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        site_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesRemoveResponse:
        """Delete the site

        ``DELETE /orgs/{orgId}/sites/{siteId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_staging(
        self,
        org_id: str,
        site_id: str,
        *,
        staging: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesSetStagingResponse:
        """Create the staging in an organization

        ``POST /orgs/{orgId}/sites/{siteId}/staging``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/staging",
            query=_query({}, extra_query),
            body=_body({"staging": staging}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_domains(
        self,
        org_id: str,
        site_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesListDomainsResponse:
        """List domains in an organization

        ``GET /orgs/{orgId}/sites/{siteId}/domains``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/domains",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_domains_all(
        self,
        org_id: str,
        site_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_domains`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/domains",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def add_domain(
        self,
        org_id: str,
        site_id: str,
        *,
        hostname: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        base_path: Union[str, NotGiven] = NOT_GIVEN,
        also_redirect_www: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesAddDomainResponse:
        """Create a domain in an organization

        ``POST /orgs/{orgId}/sites/{siteId}/domains``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/domains",
            query=_query({}, extra_query),
            body=_body({"hostname": hostname, "basePath": base_path, "alsoRedirectWww": also_redirect_www}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def domain_setup(
        self,
        org_id: str,
        site_id: str,
        domain_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DomainSetupDto:
        """Get the setup in an organization

        ``GET /orgs/{orgId}/sites/{siteId}/domains/{domainId}/setup``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/domains/{_path(domain_id)}/setup",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_domain_www(
        self,
        org_id: str,
        site_id: str,
        domain_id: str,
        *,
        also_redirect_www: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the www in an organization

        ``PUT /orgs/{orgId}/sites/{siteId}/domains/{domainId}/www``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/domains/{_path(domain_id)}/www",
            query=_query({}, extra_query),
            body=_body({"alsoRedirectWww": also_redirect_www}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def allocate_subdomain(
        self,
        org_id: str,
        site_id: str,
        *,
        subdomain: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesAllocateSubdomainResponse:
        """Create the subdomain in an organization

        ``POST /orgs/{orgId}/sites/{siteId}/domains/subdomain``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/domains/subdomain",
            query=_query({}, extra_query),
            body=_body({"subdomain": subdomain}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def verify_domain(
        self,
        org_id: str,
        site_id: str,
        domain_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        activate: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesVerifyDomainResponse:
        """Verify the domain (sites)

        ``POST /orgs/{orgId}/sites/{siteId}/domains/{domainId}/verify``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/domains/{_path(domain_id)}/verify",
            query=_query({}, extra_query),
            body=_body({"activate": activate}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def activate_domain(
        self,
        org_id: str,
        site_id: str,
        domain_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesActivateDomainResponse:
        """Activate the domain (sites)

        ``POST /orgs/{orgId}/sites/{siteId}/domains/{domainId}/activate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/domains/{_path(domain_id)}/activate",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_domain(
        self,
        org_id: str,
        site_id: str,
        domain_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitesRemoveDomainResponse:
        """Delete the domain (sites)

        ``DELETE /orgs/{orgId}/sites/{siteId}/domains/{domainId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/domains/{_path(domain_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
