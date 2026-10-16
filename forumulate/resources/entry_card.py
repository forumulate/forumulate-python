from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EntryCardResource:
    """``client.entry_card`` (9 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def overview(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryOverview:
        """Read an entry's status, schedule and locales

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def unpublish(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryOverview:
        """Unpublish an entry

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/unpublish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/unpublish",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_schedule(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryCardGetScheduleResponse:
        """Get the schedule in an organization (content libraries entries)

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/schedule``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/schedule",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def schedule(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        publish_at: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryCardScheduleResponse:
        """Schedule an entry to publish

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/schedule``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/schedule",
            query=_query({}, extra_query),
            body=_body({"publishAt": publish_at}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def cancel_schedule(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryCardCancelScheduleResponse:
        """Delete the schedule in an organization

        ``DELETE /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/schedule``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/schedule",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revisions(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryCardRevisionsResponse:
        """List an entry's revisions

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/revisions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/revisions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def revisions_all(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``revisions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/revisions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def revision(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        revision_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryRevisionFields:
        """Read one revision's field values

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/revisions/{revisionId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/revisions/{_path(revision_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def restore(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        revision_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryCardRestoreResponse:
        """Restore a revision

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/revisions/{revisionId}/restore``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/revisions/{_path(revision_id)}/restore",
            query=_query({}, extra_query),
            body=_body({"mode": mode}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def translate(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        locale: Any,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Start a translation of an entry

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/translations``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/translations",
            query=_query({}, extra_query),
            body=_body({"locale": locale}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
