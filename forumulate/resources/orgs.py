from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class OrgsCaptchaResource:
    """``client.orgs.captcha`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsCaptchaGetResponse:
        """Get the captcha in an organization

        ``GET /orgs/{orgId}/captcha``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/captcha",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        *,
        provider: str,
        site_key: str,
        secret: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsCaptchaSetResponse:
        """Replace the captcha in an organization

        ``PUT /orgs/{orgId}/captcha``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/captcha",
            query=_query({}, extra_query),
            body=_body({"provider": provider, "siteKey": site_key, "secret": secret}, extra_body),
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
    ) -> ErrorEnvelope:
        """Delete the captcha in an organization

        ``DELETE /orgs/{orgId}/captcha``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/captcha",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class OrgsHealthResource:
    """``client.orgs.health`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def report(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> HealthReport:
        """Health of an organization

        ``GET /orgs/{orgId}/health``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/health",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class OrgsSettingsResource:
    """``client.orgs.settings`` (3 operations)."""

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
    ) -> OrgsSettingsListResponse:
        """Every org setting, with its value and its bounds

        ``GET /orgs/{orgId}/settings``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/settings",
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
    ) -> Iterator[SettingView]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/settings",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="settings",
        )

    def set(
        self,
        org_id: str,
        key: str,
        *,
        value: Any,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsSettingsSetResponse:
        """Set one org setting

        ``PUT /orgs/{orgId}/settings/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/settings/{_path(key)}",
            query=_query({}, extra_query),
            body=_body({"value": value}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reset(
        self,
        org_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsSettingsResetResponse:
        """Reset one org setting to its default

        ``DELETE /orgs/{orgId}/settings/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/settings/{_path(key)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class OrgsResource:
    """``client.orgs`` (30 operations; captcha, health, settings)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.captcha = OrgsCaptchaResource(client)
        self.health = OrgsHealthResource(client)
        self.settings = OrgsSettingsResource(client)

    def email_settings(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsEmailSettingsResponse:
        """List email settings in an organization

        ``GET /orgs/{orgId}/email-settings``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/email-settings",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_email_from(
        self,
        org_id: str,
        *,
        email_from: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsSetEmailFromResponse:
        """Update the email from in an organization

        ``PATCH /orgs/{orgId}/email-from``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/email-from",
            query=_query({}, extra_query),
            body=_body({"emailFrom": email_from}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def email_branding(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsEmailBrandingResponse:
        """Get the email branding in an organization

        ``GET /orgs/{orgId}/email-branding``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/email-branding",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_email_branding(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        footer: Union[Optional[str], NotGiven] = NOT_GIVEN,
        subject_prefix: Union[Optional[str], NotGiven] = NOT_GIVEN,
        hide_branding: Union[Any, NotGiven] = NOT_GIVEN,
        logo_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        logo_alt: Union[Optional[str], NotGiven] = NOT_GIVEN,
        logo_width: Union[Optional[int], NotGiven] = NOT_GIVEN,
        display_name: Union[Optional[str], NotGiven] = NOT_GIVEN,
        primary_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        button_text_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        background_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        surface_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        text_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        muted_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        dark_mode: Union[Any, NotGiven] = NOT_GIVEN,
        dark: Union[Optional[OrgsSetEmailBrandingParamsDark], NotGiven] = NOT_GIVEN,
        font_family: Union[Optional[str], NotGiven] = NOT_GIVEN,
        web_font_name: Union[Optional[str], NotGiven] = NOT_GIVEN,
        web_font_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        address: Union[Optional[str], NotGiven] = NOT_GIVEN,
        footer_links: Union[Optional[List[OrgsSetEmailBrandingParamsFooterLink]], NotGiven] = NOT_GIVEN,
        social_links: Union[Optional[List[OrgsSetEmailBrandingParamsSocialLink]], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsSetEmailBrandingResponse:
        """Update the email branding in an organization

        ``PATCH /orgs/{orgId}/email-branding``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/email-branding",
            query=_query({}, extra_query),
            body=_body({"footer": footer, "subjectPrefix": subject_prefix, "hideBranding": hide_branding, "logoUrl": logo_url, "logoAlt": logo_alt, "logoWidth": logo_width, "displayName": display_name, "primaryColor": primary_color, "buttonTextColor": button_text_color, "backgroundColor": background_color, "surfaceColor": surface_color, "textColor": text_color, "mutedColor": muted_color, "darkMode": dark_mode, "dark": dark, "fontFamily": font_family, "webFontName": web_font_name, "webFontUrl": web_font_url, "address": address, "footerLinks": footer_links, "socialLinks": social_links}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_siem(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsGetSiemResponse:
        """Get the SIEM in an organization

        ``GET /orgs/{orgId}/siem``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/siem",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_siem(
        self,
        org_id: str,
        *,
        url: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        token: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsSetSiemResponse:
        """Replace the SIEM in an organization

        ``PUT /orgs/{orgId}/siem``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/siem",
            query=_query({}, extra_query),
            body=_body({"url": url, "token": token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def legal_status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LegalStatus:
        """Get the legal in an organization

        ``GET /orgs/{orgId}/legal``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/legal",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def upsert_legal(
        self,
        org_id: str,
        *,
        kind: str,
        title: str,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        required: Union[bool, NotGiven] = NOT_GIVEN,
        on_this_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[OrgsUpsertLegalParamsCustomization], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsUpsertLegalResponse:
        """Create the legal in an organization

        ``POST /orgs/{orgId}/legal``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/legal",
            query=_query({}, extra_query),
            body=_body({"kind": kind, "title": title, "body": body, "required": required, "onThisPage": on_this_page, "customization": customization}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def legal_embed_acceptances(
        self,
        org_id: str,
        kind: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsLegalEmbedAcceptancesResponse:
        """List acceptances in an organization

        ``GET /orgs/{orgId}/legal/{kind}/acceptances``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/legal/{_path(kind)}/acceptances",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def legal_acceptance_gate(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsLegalAcceptanceGateResponse:
        """Get the acceptance in an organization

        ``GET /orgs/{orgId}/legal/acceptance``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/legal/acceptance",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_legal_acceptance_gate(
        self,
        org_id: str,
        *,
        shared_secret: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsSetLegalAcceptanceGateResponse:
        """Replace the acceptance in an organization

        ``PUT /orgs/{orgId}/legal/acceptance``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/legal/acceptance",
            query=_query({}, extra_query),
            body=_body({"sharedSecret": shared_secret}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def legal_edition_diff(
        self,
        org_id: str,
        kind: str,
        *,
        from_: str,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsLegalEditionDiffResponse:
        """Get the diff in an organization

        ``GET /orgs/{orgId}/legal/{kind}/diff``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/legal/{_path(kind)}/diff",
            query=_query({"from": from_}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def legal_embed_acceptances_csv(
        self,
        org_id: str,
        kind: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of acceptances

        ``GET /orgs/{orgId}/legal/{kind}/acceptances.csv``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/legal/{_path(kind)}/acceptances.csv",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def bind_legal_page(
        self,
        org_id: str,
        *,
        kind: str,
        page_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        required: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsBindLegalPageResponse:
        """Bind the legal

        ``POST /orgs/{orgId}/legal/bind``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/legal/bind",
            query=_query({}, extra_query),
            body=_body({"kind": kind, "pageId": page_id, "required": required}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unbind_legal(
        self,
        org_id: str,
        kind: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsUnbindLegalResponse:
        """Delete the legal

        ``DELETE /orgs/{orgId}/legal/{kind}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/legal/{_path(kind)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def suggested_legal(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsSuggestedLegalResponse:
        """Get the suggested in an organization

        ``GET /orgs/{orgId}/legal/suggested``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/legal/suggested",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def suggested_legal_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[OrgsSuggestedLegalResponseSuggestedItem]:
        """Iterate every item of ``suggested_legal`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/legal/suggested",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="suggested",
        )

    def reorder_legal(
        self,
        org_id: str,
        *,
        kinds: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsReorderLegalResponse:
        """Reorder the legal

        ``POST /orgs/{orgId}/legal/reorder``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/legal/reorder",
            query=_query({}, extra_query),
            body=_body({"kinds": kinds}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def accept_legal(
        self,
        org_id: str,
        document_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LegalStatus:
        """Accept the legal

        ``POST /orgs/{orgId}/legal/{documentId}/accept``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/legal/{_path(document_id)}/accept",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def plan(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsPlanResponse:
        """Get the plan in an organization

        ``GET /orgs/{orgId}/plan``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/plan",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_plan(
        self,
        org_id: str,
        *,
        plan: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsSetPlanResponse:
        """Update the plan in an organization

        ``PATCH /orgs/{orgId}/plan``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/plan",
            query=_query({}, extra_query),
            body=_body({"plan": plan}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_override(
        self,
        org_id: str,
        *,
        metric: str,
        extra: Optional[int],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsSetOverrideResponse:
        """Update overrides in an organization

        ``PATCH /orgs/{orgId}/plan/overrides``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/plan/overrides",
            query=_query({}, extra_query),
            body=_body({"metric": metric, "extra": extra}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def export(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgExport:
        """Export the whole organization as one document

        ``GET /orgs/{orgId}/export``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/export",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def import_(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        format: Union[str, NotGiven] = NOT_GIVEN,
        version: Union[int, NotGiven] = NOT_GIVEN,
        exported_at: Union[str, NotGiven] = NOT_GIVEN,
        organization: Union[Any, NotGiven] = NOT_GIVEN,
        members: Union[Any, NotGiven] = NOT_GIVEN,
        spaces: Union[List[OrgsImportParamsSpace], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsImportResponse:
        """Import an export document into this organization

        ``POST /orgs/{orgId}/import``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/import",
            query=_query({}, extra_query),
            body=_body({"format": format, "version": version, "exportedAt": exported_at, "organization": organization, "members": members, "spaces": spaces}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgListDto:
        """List orgs

        ``GET /orgs``

        :param limit: Organizations per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[OrgSummaryDto]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="orgs",
        )

    def create(
        self,
        *,
        name: str,
        slug: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsCreateResponse:
        """Create an org

        ``POST /orgs``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs",
            query=_query({}, extra_query),
            body=_body({"name": name, "slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rename_slug(
        self,
        org_id: str,
        *,
        slug: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsRenameSlugResponse:
        """Rename the organization’s slug

        ``PATCH /orgs/{orgId}/slug``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/slug",
            query=_query({}, extra_query),
            body=_body({"slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsGetResponse:
        """Get the org

        ``GET /orgs/{orgId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        inbound_email_domain: Union[Optional[str], NotGiven] = NOT_GIVEN,
        content_language: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsUpdateResponse:
        """Update the org

        ``PATCH /orgs/{orgId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "inboundEmailDomain": inbound_email_domain, "contentLanguage": content_language}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgsRemoveResponse:
        """Delete the org

        ``DELETE /orgs/{orgId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def apply(
        self,
        org_id: str,
        *,
        version: float,
        apply: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        spaces: Union[List[OrgsApplyParamsSpace], NotGiven] = NOT_GIVEN,
        sources: Union[List[OrgsApplyParamsSource], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Apply a declarative site manifest (dry run by default)

        ``PUT /orgs/{orgId}/manifest``

        :param apply: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/manifest",
            query=_query({"apply": apply}, extra_query),
            body=_body({"version": version, "spaces": spaces, "sources": sources}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
