from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ThemesBundlesResource:
    """``client.themes.bundles`` (11 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def export_space(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeBundleExport:
        """Get the bundle in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/theme/bundle``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/bundle",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def import_space(
        self,
        org_id: str,
        space_id: str,
        *,
        format: str,
        format_version: float,
        meta: ThemesBundlesImportSpaceParamsMeta,
        required_origins: ThemesBundlesImportSpaceParamsRequiredOrigins,
        theme: ThemesBundlesImportSpaceParamsTheme,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        components: Union[List[ThemesBundlesImportSpaceParamsComponent], NotGiven] = NOT_GIVEN,
        front_pages: Union[List[ThemesBundlesImportSpaceParamsFrontPage], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the bundle in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/theme/bundle``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/bundle",
            query=_query({}, extra_query),
            body=_body({"format": format, "formatVersion": format_version, "meta": meta, "requiredOrigins": required_origins, "theme": theme, "components": components, "frontPages": front_pages}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def apply_space(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        component_id: Union[str, NotGiven] = NOT_GIVEN,
        first_party: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Apply the draft (spaces)

        ``POST /orgs/{orgId}/spaces/{spaceId}/theme/draft/apply``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/draft/apply",
            query=_query({}, extra_query),
            body=_body({"componentId": component_id, "firstParty": first_party}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def export_site(
        self,
        org_id: str,
        site_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeBundleExport:
        """Get the bundle in an organization (sites theme)

        ``GET /orgs/{orgId}/sites/{siteId}/theme/bundle``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/bundle",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def import_site(
        self,
        org_id: str,
        site_id: str,
        *,
        format: str,
        format_version: float,
        meta: ThemesBundlesImportSiteParamsMeta,
        required_origins: ThemesBundlesImportSiteParamsRequiredOrigins,
        theme: ThemesBundlesImportSiteParamsTheme,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        components: Union[List[ThemesBundlesImportSiteParamsComponent], NotGiven] = NOT_GIVEN,
        front_pages: Union[List[ThemesBundlesImportSiteParamsFrontPage], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the bundle in an organization

        ``PUT /orgs/{orgId}/sites/{siteId}/theme/bundle``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/bundle",
            query=_query({}, extra_query),
            body=_body({"format": format, "formatVersion": format_version, "meta": meta, "requiredOrigins": required_origins, "theme": theme, "components": components, "frontPages": front_pages}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def apply_site(
        self,
        org_id: str,
        site_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        component_id: Union[str, NotGiven] = NOT_GIVEN,
        first_party: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Apply the draft (sites)

        ``POST /orgs/{orgId}/sites/{siteId}/theme/draft/apply``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/draft/apply",
            query=_query({}, extra_query),
            body=_body({"componentId": component_id, "firstParty": first_party}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def site_draft(
        self,
        org_id: str,
        site_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeDraftState:
        """List draft theme in an organization

        ``GET /orgs/{orgId}/sites/{siteId}/theme/draft``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/draft",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_site_draft(
        self,
        org_id: str,
        site_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        primary_color: Union[str, NotGiven] = NOT_GIVEN,
        primary_color_dark: Union[str, NotGiven] = NOT_GIVEN,
        accent_color: Union[str, NotGiven] = NOT_GIVEN,
        palette: Union[ThemesBundlesSetSiteDraftParamsPalette, NotGiven] = NOT_GIVEN,
        palette_dark: Union[ThemesBundlesSetSiteDraftParamsPaletteDark, NotGiven] = NOT_GIVEN,
        font: Union[str, NotGiven] = NOT_GIVEN,
        color_scheme: Union[str, NotGiven] = NOT_GIVEN,
        color_scheme_strict: Union[bool, NotGiven] = NOT_GIVEN,
        content_width: Union[str, NotGiven] = NOT_GIVEN,
        on_this_page: Union[str, NotGiven] = NOT_GIVEN,
        layout: Union[ThemesBundlesSetSiteDraftParamsLayout, NotGiven] = NOT_GIVEN,
        custom_font_url: Union[Any, NotGiven] = NOT_GIVEN,
        custom_font_family: Union[str, NotGiven] = NOT_GIVEN,
        brand_name: Union[Any, NotGiven] = NOT_GIVEN,
        logo_includes_name: Union[bool, NotGiven] = NOT_GIVEN,
        heading_font_family: Union[str, NotGiven] = NOT_GIVEN,
        body_font_family: Union[str, NotGiven] = NOT_GIVEN,
        mono_font_family: Union[str, NotGiven] = NOT_GIVEN,
        typography: Union[ThemesBundlesSetSiteDraftParamsTypography, NotGiven] = NOT_GIVEN,
        heading_anchors: Union[str, NotGiven] = NOT_GIVEN,
        fonts: Union[ThemesBundlesSetSiteDraftParamsFonts, NotGiven] = NOT_GIVEN,
        logo_url: Union[Any, NotGiven] = NOT_GIVEN,
        logo_mark: Union[Any, NotGiven] = NOT_GIVEN,
        logo_url_light: Union[Any, NotGiven] = NOT_GIVEN,
        logo_url_dark: Union[Any, NotGiven] = NOT_GIVEN,
        logo_dark_mode: Union[str, NotGiven] = NOT_GIVEN,
        favicon_url: Union[Any, NotGiven] = NOT_GIVEN,
        custom_css: Union[str, NotGiven] = NOT_GIVEN,
        custom_js: Union[str, NotGiven] = NOT_GIVEN,
        script_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        ads: Union[ThemesBundlesSetSiteDraftParamsAds, NotGiven] = NOT_GIVEN,
        white_label: Union[bool, NotGiven] = NOT_GIVEN,
        show_language_switcher: Union[bool, NotGiven] = NOT_GIVEN,
        api_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        font_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        font_origins_removed: Union[List[str], NotGiven] = NOT_GIVEN,
        img_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        media_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        frame_origins: Union[List[str], NotGiven] = NOT_GIVEN,
        element_styles: Union[List[ThemesBundlesSetSiteDraftParamsElementStyle], NotGiven] = NOT_GIVEN,
        settings_schema: Union[List[ThemesBundlesSetSiteDraftParamsSettingsSchemaItem], NotGiven] = NOT_GIVEN,
        settings: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        string_overrides: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        css_snippets: Union[List[ThemesBundlesSetSiteDraftParamsCssSnippet], NotGiven] = NOT_GIVEN,
        announcement: Union[ThemesBundlesSetSiteDraftParamsAnnouncement, NotGiven] = NOT_GIVEN,
        chrome: Union[ThemesBundlesSetSiteDraftParamsChrome, NotGiven] = NOT_GIVEN,
        not_found: Union[ThemesBundlesSetSiteDraftParamsNotFound, NotGiven] = NOT_GIVEN,
        components: Union[ThemesBundlesSetSiteDraftParamsComponents, NotGiven] = NOT_GIVEN,
        changelog: Union[ThemesBundlesSetSiteDraftParamsChangelog, NotGiven] = NOT_GIVEN,
        forum: Union[ThemesBundlesSetSiteDraftParamsForum, NotGiven] = NOT_GIVEN,
        post: Union[ThemesBundlesSetSiteDraftParamsPost, NotGiven] = NOT_GIVEN,
        docs: Union[ThemesBundlesSetSiteDraftParamsDocs, NotGiven] = NOT_GIVEN,
        footnotes: Union[ThemesBundlesSetSiteDraftParamsFootnotes, NotGiven] = NOT_GIVEN,
        i18n: Union[ThemesBundlesSetSiteDraftParamsI18n, NotGiven] = NOT_GIVEN,
        status: Union[ThemesBundlesSetSiteDraftParamsStatus, NotGiven] = NOT_GIVEN,
        legal: Union[ThemesBundlesSetSiteDraftParamsLegal, NotGiven] = NOT_GIVEN,
        faq: Union[ThemesBundlesSetSiteDraftParamsFaq, NotGiven] = NOT_GIVEN,
        roadmap: Union[ThemesBundlesSetSiteDraftParamsRoadmap, NotGiven] = NOT_GIVEN,
        events: Union[ThemesBundlesSetSiteDraftParamsEvents, NotGiven] = NOT_GIVEN,
        courses: Union[ThemesBundlesSetSiteDraftParamsCourses, NotGiven] = NOT_GIVEN,
        careers: Union[ThemesBundlesSetSiteDraftParamsCareers, NotGiven] = NOT_GIVEN,
        contact: Union[ThemesBundlesSetSiteDraftParamsContact, NotGiven] = NOT_GIVEN,
        motion: Union[ThemesBundlesSetSiteDraftParamsMotion, NotGiven] = NOT_GIVEN,
        title_band: Union[ThemesBundlesSetSiteDraftParamsTitleBand, NotGiven] = NOT_GIVEN,
        component_installs: Union[List[ThemesBundlesSetSiteDraftParamsComponentInstall], NotGiven] = NOT_GIVEN,
        mobile: Union[ThemesBundlesSetSiteDraftParamsMobile, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """List draft theme in an organization (replace)

        ``PUT /orgs/{orgId}/sites/{siteId}/theme/draft``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/draft",
            query=_query({}, extra_query),
            body=_body({"primaryColor": primary_color, "primaryColorDark": primary_color_dark, "accentColor": accent_color, "palette": palette, "paletteDark": palette_dark, "font": font, "colorScheme": color_scheme, "colorSchemeStrict": color_scheme_strict, "contentWidth": content_width, "onThisPage": on_this_page, "layout": layout, "customFontUrl": custom_font_url, "customFontFamily": custom_font_family, "brandName": brand_name, "logoIncludesName": logo_includes_name, "headingFontFamily": heading_font_family, "bodyFontFamily": body_font_family, "monoFontFamily": mono_font_family, "typography": typography, "headingAnchors": heading_anchors, "fonts": fonts, "logoUrl": logo_url, "logoMark": logo_mark, "logoUrlLight": logo_url_light, "logoUrlDark": logo_url_dark, "logoDarkMode": logo_dark_mode, "faviconUrl": favicon_url, "customCss": custom_css, "customJs": custom_js, "scriptOrigins": script_origins, "ads": ads, "whiteLabel": white_label, "showLanguageSwitcher": show_language_switcher, "apiOrigins": api_origins, "fontOrigins": font_origins, "fontOriginsRemoved": font_origins_removed, "imgOrigins": img_origins, "mediaOrigins": media_origins, "frameOrigins": frame_origins, "elementStyles": element_styles, "settingsSchema": settings_schema, "settings": settings, "stringOverrides": string_overrides, "cssSnippets": css_snippets, "announcement": announcement, "chrome": chrome, "notFound": not_found, "components": components, "changelog": changelog, "forum": forum, "post": post, "docs": docs, "footnotes": footnotes, "i18n": i18n, "status": status, "legal": legal, "faq": faq, "roadmap": roadmap, "events": events, "courses": courses, "careers": careers, "contact": contact, "motion": motion, "titleBand": title_band, "componentInstalls": component_installs, "mobile": mobile}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def patch_site_draft(
        self,
        org_id: str,
        site_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        primary_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        primary_color_dark: Union[Optional[str], NotGiven] = NOT_GIVEN,
        accent_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        palette: Union[Optional[ThemesBundlesPatchSiteDraftParamsPalette], NotGiven] = NOT_GIVEN,
        palette_dark: Union[Optional[ThemesBundlesPatchSiteDraftParamsPaletteDark], NotGiven] = NOT_GIVEN,
        font: Union[Optional[str], NotGiven] = NOT_GIVEN,
        color_scheme: Union[Optional[str], NotGiven] = NOT_GIVEN,
        color_scheme_strict: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        content_width: Union[Optional[str], NotGiven] = NOT_GIVEN,
        on_this_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        layout: Union[Optional[ThemesBundlesPatchSiteDraftParamsLayout], NotGiven] = NOT_GIVEN,
        custom_font_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        custom_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        brand_name: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        logo_includes_name: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        heading_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        body_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        mono_font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        typography: Union[Optional[ThemesBundlesPatchSiteDraftParamsTypography], NotGiven] = NOT_GIVEN,
        heading_anchors: Union[Optional[str], NotGiven] = NOT_GIVEN,
        fonts: Union[Optional[ThemesBundlesPatchSiteDraftParamsFonts], NotGiven] = NOT_GIVEN,
        logo_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        logo_mark: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        logo_url_light: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        logo_url_dark: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        logo_dark_mode: Union[Optional[str], NotGiven] = NOT_GIVEN,
        favicon_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        custom_css: Union[Optional[str], NotGiven] = NOT_GIVEN,
        custom_js: Union[Optional[str], NotGiven] = NOT_GIVEN,
        script_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        ads: Union[Optional[ThemesBundlesPatchSiteDraftParamsAds], NotGiven] = NOT_GIVEN,
        white_label: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        show_language_switcher: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        api_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        font_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        font_origins_removed: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        img_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        media_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        frame_origins: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        element_styles: Union[Optional[List[ThemesBundlesPatchSiteDraftParamsElementStyle]], NotGiven] = NOT_GIVEN,
        settings_schema: Union[Optional[List[ThemesBundlesPatchSiteDraftParamsSettingsSchemaItem]], NotGiven] = NOT_GIVEN,
        settings: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        string_overrides: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        css_snippets: Union[Optional[List[ThemesBundlesPatchSiteDraftParamsCssSnippet]], NotGiven] = NOT_GIVEN,
        announcement: Union[Optional[ThemesBundlesPatchSiteDraftParamsAnnouncement], NotGiven] = NOT_GIVEN,
        chrome: Union[Optional[ThemesBundlesPatchSiteDraftParamsChrome], NotGiven] = NOT_GIVEN,
        not_found: Union[Optional[ThemesBundlesPatchSiteDraftParamsNotFound], NotGiven] = NOT_GIVEN,
        components: Union[Optional[ThemesBundlesPatchSiteDraftParamsComponents], NotGiven] = NOT_GIVEN,
        changelog: Union[Optional[ThemesBundlesPatchSiteDraftParamsChangelog], NotGiven] = NOT_GIVEN,
        forum: Union[Optional[ThemesBundlesPatchSiteDraftParamsForum], NotGiven] = NOT_GIVEN,
        post: Union[Optional[ThemesBundlesPatchSiteDraftParamsPost], NotGiven] = NOT_GIVEN,
        docs: Union[Optional[ThemesBundlesPatchSiteDraftParamsDocs], NotGiven] = NOT_GIVEN,
        footnotes: Union[Optional[ThemesBundlesPatchSiteDraftParamsFootnotes], NotGiven] = NOT_GIVEN,
        i18n: Union[Optional[ThemesBundlesPatchSiteDraftParamsI18n], NotGiven] = NOT_GIVEN,
        status: Union[Optional[ThemesBundlesPatchSiteDraftParamsStatus], NotGiven] = NOT_GIVEN,
        legal: Union[Optional[ThemesBundlesPatchSiteDraftParamsLegal], NotGiven] = NOT_GIVEN,
        faq: Union[Optional[ThemesBundlesPatchSiteDraftParamsFaq], NotGiven] = NOT_GIVEN,
        roadmap: Union[Optional[ThemesBundlesPatchSiteDraftParamsRoadmap], NotGiven] = NOT_GIVEN,
        events: Union[Optional[ThemesBundlesPatchSiteDraftParamsEvents], NotGiven] = NOT_GIVEN,
        courses: Union[Optional[ThemesBundlesPatchSiteDraftParamsCourses], NotGiven] = NOT_GIVEN,
        careers: Union[Optional[ThemesBundlesPatchSiteDraftParamsCareers], NotGiven] = NOT_GIVEN,
        contact: Union[Optional[ThemesBundlesPatchSiteDraftParamsContact], NotGiven] = NOT_GIVEN,
        motion: Union[Optional[ThemesBundlesPatchSiteDraftParamsMotion], NotGiven] = NOT_GIVEN,
        title_band: Union[Optional[ThemesBundlesPatchSiteDraftParamsTitleBand], NotGiven] = NOT_GIVEN,
        component_installs: Union[Optional[List[ThemesBundlesPatchSiteDraftParamsComponentInstall]], NotGiven] = NOT_GIVEN,
        mobile: Union[Optional[ThemesBundlesPatchSiteDraftParamsMobile], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """List draft theme in an organization (update)

        ``PATCH /orgs/{orgId}/sites/{siteId}/theme/draft``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/draft",
            query=_query({}, extra_query),
            body=_body({"primaryColor": primary_color, "primaryColorDark": primary_color_dark, "accentColor": accent_color, "palette": palette, "paletteDark": palette_dark, "font": font, "colorScheme": color_scheme, "colorSchemeStrict": color_scheme_strict, "contentWidth": content_width, "onThisPage": on_this_page, "layout": layout, "customFontUrl": custom_font_url, "customFontFamily": custom_font_family, "brandName": brand_name, "logoIncludesName": logo_includes_name, "headingFontFamily": heading_font_family, "bodyFontFamily": body_font_family, "monoFontFamily": mono_font_family, "typography": typography, "headingAnchors": heading_anchors, "fonts": fonts, "logoUrl": logo_url, "logoMark": logo_mark, "logoUrlLight": logo_url_light, "logoUrlDark": logo_url_dark, "logoDarkMode": logo_dark_mode, "faviconUrl": favicon_url, "customCss": custom_css, "customJs": custom_js, "scriptOrigins": script_origins, "ads": ads, "whiteLabel": white_label, "showLanguageSwitcher": show_language_switcher, "apiOrigins": api_origins, "fontOrigins": font_origins, "fontOriginsRemoved": font_origins_removed, "imgOrigins": img_origins, "mediaOrigins": media_origins, "frameOrigins": frame_origins, "elementStyles": element_styles, "settingsSchema": settings_schema, "settings": settings, "stringOverrides": string_overrides, "cssSnippets": css_snippets, "announcement": announcement, "chrome": chrome, "notFound": not_found, "components": components, "changelog": changelog, "forum": forum, "post": post, "docs": docs, "footnotes": footnotes, "i18n": i18n, "status": status, "legal": legal, "faq": faq, "roadmap": roadmap, "events": events, "courses": courses, "careers": careers, "contact": contact, "motion": motion, "titleBand": title_band, "componentInstalls": component_installs, "mobile": mobile}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def discard_site_draft(
        self,
        org_id: str,
        site_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeDraftState:
        """List draft theme in an organization (delete)

        ``DELETE /orgs/{orgId}/sites/{siteId}/theme/draft``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/draft",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def publish_site_draft(
        self,
        org_id: str,
        site_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        force: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesBundlesPublishSiteDraftResponse:
        """Publish the draft

        ``POST /orgs/{orgId}/sites/{siteId}/theme/draft/publish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/draft/publish",
            query=_query({}, extra_query),
            body=_body({"force": force}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ThemesComponentMarketplaceResource:
    """``client.themes.component_marketplace`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def browse(
        self,
        org_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        outlet: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentMarketplaceBrowseResponse:
        """Get the component marketplace in an organization

        ``GET /orgs/{orgId}/component-marketplace``

        :param featured: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/component-marketplace",
            query=_query({"q": q, "tag": tag, "featured": featured, "sort": sort, "outlet": outlet}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def detail(
        self,
        org_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentMarketplaceDetailResponse:
        """Get the component

        ``GET /orgs/{orgId}/component-marketplace/components/{slug}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/component-marketplace/components/{_path(slug)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def install(
        self,
        org_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        site_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Install the component

        ``POST /orgs/{orgId}/component-marketplace/components/{slug}/install``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/component-marketplace/components/{_path(slug)}/install",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "siteId": site_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def mine(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentMarketplaceMineResponse:
        """List listings in an organization (component marketplace)

        ``GET /orgs/{orgId}/component-marketplace/listings``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/component-marketplace/listings",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def mine_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``mine`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/component-marketplace/listings",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def submit(
        self,
        org_id: str,
        *,
        install_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentMarketplaceSubmitResponse:
        """Create a listing in an organization (component marketplace)

        ``POST /orgs/{orgId}/component-marketplace/listings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/component-marketplace/listings",
            query=_query({}, extra_query),
            body=_body({"installId": install_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def withdraw(
        self,
        org_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentMarketplaceWithdrawResponse:
        """Delete the listing (component marketplace)

        ``DELETE /orgs/{orgId}/component-marketplace/listings/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/component-marketplace/listings/{_path(slug)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ThemesComponentsResource:
    """``client.themes.components`` (18 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def gallery(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsGalleryResponse:
        """List theme components in an organization

        ``GET /orgs/{orgId}/theme-components``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-components",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def save(
        self,
        org_id: str,
        *,
        name: str,
        space_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        parent_theme_id: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsSaveResponse:
        """Create a theme component in an organization

        ``POST /orgs/{orgId}/theme-components``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/theme-components",
            query=_query({}, extra_query),
            body=_body({"name": name, "spaceId": space_id, "parentThemeId": parent_theme_id, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def patch(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        parent_theme_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsPatchResponse:
        """Update the theme component

        ``PATCH /orgs/{orgId}/theme-components/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/theme-components/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"enabled": enabled, "parentThemeId": parent_theme_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsRemoveResponse:
        """Delete the theme component

        ``DELETE /orgs/{orgId}/theme-components/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/theme-components/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def composite(
        self,
        org_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsCompositeResponse:
        """Get the composite in an organization

        ``GET /orgs/{orgId}/theme-components/{id}/composite``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-components/{_path(id)}/composite",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def import_(
        self,
        org_id: str,
        *,
        url: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsImportResponse:
        """Import the theme component

        ``POST /orgs/{orgId}/theme-components/import``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/theme-components/import",
            query=_query({}, extra_query),
            body=_body({"url": url, "name": name}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def export(
        self,
        org_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeComponentExport:
        """Export the theme component

        ``GET /orgs/{orgId}/theme-components/{id}/export``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-components/{_path(id)}/export",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def apply(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        preset_id: Union[str, NotGiven] = NOT_GIVEN,
        component_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsApplyResponse:
        """Apply the theme

        ``POST /orgs/{orgId}/spaces/{spaceId}/theme/apply``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/apply",
            query=_query({}, extra_query),
            body=_body({"presetId": preset_id, "componentId": component_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsListResponse:
        """List component installs in an organization

        ``GET /orgs/{orgId}/component-installs``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/component-installs",
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
            f"/orgs/{_path(org_id)}/component-installs",
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
        component: ThemesComponentsCreateParamsComponent,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        settings: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a component install in an organization

        ``POST /orgs/{orgId}/component-installs``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/component-installs",
            query=_query({}, extra_query),
            body=_body({"component": component, "settings": settings, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsGetResponse:
        """Get the component install

        ``GET /orgs/{orgId}/component-installs/{id}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/component-installs/{_path(id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        component: Union[ThemesComponentsUpdateParamsComponent, NotGiven] = NOT_GIVEN,
        settings: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsUpdateResponse:
        """Update the component install

        ``PATCH /orgs/{orgId}/component-installs/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/component-installs/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"component": component, "settings": settings, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def componentinstalls(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsComponentinstallsResponse:
        """Delete the component install

        ``DELETE /orgs/{orgId}/component-installs/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/component-installs/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def package(
        self,
        org_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesComponentsPackageResponse:
        """Get the package in an organization

        ``GET /orgs/{orgId}/component-installs/{id}/package``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/component-installs/{_path(id)}/package",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def space_components(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> TargetComponents:
        """List components in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/theme/components``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/components",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_space_components(
        self,
        org_id: str,
        space_id: str,
        *,
        components: List[ThemesComponentsSetSpaceComponentsParamsComponent],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace components in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/theme/components``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/theme/components",
            query=_query({}, extra_query),
            body=_body({"components": components}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def site_components(
        self,
        org_id: str,
        site_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> TargetComponents:
        """List components in an organization

        ``GET /orgs/{orgId}/sites/{siteId}/theme/components``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/components",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_site_components(
        self,
        org_id: str,
        site_id: str,
        *,
        components: List[ThemesComponentsSetSiteComponentsParamsComponent],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace components in an organization

        ``PUT /orgs/{orgId}/sites/{siteId}/theme/components``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/theme/components",
            query=_query({}, extra_query),
            body=_body({"components": components}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ThemesLibraryResource:
    """``client.themes.library`` (7 operations)."""

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
    ) -> ThemesLibraryListResponse:
        """Get the theme library in an organization

        ``GET /orgs/{orgId}/theme-library``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-library",
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
            f"/orgs/{_path(org_id)}/theme-library",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def save(
        self,
        org_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        site_id: Union[str, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        space_types: Union[List[str], NotGiven] = NOT_GIVEN,
        preview_images: Union[List[ThemesLibrarySaveParamsPreviewImage], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the theme library in an organization

        ``POST /orgs/{orgId}/theme-library``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/theme-library",
            query=_query({}, extra_query),
            body=_body({"name": name, "description": description, "spaceId": space_id, "siteId": site_id, "version": version, "tags": tags, "spaceTypes": space_types, "previewImages": preview_images}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def import_(
        self,
        org_id: str,
        *,
        format: str,
        format_version: float,
        meta: ThemesLibraryImportParamsMeta,
        required_origins: ThemesLibraryImportParamsRequiredOrigins,
        theme: ThemesLibraryImportParamsTheme,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        components: Union[List[ThemesLibraryImportParamsComponent], NotGiven] = NOT_GIVEN,
        front_pages: Union[List[ThemesLibraryImportParamsFrontPage], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Import the theme library

        ``POST /orgs/{orgId}/theme-library/import``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/theme-library/import",
            query=_query({}, extra_query),
            body=_body({"format": format, "formatVersion": format_version, "meta": meta, "requiredOrigins": required_origins, "theme": theme, "components": components, "frontPages": front_pages}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesLibraryGetResponse:
        """Get the theme library

        ``GET /orgs/{orgId}/theme-library/{id}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-library/{_path(id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def patch(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        author: Union[ThemesLibraryPatchParamsAuthor, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        license: Union[str, NotGiven] = NOT_GIVEN,
        homepage: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        space_types: Union[List[str], NotGiven] = NOT_GIVEN,
        preview_images: Union[List[ThemesLibraryPatchParamsPreviewImage], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesLibraryPatchResponse:
        """Update the theme library

        ``PATCH /orgs/{orgId}/theme-library/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/theme-library/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"slug": slug, "author": author, "version": version, "license": license, "homepage": homepage, "tags": tags, "spaceTypes": space_types, "previewImages": preview_images, "name": name, "description": description}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesLibraryRemoveResponse:
        """Delete the theme library

        ``DELETE /orgs/{orgId}/theme-library/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/theme-library/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bundle(
        self,
        org_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeBundleExport:
        """Get the bundle in an organization (theme library)

        ``GET /orgs/{orgId}/theme-library/{id}/bundle``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-library/{_path(id)}/bundle",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class ThemesMarketplaceResource:
    """``client.themes.marketplace`` (12 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def browse(
        self,
        org_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        space_type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeBrowseResult:
        """Get the theme marketplace in an organization

        ``GET /orgs/{orgId}/theme-marketplace``

        :param featured: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-marketplace",
            query=_query({"q": q, "tag": tag, "featured": featured, "sort": sort, "spaceType": space_type}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def detail(
        self,
        org_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplaceDetailResponse:
        """Get one marketplace theme, with its look

        ``GET /orgs/{orgId}/theme-marketplace/themes/{slug}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-marketplace/themes/{_path(slug)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def install(
        self,
        org_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        site_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Install the theme

        ``POST /orgs/{orgId}/theme-marketplace/themes/{slug}/install``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/theme-marketplace/themes/{_path(slug)}/install",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "siteId": site_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def purchase(
        self,
        org_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplacePurchaseResponse:
        """Create the purchase in an organization (theme marketplace themes)

        ``POST /orgs/{orgId}/theme-marketplace/themes/{slug}/purchase``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/theme-marketplace/themes/{_path(slug)}/purchase",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def mine(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplaceMineResponse:
        """List listings in an organization (theme marketplace)

        ``GET /orgs/{orgId}/theme-marketplace/listings``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-marketplace/listings",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def mine_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``mine`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/theme-marketplace/listings",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def submit(
        self,
        org_id: str,
        *,
        component_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        pricing: Union[str, NotGiven] = NOT_GIVEN,
        price_cents: Union[int, NotGiven] = NOT_GIVEN,
        currency: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplaceSubmitResponse:
        """Create a listing in an organization (theme marketplace)

        ``POST /orgs/{orgId}/theme-marketplace/listings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/theme-marketplace/listings",
            query=_query({}, extra_query),
            body=_body({"componentId": component_id, "pricing": pricing, "priceCents": price_cents, "currency": currency}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def pricing(
        self,
        org_id: str,
        slug: str,
        *,
        pricing: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        price_cents: Union[int, NotGiven] = NOT_GIVEN,
        currency: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplacePricingResponse:
        """Replace the pricing in an organization

        ``PUT /orgs/{orgId}/theme-marketplace/listings/{slug}/pricing``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/theme-marketplace/listings/{_path(slug)}/pricing",
            query=_query({}, extra_query),
            body=_body({"pricing": pricing, "priceCents": price_cents, "currency": currency}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def withdraw(
        self,
        org_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplaceWithdrawResponse:
        """Delete the listing (theme marketplace)

        ``DELETE /orgs/{orgId}/theme-marketplace/listings/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/theme-marketplace/listings/{_path(slug)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def browse_registry(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplaceBrowseRegistryResponse:
        """Get the theme registry in an organization

        ``GET /orgs/{orgId}/theme-registry``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/theme-registry",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def browse_registry_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``browse_registry`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/theme-registry",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def publish(
        self,
        org_id: str,
        *,
        component_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplacePublishResponse:
        """Publish the theme registry

        ``POST /orgs/{orgId}/theme-registry/publish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/theme-registry/publish",
            query=_query({}, extra_query),
            body=_body({"componentId": component_id, "description": description}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def legacy_install(
        self,
        org_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplaceLegacyInstallResponse:
        """Install the theme registry

        ``POST /orgs/{orgId}/theme-registry/{slug}/install``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/theme-registry/{_path(slug)}/install",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unpublish(
        self,
        org_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesMarketplaceUnpublishResponse:
        """Delete the theme registry

        ``DELETE /orgs/{orgId}/theme-registry/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/theme-registry/{_path(slug)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ThemesResource:
    """``client.themes`` (1 operation; bundles, component_marketplace, components, library, marketplace)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.bundles = ThemesBundlesResource(client)
        self.component_marketplace = ThemesComponentMarketplaceResource(client)
        self.components = ThemesComponentsResource(client)
        self.library = ThemesLibraryResource(client)
        self.marketplace = ThemesMarketplaceResource(client)

    def outlets(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemesOutletsResponse:
        """List theme outlets

        ``GET /theme-outlets``
        """
        return self._client._request(
            "GET",
            f"/theme-outlets",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
