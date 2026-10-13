from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class FormsSubmissionsResource:
    """``client.forms.submissions`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def by_email(
        self,
        org_id: str,
        *,
        email: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsSubmissionsByEmailResponse:
        """List form submissions in an organization

        ``GET /orgs/{orgId}/form-submissions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/form-submissions",
            query=_query({"email": email, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def by_email_all(
        self,
        org_id: str,
        *,
        email: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[FormSubmissionRow]:
        """Iterate every item of ``by_email`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/form-submissions",
            query=_query({"email": email, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="submissions",
        )

    def erase_by_email(
        self,
        org_id: str,
        *,
        email: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsSubmissionsEraseByEmailResponse:
        """Delete form submissions in an organization

        ``DELETE /orgs/{orgId}/form-submissions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/form-submissions",
            query=_query({"email": email}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class FormsTemplatesResource:
    """``client.forms.templates`` (6 operations)."""

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
    ) -> FormsTemplatesListResponse:
        """List form templates in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/form-templates``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/form-templates",
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
    ) -> Iterator[FormsTemplatesListResponseFormTemplate]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/form-templates",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="formTemplates",
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        template: Union[List[FormsTemplatesCreateParamsTemplateItem], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsTemplatesCreateResponse:
        """Create a form template in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/form-templates``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/form-templates",
            query=_query({}, extra_query),
            body=_body({"name": name, "template": template}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsTemplatesGetResponse:
        """Get the form template

        ``GET /orgs/{orgId}/spaces/{spaceId}/form-templates/{id}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/form-templates/{_path(id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        template: Union[List[FormsTemplatesUpdateParamsTemplateItem], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsTemplatesUpdateResponse:
        """Update the form template

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/form-templates/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/form-templates/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "template": template}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsTemplatesRemoveResponse:
        """Delete the form template

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/form-templates/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/form-templates/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def attach(
        self,
        org_id: str,
        space_id: str,
        *,
        category_id: str,
        form_template_id: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsTemplatesAttachResponse:
        """Attach the form template

        ``POST /orgs/{orgId}/spaces/{spaceId}/form-templates/attach``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/form-templates/attach",
            query=_query({}, extra_query),
            body=_body({"categoryId": category_id, "formTemplateId": form_template_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class FormsResource:
    """``client.forms`` (9 operations; submissions, templates)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.submissions = FormsSubmissionsResource(client)
        self.templates = FormsTemplatesResource(client)

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsListResponse:
        """List forms in an organization

        ``GET /orgs/{orgId}/forms``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/forms",
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
    ) -> Iterator[FormSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/forms",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="forms",
        )

    def create(
        self,
        org_id: str,
        *,
        name: str,
        fields: List[FormsCreateParamsField],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        submit_label: Union[str, NotGiven] = NOT_GIVEN,
        success_message: Union[str, NotGiven] = NOT_GIVEN,
        redirect_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        layout: Union[str, NotGiven] = NOT_GIVEN,
        consent_text: Union[Optional[str], NotGiven] = NOT_GIVEN,
        notify_emails: Union[List[str], NotGiven] = NOT_GIVEN,
        status: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsCreateResponse:
        """Create a form in an organization

        ``POST /orgs/{orgId}/forms``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/forms",
            query=_query({}, extra_query),
            body=_body({"name": name, "fields": fields, "submitLabel": submit_label, "successMessage": success_message, "redirectUrl": redirect_url, "layout": layout, "consentText": consent_text, "notifyEmails": notify_emails, "status": status}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        form_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsGetResponse:
        """Get the form

        ``GET /orgs/{orgId}/forms/{formId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/forms/{_path(form_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        form_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        fields: Union[List[FormsUpdateParamsField], NotGiven] = NOT_GIVEN,
        submit_label: Union[str, NotGiven] = NOT_GIVEN,
        success_message: Union[str, NotGiven] = NOT_GIVEN,
        redirect_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        layout: Union[str, NotGiven] = NOT_GIVEN,
        consent_text: Union[Optional[str], NotGiven] = NOT_GIVEN,
        notify_emails: Union[List[str], NotGiven] = NOT_GIVEN,
        status: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsUpdateResponse:
        """Update the form

        ``PATCH /orgs/{orgId}/forms/{formId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/forms/{_path(form_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "fields": fields, "submitLabel": submit_label, "successMessage": success_message, "redirectUrl": redirect_url, "layout": layout, "consentText": consent_text, "notifyEmails": notify_emails, "status": status}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        form_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Delete the form

        ``DELETE /orgs/{orgId}/forms/{formId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/forms/{_path(form_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_submissions(
        self,
        org_id: str,
        form_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        spam: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsListSubmissionsResponse:
        """List submissions in an organization

        ``GET /orgs/{orgId}/forms/{formId}/submissions``

        :param limit: Submissions per page, once a version is stated.
        :param spam: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/forms/{_path(form_id)}/submissions",
            query=_query({"limit": limit, "spam": spam, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_submissions_all(
        self,
        org_id: str,
        form_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        spam: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[FormSubmissionRow]:
        """Iterate every item of ``list_submissions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/forms/{_path(form_id)}/submissions",
            query=_query({"limit": limit, "spam": spam}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="submissions",
        )

    def export_csv(
        self,
        org_id: str,
        form_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of submissions

        ``GET /orgs/{orgId}/forms/{formId}/submissions.csv``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/forms/{_path(form_id)}/submissions.csv",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_spam(
        self,
        org_id: str,
        form_id: str,
        submission_id: str,
        *,
        spam: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FormsSetSpamResponse:
        """Update the submission

        ``PATCH /orgs/{orgId}/forms/{formId}/submissions/{submissionId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/forms/{_path(form_id)}/submissions/{_path(submission_id)}",
            query=_query({}, extra_query),
            body=_body({"spam": spam}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_submission(
        self,
        org_id: str,
        form_id: str,
        submission_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Delete the submission

        ``DELETE /orgs/{orgId}/forms/{formId}/submissions/{submissionId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/forms/{_path(form_id)}/submissions/{_path(submission_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
