from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SpacesAddressesResource:
    """``client.spaces.addresses`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesAddressesListResponse:
        """List addresses in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/addresses``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/addresses",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class SpacesAssetsResource:
    """``client.spaces.assets`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesAssetsListResponse:
        """List assets in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/assets``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/assets",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[UploadedAsset]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/assets",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="assets",
        )

    def upload(
        self,
        org_id: str,
        space_id: str,
        *,
        file: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesAssetsUploadResponse:
        """Create an asset in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/assets``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/assets",
            query=_query({}, extra_query),
            body=_body({"file": file}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def catalog(
        self,
        org_id: str,
        *,
        page_size: Union[int, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        search: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesAssetsCatalogResponse:
        """List assets in an organization

        ``GET /orgs/{orgId}/assets``

        :param page_size: Assets per page.
        :param page: Which page of results to return, 1-based.
        :param limit: Rows per page — the spelling used everywhere else in this API.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/assets",
            query=_query({"pageSize": page_size, "spaceId": space_id, "type": type, "search": search, "page": page, "cursor": cursor, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def catalog_all(
        self,
        org_id: str,
        *,
        page_size: Union[int, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        search: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CatalogedAsset]:
        """Iterate every item of ``catalog`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/assets",
            query=_query({"pageSize": page_size, "spaceId": space_id, "type": type, "search": search, "page": page, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="assets",
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        asset_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesAssetsRemoveResponse:
        """Delete the asset

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/assets/{assetId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/assets/{_path(asset_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def serve(
        self,
        id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        w: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the asset

        ``GET /assets/{id}``
        """
        return self._client._request(
            "GET",
            f"/assets/{_path(id)}",
            query=_query({"share": share, "w": w}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class SpacesDomainsResource:
    """``client.spaces.domains`` (11 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DomainListDto:
        """List domains in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/domains``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[DomainSummaryDto]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="domains",
        )

    def add(
        self,
        org_id: str,
        space_id: str,
        *,
        hostname: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        base_path: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a domain in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/domains``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains",
            query=_query({}, extra_query),
            body=_body({"hostname": hostname, "basePath": base_path}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def allocate_subdomain(
        self,
        org_id: str,
        space_id: str,
        *,
        subdomain: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the subdomain in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/domains/subdomain``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains/subdomain",
            query=_query({}, extra_query),
            body=_body({"subdomain": subdomain}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_acme_challenge(
        self,
        org_id: str,
        space_id: str,
        *,
        hostname: str,
        token: str,
        key_authorization: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesDomainsSetAcmeChallengeResponse:
        """Create the acme challenge in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/domains/acme-challenge``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains/acme-challenge",
            query=_query({}, extra_query),
            body=_body({"hostname": hostname, "token": token, "keyAuthorization": key_authorization}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def verify(
        self,
        org_id: str,
        space_id: str,
        domain_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        activate: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Verify the domain (spaces)

        ``POST /orgs/{orgId}/spaces/{spaceId}/domains/{domainId}/verify``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains/{_path(domain_id)}/verify",
            query=_query({}, extra_query),
            body=_body({"activate": activate}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def activate(
        self,
        org_id: str,
        space_id: str,
        domain_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DomainResponseDto:
        """Activate the domain (spaces)

        ``POST /orgs/{orgId}/spaces/{spaceId}/domains/{domainId}/activate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains/{_path(domain_id)}/activate",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def preview(
        self,
        org_id: str,
        space_id: str,
        *,
        hostname: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        base_path: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DomainPreview:
        """Preview the domain

        ``POST /orgs/{orgId}/spaces/{spaceId}/domains/preview``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains/preview",
            query=_query({}, extra_query),
            body=_body({"hostname": hostname, "basePath": base_path}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        domain_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesDomainsRemoveResponse:
        """Delete the domain (spaces)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/domains/{domainId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains/{_path(domain_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def setup(
        self,
        org_id: str,
        space_id: str,
        domain_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DomainSetupDto:
        """Get the setup in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/domains/{domainId}/setup``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains/{_path(domain_id)}/setup",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_ip_allow_list(
        self,
        org_id: str,
        space_id: str,
        domain_id: str,
        *,
        ip_allow_list: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesDomainsSetIpAllowListResponse:
        """Replace the IP allow list in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/domains/{domainId}/ip-allow-list``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains/{_path(domain_id)}/ip-allow-list",
            query=_query({}, extra_query),
            body=_body({"ipAllowList": ip_allow_list}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_redirect(
        self,
        org_id: str,
        space_id: str,
        domain_id: str,
        *,
        redirect_to: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesDomainsSetRedirectResponse:
        """Replace the redirect in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/domains/{domainId}/redirect``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/domains/{_path(domain_id)}/redirect",
            query=_query({}, extra_query),
            body=_body({"redirectTo": redirect_to}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SpacesHubIntrosResource:
    """``client.spaces.hub_intros`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        space_id: str,
        kind: str,
        key: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesHubIntrosGetResponse:
        """Get the intro in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/hubs/{kind}/{key}/intro``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/hubs/{_path(kind)}/{_path(key)}/intro",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        space_id: str,
        kind: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        doc: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesHubIntrosSetResponse:
        """Replace the intro in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/hubs/{kind}/{key}/intro``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/hubs/{_path(kind)}/{_path(key)}/intro",
            query=_query({}, extra_query),
            body=_body({"doc": doc}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rename_series(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesHubIntrosRenameSeriesResponse:
        """Update the series

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/hubs/series/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/hubs/series/{_path(key)}",
            query=_query({}, extra_query),
            body=_body({"name": name}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SpacesPreviewLinksResource:
    """``client.spaces.preview_links`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def mint(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PreviewLink:
        """Mint a preview link

        ``POST /orgs/{orgId}/spaces/{spaceId}/preview``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/preview",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SpacesSettingsResource:
    """``client.spaces.settings`` (36 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get_theme(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetThemeResponse:
        """The live theme

        ``GET /orgs/{orgId}/spaces/{spaceId}/theme``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_theme(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        primary_color: Union[str, NotGiven] = NOT_GIVEN,
        accent_color: Union[str, NotGiven] = NOT_GIVEN,
        palette: Union[SpacesSettingsSetThemeParamsPalette, NotGiven] = NOT_GIVEN,
        palette_dark: Union[SpacesSettingsSetThemeParamsPaletteDark, NotGiven] = NOT_GIVEN,
        font: Union[str, NotGiven] = NOT_GIVEN,
        color_scheme: Union[str, NotGiven] = NOT_GIVEN,
        content_width: Union[str, NotGiven] = NOT_GIVEN,
        on_this_page: Union[str, NotGiven] = NOT_GIVEN,
        layout: Union[SpacesSettingsSetThemeParamsLayout, NotGiven] = NOT_GIVEN,
        custom_font_url: Union[Any, NotGiven] = NOT_GIVEN,
        custom_font_family: Union[str, NotGiven] = NOT_GIVEN,
        brand_name: Union[Any, NotGiven] = NOT_GIVEN,
        heading_font_family: Union[str, NotGiven] = NOT_GIVEN,
        body_font_family: Union[str, NotGiven] = NOT_GIVEN,
        mono_font_family: Union[str, NotGiven] = NOT_GIVEN,
        typography: Union[SpacesSettingsSetThemeParamsTypography, NotGiven] = NOT_GIVEN,
        fonts: Union[SpacesSettingsSetThemeParamsFonts, NotGiven] = NOT_GIVEN,
        logo_url: Union[Any, NotGiven] = NOT_GIVEN,
        logo_mark: Union[Any, NotGiven] = NOT_GIVEN,
        favicon_url: Union[Any, NotGiven] = NOT_GIVEN,
        custom_css: Union[str, NotGiven] = NOT_GIVEN,
        custom_js: Union[str, NotGiven] = NOT_GIVEN,
        script_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        ads: Union[SpacesSettingsSetThemeParamsAds, NotGiven] = NOT_GIVEN,
        white_label: Union[bool, NotGiven] = NOT_GIVEN,
        show_language_switcher: Union[bool, NotGiven] = NOT_GIVEN,
        api_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        font_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        font_origins_removed: Union[List[str], NotGiven] = NOT_GIVEN,
        img_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        media_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        frame_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        element_styles: Union[List[SpacesSettingsSetThemeParamsElementStyle], NotGiven] = NOT_GIVEN,
        settings_schema: Union[List[SpacesSettingsSetThemeParamsSettingsSchemaItem], NotGiven] = NOT_GIVEN,
        settings: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        string_overrides: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        css_snippets: Union[List[SpacesSettingsSetThemeParamsCssSnippet], NotGiven] = NOT_GIVEN,
        announcement: Union[SpacesSettingsSetThemeParamsAnnouncement, NotGiven] = NOT_GIVEN,
        chrome: Union[SpacesSettingsSetThemeParamsChrome, NotGiven] = NOT_GIVEN,
        not_found: Union[SpacesSettingsSetThemeParamsNotFound, NotGiven] = NOT_GIVEN,
        components: Union[SpacesSettingsSetThemeParamsComponents, NotGiven] = NOT_GIVEN,
        motion: Union[SpacesSettingsSetThemeParamsMotion, NotGiven] = NOT_GIVEN,
        component_installs: Union[List[SpacesSettingsSetThemeParamsComponentInstall], NotGiven] = NOT_GIVEN,
        mobile: Union[SpacesSettingsSetThemeParamsMobile, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetThemeResponse:
        """Replace the live theme

        ``PUT /orgs/{orgId}/spaces/{spaceId}/theme``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme",
            query=_query({}, extra_query),
            body=_body({"primaryColor": primary_color, "accentColor": accent_color, "palette": palette, "paletteDark": palette_dark, "font": font, "colorScheme": color_scheme, "contentWidth": content_width, "onThisPage": on_this_page, "layout": layout, "customFontUrl": custom_font_url, "customFontFamily": custom_font_family, "brandName": brand_name, "headingFontFamily": heading_font_family, "bodyFontFamily": body_font_family, "monoFontFamily": mono_font_family, "typography": typography, "fonts": fonts, "logoUrl": logo_url, "logoMark": logo_mark, "faviconUrl": favicon_url, "customCss": custom_css, "customJs": custom_js, "scriptOrigins": script_origins, "ads": ads, "whiteLabel": white_label, "showLanguageSwitcher": show_language_switcher, "apiOrigins": api_origins, "fontOrigins": font_origins, "fontOriginsRemoved": font_origins_removed, "imgOrigins": img_origins, "mediaOrigins": media_origins, "frameOrigins": frame_origins, "elementStyles": element_styles, "settingsSchema": settings_schema, "settings": settings, "stringOverrides": string_overrides, "cssSnippets": css_snippets, "announcement": announcement, "chrome": chrome, "notFound": not_found, "components": components, "motion": motion, "componentInstalls": component_installs, "mobile": mobile}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def patch_theme(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        primary_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        accent_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        palette: Union[Optional[SpacesSettingsPatchThemeParamsPalette], NotGiven] = NOT_GIVEN,
        palette_dark: Union[Optional[SpacesSettingsPatchThemeParamsPaletteDark], NotGiven] = NOT_GIVEN,
        font: Union[Optional[str], NotGiven] = NOT_GIVEN,
        color_scheme: Union[Optional[str], NotGiven] = NOT_GIVEN,
        content_width: Union[Optional[str], NotGiven] = NOT_GIVEN,
        on_this_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        layout: Union[Optional[SpacesSettingsPatchThemeParamsLayout], NotGiven] = NOT_GIVEN,
        custom_font_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        custom_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        brand_name: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        heading_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        body_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        mono_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        typography: Union[Optional[SpacesSettingsPatchThemeParamsTypography], NotGiven] = NOT_GIVEN,
        fonts: Union[Optional[SpacesSettingsPatchThemeParamsFonts], NotGiven] = NOT_GIVEN,
        logo_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        logo_mark: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        favicon_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        custom_css: Union[Optional[str], NotGiven] = NOT_GIVEN,
        custom_js: Union[Optional[str], NotGiven] = NOT_GIVEN,
        script_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        ads: Union[Optional[SpacesSettingsPatchThemeParamsAds], NotGiven] = NOT_GIVEN,
        white_label: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        show_language_switcher: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        api_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        font_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        font_origins_removed: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        img_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        media_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        frame_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        element_styles: Union[Optional[List[SpacesSettingsPatchThemeParamsElementStyle]], NotGiven] = NOT_GIVEN,
        settings_schema: Union[Optional[List[SpacesSettingsPatchThemeParamsSettingsSchemaItem]], NotGiven] = NOT_GIVEN,
        settings: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        string_overrides: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        css_snippets: Union[Optional[List[SpacesSettingsPatchThemeParamsCssSnippet]], NotGiven] = NOT_GIVEN,
        announcement: Union[Optional[SpacesSettingsPatchThemeParamsAnnouncement], NotGiven] = NOT_GIVEN,
        chrome: Union[Optional[SpacesSettingsPatchThemeParamsChrome], NotGiven] = NOT_GIVEN,
        not_found: Union[Optional[SpacesSettingsPatchThemeParamsNotFound], NotGiven] = NOT_GIVEN,
        components: Union[Optional[SpacesSettingsPatchThemeParamsComponents], NotGiven] = NOT_GIVEN,
        motion: Union[Optional[SpacesSettingsPatchThemeParamsMotion], NotGiven] = NOT_GIVEN,
        component_installs: Union[Optional[List[SpacesSettingsPatchThemeParamsComponentInstall]], NotGiven] = NOT_GIVEN,
        mobile: Union[Optional[SpacesSettingsPatchThemeParamsMobile], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsPatchThemeResponse:
        """Update the theme in a space

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/theme``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme",
            query=_query({}, extra_query),
            body=_body({"primaryColor": primary_color, "accentColor": accent_color, "palette": palette, "paletteDark": palette_dark, "font": font, "colorScheme": color_scheme, "contentWidth": content_width, "onThisPage": on_this_page, "layout": layout, "customFontUrl": custom_font_url, "customFontFamily": custom_font_family, "brandName": brand_name, "headingFontFamily": heading_font_family, "bodyFontFamily": body_font_family, "monoFontFamily": mono_font_family, "typography": typography, "fonts": fonts, "logoUrl": logo_url, "logoMark": logo_mark, "faviconUrl": favicon_url, "customCss": custom_css, "customJs": custom_js, "scriptOrigins": script_origins, "ads": ads, "whiteLabel": white_label, "showLanguageSwitcher": show_language_switcher, "apiOrigins": api_origins, "fontOrigins": font_origins, "fontOriginsRemoved": font_origins_removed, "imgOrigins": img_origins, "mediaOrigins": media_origins, "frameOrigins": frame_origins, "elementStyles": element_styles, "settingsSchema": settings_schema, "settings": settings, "stringOverrides": string_overrides, "cssSnippets": css_snippets, "announcement": announcement, "chrome": chrome, "notFound": not_found, "components": components, "motion": motion, "componentInstalls": component_installs, "mobile": mobile}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_theme_draft(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeDraftState:
        """The theme draft, if there is one

        ``GET /orgs/{orgId}/spaces/{spaceId}/theme/draft``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/draft",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_theme_draft(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        primary_color: Union[str, NotGiven] = NOT_GIVEN,
        accent_color: Union[str, NotGiven] = NOT_GIVEN,
        palette: Union[SpacesSettingsSetThemeDraftParamsPalette, NotGiven] = NOT_GIVEN,
        palette_dark: Union[SpacesSettingsSetThemeDraftParamsPaletteDark, NotGiven] = NOT_GIVEN,
        font: Union[str, NotGiven] = NOT_GIVEN,
        color_scheme: Union[str, NotGiven] = NOT_GIVEN,
        content_width: Union[str, NotGiven] = NOT_GIVEN,
        on_this_page: Union[str, NotGiven] = NOT_GIVEN,
        layout: Union[SpacesSettingsSetThemeDraftParamsLayout, NotGiven] = NOT_GIVEN,
        custom_font_url: Union[Any, NotGiven] = NOT_GIVEN,
        custom_font_family: Union[str, NotGiven] = NOT_GIVEN,
        brand_name: Union[Any, NotGiven] = NOT_GIVEN,
        heading_font_family: Union[str, NotGiven] = NOT_GIVEN,
        body_font_family: Union[str, NotGiven] = NOT_GIVEN,
        mono_font_family: Union[str, NotGiven] = NOT_GIVEN,
        typography: Union[SpacesSettingsSetThemeDraftParamsTypography, NotGiven] = NOT_GIVEN,
        fonts: Union[SpacesSettingsSetThemeDraftParamsFonts, NotGiven] = NOT_GIVEN,
        logo_url: Union[Any, NotGiven] = NOT_GIVEN,
        logo_mark: Union[Any, NotGiven] = NOT_GIVEN,
        favicon_url: Union[Any, NotGiven] = NOT_GIVEN,
        custom_css: Union[str, NotGiven] = NOT_GIVEN,
        custom_js: Union[str, NotGiven] = NOT_GIVEN,
        script_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        ads: Union[SpacesSettingsSetThemeDraftParamsAds, NotGiven] = NOT_GIVEN,
        white_label: Union[bool, NotGiven] = NOT_GIVEN,
        show_language_switcher: Union[bool, NotGiven] = NOT_GIVEN,
        api_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        font_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        font_origins_removed: Union[List[str], NotGiven] = NOT_GIVEN,
        img_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        media_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        frame_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        element_styles: Union[List[SpacesSettingsSetThemeDraftParamsElementStyle], NotGiven] = NOT_GIVEN,
        settings_schema: Union[List[SpacesSettingsSetThemeDraftParamsSettingsSchemaItem], NotGiven] = NOT_GIVEN,
        settings: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        string_overrides: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        css_snippets: Union[List[SpacesSettingsSetThemeDraftParamsCssSnippet], NotGiven] = NOT_GIVEN,
        announcement: Union[SpacesSettingsSetThemeDraftParamsAnnouncement, NotGiven] = NOT_GIVEN,
        chrome: Union[SpacesSettingsSetThemeDraftParamsChrome, NotGiven] = NOT_GIVEN,
        not_found: Union[SpacesSettingsSetThemeDraftParamsNotFound, NotGiven] = NOT_GIVEN,
        components: Union[SpacesSettingsSetThemeDraftParamsComponents, NotGiven] = NOT_GIVEN,
        motion: Union[SpacesSettingsSetThemeDraftParamsMotion, NotGiven] = NOT_GIVEN,
        component_installs: Union[List[SpacesSettingsSetThemeDraftParamsComponentInstall], NotGiven] = NOT_GIVEN,
        mobile: Union[SpacesSettingsSetThemeDraftParamsMobile, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Save a theme draft

        ``PUT /orgs/{orgId}/spaces/{spaceId}/theme/draft``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/draft",
            query=_query({}, extra_query),
            body=_body({"primaryColor": primary_color, "accentColor": accent_color, "palette": palette, "paletteDark": palette_dark, "font": font, "colorScheme": color_scheme, "contentWidth": content_width, "onThisPage": on_this_page, "layout": layout, "customFontUrl": custom_font_url, "customFontFamily": custom_font_family, "brandName": brand_name, "headingFontFamily": heading_font_family, "bodyFontFamily": body_font_family, "monoFontFamily": mono_font_family, "typography": typography, "fonts": fonts, "logoUrl": logo_url, "logoMark": logo_mark, "faviconUrl": favicon_url, "customCss": custom_css, "customJs": custom_js, "scriptOrigins": script_origins, "ads": ads, "whiteLabel": white_label, "showLanguageSwitcher": show_language_switcher, "apiOrigins": api_origins, "fontOrigins": font_origins, "fontOriginsRemoved": font_origins_removed, "imgOrigins": img_origins, "mediaOrigins": media_origins, "frameOrigins": frame_origins, "elementStyles": element_styles, "settingsSchema": settings_schema, "settings": settings, "stringOverrides": string_overrides, "cssSnippets": css_snippets, "announcement": announcement, "chrome": chrome, "notFound": not_found, "components": components, "motion": motion, "componentInstalls": component_installs, "mobile": mobile}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def patch_theme_draft(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        primary_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        accent_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        palette: Union[Optional[SpacesSettingsPatchThemeDraftParamsPalette], NotGiven] = NOT_GIVEN,
        palette_dark: Union[Optional[SpacesSettingsPatchThemeDraftParamsPaletteDark], NotGiven] = NOT_GIVEN,
        font: Union[Optional[str], NotGiven] = NOT_GIVEN,
        color_scheme: Union[Optional[str], NotGiven] = NOT_GIVEN,
        content_width: Union[Optional[str], NotGiven] = NOT_GIVEN,
        on_this_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        layout: Union[Optional[SpacesSettingsPatchThemeDraftParamsLayout], NotGiven] = NOT_GIVEN,
        custom_font_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        custom_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        brand_name: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        heading_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        body_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        mono_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        typography: Union[Optional[SpacesSettingsPatchThemeDraftParamsTypography], NotGiven] = NOT_GIVEN,
        fonts: Union[Optional[SpacesSettingsPatchThemeDraftParamsFonts], NotGiven] = NOT_GIVEN,
        logo_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        logo_mark: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        favicon_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        custom_css: Union[Optional[str], NotGiven] = NOT_GIVEN,
        custom_js: Union[Optional[str], NotGiven] = NOT_GIVEN,
        script_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        ads: Union[Optional[SpacesSettingsPatchThemeDraftParamsAds], NotGiven] = NOT_GIVEN,
        white_label: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        show_language_switcher: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        api_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        font_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        font_origins_removed: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        img_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        media_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        frame_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        element_styles: Union[Optional[List[SpacesSettingsPatchThemeDraftParamsElementStyle]], NotGiven] = NOT_GIVEN,
        settings_schema: Union[Optional[List[SpacesSettingsPatchThemeDraftParamsSettingsSchemaItem]], NotGiven] = NOT_GIVEN,
        settings: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        string_overrides: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        css_snippets: Union[Optional[List[SpacesSettingsPatchThemeDraftParamsCssSnippet]], NotGiven] = NOT_GIVEN,
        announcement: Union[Optional[SpacesSettingsPatchThemeDraftParamsAnnouncement], NotGiven] = NOT_GIVEN,
        chrome: Union[Optional[SpacesSettingsPatchThemeDraftParamsChrome], NotGiven] = NOT_GIVEN,
        not_found: Union[Optional[SpacesSettingsPatchThemeDraftParamsNotFound], NotGiven] = NOT_GIVEN,
        components: Union[Optional[SpacesSettingsPatchThemeDraftParamsComponents], NotGiven] = NOT_GIVEN,
        motion: Union[Optional[SpacesSettingsPatchThemeDraftParamsMotion], NotGiven] = NOT_GIVEN,
        component_installs: Union[Optional[List[SpacesSettingsPatchThemeDraftParamsComponentInstall]], NotGiven] = NOT_GIVEN,
        mobile: Union[Optional[SpacesSettingsPatchThemeDraftParamsMobile], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Merge into the theme draft

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/theme/draft``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/draft",
            query=_query({}, extra_query),
            body=_body({"primaryColor": primary_color, "accentColor": accent_color, "palette": palette, "paletteDark": palette_dark, "font": font, "colorScheme": color_scheme, "contentWidth": content_width, "onThisPage": on_this_page, "layout": layout, "customFontUrl": custom_font_url, "customFontFamily": custom_font_family, "brandName": brand_name, "headingFontFamily": heading_font_family, "bodyFontFamily": body_font_family, "monoFontFamily": mono_font_family, "typography": typography, "fonts": fonts, "logoUrl": logo_url, "logoMark": logo_mark, "faviconUrl": favicon_url, "customCss": custom_css, "customJs": custom_js, "scriptOrigins": script_origins, "ads": ads, "whiteLabel": white_label, "showLanguageSwitcher": show_language_switcher, "apiOrigins": api_origins, "fontOrigins": font_origins, "fontOriginsRemoved": font_origins_removed, "imgOrigins": img_origins, "mediaOrigins": media_origins, "frameOrigins": frame_origins, "elementStyles": element_styles, "settingsSchema": settings_schema, "settings": settings, "stringOverrides": string_overrides, "cssSnippets": css_snippets, "announcement": announcement, "chrome": chrome, "notFound": not_found, "components": components, "motion": motion, "componentInstalls": component_installs, "mobile": mobile}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def discard_theme_draft(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeDraftState:
        """Discard the theme draft

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/theme/draft``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/draft",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def publish_theme_draft(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        force: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsPublishThemeDraftResponse:
        """Make the theme draft live

        ``POST /orgs/{orgId}/spaces/{spaceId}/theme/draft/publish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/draft/publish",
            query=_query({}, extra_query),
            body=_body({"force": force}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_reader_themes(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetReaderThemesResponse:
        """List reader themes in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/reader-themes``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-themes",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get_reader_themes_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ReaderThemeOption]:
        """Iterate every item of ``get_reader_themes`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-themes",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="themes",
        )

    def set_reader_themes(
        self,
        org_id: str,
        space_id: str,
        *,
        themes: List[SpacesSettingsSetReaderThemesParamsTheme],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetReaderThemesResponse:
        """Replace reader themes in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/reader-themes``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-themes",
            query=_query({}, extra_query),
            body=_body({"themes": themes}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_preset(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        preset: Union[str, NotGiven] = NOT_GIVEN,
        piece_preset: Union[str, NotGiven] = NOT_GIVEN,
        front_door: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetPresetResponse:
        """Replace the preset in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/preset``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/preset",
            query=_query({}, extra_query),
            body=_body({"preset": preset, "piecePreset": piece_preset, "frontDoor": front_door}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_redirects(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetRedirectsResponse:
        """List redirects in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/redirects``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/redirects",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get_redirects_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[RedirectRule]:
        """Iterate every item of ``get_redirects`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/redirects",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="redirects",
        )

    def set_redirects(
        self,
        org_id: str,
        space_id: str,
        *,
        redirects: List[SpacesSettingsSetRedirectsParamsRedirect],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetRedirectsResponse:
        """Replace redirects in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/redirects``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/redirects",
            query=_query({}, extra_query),
            body=_body({"redirects": redirects}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_analytics(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AnalyticsTags:
        """List analytics tags in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/analytics-tags``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/analytics-tags",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_analytics(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        ga4: Union[str, NotGiven] = NOT_GIVEN,
        gtm: Union[str, NotGiven] = NOT_GIVEN,
        segment: Union[str, NotGiven] = NOT_GIVEN,
        intercom: Union[str, NotGiven] = NOT_GIVEN,
        custom_head: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace analytics tags in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/analytics-tags``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/analytics-tags",
            query=_query({}, extra_query),
            body=_body({"ga4": ga4, "gtm": gtm, "segment": segment, "intercom": intercom, "customHead": custom_head}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_discovery(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetDiscoveryResponse:
        """Get the discovery in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/discovery``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/discovery",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_discovery(
        self,
        org_id: str,
        space_id: str,
        *,
        ai_ingestion: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetDiscoveryResponse:
        """Replace the discovery in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/discovery``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/discovery",
            query=_query({}, extra_query),
            body=_body({"aiIngestion": ai_ingestion}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_seo(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetSeoResponse:
        """List SEO settings in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/seo``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/seo",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_seo(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[Any, NotGiven] = NOT_GIVEN,
        social_image_url: Union[Any, NotGiven] = NOT_GIVEN,
        social_card: Union[SpacesSettingsSetSeoParamsSocialCard, NotGiven] = NOT_GIVEN,
        verification: Union[SpacesSettingsSetSeoParamsVerification, NotGiven] = NOT_GIVEN,
        noindex: Union[bool, NotGiven] = NOT_GIVEN,
        content_language: Union[Any, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetSeoResponse:
        """Replace SEO settings in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/seo``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/seo",
            query=_query({}, extra_query),
            body=_body({"description": description, "socialImageUrl": social_image_url, "socialCard": social_card, "verification": verification, "noindex": noindex, "contentLanguage": content_language}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_glossary(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetGlossaryResponse:
        """Get the glossary in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/glossary``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/glossary",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get_glossary_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[SpacesSettingsGetGlossaryResponseGlossaryItem]:
        """Iterate every item of ``get_glossary`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/glossary",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="glossary",
        )

    def set_glossary(
        self,
        org_id: str,
        space_id: str,
        *,
        glossary: List[SpacesSettingsSetGlossaryParamsGlossaryItem],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetGlossaryResponse:
        """Replace the glossary in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/glossary``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/glossary",
            query=_query({}, extra_query),
            body=_body({"glossary": glossary}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_roadmap_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetRoadmapSettingsResponse:
        """List roadmap settings in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/roadmap-settings``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap-settings",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_roadmap_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        anonymous_votes: Union[bool, NotGiven] = NOT_GIVEN,
        status_labels: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        status_order: Union[List[str], NotGiven] = NOT_GIVEN,
        hidden_statuses: Union[List[str], NotGiven] = NOT_GIVEN,
        vote_budget: Union[int, NotGiven] = NOT_GIVEN,
        vote_weights: Union[List[int], NotGiven] = NOT_GIVEN,
        moderate_submissions: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetRoadmapSettingsResponse:
        """Replace roadmap settings in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/roadmap-settings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap-settings",
            query=_query({}, extra_query),
            body=_body({"anonymousVotes": anonymous_votes, "statusLabels": status_labels, "statusOrder": status_order, "hiddenStatuses": hidden_statuses, "voteBudget": vote_budget, "voteWeights": vote_weights, "moderateSubmissions": moderate_submissions}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rename_roadmap_lane(
        self,
        org_id: str,
        space_id: str,
        lane_key: str,
        *,
        label: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsRenameRoadmapLaneResponse:
        """Update the lane

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/roadmap-settings/lanes/{laneKey}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap-settings/lanes/{_path(lane_key)}",
            query=_query({}, extra_query),
            body=_body({"label": label}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_home_page(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetHomePageResponse:
        """Get the home page in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/home-page``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/home-page",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_home_page(
        self,
        org_id: str,
        space_id: str,
        *,
        home_page_id: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetHomePageResponse:
        """Replace the home page in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/home-page``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/home-page",
            query=_query({}, extra_query),
            body=_body({"homePageId": home_page_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_home_doc(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetHomeDocResponse:
        """Get the home doc in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/home-doc``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/home-doc",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_home_doc(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        doc: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetHomeDocResponse:
        """Replace the home doc in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/home-doc``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/home-doc",
            query=_query({}, extra_query),
            body=_body({"doc": doc}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_faq_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetFaqSettingsResponse:
        """List FAQ settings in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/faq-settings``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/faq-settings",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_faq_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        contact_space_id: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetFaqSettingsResponse:
        """Replace FAQ settings in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/faq-settings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/faq-settings",
            query=_query({}, extra_query),
            body=_body({"contactSpaceId": contact_space_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_comment_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetCommentSettingsResponse:
        """List comment settings in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/comment-settings``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/comment-settings",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_comment_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        moderated: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetCommentSettingsResponse:
        """Turn reader comments on, and whether they are moderated

        ``PUT /orgs/{orgId}/spaces/{spaceId}/comment-settings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/comment-settings",
            query=_query({}, extra_query),
            body=_body({"enabled": enabled, "moderated": moderated}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_ai_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetAiSettingsResponse:
        """List AI settings in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/ai-settings``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/ai-settings",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_ai_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        enabled: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetAiSettingsResponse:
        """Replace AI settings in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/ai-settings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/ai-settings",
            query=_query({}, extra_query),
            body=_body({"enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_visitor_auth(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsGetVisitorAuthResponse:
        """Get the visitor auth in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/visitor-auth``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/visitor-auth",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_visitor_auth(
        self,
        org_id: str,
        space_id: str,
        *,
        mode: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        password: Union[str, NotGiven] = NOT_GIVEN,
        jwt_secret: Union[str, NotGiven] = NOT_GIVEN,
        oidc: Union[SpacesSettingsSetVisitorAuthParamsOidc, NotGiven] = NOT_GIVEN,
        provision_identity: Union[bool, NotGiven] = NOT_GIVEN,
        approve_new_members: Union[bool, NotGiven] = NOT_GIVEN,
        hosted_signup: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSettingsSetVisitorAuthResponse:
        """Replace the visitor auth in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/visitor-auth``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/visitor-auth",
            query=_query({}, extra_query),
            body=_body({"mode": mode, "password": password, "jwtSecret": jwt_secret, "oidc": oidc, "provisionIdentity": provision_identity, "approveNewMembers": approve_new_members, "hostedSignup": hosted_signup}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SpacesShapeResource:
    """``client.spaces.shape`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        space_id: str,
        *,
        preset: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceShapeView:
        """Get the shape in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/shape``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/shape",
            query=_query({"preset": preset}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def put(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space: Union[SpacesShapePutParamsSpace, NotGiven] = NOT_GIVEN,
        sections: Union[SpacesShapePutParamsSections, NotGiven] = NOT_GIVEN,
        params: Union[SpacesShapePutParamsParams, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the space's shape override

        ``PUT /orgs/{orgId}/spaces/{spaceId}/shape``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/shape",
            query=_query({}, extra_query),
            body=_body({"space": space, "sections": sections, "params": params}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def patch(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space: Union[SpacesShapePatchParamsSpace, NotGiven] = NOT_GIVEN,
        sections: Union[SpacesShapePatchParamsSections, NotGiven] = NOT_GIVEN,
        params: Union[SpacesShapePatchParamsParams, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Merge a patch into the space's shape override

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/shape``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/shape",
            query=_query({}, extra_query),
            body=_body({"space": space, "sections": sections, "params": params}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_default_kind(
        self,
        org_id: str,
        space_id: str,
        *,
        kind: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the default kind in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/shape/default-kind``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/shape/default-kind",
            query=_query({}, extra_query),
            body=_body({"kind": kind}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_kind(
        self,
        org_id: str,
        space_id: str,
        name: str,
        *,
        label: str,
        patch: SpacesShapeSetKindParamsPatch,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the kind

        ``PUT /orgs/{orgId}/spaces/{spaceId}/shape/kinds/{name}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/shape/kinds/{_path(name)}",
            query=_query({}, extra_query),
            body=_body({"label": label, "description": description, "patch": patch}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_kind(
        self,
        org_id: str,
        space_id: str,
        name: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceShapeView:
        """Delete the kind

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/shape/kinds/{name}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/shape/kinds/{_path(name)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def apply_preset(
        self,
        org_id: str,
        space_id: str,
        name: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceShapeView:
        """Create the preset

        ``POST /orgs/{orgId}/spaces/{spaceId}/shape/presets/{name}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/shape/presets/{_path(name)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SpacesShareLinksResource:
    """``client.spaces.share_links`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesShareLinksListResponse:
        """List share links in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/share-links``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/share-links",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ShareLinkSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/share-links",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="links",
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        label: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesShareLinksCreateResponse:
        """Create a share link in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/share-links``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/share-links",
            query=_query({}, extra_query),
            body=_body({"label": label}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def preview(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesShareLinksPreviewResponse:
        """Preview the share link

        ``POST /orgs/{orgId}/spaces/{spaceId}/share-links/preview``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/share-links/preview",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesShareLinksRevokeResponse:
        """Delete the share link

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/share-links/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/share-links/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SpacesSnapshotsResource:
    """``client.spaces.snapshots`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSnapshotsListResponse:
        """List snapshots in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/snapshots``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/snapshots",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[SnapshotSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/snapshots",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="snapshots",
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        label: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSnapshotsCreateResponse:
        """Create a snapshot in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/snapshots``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/snapshots",
            query=_query({}, extra_query),
            body=_body({"label": label}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def restore(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        new_pages: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSnapshotsRestoreResponse:
        """Restore the snapshot

        ``POST /orgs/{orgId}/spaces/{spaceId}/snapshots/{id}/restore``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/snapshots/{_path(id)}/restore",
            query=_query({}, extra_query),
            body=_body({"newPages": new_pages}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSnapshotsRemoveResponse:
        """Delete the snapshot

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/snapshots/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/snapshots/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SpacesThemeOriginsResource:
    """``client.spaces.theme_origins`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesThemeOriginsListResponse:
        """List origins in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/theme/origins``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/origins",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def restore(
        self,
        org_id: str,
        space_id: str,
        origin: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesThemeOriginsRestoreResponse:
        """Create the origin

        ``POST /orgs/{orgId}/spaces/{spaceId}/theme/origins/{origin}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/origins/{_path(origin)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        origin: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesThemeOriginsRemoveResponse:
        """Delete the origin

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/theme/origins/{origin}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/origins/{_path(origin)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SpacesResource:
    """``client.spaces`` (16 operations; addresses, assets, domains, hub_intros, preview_links, settings, shape, share_links, snapshots, theme_origins)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.addresses = SpacesAddressesResource(client)
        self.assets = SpacesAssetsResource(client)
        self.domains = SpacesDomainsResource(client)
        self.hub_intros = SpacesHubIntrosResource(client)
        self.preview_links = SpacesPreviewLinksResource(client)
        self.settings = SpacesSettingsResource(client)
        self.shape = SpacesShapeResource(client)
        self.share_links = SpacesShareLinksResource(client)
        self.snapshots = SpacesSnapshotsResource(client)
        self.theme_origins = SpacesThemeOriginsResource(client)

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        deleted: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceListDto:
        """List spaces in an organization

        ``GET /orgs/{orgId}/spaces``

        :param limit: Spaces per page, once a version is stated.
        :param deleted: List the soft-deleted spaces instead of the live ones.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces",
            query=_query({"limit": limit, "deleted": deleted, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        deleted: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[SpaceSummaryDto]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces",
            query=_query({"limit": limit, "deleted": deleted}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="spaces",
        )

    def create(
        self,
        org_id: str,
        *,
        name: str,
        slug: str,
        type: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        visibility: Union[str, NotGiven] = NOT_GIVEN,
        seed: Union[bool, NotGiven] = NOT_GIVEN,
        preset: Union[str, NotGiven] = NOT_GIVEN,
        shape: Union[SpacesCreateParamsShape, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceCreatedDto:
        """Create a space in an organization

        ``POST /orgs/{orgId}/spaces``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces",
            query=_query({}, extra_query),
            body=_body({"name": name, "slug": slug, "type": type, "visibility": visibility, "seed": seed, "preset": preset, "shape": shape}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def my_access(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesMyAccessResponse:
        """Your access to a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/my-access``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/my-access",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def overview(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesOverviewResponse:
        """Get the overview in a space

        ``GET /orgs/{orgId}/spaces/overview``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/overview",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def overview_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[SpaceOverview]:
        """Iterate every item of ``overview`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/overview",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="overview",
        )

    def preview(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the preview svg in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/preview.svg``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/preview.svg",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceDetailDto:
        """Get the space

        ``GET /orgs/{orgId}/spaces/{spaceId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        visibility: Union[str, NotGiven] = NOT_GIVEN,
        settings: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesUpdateResponse:
        """Update the space

        ``PATCH /orgs/{orgId}/spaces/{spaceId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "visibility": visibility, "settings": settings}, extra_body),
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
    ) -> SpacesRemoveResponse:
        """Delete the space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rename(
        self,
        org_id: str,
        space_id: str,
        *,
        slug: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesRenameResponse:
        """Update the slug in a space

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/slug``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/slug",
            query=_query({}, extra_query),
            body=_body({"slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def slug_history(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesSlugHistoryResponse:
        """Get the history in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/slug/history``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/slug/history",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def slug_history_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``slug_history`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/slug/history",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="slugs",
        )

    def forget_slug(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesForgetSlugResponse:
        """Delete the history

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/slug/history/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/slug/history/{_path(slug)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def purge(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesPurgeResponse:
        """Purge the space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/purge``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/purge",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def restore(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesRestoreResponse:
        """Restore the space

        ``POST /orgs/{orgId}/spaces/{spaceId}/restore``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/restore",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def duplicate(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        slug: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        publish: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesDuplicateResponse:
        """Duplicate the space

        ``POST /orgs/{orgId}/spaces/{spaceId}/duplicate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/duplicate",
            query=_query({}, extra_query),
            body=_body({"name": name, "slug": slug, "publish": publish}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def move(
        self,
        org_id: str,
        space_id: str,
        *,
        target_org_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesMoveResponse:
        """Move the space

        ``POST /orgs/{orgId}/spaces/{spaceId}/move``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/move",
            query=_query({}, extra_query),
            body=_body({"targetOrgId": target_org_id, "slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def publish_all(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacesPublishAllResponse:
        """Publish all in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/publish-all``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/publish-all",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
