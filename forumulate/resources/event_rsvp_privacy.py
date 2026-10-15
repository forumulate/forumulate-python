from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventRsvpPrivacyResource:
    """``client.event_rsvp_privacy`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def request(
        self,
        org_id: str,
        space_id: str,
        *,
        email: str,
        kind: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Create the privacy in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/event-rsvps/privacy``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-rsvps/privacy",
            query=_query({}, extra_query),
            body=_body({"email": email, "kind": kind, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def confirm(
        self,
        org_id: str,
        space_id: str,
        *,
        token: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Confirm the privacy

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/event-rsvps/privacy/confirm``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/event-rsvps/privacy/confirm",
            query=_query({}, extra_query),
            body=_body({"token": token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
