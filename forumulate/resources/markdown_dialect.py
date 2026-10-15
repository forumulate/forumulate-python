from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class MarkdownDialectResource:
    """``client.markdown_dialect`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> MarkdownDialectGetResponse:
        """Get the markdown dialect

        ``GET /docs/markdown-dialect``
        """
        return self._client._request(
            "GET",
            f"/docs/markdown-dialect",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
