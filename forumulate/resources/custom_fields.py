from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class CustomFieldsResource:
    """``client.custom_fields`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list_defs(
        self,
        org_id: str,
        entity_type: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CustomFieldsListDefsResponse:
        """Get the custom field

        ``GET /orgs/{orgId}/custom-fields/{entityType}``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/custom-fields/{_path(entity_type)}",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_defs_all(
        self,
        org_id: str,
        entity_type: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_defs`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/custom-fields/{_path(entity_type)}",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create_def(
        self,
        org_id: str,
        entity_type: str,
        *,
        label: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        options: Union[List[str], NotGiven] = NOT_GIVEN,
        sort_order: Union[int, NotGiven] = NOT_GIVEN,
        visibility: Union[str, NotGiven] = NOT_GIVEN,
        show_on_card: Union[bool, NotGiven] = NOT_GIVEN,
        editable_by_user: Union[bool, NotGiven] = NOT_GIVEN,
        required_at_signup: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CustomFieldsCreateDefResponse:
        """Create the custom field

        ``POST /orgs/{orgId}/custom-fields/{entityType}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/custom-fields/{_path(entity_type)}",
            query=_query({}, extra_query),
            body=_body({"label": label, "type": type, "options": options, "sortOrder": sort_order, "visibility": visibility, "showOnCard": show_on_card, "editableByUser": editable_by_user, "requiredAtSignup": required_at_signup}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_def(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CustomFieldsDeleteDefResponse:
        """Delete the field definition

        ``DELETE /orgs/{orgId}/custom-fields/defs/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/custom-fields/defs/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_values(
        self,
        org_id: str,
        entity_type: str,
        entity_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CustomFieldsGetValuesResponse:
        """List values in an organization

        ``GET /orgs/{orgId}/custom-fields/{entityType}/{entityId}/values``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/custom-fields/{_path(entity_type)}/{_path(entity_id)}/values",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get_values_all(
        self,
        org_id: str,
        entity_type: str,
        entity_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``get_values`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/custom-fields/{_path(entity_type)}/{_path(entity_id)}/values",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def set_value(
        self,
        org_id: str,
        entity_type: str,
        entity_id: str,
        *,
        key: str,
        value: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CustomFieldsSetValueResponse:
        """Create a value in an organization

        ``POST /orgs/{orgId}/custom-fields/{entityType}/{entityId}/values``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/custom-fields/{_path(entity_type)}/{_path(entity_id)}/values",
            query=_query({}, extra_query),
            body=_body({"key": key, "value": value}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_own_values(
        self,
        org_id: str,
        *,
        values: List[CustomFieldsSetOwnValuesParamsValue],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CustomFieldsSetOwnValuesResponse:
        """Set your own member fields

        ``PUT /orgs/{orgId}/custom-fields/member/me``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/custom-fields/member/me",
            query=_query({}, extra_query),
            body=_body({"values": values}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
