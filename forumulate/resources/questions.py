from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class QuestionsResource:
    """``client.questions`` (11 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

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
    ) -> QuestionsListResponse:
        """List questions in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/questions``

        :param limit: Questions listed.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/questions",
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
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/questions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def ingest(
        self,
        org_id: str,
        space_id: str,
        *,
        source: str,
        questions: List[QuestionsIngestParamsQuestion],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Create a question in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/questions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/questions",
            query=_query({}, extra_query),
            body=_body({"source": source, "questions": questions}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def clusters(
        self,
        org_id: str,
        space_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> QuestionsClustersResponse:
        """List clusters in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/questions/clusters``

        :param days: How far back to cluster.
        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/questions/clusters",
            query=_query({"days": days, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def clusters_all(
        self,
        org_id: str,
        space_id: str,
        *,
        days: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``clusters`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/questions/clusters",
            query=_query({"days": days, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        question_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> QuestionsRemoveResponse:
        """Delete the question

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/questions/{questionId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/questions/{_path(question_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def draft(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        max: Union[int, NotGiven] = NOT_GIVEN,
        days: Union[int, NotGiven] = NOT_GIVEN,
        preset: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> QuestionsDraftResponse:
        """Create a draft in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/questions/drafts``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/questions/drafts",
            query=_query({}, extra_query),
            body=_body({"max": max, "days": days, "preset": preset}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def suggest(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        source: str,
        markdown: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slot: Union[str, NotGiven] = NOT_GIVEN,
        note: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a suggestion in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/suggestions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/suggestions",
            query=_query({}, extra_query),
            body=_body({"source": source, "slot": slot, "markdown": markdown, "note": note}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_assertions(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> QuestionsListAssertionsResponse:
        """List assertions in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/assertions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/assertions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_assertions_all(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_assertions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/assertions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def add_assertion(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        slot: str,
        kind: str,
        target: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        expects: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> QuestionsAddAssertionResponse:
        """Create an assertion in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/assertions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/assertions",
            query=_query({}, extra_query),
            body=_body({"slot": slot, "kind": kind, "target": target, "expects": expects}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def run_assertions(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> QuestionsRunAssertionsResponse:
        """Run the assertion

        ``POST /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/assertions/run``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/assertions/run",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_assertion(
        self,
        org_id: str,
        space_id: str,
        item_id: str,
        assertion_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> QuestionsRemoveAssertionResponse:
        """Delete the assertion

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/items/{itemId}/assertions/{assertionId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/items/{_path(item_id)}/assertions/{_path(assertion_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def uncovered(
        self,
        org_id: str,
        space_id: str,
        *,
        docs_space_id: str,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> QuestionsUncoveredResponse:
        """Get the uncovered in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/uncovered``

        :param limit: Threads listed.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/uncovered",
            query=_query({"docsSpaceId": docs_space_id, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
