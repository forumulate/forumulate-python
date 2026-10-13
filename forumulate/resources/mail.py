from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class MailProviderResource:
    """``client.mail.provider`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailProviderView:
        """Get the provider in an organization (mail)

        ``GET /orgs/{orgId}/mail/provider``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/mail/provider",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def connect(
        self,
        org_id: str,
        *,
        provider: str,
        api_key: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        domain: Union[str, NotGiven] = NOT_GIVEN,
        region: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailProviderConnectResponse:
        """Replace the provider in an organization (mail)

        ``PUT /orgs/{orgId}/mail/provider``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/mail/provider",
            query=_query({}, extra_query),
            body=_body({"provider": provider, "apiKey": api_key, "domain": domain, "region": region}, extra_body),
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
    ) -> MailProviderDisconnectResponse:
        """Delete the provider in an organization (mail)

        ``DELETE /orgs/{orgId}/mail/provider``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/mail/provider",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def test(
        self,
        org_id: str,
        *,
        to: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailProviderTestResponse:
        """Test the provider (mail)

        ``POST /orgs/{orgId}/mail/provider/test``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/mail/provider/test",
            query=_query({}, extra_query),
            body=_body({"to": to}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class MailTemplatesResource:
    """``client.mail.templates`` (6 operations)."""

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
    ) -> MailTemplatesListResponse:
        """List email templates in an organization

        ``GET /orgs/{orgId}/email-templates``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/email-templates",
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
    ) -> Iterator[EmailTemplateSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/email-templates",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="templates",
        )

    def get(
        self,
        org_id: str,
        key: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailTemplatesGetResponse:
        """Get the email template

        ``GET /orgs/{orgId}/email-templates/{key}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/email-templates/{_path(key)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def save(
        self,
        org_id: str,
        key: str,
        *,
        subject: str,
        blocks: List[MailTemplatesSaveParamsBlock],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        preheader: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        locale: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailTemplatesSaveResponse:
        """Replace the email template

        ``PUT /orgs/{orgId}/email-templates/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/email-templates/{_path(key)}",
            query=_query({}, extra_query),
            body=_body({"subject": subject, "preheader": preheader, "blocks": blocks, "spaceId": space_id, "locale": locale}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reset(
        self,
        org_id: str,
        key: str,
        *,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailTemplatesResetResponse:
        """Delete the email template

        ``DELETE /orgs/{orgId}/email-templates/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/email-templates/{_path(key)}",
            query=_query({"spaceId": space_id, "locale": locale}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def preview(
        self,
        org_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        locale: Union[Optional[str], NotGiven] = NOT_GIVEN,
        content: Union[MailTemplatesPreviewParamsContent, NotGiven] = NOT_GIVEN,
        vars: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        scheme: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Preview the email template

        ``POST /orgs/{orgId}/email-templates/{key}/preview``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/email-templates/{_path(key)}/preview",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "locale": locale, "content": content, "vars": vars, "scheme": scheme}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def test(
        self,
        org_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        locale: Union[Optional[str], NotGiven] = NOT_GIVEN,
        content: Union[MailTemplatesTestParamsContent, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailTemplatesTestResponse:
        """Test the email template

        ``POST /orgs/{orgId}/email-templates/{key}/test``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/email-templates/{_path(key)}/test",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "locale": locale, "content": content}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class MailUnsubscribeResource:
    """``client.mail.unsubscribe`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def page(
        self,
        *,
        token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Unsubscribe confirmation page

        ``GET /mail/unsubscribe``
        """
        return self._client._request(
            "GET",
            f"/mail/unsubscribe",
            query=_query({"token": token}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def one_click(
        self,
        *,
        token: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailUnsubscribeOneClickResponse:
        """One-click unsubscribe from an email list

        ``POST /mail/unsubscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/mail/unsubscribe",
            query=_query({"token": token}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class MailResource:
    """``client.mail`` (5 operations; provider, templates, unsubscribe)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.provider = MailProviderResource(client)
        self.templates = MailTemplatesResource(client)
        self.unsubscribe = MailUnsubscribeResource(client)

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailListResponse:
        """List suppressions in an organization

        ``GET /orgs/{orgId}/mail/suppressions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/mail/suppressions",
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
    ) -> Iterator[SuppressionRow]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/mail/suppressions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="suppressions",
        )

    def suppress(
        self,
        org_id: str,
        *,
        email: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailSuppressResponse:
        """Create a suppression in an organization

        ``POST /orgs/{orgId}/mail/suppressions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/mail/suppressions",
            query=_query({}, extra_query),
            body=_body({"email": email}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unsuppress(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailUnsuppressResponse:
        """Delete suppressions in an organization

        ``DELETE /orgs/{orgId}/mail/suppressions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/mail/suppressions",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def log(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailLogResponse:
        """Get the log in an organization (mail)

        ``GET /orgs/{orgId}/mail/log``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/mail/log",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def log_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[MailLogRow]:
        """Iterate every item of ``log`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/mail/log",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="log",
        )

    def check(
        self,
        org_id: str,
        *,
        email: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MailCheckResponse:
        """Get the suppression in an organization

        ``GET /orgs/{orgId}/mail/suppression``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/mail/suppression",
            query=_query({"email": email}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
