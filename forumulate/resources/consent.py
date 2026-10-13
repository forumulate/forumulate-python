from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ConsentResource:
    """``client.consent`` (10 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get_org(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConsentConfigView:
        """Get the consent in an organization

        ``GET /orgs/{orgId}/consent``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/consent",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_org(
        self,
        org_id: str,
        *,
        provider: str,
        validate: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        preset: Union[ConsentPreset, NotGiven] = NOT_GIVEN,
        custom: Union[ConsentConfigCustom, NotGiven] = NOT_GIVEN,
        hosted: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        policy_version: Union[str, NotGiven] = NOT_GIVEN,
        webhook_secret: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the consent in an organization

        ``PUT /orgs/{orgId}/consent``

        :param validate: Set true for a dry run: validate the body and return the resulting `ResolvedConsentConfig`, writing NOTHING.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/consent",
            query=_query({"validate": validate}, extra_query),
            body=_body({"provider": provider, "preset": preset, "custom": custom, "hosted": hosted, "policyVersion": policy_version, "webhookSecret": webhook_secret}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rotate_webhook_secret(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConsentRotateWebhookSecretResponse:
        """Create the webhook secret in an organization

        ``POST /orgs/{orgId}/consent/webhook-secret``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/consent/webhook-secret",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def executor_key_status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConsentExecutorKeyStatusResponse:
        """Is a privacy-executor credential configured?

        ``GET /orgs/{orgId}/privacy/executor-key``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/privacy/executor-key",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def rotate_executor_key(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConsentRotateExecutorKeyResponse:
        """Mint this organization’s privacy-executor credential

        ``POST /orgs/{orgId}/privacy/executor-key``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/privacy/executor-key",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def send_test_event(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConsentSendTestEventResponse:
        """Create the webhook test in an organization

        ``POST /orgs/{orgId}/consent/webhook-test``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/consent/webhook-test",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def purge_org(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Purge the cache (consent)

        ``POST /orgs/{orgId}/consent/cache/purge``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/consent/cache/purge",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_space(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceConsentConfig:
        """Get the consent in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/consent``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/consent",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_space(
        self,
        org_id: str,
        space_id: str,
        *,
        validate: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        body: Any = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the consent in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/consent``

        :param validate: Set true for a dry run: validate the body and return the resulting `ResolvedConsentConfig`, writing NOTHING.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/consent",
            query=_query({"validate": validate}, extra_query),
            body=body,
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def purge_space(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Purge the cache (spaces)

        ``POST /orgs/{orgId}/spaces/{spaceId}/cache/purge``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/cache/purge",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
