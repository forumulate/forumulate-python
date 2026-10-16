from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EntryFieldsResource:
    """``client.entry_fields`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def read(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryFields:
        """List fields in an organization (entries)

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/fields``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/fields",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def patch(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        ops: List[EntryFieldsPatchParamsOp],
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update fields in an organization (entries)

        ``PATCH /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/fields``

        :param if_match: The `etag` from `GET …/fields` (or the last write).
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/fields",
            query=_query({}, extra_query),
            body=_body({"ops": ops}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def lock(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryLockState:
        """Lock the entry

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/lock``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/lock",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def take_lock(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        take_over: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Lock the entry (create)

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/lock``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/lock",
            query=_query({}, extra_query),
            body=_body({"takeOver": take_over}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def release_lock(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryLockState:
        """Lock the entry (delete)

        ``DELETE /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/lock``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/lock",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def heartbeat(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryLockState:
        """Create the heartbeat in an organization (content libraries entries lock)

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/lock/heartbeat``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/lock/heartbeat",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
