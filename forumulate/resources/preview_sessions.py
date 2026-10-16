from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class PreviewSessionsResource:
    """``client.preview_sessions`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def mint(
        self,
        org_id: str,
        library_id: str,
        *,
        entry_id: str,
        path: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        release_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PreviewSessionsMintResponse:
        """Mint a preview token for an entry

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/preview/sessions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/preview/sessions",
            query=_query({}, extra_query),
            body=_body({"entryId": entry_id, "releaseId": release_id, "path": path}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
