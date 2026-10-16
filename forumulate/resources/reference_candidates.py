from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ReferenceCandidatesResource:
    """``client.reference_candidates`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def search(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[List[str], NotGiven] = NOT_GIVEN,
        refs: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReferenceCandidatesSearchResponse:
        """Search what a reference field can point at

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/reference-candidates``

        :param limit: Candidates returned.
        :param q: Words in the title.
        :param to: The kinds to search, comma-separated, as the field’s `to` declares them.
        :param refs: Stored references to label, `kind:id`, comma-separated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/reference-candidates",
            query=_query({"limit": limit, "q": q, "to": to, "refs": refs}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
