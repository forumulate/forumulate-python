from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class McpResource:
    """``client.mcp`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def info(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> McpInfoResponse:
        """Get the MCP server in an organization

        ``GET /orgs/{orgId}/mcp``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/mcp",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def rpc(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the MCP server in an organization

        ``POST /orgs/{orgId}/mcp``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/mcp",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def info_read_only(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> McpInfoReadOnlyResponse:
        """Get the readonly in an organization

        ``GET /orgs/{orgId}/mcp/readonly``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/mcp/readonly",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def rpc_read_only(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the readonly in an organization

        ``POST /orgs/{orgId}/mcp/readonly``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/mcp/readonly",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
