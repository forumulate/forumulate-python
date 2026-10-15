from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class AuditResource:
    """``client.audit`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        actor_user_id: Union[str, NotGiven] = NOT_GIVEN,
        action: Union[str, NotGiven] = NOT_GIVEN,
        target_type: Union[str, NotGiven] = NOT_GIVEN,
        target_id: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AuditPageEnveloped:
        """Get the audit in an organization

        ``GET /orgs/{orgId}/audit``

        :param limit: Audit rows per page, newest first.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/audit",
            query=_query({"limit": limit, "cursor": cursor, "actorUserId": actor_user_id, "action": action, "targetType": target_type, "targetId": target_id, "from": from_, "to": to}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        actor_user_id: Union[str, NotGiven] = NOT_GIVEN,
        action: Union[str, NotGiven] = NOT_GIVEN,
        target_type: Union[str, NotGiven] = NOT_GIVEN,
        target_id: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/audit",
            query=_query({"limit": limit, "actorUserId": actor_user_id, "action": action, "targetType": target_type, "targetId": target_id, "from": from_, "to": to}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def export_csv(
        self,
        org_id: str,
        *,
        actor_user_id: Union[str, NotGiven] = NOT_GIVEN,
        action: Union[str, NotGiven] = NOT_GIVEN,
        target_type: Union[str, NotGiven] = NOT_GIVEN,
        target_id: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of export (audit)

        ``GET /orgs/{orgId}/audit/export.csv``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/audit/export.csv",
            query=_query({"actorUserId": actor_user_id, "action": action, "targetType": target_type, "targetId": target_id, "from": from_, "to": to}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def actions(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AuditActionsResponse:
        """List actions in an organization

        ``GET /orgs/{orgId}/audit/actions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/audit/actions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def actions_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``actions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/audit/actions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )
