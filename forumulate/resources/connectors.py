from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ConnectorsKbResource:
    """``client.connectors.kb`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def manifest(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorManifest:
        """Get the manifest

        ``GET /connector/kb/manifest``
        """
        return self._client._request(
            "GET",
            f"/connector/kb/manifest",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def chunks(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        since: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorChunksPage:
        """List chunks

        ``GET /connector/kb/chunks``

        :param limit: Chunks per page.
        """
        return self._client._request(
            "GET",
            f"/connector/kb/chunks",
            query=_query({"limit": limit, "cursor": cursor, "since": since}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def chunks_all(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        since: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ConnectorChunkedItem]:
        """Iterate every item of ``chunks`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/connector/kb/chunks",
            query=_query({"limit": limit, "since": since}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="items",
        )

    def search(
        self,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorSearchResult:
        """Get the search

        ``GET /connector/kb/search``
        """
        return self._client._request(
            "GET",
            f"/connector/kb/search",
            query=_query({"q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def llms(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorsKbLlmsResponse:
        """File of llms (connector kb)

        ``GET /connector/kb/llms.txt``
        """
        return self._client._request(
            "GET",
            f"/connector/kb/llms.txt",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def ask(
        self,
        *,
        question: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the ask

        ``POST /connector/kb/ask``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/connector/kb/ask",
            query=_query({}, extra_query),
            body=_body({"question": question}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def questions(
        self,
        *,
        questions: List[ConnectorsKbQuestionsParamsQuestion],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a question

        ``POST /connector/kb/questions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/connector/kb/questions",
            query=_query({}, extra_query),
            body=_body({"questions": questions}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def suggest(
        self,
        *,
        item_id: str,
        markdown: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slot: Union[str, NotGiven] = NOT_GIVEN,
        note: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a suggestion

        ``POST /connector/kb/suggestions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/connector/kb/suggestions",
            query=_query({}, extra_query),
            body=_body({"itemId": item_id, "slot": slot, "markdown": markdown, "note": note}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ConnectorsProvidersResource:
    """``client.connectors.providers`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorsProvidersListResponse:
        """List connector providers in an organization

        ``GET /orgs/{orgId}/connector-providers``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/connector-providers",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ChatProviderDef]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/connector-providers",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="providers",
        )


class ConnectorsResource:
    """``client.connectors`` (9 operations; kb, providers)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.kb = ConnectorsKbResource(client)
        self.providers = ConnectorsProvidersResource(client)

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorsListResponse:
        """List connectors in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/connectors``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ConnectorSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="connectors",
        )

    def install(
        self,
        org_id: str,
        space_id: str,
        *,
        provider_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        embed_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        knowledge_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        knowledge_scopes: Union[List[str], NotGiven] = NOT_GIVEN,
        appearance: Union[ConnectorsInstallParamsAppearance, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorsInstallResponse:
        """Create a connector in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/connectors``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors",
            query=_query({}, extra_query),
            body=_body({"providerId": provider_id, "config": config, "embedEnabled": embed_enabled, "knowledgeEnabled": knowledge_enabled, "knowledgeScopes": knowledge_scopes, "appearance": appearance}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        connector_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        embed_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        knowledge_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        knowledge_scopes: Union[List[str], NotGiven] = NOT_GIVEN,
        appearance: Union[ConnectorsUpdateParamsAppearance, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorsUpdateResponse:
        """Update the connector

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/connectors/{connectorId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors/{_path(connector_id)}",
            query=_query({}, extra_query),
            body=_body({"embedEnabled": embed_enabled, "knowledgeEnabled": knowledge_enabled, "knowledgeScopes": knowledge_scopes, "appearance": appearance, "config": config}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        connector_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorsRemoveResponse:
        """Delete the connector

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/connectors/{connectorId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors/{_path(connector_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def mint_token(
        self,
        org_id: str,
        space_id: str,
        connector_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorTokenMinted:
        """Create the token in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/connectors/{connectorId}/token``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors/{_path(connector_id)}/token",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revoke_token(
        self,
        org_id: str,
        space_id: str,
        connector_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorsRevokeTokenResponse:
        """Delete the token in a space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/connectors/{connectorId}/token``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors/{_path(connector_id)}/token",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def test(
        self,
        org_id: str,
        space_id: str,
        connector_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        on_custom_domain: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Test the connector

        ``POST /orgs/{orgId}/spaces/{spaceId}/connectors/{connectorId}/test``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors/{_path(connector_id)}/test",
            query=_query({}, extra_query),
            body=_body({"onCustomDomain": on_custom_domain}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def register_knowledge(
        self,
        org_id: str,
        space_id: str,
        connector_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> KnowledgeRegistration:
        """Create the register in a space (connectors knowledge)

        ``POST /orgs/{orgId}/spaces/{spaceId}/connectors/{connectorId}/knowledge/register``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors/{_path(connector_id)}/knowledge/register",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def activity(
        self,
        org_id: str,
        space_id: str,
        connector_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ConnectorsActivityResponse:
        """Get the activity in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/connectors/{connectorId}/activity``

        :param limit: Activity entries.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors/{_path(connector_id)}/activity",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def activity_all(
        self,
        org_id: str,
        space_id: str,
        connector_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ConnectorActivityEntry]:
        """Iterate every item of ``activity`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/connectors/{_path(connector_id)}/activity",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="activity",
        )
