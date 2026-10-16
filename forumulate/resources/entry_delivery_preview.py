from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EntryDeliveryPreviewResource:
    """``client.entry_delivery_preview`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def preview(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        stage: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryDeliveryPreview:
        """Preview what delivery serves for an entry

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/delivery``

        :param locale: A BCP-47 code the library has.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/delivery",
            query=_query({"stage": stage, "locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def resolve(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        fields: Dict[str, Any],
        locale: Union[str, NotGiven] = NOT_GIVEN,
        depth: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryDeliveryPreviewResolveResponse:
        """Resolve an entry’s unsaved draft for live preview

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/resolve``

        :param locale: A BCP-47 code the library has.
        :param depth: How deep references are populated (the plan caps it).
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/resolve",
            query=_query({"locale": locale, "depth": depth}, extra_query),
            body=_body({"fields": fields}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
