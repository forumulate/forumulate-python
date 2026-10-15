from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class CareersResource:
    """``client.careers`` (16 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get_pipeline(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersGetPipelineResponse:
        """Get the pipeline in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/careers/pipeline``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/pipeline",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_pipeline(
        self,
        org_id: str,
        space_id: str,
        *,
        stages: List[CareersSetPipelineParamsStage],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        rating_scale: Union[str, NotGiven] = NOT_GIVEN,
        move_to: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersSetPipelineResponse:
        """Replace the pipeline in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/careers/pipeline``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/pipeline",
            query=_query({}, extra_query),
            body=_body({"stages": stages, "ratingScale": rating_scale, "moveTo": move_to}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def form(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersFormResponse:
        """Get the form in a space (careers)

        ``GET /orgs/{orgId}/spaces/{spaceId}/careers/form``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/form",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_form(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        fields: Union[List[CareersSetFormParamsField], NotGiven] = NOT_GIVEN,
        role_fields: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        eeo: Union[bool, NotGiven] = NOT_GIVEN,
        consent_text: Union[Optional[str], NotGiven] = NOT_GIVEN,
        retention_days: Union[Optional[int], NotGiven] = NOT_GIVEN,
        success_message: Union[Optional[str], NotGiven] = NOT_GIVEN,
        redirect_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        notify_emails: Union[List[str], NotGiven] = NOT_GIVEN,
        confirmation: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersSetFormResponse:
        """Update the form in a space (careers)

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/careers/form``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/form",
            query=_query({}, extra_query),
            body=_body({"fields": fields, "roleFields": role_fields, "eeo": eeo, "consentText": consent_text, "retentionDays": retention_days, "successMessage": success_message, "redirectUrl": redirect_url, "notifyEmails": notify_emails, "confirmation": confirmation}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def export_csv(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of applications

        ``GET /orgs/{orgId}/spaces/{spaceId}/careers/applications.csv``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications.csv",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def eeo_summary(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersEeoSummaryResponse:
        """Get the eeo summary in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/careers/eeo-summary``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/eeo-summary",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        status: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersListResponse:
        """List applications in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/careers/applications``

        :param limit: Applications per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications",
            query=_query({"limit": limit, "status": status, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        status: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications",
            query=_query({"limit": limit, "status": status}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def set_status(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        status: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersSetStatusResponse:
        """Update the application

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/careers/applications/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"status": status}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def replies(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersRepliesResponse:
        """List replies in a space (careers applications)

        ``GET /orgs/{orgId}/spaces/{spaceId}/careers/applications/{id}/replies``

        :param limit: Replies per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/replies",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def replies_all(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``replies`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/replies",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def reply(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersReplyResponse:
        """Create the reply in a space (careers applications)

        ``POST /orgs/{orgId}/spaces/{spaceId}/careers/applications/{id}/reply``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/reply",
            query=_query({}, extra_query),
            body=_body({"body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def assign(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        assignee_id: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersAssignResponse:
        """Assign the application

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/careers/applications/{id}/assign``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/assign",
            query=_query({}, extra_query),
            body=_body({"assigneeId": assignee_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def notes(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersNotesResponse:
        """List notes in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/careers/applications/{id}/notes``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/notes",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def notes_all(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``notes`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/notes",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def add_note(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersAddNoteResponse:
        """Create a note in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/careers/applications/{id}/notes``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/notes",
            query=_query({}, extra_query),
            body=_body({"body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_note(
        self,
        org_id: str,
        space_id: str,
        id: str,
        note_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersDeleteNoteResponse:
        """Delete the note (spaces careers applications)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/careers/applications/{id}/notes/{noteId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/notes/{_path(note_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ratings(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersRatingsResponse:
        """List ratings in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/careers/applications/{id}/ratings``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/ratings",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def ratings_all(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``ratings`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/ratings",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def rate(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        score: Optional[int],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CareersRateResponse:
        """Replace the rating in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/careers/applications/{id}/rating``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/applications/{_path(id)}/rating",
            query=_query({}, extra_query),
            body=_body({"score": score}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
