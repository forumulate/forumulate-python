from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SsoAtlasResource:
    """``client.sso.atlas`` (13 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list_sso(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasListSsoResponse:
        """Get the SSO in an organization (atlas enterprise)

        ``GET /orgs/{orgId}/atlas-enterprise/sso``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/atlas-enterprise/sso",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_sso_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_sso`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/atlas-enterprise/sso",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create_sso(
        self,
        org_id: str,
        *,
        type: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        domain: Union[str, NotGiven] = NOT_GIVEN,
        oidc: Union[SsoAtlasCreateSsoParamsOidc, NotGiven] = NOT_GIVEN,
        saml: Union[SsoAtlasCreateSsoParamsSaml, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasCreateSsoResponse:
        """Create the SSO in an organization

        ``POST /orgs/{orgId}/atlas-enterprise/sso``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/atlas-enterprise/sso",
            query=_query({}, extra_query),
            body=_body({"type": type, "name": name, "domain": domain, "oidc": oidc, "saml": saml}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_sso(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        domain: Union[str, NotGiven] = NOT_GIVEN,
        active: Union[bool, NotGiven] = NOT_GIVEN,
        oidc: Union[SsoAtlasUpdateSsoParamsOidc, NotGiven] = NOT_GIVEN,
        saml: Union[SsoAtlasUpdateSsoParamsSaml, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasUpdateSsoResponse:
        """Update the SSO

        ``PATCH /orgs/{orgId}/atlas-enterprise/sso/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/atlas-enterprise/sso/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "domain": domain, "active": active, "oidc": oidc, "saml": saml}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_sso(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasDeleteSsoResponse:
        """Delete the SSO

        ``DELETE /orgs/{orgId}/atlas-enterprise/sso/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/atlas-enterprise/sso/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_enforced(
        self,
        org_id: str,
        *,
        enforced: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasSetEnforcedResponse:
        """Update the enforce in an organization

        ``PATCH /orgs/{orgId}/atlas-enterprise/sso/enforce``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/atlas-enterprise/sso/enforce",
            query=_query({}, extra_query),
            body=_body({"enforced": enforced}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_scim(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasGetScimResponse:
        """Get the SCIM in an organization

        ``GET /orgs/{orgId}/atlas-enterprise/scim``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/atlas-enterprise/scim",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def mint_scim(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasMintScimResponse:
        """Create the mint in an organization

        ``POST /orgs/{orgId}/atlas-enterprise/scim/mint``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/atlas-enterprise/scim/mint",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rotate_scim(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasRotateScimResponse:
        """Rotate the SCIM

        ``POST /orgs/{orgId}/atlas-enterprise/scim/rotate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/atlas-enterprise/scim/rotate",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def disable_scim(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasDisableScimResponse:
        """Disable the SCIM

        ``POST /orgs/{orgId}/atlas-enterprise/scim/disable``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/atlas-enterprise/scim/disable",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_oauth_clients(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasListOauthClientsResponse:
        """List OAuth clients in an organization

        ``GET /orgs/{orgId}/atlas-enterprise/oauth-clients``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/atlas-enterprise/oauth-clients",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_oauth_clients_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_oauth_clients`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/atlas-enterprise/oauth-clients",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create_oauth_client(
        self,
        org_id: str,
        *,
        name: str,
        redirect_uris: List[str],
        scopes: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasCreateOauthClientResponse:
        """Create an OAuth client in an organization

        ``POST /orgs/{orgId}/atlas-enterprise/oauth-clients``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/atlas-enterprise/oauth-clients",
            query=_query({}, extra_query),
            body=_body({"name": name, "redirectUris": redirect_uris, "scopes": scopes, "type": type}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rotate_oauth_client_secret(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasRotateOauthClientSecretResponse:
        """Rotate secret in an organization (atlas enterprise OAuth clients)

        ``POST /orgs/{orgId}/atlas-enterprise/oauth-clients/{id}/rotate-secret``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/atlas-enterprise/oauth-clients/{_path(id)}/rotate-secret",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_oauth_client(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoAtlasDeleteOauthClientResponse:
        """Delete the OAuth client

        ``DELETE /orgs/{orgId}/atlas-enterprise/oauth-clients/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/atlas-enterprise/oauth-clients/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SsoDiscourseConnectResource:
    """``client.sso.discourse_connect`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get_config(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoDiscourseConnectGetConfigResponse:
        """Get the config in an organization

        ``GET /orgs/{orgId}/discourse-connect/config``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/discourse-connect/config",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_config(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        secret: Union[str, NotGiven] = NOT_GIVEN,
        provider_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        allowed_domain: Union[Optional[str], NotGiven] = NOT_GIVEN,
        default_role: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoDiscourseConnectSetConfigResponse:
        """Replace the config in an organization

        ``PUT /orgs/{orgId}/discourse-connect/config``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/discourse-connect/config",
            query=_query({}, extra_query),
            body=_body({"mode": mode, "secret": secret, "providerUrl": provider_url, "allowedDomain": allowed_domain, "defaultRole": default_role, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def provider(
        self,
        org_id: str,
        *,
        sso: str,
        sig: str,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Get the provider in an organization (discourse connect)

        ``GET /orgs/{orgId}/discourse-connect/provider``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/discourse-connect/provider",
            query=_query({"sso": sso, "sig": sig}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class SsoLtiResource:
    """``client.sso.lti`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoLtiGetResponse:
        """Get the LTI in an organization

        ``GET /orgs/{orgId}/lti``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/lti",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        *,
        issuer: str,
        client_id: str,
        auth_login_url: str,
        jwks_url: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        deployment_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        allowed_domain: Union[Optional[str], NotGiven] = NOT_GIVEN,
        default_role: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoLtiSetResponse:
        """Replace the LTI in an organization

        ``PUT /orgs/{orgId}/lti``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/lti",
            query=_query({}, extra_query),
            body=_body({"issuer": issuer, "clientId": client_id, "authLoginUrl": auth_login_url, "jwksUrl": jwks_url, "deploymentId": deployment_id, "allowedDomain": allowed_domain, "defaultRole": default_role, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SsoSamlResource:
    """``client.sso.saml`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoSamlGetResponse:
        """Get the SAML in an organization

        ``GET /orgs/{orgId}/saml``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/saml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        *,
        idp_entry_point: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        idp_cert: Union[str, NotGiven] = NOT_GIVEN,
        allowed_domain: Union[Optional[str], NotGiven] = NOT_GIVEN,
        default_role: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoSamlSetResponse:
        """Replace the SAML in an organization

        ``PUT /orgs/{orgId}/saml``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/saml",
            query=_query({}, extra_query),
            body=_body({"idpEntryPoint": idp_entry_point, "idpCert": idp_cert, "allowedDomain": allowed_domain, "defaultRole": default_role, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SsoScimResource:
    """``client.sso.scim`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoScimStatusResponse:
        """Get the token in an organization

        ``GET /orgs/{orgId}/scim/token``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/scim/token",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def create(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoScimCreateResponse:
        """Create the token in an organization

        ``POST /orgs/{orgId}/scim/token``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/scim/token",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoScimRevokeResponse:
        """Delete the token in an organization

        ``DELETE /orgs/{orgId}/scim/token``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/scim/token",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SsoResource:
    """``client.sso`` (3 operations; atlas, discourse_connect, lti, saml, scim)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.atlas = SsoAtlasResource(client)
        self.discourse_connect = SsoDiscourseConnectResource(client)
        self.lti = SsoLtiResource(client)
        self.saml = SsoSamlResource(client)
        self.scim = SsoScimResource(client)

    def get(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoGetResponse:
        """Get the SSO in an organization

        ``GET /orgs/{orgId}/sso``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sso",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        *,
        client_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        provider: Union[str, NotGiven] = NOT_GIVEN,
        issuer: Union[str, NotGiven] = NOT_GIVEN,
        client_secret: Union[str, NotGiven] = NOT_GIVEN,
        allowed_domain: Union[Optional[str], NotGiven] = NOT_GIVEN,
        default_role: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        require_sso: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoSetResponse:
        """Replace the SSO in an organization

        ``PUT /orgs/{orgId}/sso``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/sso",
            query=_query({}, extra_query),
            body=_body({"provider": provider, "issuer": issuer, "clientId": client_id, "clientSecret": client_secret, "allowedDomain": allowed_domain, "defaultRole": default_role, "enabled": enabled, "requireSso": require_sso}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def providers(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SsoProvidersResponse:
        """List providers in an organization

        ``GET /orgs/{orgId}/sso/providers``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sso/providers",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def providers_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``providers`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/sso/providers",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )
