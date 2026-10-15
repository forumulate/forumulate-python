from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SearchEmbeddingProviderResource:
    """``client.search.embedding_provider`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchEmbeddingProviderStatusResponse:
        """Get the embedding provider in an organization

        ``GET /orgs/{orgId}/search/embedding-provider``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/search/embedding-provider",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def connect(
        self,
        org_id: str,
        *,
        provider: str,
        api_key: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        model: Union[str, NotGiven] = NOT_GIVEN,
        dimensions: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchEmbeddingProviderConnectResponse:
        """Replace the embedding provider in an organization

        ``PUT /orgs/{orgId}/search/embedding-provider``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/search/embedding-provider",
            query=_query({}, extra_query),
            body=_body({"provider": provider, "apiKey": api_key, "model": model, "dimensions": dimensions}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def disconnect(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchEmbeddingProviderDisconnectResponse:
        """Delete the embedding provider in an organization

        ``DELETE /orgs/{orgId}/search/embedding-provider``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/search/embedding-provider",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def test(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchEmbeddingProviderTestResponse:
        """Test the embedding provider

        ``POST /orgs/{orgId}/search/embedding-provider/test``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/search/embedding-provider/test",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reindex(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchEmbeddingProviderReindexResponse:
        """Create the reindex in an organization (embedding provider)

        ``POST /orgs/{orgId}/search/embedding-provider/reindex``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/search/embedding-provider/reindex",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class SearchResource:
    """``client.search`` (8 operations; embedding_provider)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.embedding_provider = SearchEmbeddingProviderResource(client)

    def query(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        offset: Union[int, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UnifiedSearchResult:
        """Get the search in an organization

        ``GET /orgs/{orgId}/search``

        :param limit: Hits per page.
        :param offset: Where in the fused list to start.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/search",
            query=_query({"limit": limit, "offset": offset, "q": q, "type": type}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def query_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[UnifiedHit]:
        """Iterate every item of ``query`` across all pages, following ``offset``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/search",
            query=_query({"limit": limit, "q": q, "type": type}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="offset",
            items_key="hits",
        )

    def recent(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchRecentResponse:
        """List recent search in an organization

        ``GET /orgs/{orgId}/search/recent``

        :param limit: Recent terms returned.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/search/recent",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def semantic_search(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchSemanticSearchResponse:
        """Get the semantic in an organization

        ``GET /orgs/{orgId}/search/semantic``

        :param limit: Hits returned.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/search/semantic",
            query=_query({"limit": limit, "q": q, "mode": mode}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def reindex(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchReindexResponse:
        """Create the reindex in an organization

        ``POST /orgs/{orgId}/search/reindex``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/search/reindex",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def tags(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchTagsResponse:
        """List tags in an organization

        ``GET /orgs/{orgId}/search/tags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/search/tags",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def tags_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/search/tags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def tag(
        self,
        org_id: str,
        tag: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> TagHub:
        """Get the tag (search)

        ``GET /orgs/{orgId}/search/tags/{tag}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/search/tags/{_path(tag)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def gaps(
        self,
        org_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchGapsResponse:
        """List gaps in an organization

        ``GET /orgs/{orgId}/search/gaps``

        :param days: How far back to look.
        :param limit: Gaps returned.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/search/gaps",
            query=_query({"days": days, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def retrieve(
        self,
        org_id: str,
        *,
        q: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        roles: Union[List[str], NotGiven] = NOT_GIVEN,
        boost: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        max_staleness_days: Union[int, NotGiven] = NOT_GIVEN,
        space_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SearchRetrieveResponse:
        """Create the search in an organization

        ``POST /orgs/{orgId}/search``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/search",
            query=_query({}, extra_query),
            body=_body({"q": q, "roles": roles, "boost": boost, "limit": limit, "maxStalenessDays": max_staleness_days, "spaceIds": space_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
