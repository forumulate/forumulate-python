from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EventTicketWebhookResource:
    """``client.event_ticket_webhook`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def webhook(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventTicketWebhookWebhookResponse:
        """Create the webhook (public reader payments stripe)

        ``POST /public/payments/stripe/{orgId}/webhook``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/payments/stripe/{_path(org_id)}/webhook",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
