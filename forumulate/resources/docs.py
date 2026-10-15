from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class DocsAiResource:
    """``client.docs.ai`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def review(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        recent_changes: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAiReviewResponse:
        """Create the review in a space (pages AI)

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/ai/review``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/ai/review",
            query=_query({}, extra_query),
            body=_body({"recentChanges": recent_changes}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rewrite(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        instruction: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Any, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAiRewriteResponse:
        """Create the rewrite in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/ai/rewrite``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/ai/rewrite",
            query=_query({}, extra_query),
            body=_body({"content": content, "instruction": instruction}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def translate(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        language: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Any, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAiTranslateResponse:
        """Create the translate in a space (pages AI)

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/ai/translate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/ai/translate",
            query=_query({}, extra_query),
            body=_body({"content": content, "language": language}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ask(
        self,
        org_id: str,
        space_id: str,
        *,
        question: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAiAskResponse:
        """Create the ask in a space (docs)

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/ask``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/ask",
            query=_query({}, extra_query),
            body=_body({"question": question}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ask_stream(
        self,
        org_id: str,
        space_id: str,
        *,
        question: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the stream in a space (docs)

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/ask/stream``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/ask/stream",
            query=_query({}, extra_query),
            body=_body({"question": question}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ask_stream_stream(
        self,
        org_id: str,
        space_id: str,
        *,
        question: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Stream ``ask_stream`` as server-sent events, yielding each decoded event."""
        yield from self._client._stream(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/ask/stream",
            query=_query({}, extra_query),
            body=_body({"question": question}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ask_feedback(
        self,
        org_id: str,
        space_id: str,
        query_id: str,
        *,
        helpful: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        comment: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAiAskFeedbackResponse:
        """Create the feedback in a space (docs ask)

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/ask/{queryId}/feedback``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/ask/{_path(query_id)}/feedback",
            query=_query({}, extra_query),
            body=_body({"helpful": helpful, "comment": comment}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def agent(
        self,
        org_id: str,
        space_id: str,
        *,
        collection_id: str,
        instruction: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAiAgentResponse:
        """Create the agent in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/agent``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/agent",
            query=_query({}, extra_query),
            body=_body({"collectionId": collection_id, "instruction": instruction}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsAnalyticsResource:
    """``client.docs.analytics`` (15 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def analytics_summary(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AnalyticsSummary:
        """List analytics in a space (orgs docs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/analytics``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/analytics",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def feedback_comments(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        page_id: Union[str, NotGiven] = NOT_GIVEN,
        rating: Union[str, NotGiven] = NOT_GIVEN,
        since_days: Union[float, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAnalyticsFeedbackCommentsResponse:
        """Get the feedback in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/feedback``

        :param limit: Comments per page.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/feedback",
            query=_query({"limit": limit, "pageId": page_id, "rating": rating, "sinceDays": since_days, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def feedback_comments_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        page_id: Union[str, NotGiven] = NOT_GIVEN,
        rating: Union[str, NotGiven] = NOT_GIVEN,
        since_days: Union[float, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``feedback_comments`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/feedback",
            query=_query({"limit": limit, "pageId": page_id, "rating": rating, "sinceDays": since_days}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def feedback_csv(
        self,
        org_id: str,
        space_id: str,
        *,
        page_id: Union[str, NotGiven] = NOT_GIVEN,
        rating: Union[str, NotGiven] = NOT_GIVEN,
        since_days: Union[float, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of feedback

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/feedback.csv``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/feedback.csv",
            query=_query({"pageId": page_id, "rating": rating, "sinceDays": since_days}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def llms_full(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of llms full (docs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/llms-full.txt``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/llms-full.txt",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def tags(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAnalyticsTagsResponse:
        """List tags in a space (docs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/tags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/tags",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def tags_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/tags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def tag_pages(
        self,
        org_id: str,
        space_id: str,
        tag: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAnalyticsTagPagesResponse:
        """Get the tag (spaces docs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/tags/{tag}``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/tags/{_path(tag)}",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def tag_pages_all(
        self,
        org_id: str,
        space_id: str,
        tag: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``tag_pages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/tags/{_path(tag)}",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def skill_md(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of skill (docs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/skill.md``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/skill.md",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def llms_txt(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of llms (orgs spaces docs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/llms.txt``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/llms.txt",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def page_markdown(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        form: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the markdown in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/markdown``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/markdown",
            query=_query({"form": form}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def draft_markdown(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        form: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the markdown in a space (draft)

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/draft/markdown``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/draft/markdown",
            query=_query({"form": form}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def check_links(
        self,
        org_id: str,
        space_id: str,
        *,
        external: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAnalyticsCheckLinksResponse:
        """Create a check link in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/check-links``

        :param external: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/check-links",
            query=_query({"external": external}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def empty_sections(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAnalyticsEmptySectionsResponse:
        """List empty sections in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/empty-sections``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/empty-sections",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def empty_sections_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``empty_sections`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/empty-sections",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def orphans(
        self,
        org_id: str,
        space_id: str,
        *,
        scope: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAnalyticsOrphansResponse:
        """List orphans in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/orphans``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/orphans",
            query=_query({"scope": scope}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def backlinks(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsAnalyticsBacklinksResponse:
        """List backlinks in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/backlinks``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/backlinks",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def backlinks_all(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``backlinks`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/backlinks",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def stale(
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
    ) -> DocsAnalyticsStaleResponse:
        """Get the stale in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/stale``

        :param days: How many days of no change counts as stale.
        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/stale",
            query=_query({"days": days, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def stale_all(
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
        """Iterate every item of ``stale`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/stale",
            query=_query({"days": days, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )


class DocsChangeRequestsResource:
    """``client.docs.change_requests`` (22 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def agent_review(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsAgentReviewResponse:
        """Create the agent review in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/agent-review``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/agent-review",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def agent_run(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        instruction: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the agent run in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/agent-run``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/agent-run",
            query=_query({}, extra_query),
            body=_body({"instruction": instruction}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

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
    ) -> DocsChangeRequestsListResponse:
        """List change requests in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/change-requests``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsCreateResponse:
        """Create a change request in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests",
            query=_query({}, extra_query),
            body=_body({"title": title}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def merge_rules(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsMergeRulesResponse:
        """List merge rules in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/change-requests/merge-rules``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/merge-rules",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_merge_rules(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        required_approvals: Union[int, NotGiven] = NOT_GIVEN,
        require_all_reviewers: Union[bool, NotGiven] = NOT_GIVEN,
        block_on_changes_requested: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsSetMergeRulesResponse:
        """Replace merge rules in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/change-requests/merge-rules``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/merge-rules",
            query=_query({}, extra_query),
            body=_body({"requiredApprovals": required_approvals, "requireAllReviewers": require_all_reviewers, "blockOnChangesRequested": block_on_changes_requested}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def merge_blockers(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsMergeBlockersResponse:
        """List merge blockers in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/merge-blockers``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/merge-blockers",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def merge_blockers_all(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``merge_blockers`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/merge-blockers",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def conflicts(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsConflictsResponse:
        """List conflicts in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/conflicts``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/conflicts",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def conflicts_all(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``conflicts`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/conflicts",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def eligibility(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsEligibilityResponse:
        """Get the eligibility in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/change-requests/eligibility``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/eligibility",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangeRequestDetail:
        """Get the change request

        ``GET /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def pages(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsPagesResponse:
        """List pages in a space (orgs change requests)

        ``GET /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/pages``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/pages",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def pages_all(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``pages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/pages",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def request_review(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsRequestReviewResponse:
        """Create the request review in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/request-review``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/request-review",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def approve(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsApproveResponse:
        """Approve the change request

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/approve``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/approve",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def merge(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        force: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsMergeResponse:
        """Merge the change request

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/merge``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/merge",
            query=_query({}, extra_query),
            body=_body({"force": force}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rebase(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsRebaseResponse:
        """Create the rebase in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/rebase``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/rebase",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_reviewers(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsListReviewersResponse:
        """List reviewers in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/reviewers``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/reviewers",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_reviewers_all(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_reviewers`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/reviewers",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def add_reviewers(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        user_ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsAddReviewersResponse:
        """Create a reviewer in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/reviewers``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/reviewers",
            query=_query({}, extra_query),
            body=_body({"userIds": user_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_reviewer(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        reviewer_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsRemoveReviewerResponse:
        """Delete the reviewer

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/reviewers/{reviewerId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/reviewers/{_path(reviewer_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def review(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        verdict: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsReviewResponse:
        """Create the review in a space (change requests)

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/review``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/review",
            query=_query({}, extra_query),
            body=_body({"verdict": verdict}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def close(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsCloseResponse:
        """Close the change request

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/close``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/close",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def comments(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsCommentsResponse:
        """List comments in a space (change requests)

        ``GET /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/comments``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/comments",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def comments_all(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``comments`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/comments",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def comment(
        self,
        org_id: str,
        space_id: str,
        cr_id: str,
        *,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        page_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        parent_comment_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        anchor: Union[Optional[DocsChangeRequestsCommentParamsAnchor], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsChangeRequestsCommentResponse:
        """Create a comment in a space (change requests)

        ``POST /orgs/{orgId}/spaces/{spaceId}/change-requests/{crId}/comments``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/change-requests/{_path(cr_id)}/comments",
            query=_query({}, extra_query),
            body=_body({"body": body, "pageId": page_id, "parentCommentId": parent_comment_id, "anchor": anchor}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsCollectionsResource:
    """``client.docs.collections`` (8 operations)."""

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
    ) -> DocsCollectionsListResponse:
        """List collections in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/collections``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        nav: Union[DocsCollectionsCreateParamsNav, NotGiven] = NOT_GIVEN,
        description: Union[Optional[str], NotGiven] = NOT_GIVEN,
        cover_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        seo: Union[DocsCollectionsCreateParamsSeo, NotGiven] = NOT_GIVEN,
        translations: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCollectionsCreateResponse:
        """Create a collection in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/collections``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections",
            query=_query({}, extra_query),
            body=_body({"name": name, "slug": slug, "nav": nav, "description": description, "coverUrl": cover_url, "seo": seo, "translations": translations}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        collection_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCollectionsGetResponse:
        """Get the collection

        ``GET /orgs/{orgId}/spaces/{spaceId}/collections/{collectionId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections/{_path(collection_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        collection_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        nav: Union[DocsCollectionsUpdateParamsNav, NotGiven] = NOT_GIVEN,
        description: Union[Optional[str], NotGiven] = NOT_GIVEN,
        cover_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        seo: Union[DocsCollectionsUpdateParamsSeo, NotGiven] = NOT_GIVEN,
        translations: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCollectionsUpdateResponse:
        """Update the collection

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/collections/{collectionId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections/{_path(collection_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "slug": slug, "nav": nav, "description": description, "coverUrl": cover_url, "seo": seo, "translations": translations}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        collection_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCollectionsRemoveResponse:
        """Delete the collection

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/collections/{collectionId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections/{_path(collection_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reorder(
        self,
        org_id: str,
        space_id: str,
        *,
        ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCollectionsReorderResponse:
        """Reorder the collection

        ``POST /orgs/{orgId}/spaces/{spaceId}/collections/reorder``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections/reorder",
            query=_query({}, extra_query),
            body=_body({"ids": ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def pages(
        self,
        org_id: str,
        space_id: str,
        collection_id: str,
        *,
        locale: str,
        version: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCollectionsPagesResponse:
        """List pages in a space (orgs collections)

        ``GET /orgs/{orgId}/spaces/{spaceId}/collections/{collectionId}/pages``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections/{_path(collection_id)}/pages",
            query=_query({"locale": locale, "version": version, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def pages_all(
        self,
        org_id: str,
        space_id: str,
        collection_id: str,
        *,
        locale: str,
        version: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``pages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections/{_path(collection_id)}/pages",
            query=_query({"locale": locale, "version": version, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def order(
        self,
        org_id: str,
        space_id: str,
        collection_id: str,
        *,
        page_ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCollectionsOrderResponse:
        """Create the order in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/collections/{collectionId}/order``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections/{_path(collection_id)}/order",
            query=_query({}, extra_query),
            body=_body({"pageIds": page_ids, "parentId": parent_id, "version": version, "locale": locale}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsCommentsResource:
    """``client.docs.comments`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCommentsListResponse:
        """List comments in a space (pages)

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/comments``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/comments",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/comments",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def moderate(
        self,
        org_id: str,
        space_id: str,
        comment_id: str,
        *,
        status: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCommentsModerateResponse:
        """Update the comment

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/comments/{commentId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/comments/{_path(comment_id)}",
            query=_query({}, extra_query),
            body=_body({"status": status}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        comment_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCommentsRemoveResponse:
        """Delete the comment

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/comments/{commentId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/comments/{_path(comment_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def resolve(
        self,
        org_id: str,
        space_id: str,
        comment_id: str,
        *,
        resolved: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCommentsResolveResponse:
        """Resolve the comment

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/comments/{commentId}/resolve``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/comments/{_path(comment_id)}/resolve",
            query=_query({}, extra_query),
            body=_body({"resolved": resolved}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def apply_suggestion(
        self,
        org_id: str,
        space_id: str,
        comment_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsCommentsApplySuggestionResponse:
        """Apply suggestion in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/comments/{commentId}/apply-suggestion``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/comments/{_path(comment_id)}/apply-suggestion",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsImportsResource:
    """``client.docs.imports`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def dedupe_titles(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        dry_run: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a dedupe title in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/import/dedupe-titles``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/import/dedupe-titles",
            query=_query({}, extra_query),
            body=_body({"dryRun": dry_run}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def import_files(
        self,
        org_id: str,
        space_id: str,
        *,
        files: List[DocsImportsImportFilesParamsFile],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        collection: Union[str, NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        replace_collection: Union[bool, NotGiven] = NOT_GIVEN,
        on_existing: Union[str, NotGiven] = NOT_GIVEN,
        prune: Union[str, NotGiven] = NOT_GIVEN,
        dry_run: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Import the doc

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/import``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/import",
            query=_query({}, extra_query),
            body=_body({"files": files, "collection": collection, "collectionId": collection_id, "replaceCollection": replace_collection, "onExisting": on_existing, "prune": prune, "dryRun": dry_run}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def import_zip(
        self,
        org_id: str,
        space_id: str,
        *,
        file: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the zip in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/import/zip``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/import/zip",
            query=_query({}, extra_query),
            body=_body({"file": file}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def import_url(
        self,
        org_id: str,
        space_id: str,
        *,
        url: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        branch: Union[str, NotGiven] = NOT_GIVEN,
        collection: Union[str, NotGiven] = NOT_GIVEN,
        on_existing: Union[str, NotGiven] = NOT_GIVEN,
        prune: Union[str, NotGiven] = NOT_GIVEN,
        dry_run: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the URL in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/import/url``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/import/url",
            query=_query({}, extra_query),
            body=_body({"url": url, "branch": branch, "collection": collection, "onExisting": on_existing, "prune": prune, "dryRun": dry_run}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def import_docx(
        self,
        org_id: str,
        space_id: str,
        *,
        file: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the docx in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/import/docx``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/import/docx",
            query=_query({}, extra_query),
            body=_body({"file": file}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsOpenapiResource:
    """``client.docs.openapi`` (17 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list_specs(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiListSpecsResponse:
        """List specs in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/openapi/specs``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_specs_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_specs`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def register_spec(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        source_url: Union[str, NotGiven] = NOT_GIVEN,
        url: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        slug_prefix: Union[str, NotGiven] = NOT_GIVEN,
        include_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        exclude_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        slug_style: Union[str, NotGiven] = NOT_GIVEN,
        landing: Union[bool, NotGiven] = NOT_GIVEN,
        tag_pages: Union[str, NotGiven] = NOT_GIVEN,
        on_existing: Union[str, NotGiven] = NOT_GIVEN,
        changelog: Union[DocsOpenapiRegisterSpecParamsChangelog, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiRegisterSpecResponse:
        """Create a spec in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/openapi/specs``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs",
            query=_query({}, extra_query),
            body=_body({"sourceUrl": source_url, "url": url, "name": name, "collectionId": collection_id, "mode": mode, "slugPrefix": slug_prefix, "includeTags": include_tags, "excludeTags": exclude_tags, "slugStyle": slug_style, "landing": landing, "tagPages": tag_pages, "onExisting": on_existing, "changelog": changelog}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def resync_spec(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        slug_prefix: Union[str, NotGiven] = NOT_GIVEN,
        include_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        exclude_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        slug_style: Union[str, NotGiven] = NOT_GIVEN,
        landing: Union[bool, NotGiven] = NOT_GIVEN,
        tag_pages: Union[str, NotGiven] = NOT_GIVEN,
        on_existing: Union[str, NotGiven] = NOT_GIVEN,
        changelog: Union[DocsOpenapiResyncSpecParamsChangelog, NotGiven] = NOT_GIVEN,
        background: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Resync the spec

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/openapi/specs/{id}/resync``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs/{_path(id)}/resync",
            query=_query({}, extra_query),
            body=_body({"collectionId": collection_id, "title": title, "mode": mode, "slugPrefix": slug_prefix, "includeTags": include_tags, "excludeTags": exclude_tags, "slugStyle": slug_style, "landing": landing, "tagPages": tag_pages, "onExisting": on_existing, "changelog": changelog, "background": background}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def resync_status(
        self,
        org_id: str,
        space_id: str,
        id: str,
        job_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiResyncStatusResponse:
        """Get the resync

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/openapi/specs/{id}/resync/{jobId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs/{_path(id)}/resync/{_path(job_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def spec_reference(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiSpecReferenceResponse:
        """Get the reference in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/openapi/specs/{id}/reference``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs/{_path(id)}/reference",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def remove_spec(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiRemoveSpecResponse:
        """Delete the spec

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/docs/openapi/specs/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def sdk_languages(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiSdkLanguagesResponse:
        """List languages in a space (docs OpenAPI)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/openapi/sdk/languages``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/sdk/languages",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def sdk_languages_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``sdk_languages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/sdk/languages",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def spec_sdk(
        self,
        org_id: str,
        space_id: str,
        id: str,
        language: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiSpecSdkResponse:
        """Get the SDK (docs OpenAPI specs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/openapi/specs/{id}/sdk/{language}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs/{_path(id)}/sdk/{_path(language)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def spec_sdk_package(
        self,
        org_id: str,
        space_id: str,
        id: str,
        language: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the package in a space (docs OpenAPI specs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/openapi/specs/{id}/sdk/{language}/package``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs/{_path(id)}/sdk/{_path(language)}/package",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def spec_lint(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiSpecLintResponse:
        """Get the lint in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/openapi/specs/{id}/lint``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/specs/{_path(id)}/lint",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def lint_url(
        self,
        org_id: str,
        space_id: str,
        *,
        source_url: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiLintUrlResponse:
        """Create the lint in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/openapi/lint``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/lint",
            query=_query({}, extra_query),
            body=_body({"sourceUrl": source_url}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def operations(
        self,
        org_id: str,
        space_id: str,
        *,
        url: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiOperationsResponse:
        """Create an operation in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/openapi/operations``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/operations",
            query=_query({}, extra_query),
            body=_body({"url": url}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def resolve(
        self,
        org_id: str,
        space_id: str,
        *,
        url: str,
        method: str,
        path: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiResolveResponse:
        """Resolve the OpenAPI

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/openapi/resolve``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/resolve",
            query=_query({}, extra_query),
            body=_body({"url": url, "method": method, "path": path}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def generate(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        url: Union[str, NotGiven] = NOT_GIVEN,
        source_url: Union[str, NotGiven] = NOT_GIVEN,
        spec: Union[Any, NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        enhance: Union[DocsOpenapiGenerateParamsEnhance, NotGiven] = NOT_GIVEN,
        landing: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiGenerateResponse:
        """Generate the OpenAPI

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/openapi/generate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/generate",
            query=_query({}, extra_query),
            body=_body({"url": url, "sourceUrl": source_url, "spec": spec, "collectionId": collection_id, "enhance": enhance, "landing": landing}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def generate_status(
        self,
        org_id: str,
        space_id: str,
        job_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsOpenapiGenerateStatusResponse:
        """Get the generate

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/openapi/generate/{jobId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/generate/{_path(job_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def import_(
        self,
        org_id: str,
        space_id: str,
        *,
        collection_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        url: Union[str, NotGiven] = NOT_GIVEN,
        source_url: Union[str, NotGiven] = NOT_GIVEN,
        spec: Union[Any, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        slug_prefix: Union[str, NotGiven] = NOT_GIVEN,
        replace_collection: Union[bool, NotGiven] = NOT_GIVEN,
        dry_run: Union[bool, NotGiven] = NOT_GIVEN,
        include_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        exclude_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        slug_style: Union[str, NotGiven] = NOT_GIVEN,
        landing: Union[bool, NotGiven] = NOT_GIVEN,
        tag_pages: Union[str, NotGiven] = NOT_GIVEN,
        on_existing: Union[str, NotGiven] = NOT_GIVEN,
        relayout: Union[bool, NotGiven] = NOT_GIVEN,
        spec_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ImportOutcome:
        """Import the OpenAPI

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/openapi/import``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/import",
            query=_query({}, extra_query),
            body=_body({"url": url, "sourceUrl": source_url, "spec": spec, "collectionId": collection_id, "title": title, "mode": mode, "slugPrefix": slug_prefix, "replaceCollection": replace_collection, "dryRun": dry_run, "includeTags": include_tags, "excludeTags": exclude_tags, "slugStyle": slug_style, "landing": landing, "tagPages": tag_pages, "onExisting": on_existing, "relayout": relayout, "specId": spec_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def import_file(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        slug_prefix: Union[str, NotGiven] = NOT_GIVEN,
        replace_collection: Union[bool, NotGiven] = NOT_GIVEN,
        dry_run: Union[bool, NotGiven] = NOT_GIVEN,
        include_tags: Union[str, NotGiven] = NOT_GIVEN,
        exclude_tags: Union[str, NotGiven] = NOT_GIVEN,
        on_existing: Union[str, NotGiven] = NOT_GIVEN,
        slug_style: Union[str, NotGiven] = NOT_GIVEN,
        landing: Union[bool, NotGiven] = NOT_GIVEN,
        tag_pages: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ImportOutcome:
        """Import file in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/openapi/import-file``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/openapi/import-file",
            query=_query({}, extra_query),
            body=_body({"collectionId": collection_id, "title": title, "mode": mode, "slugPrefix": slug_prefix, "replaceCollection": replace_collection, "dryRun": dry_run, "includeTags": include_tags, "excludeTags": exclude_tags, "onExisting": on_existing, "slugStyle": slug_style, "landing": landing, "tagPages": tag_pages}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsPagesRevisionsResource:
    """``client.docs.pages.revisions`` (12 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def save(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[BlockDoc, NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        change_request_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRevisionsSaveResponse:
        """Replace the content in a space (pages)

        ``PUT /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/content``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/content",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "body": body, "changeRequestId": change_request_id}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def put_section(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        key: str,
        *,
        markdown: str,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRevisionsPutSectionResponse:
        """Replace the section (pages)

        ``PUT /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/sections/{key}``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/sections/{_path(key)}",
            query=_query({}, extra_query),
            body=_body({"markdown": markdown}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_shape(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        preset: Optional[str],
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRevisionsSetShapeResponse:
        """Replace the shape in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/shape``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/shape",
            query=_query({}, extra_query),
            body=_body({"preset": preset}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def draft(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DraftView:
        """List draft pages in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/draft``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/draft",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def published(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublishedPage:
        """List published pages in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/published``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/published",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def history(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRevisionsHistoryResponse:
        """List revisions in a space (pages)

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/revisions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/revisions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def history_all(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``history`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/revisions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def diff(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        revision_id: str,
        *,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> RevisionDiff:
        """Get the diff in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/revisions/{revisionId}/diff``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/revisions/{_path(revision_id)}/diff",
            query=_query({"from": from_}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def checkpoints(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRevisionsCheckpointsResponse:
        """List checkpoints in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/checkpoints``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/checkpoints",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def checkpoint(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        checkpoint_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRevisionsCheckpointResponse:
        """Get the checkpoint

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/checkpoints/{checkpointId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/checkpoints/{_path(checkpoint_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def restore_checkpoint(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        checkpoint_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRevisionsRestoreCheckpointResponse:
        """Restore the checkpoint

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/checkpoints/{checkpointId}/restore``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/checkpoints/{_path(checkpoint_id)}/restore",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_schedule(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRevisionsGetScheduleResponse:
        """Get the schedule in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/schedule``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/schedule",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def cancel_schedule(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRevisionsCancelScheduleResponse:
        """Delete the schedule in a space (pages)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/schedule``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/schedule",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsPagesResource:
    """``client.docs.pages`` (22 operations; revisions)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.revisions = DocsPagesRevisionsResource(client)

    def create(
        self,
        org_id: str,
        space_id: str,
        collection_id: str,
        *,
        title: str,
        slug: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        preset: Union[Optional[str], NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        content: Union[BlockDoc, NotGiven] = NOT_GIVEN,
        sections: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        params: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        version_key: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        on_slug_taken: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesCreateResponse:
        """Create a page in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/collections/{collectionId}/pages``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/collections/{_path(collection_id)}/pages",
            query=_query({}, extra_query),
            body=_body({"preset": preset, "title": title, "slug": slug, "parentId": parent_id, "content": content, "sections": sections, "body": body, "params": params, "versionKey": version_key, "locale": locale, "onSlugTaken": on_slug_taken}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        include: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesGetResponse:
        """Get the page (orgs spaces)

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}``

        :param include: Comma-separated relations to fold in.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}",
            query=_query({"include": include}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        on_slug_taken: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesUpdateResponse:
        """Update the page

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}",
            query=_query({}, extra_query),
            body=_body({"slug": slug, "title": title, "onSlugTaken": on_slug_taken}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRemoveResponse:
        """Delete the page

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_metadata(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesGetMetadataResponse:
        """Get the metadata in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/metadata``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/metadata",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_metadata(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        audience: Union[Optional[DocsPagesSetMetadataParamsAudience], NotGiven] = NOT_GIVEN,
        fields: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        kind: Union[Optional[str], NotGiven] = NOT_GIVEN,
        icon: Union[Optional[PageIconName], NotGiven] = NOT_GIVEN,
        hide_from_nav: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        external_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        nav_title: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        badge: Union[Optional[DocsPagesSetMetadataParamsBadge], NotGiven] = NOT_GIVEN,
        nav_kind: Union[Optional[str], NotGiven] = NOT_GIVEN,
        nav_font: Union[Optional[str], NotGiven] = NOT_GIVEN,
        search_exclude: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        cover_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        layout: Union[Optional[str], NotGiven] = NOT_GIVEN,
        hide_title: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        subtitle: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        hide_updated: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        hide_cover: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        template: Union[Optional[str], NotGiven] = NOT_GIVEN,
        hero: Union[Optional[DocsPagesSetMetadataParamsHero], NotGiven] = NOT_GIVEN,
        toc_levels: Union[Optional[DocsPagesSetMetadataParamsTocLevels], NotGiven] = NOT_GIVEN,
        page_chrome: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        title_align: Union[Optional[str], NotGiven] = NOT_GIVEN,
        theme_patch: Union[Optional[DocsPagesSetMetadataParamsThemePatch], NotGiven] = NOT_GIVEN,
        on_this_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        api_method: Union[Optional[str], NotGiven] = NOT_GIVEN,
        api_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        api: Union[Optional[str], NotGiven] = NOT_GIVEN,
        seo_title: Union[Optional[str], NotGiven] = NOT_GIVEN,
        seo_description: Union[Optional[str], NotGiven] = NOT_GIVEN,
        noindex: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        content_language: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        canonical_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        hide_feedback: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        edit_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        source_path: Union[Optional[str], NotGiven] = NOT_GIVEN,
        pager: Union[Optional[DocsPagesSetMetadataParamsPager], NotGiven] = NOT_GIVEN,
        hide_pager: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        keywords: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        comments_enabled: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        custom_css: Union[Optional[str], NotGiven] = NOT_GIVEN,
        theme: Union[Optional[DocsPagesSetMetadataParamsTheme], NotGiven] = NOT_GIVEN,
        share_image_url: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        og_title: Union[Optional[str], NotGiven] = NOT_GIVEN,
        og_description: Union[Optional[str], NotGiven] = NOT_GIVEN,
        twitter_card: Union[Optional[str], NotGiven] = NOT_GIVEN,
        json_ld: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesSetMetadataResponse:
        """Update the metadata in a space

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/metadata``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/metadata",
            query=_query({}, extra_query),
            body=_body({"tags": tags, "audience": audience, "fields": fields, "kind": kind, "icon": icon, "hideFromNav": hide_from_nav, "externalUrl": external_url, "navTitle": nav_title, "badge": badge, "navKind": nav_kind, "navFont": nav_font, "searchExclude": search_exclude, "coverUrl": cover_url, "layout": layout, "hideTitle": hide_title, "subtitle": subtitle, "hideUpdated": hide_updated, "hideCover": hide_cover, "template": template, "hero": hero, "tocLevels": toc_levels, "pageChrome": page_chrome, "titleAlign": title_align, "themePatch": theme_patch, "onThisPage": on_this_page, "apiMethod": api_method, "apiPage": api_page, "api": api, "seoTitle": seo_title, "seoDescription": seo_description, "noindex": noindex, "contentLanguage": content_language, "canonicalUrl": canonical_url, "hideFeedback": hide_feedback, "editUrl": edit_url, "sourcePath": source_path, "pager": pager, "hidePager": hide_pager, "keywords": keywords, "commentsEnabled": comments_enabled, "customCss": custom_css, "theme": theme, "shareImageUrl": share_image_url, "ogTitle": og_title, "ogDescription": og_description, "twitterCard": twitter_card, "jsonLd": json_ld}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reorder(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        after_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesReorderResponse:
        """Reorder the page

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/reorder``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/reorder",
            query=_query({}, extra_query),
            body=_body({"parentId": parent_id, "afterId": after_id, "collectionId": collection_id}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesListResponse:
        """List pages in a space (orgs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages``

        :param limit: Pages per page, once a version is stated.
        :param version: Only this content version.
        :param locale: Only this language.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages",
            query=_query({"limit": limit, "cursor": cursor, "version": version, "locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages",
            query=_query({"limit": limit, "version": version, "locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def inventory(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesInventoryResponse:
        """Get the inventory in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/inventory``

        :param limit: Pages per page, once a version is stated.
        :param version: Only this content version.
        :param locale: Only this language.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/inventory",
            query=_query({"limit": limit, "cursor": cursor, "version": version, "locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def inventory_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``inventory`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/inventory",
            query=_query({"limit": limit, "version": version, "locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def bulk_delete(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        ids: Union[List[str], NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesBulkDeleteResponse:
        """Create the bulk delete in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/bulk-delete``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/bulk-delete",
            query=_query({}, extra_query),
            body=_body({"ids": ids, "collectionId": collection_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bulk_move(
        self,
        org_id: str,
        space_id: str,
        *,
        ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesBulkMoveResponse:
        """Create the bulk move in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/bulk-move``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/bulk-move",
            query=_query({}, extra_query),
            body=_body({"ids": ids, "collectionId": collection_id, "parentId": parent_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def duplicate(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesDuplicateResponse:
        """Duplicate the page

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/duplicate``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/duplicate",
            query=_query({}, extra_query),
            body=_body({"title": title, "slug": slug, "collectionId": collection_id, "parentId": parent_id}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def trash(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesTrashResponse:
        """List trash pages in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/trash``

        :param limit: Deleted pages per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/trash",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def trash_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``trash`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/trash",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def empty_trash(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesEmptyTrashResponse:
        """Create the empty trash in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/empty-trash``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/empty-trash",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def restore(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRestoreResponse:
        """Restore the page

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/restore``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/restore",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unpublish(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesUnpublishResponse:
        """Unpublish the page

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/unpublish``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/unpublish",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def purge(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesPurgeResponse:
        """Purge the page

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/purge``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/purge",
            query=_query({}, extra_query),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def publish(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        editorial: Union[bool, NotGiven] = NOT_GIVEN,
        editorial_note: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesPublishResponse:
        """Publish the page

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/publish``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/publish",
            query=_query({}, extra_query),
            body=_body({"editorial": editorial, "editorialNote": editorial_note}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def schedule_publish(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        publish_at: str,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesSchedulePublishResponse:
        """Create the schedule in a space (pages)

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/schedule``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/schedule",
            query=_query({}, extra_query),
            body=_body({"publishAt": publish_at}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rollback(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        revision_id: str,
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesRollbackResponse:
        """Create the rollback in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/rollback``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/rollback",
            query=_query({}, extra_query),
            body=_body({"revisionId": revision_id, "mode": mode}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def collab_token(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesCollabTokenResponse:
        """Create the collab token in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/collab-token``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/collab-token",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def collab_state(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsPagesCollabStateResponse:
        """Get the collab state in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/collab-state``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/collab-state",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class DocsReusablesResource:
    """``client.docs.reusables`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list_reusable(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsReusablesListReusableResponse:
        """Get the reusable content in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/reusable-content``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reusable-content",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_reusable_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_reusable`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reusable-content",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create_reusable(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Any, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsReusablesCreateReusableResponse:
        """Create the reusable content in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/reusable-content``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reusable-content",
            query=_query({}, extra_query),
            body=_body({"name": name, "content": content}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_reusable(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Any, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsReusablesUpdateReusableResponse:
        """Update the reusable content

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/reusable-content/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reusable-content/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "content": content}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_reusable(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsReusablesDeleteReusableResponse:
        """Delete the reusable content

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/reusable-content/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reusable-content/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_variables(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsReusablesListVariablesResponse:
        """List variables in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/variables``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/variables",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_variables_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_variables`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/variables",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def set_variable(
        self,
        org_id: str,
        space_id: str,
        *,
        key: str,
        value: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsReusablesSetVariableResponse:
        """Replace variables in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/variables``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/variables",
            query=_query({}, extra_query),
            body=_body({"key": key, "value": value, "type": type}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_variable(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsReusablesDeleteVariableResponse:
        """Delete the variable (spaces)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/variables/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/variables/{_path(key)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsTemplatesResource:
    """``client.docs.templates`` (4 operations)."""

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
    ) -> DocsTemplatesListResponse:
        """List page templates in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/page-templates``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/page-templates",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/page-templates",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def save(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Any, NotGiven] = NOT_GIVEN,
        org_wide: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsTemplatesSaveResponse:
        """Create a page template in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/page-templates``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/page-templates",
            query=_query({}, extra_query),
            body=_body({"name": name, "content": content, "orgWide": org_wide}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsTemplatesRemoveResponse:
        """Delete the page template

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/page-templates/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/page-templates/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def new_page(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        collection_id: str,
        title: str,
        slug: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsTemplatesNewPageResponse:
        """Create the new page in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/page-templates/{id}/new-page``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/page-templates/{_path(id)}/new-page",
            query=_query({}, extra_query),
            body=_body({"collectionId": collection_id, "title": title, "slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsTranslationsResource:
    """``client.docs.translations`` (4 operations)."""

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
    ) -> DocsTranslationsListResponse:
        """List locales in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/locales``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/locales",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/locales",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        code: str,
        label: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsTranslationsCreateResponse:
        """Create a locale in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/locales``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/locales",
            query=_query({}, extra_query),
            body=_body({"code": code, "label": label}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        code: str,
        *,
        label: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsTranslationsUpdateResponse:
        """Update the locale

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/docs/locales/{code}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/locales/{_path(code)}",
            query=_query({}, extra_query),
            body=_body({"label": label}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        code: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsTranslationsRemoveResponse:
        """Delete the locale

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/docs/locales/{code}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/locales/{_path(code)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsVersionsResource:
    """``client.docs.versions`` (5 operations)."""

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
    ) -> DocsVersionsListResponse:
        """List versions in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/versions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/versions",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/versions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        key: str,
        label: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        from_version: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsVersionsCreateResponse:
        """Create a version in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/versions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/versions",
            query=_query({}, extra_query),
            body=_body({"key": key, "label": label, "fromVersion": from_version}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        label: Union[str, NotGiven] = NOT_GIVEN,
        badge: Union[Any, NotGiven] = NOT_GIVEN,
        banner: Union[str, NotGiven] = NOT_GIVEN,
        hidden: Union[bool, NotGiven] = NOT_GIVEN,
        archived: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsVersionsUpdateResponse:
        """Update the version

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/docs/versions/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/versions/{_path(key)}",
            query=_query({}, extra_query),
            body=_body({"label": label, "badge": badge, "banner": banner, "hidden": hidden, "archived": archived}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsVersionsRemoveResponse:
        """Delete the version

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/docs/versions/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/versions/{_path(key)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def make_default(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        retire_as: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        retire_label: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsVersionsMakeDefaultResponse:
        """Create the make default in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/docs/versions/{key}/make-default``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/versions/{_path(key)}/make-default",
            query=_query({}, extra_query),
            body=_body({"retireAs": retire_as, "retireLabel": retire_label}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class DocsResource:
    """``client.docs`` (2 operations; ai, analytics, change_requests, collections, comments, imports, openapi, pages, reusables, templates, translations, versions)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.ai = DocsAiResource(client)
        self.analytics = DocsAnalyticsResource(client)
        self.change_requests = DocsChangeRequestsResource(client)
        self.collections = DocsCollectionsResource(client)
        self.comments = DocsCommentsResource(client)
        self.imports = DocsImportsResource(client)
        self.openapi = DocsOpenapiResource(client)
        self.pages = DocsPagesResource(client)
        self.reusables = DocsReusablesResource(client)
        self.templates = DocsTemplatesResource(client)
        self.translations = DocsTranslationsResource(client)
        self.versions = DocsVersionsResource(client)

    def block_schema(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsBlockSchemaResponse:
        """Get the block schema

        ``GET /docs/block-schema``
        """
        return self._client._request(
            "GET",
            f"/docs/block-schema",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def search(
        self,
        org_id: str,
        space_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> DocsSearchResponse:
        """Get the search in a space (docs)

        ``GET /orgs/{orgId}/spaces/{spaceId}/docs/search``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/docs/search",
            query=_query({"q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
