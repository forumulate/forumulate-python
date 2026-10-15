from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class StatusTranslationsResource:
    """``client.status_translations`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        incident_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusTranslationsListResponse:
        """List an incident’s translations

        ``GET /orgs/{orgId}/spaces/{spaceId}/status/incidents/{incidentId}/translations``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents/{_path(incident_id)}/translations",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        incident_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents/{_path(incident_id)}/translations",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def put(
        self,
        org_id: str,
        space_id: str,
        incident_id: str,
        locale: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[Optional[str], NotGiven] = NOT_GIVEN,
        body: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        updates: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusTranslationsPutResponse:
        """Write an incident’s translation

        ``PUT /orgs/{orgId}/spaces/{spaceId}/status/incidents/{incidentId}/translations/{locale}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents/{_path(incident_id)}/translations/{_path(locale)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "body": body, "markdown": markdown, "updates": updates}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        incident_id: str,
        locale: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusTranslationsRemoveResponse:
        """Remove an incident’s translation

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/status/incidents/{incidentId}/translations/{locale}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents/{_path(incident_id)}/translations/{_path(locale)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def machine(
        self,
        org_id: str,
        space_id: str,
        incident_id: str,
        locale: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        replace: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusTranslationsMachineResponse:
        """Machine-translate an incident

        ``POST /orgs/{orgId}/spaces/{spaceId}/status/incidents/{incidentId}/translations/{locale}/machine``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents/{_path(incident_id)}/translations/{_path(locale)}/machine",
            query=_query({}, extra_query),
            body=_body({"replace": replace}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
