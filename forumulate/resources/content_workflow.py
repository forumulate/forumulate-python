from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ContentWorkflowResource:
    """``client.content_workflow`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def settings(
        self,
        org_id: str,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentWorkflowSettingsResponse:
        """Get the workflow in an organization

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/workflow``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/workflow",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def put_settings(
        self,
        org_id: str,
        library_id: str,
        *,
        gates: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentWorkflowPutSettingsResponse:
        """Replace the workflow in an organization

        ``PUT /orgs/{orgId}/content/libraries/{libraryId}/workflow``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/workflow",
            query=_query({}, extra_query),
            body=_body({"gates": gates}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        library_id: str,
        *,
        open: Union[str, NotGiven] = NOT_GIVEN,
        assignee: Union[str, NotGiven] = NOT_GIVEN,
        entry_id: Union[str, NotGiven] = NOT_GIVEN,
        stage: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentWorkflowListResponse:
        """List change requests in an organization

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/change-requests``

        :param open: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/change-requests",
            query=_query({"open": open, "assignee": assignee, "entryId": entry_id, "stage": stage, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        library_id: str,
        *,
        open: Union[str, NotGiven] = NOT_GIVEN,
        assignee: Union[str, NotGiven] = NOT_GIVEN,
        entry_id: Union[str, NotGiven] = NOT_GIVEN,
        stage: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/change-requests",
            query=_query({"open": open, "assignee": assignee, "entryId": entry_id, "stage": stage, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        library_id: str,
        *,
        entry_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        assignee_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        submit: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentWorkflowCreateResponse:
        """Create a change request in an organization

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/change-requests``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/change-requests",
            query=_query({}, extra_query),
            body=_body({"entryId": entry_id, "title": title, "assigneeIds": assignee_ids, "submit": submit}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        library_id: str,
        cr_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentWorkflowGetResponse:
        """Get the change request (content libraries)

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/change-requests/{crId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/change-requests/{_path(cr_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        library_id: str,
        cr_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        assignee_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentWorkflowUpdateResponse:
        """Update the change request

        ``PATCH /orgs/{orgId}/content/libraries/{libraryId}/change-requests/{crId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/change-requests/{_path(cr_id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "assigneeIds": assignee_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def transition(
        self,
        org_id: str,
        library_id: str,
        cr_id: str,
        *,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        publish_at: Union[str, NotGiven] = NOT_GIVEN,
        note: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentWorkflowTransitionResponse:
        """Create the transition in an organization

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/change-requests/{crId}/transition``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/change-requests/{_path(cr_id)}/transition",
            query=_query({}, extra_query),
            body=_body({"action": action, "publishAt": publish_at, "note": note}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
