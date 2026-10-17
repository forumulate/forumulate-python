from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class TranslationCoverageResource:
    """``client.translation_coverage`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def coverage(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> TranslationCoverage:
        """Get a space’s translation coverage

        ``GET /orgs/{orgId}/spaces/{spaceId}/translations``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/translations",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
