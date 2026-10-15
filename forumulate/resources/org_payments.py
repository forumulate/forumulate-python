from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class OrgPaymentsResource:
    """``client.org_payments`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgPaymentsStatus:
        """Get the stripe in an organization

        ``GET /orgs/{orgId}/payments/stripe``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/payments/stripe",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        secret_key: Union[str, NotGiven] = NOT_GIVEN,
        webhook_secret: Union[Optional[str], NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the stripe in an organization

        ``PUT /orgs/{orgId}/payments/stripe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/payments/stripe",
            query=_query({}, extra_query),
            body=_body({"secretKey": secret_key, "webhookSecret": webhook_secret, "enabled": enabled}, extra_body),
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
    ) -> OrgPaymentsClearResponse:
        """Delete the stripe in an organization

        ``DELETE /orgs/{orgId}/payments/stripe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/payments/stripe",
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
    ) -> OrgPaymentsTestResponse:
        """Test the stripe

        ``POST /orgs/{orgId}/payments/stripe/test``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/payments/stripe/test",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
