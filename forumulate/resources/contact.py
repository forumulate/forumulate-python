from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ContactResource:
    """``client.contact`` (13 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def departments(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContactDepartmentsResponse:
        """List departments in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/contact/departments``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/departments",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def departments_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``departments`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/departments",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def set_departments(
        self,
        org_id: str,
        space_id: str,
        *,
        departments: List[ContactSetDepartmentsParamsDepartment],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContactSetDepartmentsResponse:
        """Update departments in a space

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/contact/departments``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/departments",
            query=_query({}, extra_query),
            body=_body({"departments": departments}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def form_fields(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContactFormFieldsResponse:
        """List form fields in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/contact/form-fields``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/form-fields",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def form_fields_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``form_fields`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/form-fields",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def set_form_fields(
        self,
        org_id: str,
        space_id: str,
        *,
        fields: List[ContactSetFormFieldsParamsField],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContactSetFormFieldsResponse:
        """Update form fields in a space

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/contact/form-fields``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/form-fields",
            query=_query({}, extra_query),
            body=_body({"fields": fields}, extra_body),
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
    ) -> ContactFormResponse:
        """Get the form in a space (contact)

        ``GET /orgs/{orgId}/spaces/{spaceId}/contact/form``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/form",
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
        success_message: Union[Optional[str], NotGiven] = NOT_GIVEN,
        redirect_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        submit_label: Union[Optional[str], NotGiven] = NOT_GIVEN,
        success_title: Union[Optional[str], NotGiven] = NOT_GIVEN,
        next_steps: Union[Optional[List[ContactSetFormParamsNextStep]], NotGiven] = NOT_GIVEN,
        work_email_only: Union[Any, NotGiven] = NOT_GIVEN,
        spam_filter: Union[Any, NotGiven] = NOT_GIVEN,
        booking_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        retention_days: Union[Optional[int], NotGiven] = NOT_GIVEN,
        translations: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        fields: Union[List[ContactSetFormParamsField], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContactSetFormResponse:
        """Update the form in a space (contact)

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/contact/form``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/form",
            query=_query({}, extra_query),
            body=_body({"successMessage": success_message, "redirectUrl": redirect_url, "submitLabel": submit_label, "successTitle": success_title, "nextSteps": next_steps, "workEmailOnly": work_email_only, "spamFilter": spam_filter, "bookingUrl": booking_url, "retentionDays": retention_days, "translations": translations, "fields": fields}, extra_body),
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
        """File of export (spaces contact)

        ``GET /orgs/{orgId}/spaces/{spaceId}/contact/export.csv``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/export.csv",
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
        unhandled: Union[str, NotGiven] = NOT_GIVEN,
        folder: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContactListResponse:
        """Get the contact in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/contact``

        :param limit: Submissions per page, once a version is stated.
        :param unhandled: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact",
            query=_query({"limit": limit, "unhandled": unhandled, "folder": folder, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        unhandled: Union[str, NotGiven] = NOT_GIVEN,
        folder: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact",
            query=_query({"limit": limit, "unhandled": unhandled, "folder": folder}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def set_handled(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        handled: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContactSetHandledResponse:
        """Update the contact

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/contact/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"handled": handled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
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
    ) -> ContactSetStatusResponse:
        """Update the status in a space

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/contact/{id}/status``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/{_path(id)}/status",
            query=_query({}, extra_query),
            body=_body({"status": status}, extra_body),
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
    ) -> ContactAssignResponse:
        """Assign the contact

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/contact/{id}/assign``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/{_path(id)}/assign",
            query=_query({}, extra_query),
            body=_body({"assigneeId": assignee_id}, extra_body),
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
    ) -> ContactRepliesResponse:
        """List replies in a space (contact)

        ``GET /orgs/{orgId}/spaces/{spaceId}/contact/{id}/replies``

        :param limit: Replies per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/{_path(id)}/replies",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/{_path(id)}/replies",
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
    ) -> ContactReplyResponse:
        """Create the reply in a space (contact)

        ``POST /orgs/{orgId}/spaces/{spaceId}/contact/{id}/reply``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/{_path(id)}/reply",
            query=_query({}, extra_query),
            body=_body({"body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
