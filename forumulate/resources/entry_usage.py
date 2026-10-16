from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class EntryUsageResource:
    """``client.entry_usage`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def used_in(
        self,
        org_id: str,
        library_id: str,
        item_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EntryUsage:
        """List the entries that reference an entry

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/items/{itemId}/used-in``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/items/{_path(item_id)}/used-in",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
