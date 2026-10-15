from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class StatusTemplatesResource:
    """``client.status_templates`` (5 operations)."""

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
    ) -> StatusTemplatesListResponse:
        """List the status page’s incident templates

        ``GET /orgs/{orgId}/spaces/{spaceId}/status/templates``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/templates",
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
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/templates",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        severity: Union[str, NotGiven] = NOT_GIVEN,
        state: Union[str, NotGiven] = NOT_GIVEN,
        body: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        components: Union[List[StatusTemplatesCreateParamsComponent], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusTemplatesCreateResponse:
        """Save an incident template

        ``POST /orgs/{orgId}/spaces/{spaceId}/status/templates``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/templates",
            query=_query({}, extra_query),
            body=_body({"name": name, "title": title, "severity": severity, "state": state, "body": body, "markdown": markdown, "components": components}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        template_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        severity: Union[str, NotGiven] = NOT_GIVEN,
        state: Union[str, NotGiven] = NOT_GIVEN,
        body: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        components: Union[List[StatusTemplatesUpdateParamsComponent], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusTemplatesUpdateResponse:
        """Update the template

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/status/templates/{templateId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/templates/{_path(template_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "title": title, "severity": severity, "state": state, "body": body, "markdown": markdown, "components": components}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        template_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusTemplatesRemoveResponse:
        """Delete the template

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/status/templates/{templateId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/templates/{_path(template_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def use(
        self,
        org_id: str,
        space_id: str,
        template_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        notify_subscribers: Union[bool, NotGiven] = NOT_GIVEN,
        scheduled_for: Union[Optional[str], NotGiven] = NOT_GIVEN,
        scheduled_until: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusTemplatesUseResponse:
        """Open an incident from a template

        ``POST /orgs/{orgId}/spaces/{spaceId}/status/templates/{templateId}/incidents``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/templates/{_path(template_id)}/incidents",
            query=_query({}, extra_query),
            body=_body({"title": title, "notifySubscribers": notify_subscribers, "scheduledFor": scheduled_for, "scheduledUntil": scheduled_until}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
