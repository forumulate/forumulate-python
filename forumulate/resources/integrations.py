from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class IntegrationsCloudflareResource:
    """``client.integrations.cloudflare`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgCloudflareView:
        """Get the cloudflare in an organization

        ``GET /orgs/{orgId}/integrations/cloudflare``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/integrations/cloudflare",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        token: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        zone_mode: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the cloudflare in an organization

        ``PUT /orgs/{orgId}/integrations/cloudflare``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/integrations/cloudflare",
            query=_query({}, extra_query),
            body=_body({"token": token, "enabled": enabled, "zoneMode": zone_mode}, extra_body),
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
    ) -> IntegrationsCloudflareClearResponse:
        """Delete the cloudflare in an organization

        ``DELETE /orgs/{orgId}/integrations/cloudflare``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/integrations/cloudflare",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def test(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsCloudflareTestResponse:
        """Test the cloudflare

        ``POST /orgs/{orgId}/integrations/cloudflare/test``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/integrations/cloudflare/test",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class IntegrationsDeeplResource:
    """``client.integrations.deepl`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsDeeplStatusResponse:
        """Get the deepl in an organization

        ``GET /orgs/{orgId}/deepl``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/deepl",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_key(
        self,
        org_id: str,
        *,
        api_key: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsDeeplSetKeyResponse:
        """Replace the deepl in an organization

        ``PUT /orgs/{orgId}/deepl``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/deepl",
            query=_query({}, extra_query),
            body=_body({"apiKey": api_key}, extra_body),
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
    ) -> IntegrationsDeeplClearResponse:
        """Delete the deepl in an organization

        ``DELETE /orgs/{orgId}/deepl``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/deepl",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class IntegrationsGithubResource:
    """``client.integrations.github`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsGithubStatusResponse:
        """Get the GitHub in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/github``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/github",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def connect(
        self,
        org_id: str,
        space_id: str,
        *,
        repo: str,
        token: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        provider: Union[str, NotGiven] = NOT_GIVEN,
        branch: Union[str, NotGiven] = NOT_GIVEN,
        path: Union[str, NotGiven] = NOT_GIVEN,
        auto_export: Union[bool, NotGiven] = NOT_GIVEN,
        commit_template: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsGithubConnectResponse:
        """Replace the GitHub in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/github``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/github",
            query=_query({}, extra_query),
            body=_body({"provider": provider, "repo": repo, "branch": branch, "path": path, "token": token, "autoExport": auto_export, "commitTemplate": commit_template}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def egress_ips(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsGithubEgressIpsResponse:
        """List egress IPs in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/github/egress-ips``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/github/egress-ips",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def egress_ips_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``egress_ips`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/github/egress-ips",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def import_(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsGithubImportResponse:
        """Import the GitHub

        ``POST /orgs/{orgId}/spaces/{spaceId}/github/import``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/github/import",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def export(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsGithubExportResponse:
        """Export the GitHub

        ``POST /orgs/{orgId}/spaces/{spaceId}/github/export``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/github/export",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def pull_request(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsGithubPullRequestResponse:
        """Create the pull request in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/github/change-requests/{crId}/pull-request``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/github/change-requests/{_path(cr_id)}/pull-request",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class IntegrationsGithubAgentResource:
    """``client.integrations.github_agent`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsGithubAgentStatusResponse:
        """Get the GitHub agent in an organization

        ``GET /orgs/{orgId}/github-agent``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/github-agent",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def connect(
        self,
        org_id: str,
        *,
        repo_full_name: str,
        webhook_secret: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        access_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsGithubAgentConnectResponse:
        """Create the GitHub agent in an organization

        ``POST /orgs/{orgId}/github-agent``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/github-agent",
            query=_query({}, extra_query),
            body=_body({"repoFullName": repo_full_name, "webhookSecret": webhook_secret, "accessToken": access_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def disconnect(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsGithubAgentDisconnectResponse:
        """Delete the GitHub agent in an organization

        ``DELETE /orgs/{orgId}/github-agent``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/github-agent",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class IntegrationsSlackResource:
    """``client.integrations.slack`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsSlackStatusResponse:
        """Get the slack in an organization

        ``GET /orgs/{orgId}/slack``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/slack",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def connect(
        self,
        org_id: str,
        *,
        team_id: str,
        bot_token: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        team_name: Union[str, NotGiven] = NOT_GIVEN,
        bot_user_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the slack in an organization

        ``PUT /orgs/{orgId}/slack``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/slack",
            query=_query({}, extra_query),
            body=_body({"teamId": team_id, "teamName": team_name, "botToken": bot_token, "botUserId": bot_user_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def disconnect(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsSlackDisconnectResponse:
        """Delete the slack in an organization

        ``DELETE /orgs/{orgId}/slack``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/slack",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def install_url(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsSlackInstallUrlResponse:
        """Install URL in an organization

        ``GET /orgs/{orgId}/slack/install-url``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/slack/install-url",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class IntegrationsResource:
    """``client.integrations`` (6 operations; cloudflare, deepl, github, github_agent, slack)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.cloudflare = IntegrationsCloudflareResource(client)
        self.deepl = IntegrationsDeeplResource(client)
        self.github = IntegrationsGithubResource(client)
        self.github_agent = IntegrationsGithubAgentResource(client)
        self.slack = IntegrationsSlackResource(client)

    def catalog(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsCatalogResponse:
        """Get the catalog in an organization (integrations)

        ``GET /orgs/{orgId}/integrations/catalog``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/integrations/catalog",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def catalog_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``catalog`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/integrations/catalog",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    ) -> IntegrationsListResponse:
        """List integrations in an organization

        ``GET /orgs/{orgId}/integrations``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/integrations",
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
            f"/orgs/{_path(org_id)}/integrations",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def install(
        self,
        org_id: str,
        *,
        integration_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        events: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsInstallResponse:
        """Create an integration in an organization

        ``POST /orgs/{orgId}/integrations``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/integrations",
            query=_query({}, extra_query),
            body=_body({"integrationId": integration_id, "config": config, "events": events}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        events: Union[List[str], NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsUpdateResponse:
        """Update the integration

        ``PATCH /orgs/{orgId}/integrations/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/integrations/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"config": config, "events": events, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def uninstall(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsUninstallResponse:
        """Delete the integration

        ``DELETE /orgs/{orgId}/integrations/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/integrations/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def test(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IntegrationsTestResponse:
        """Test the integration

        ``POST /orgs/{orgId}/integrations/{id}/test``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/integrations/{_path(id)}/test",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
