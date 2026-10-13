from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class PublicBlogResource:
    """``client.public.blog`` (14 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def subscribe(
        self,
        org_id: str,
        space_id: str,
        *,
        email: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogSubscribeResponse:
        """Subscribe the blog

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/blog/subscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/subscribe",
            query=_query({}, extra_query),
            body=_body({"email": email, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def index(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        author_id: Union[str, NotGiven] = NOT_GIVEN,
        author: Union[str, NotGiven] = NOT_GIVEN,
        series: Union[str, NotGiven] = NOT_GIVEN,
        month: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogIndexResponse:
        """Get the blog in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog``

        :param limit: Articles per page.
        :param page: Which page of results to return, 1-based.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog",
            query=_query({"limit": limit, "tag": tag, "authorId": author_id, "author": author, "series": series, "month": month, "page": page, "cursor": cursor, "share": share, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def index_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        author_id: Union[str, NotGiven] = NOT_GIVEN,
        author: Union[str, NotGiven] = NOT_GIVEN,
        series: Union[str, NotGiven] = NOT_GIVEN,
        month: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ArticleSummary]:
        """Iterate every item of ``index`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog",
            query=_query({"limit": limit, "tag": tag, "authorId": author_id, "author": author, "series": series, "month": month, "page": page, "share": share, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="articles",
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
    ) -> PublicBlogTagsResponse:
        """List tags in a space (public reader blog)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/tags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags",
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
    ) -> Iterator[PublicBlogTagsResponseTag]:
        """Iterate every item of ``tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="tags",
        )

    def search(
        self,
        org_id: str,
        space_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogSearchResponse:
        """Get the search in a space (public reader blog)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/search``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/search",
            query=_query({"q": q, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def search_all(
        self,
        org_id: str,
        space_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicBlogSearchResponseHit]:
        """Iterate every item of ``search`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/search",
            query=_query({"q": q, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="hits",
        )

    def rss(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of the blog (rss.xml)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/rss.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def rss_alias(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of the blog (feed.xml)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/feed.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/feed.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def json_feed(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """JSON feed of the blog

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/feed.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/feed.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def permalink(
        self,
        org_id: str,
        space_id: str,
        *,
        path: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogPermalinkResponse:
        """Get the permalink in a space (blog)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/permalink``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/permalink",
            query=_query({"path": path}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def archive(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogArchiveResponse:
        """Archive the blog

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/archive``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/archive",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def archive_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicBlogArchiveResponseMonth]:
        """Iterate every item of ``archive`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/archive",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="months",
        )

    def series(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogSeriesResponse:
        """List series in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/series``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/series",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def series_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicBlogSeriesResponseSery]:
        """Iterate every item of ``series`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/series",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="series",
        )

    def piece_markdown(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read a blog article as markdown

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/t/{slug}.md``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/t/{_path(slug)}.md",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def article(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogArticleResponse:
        """Read a blog article

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/t/{slug}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/t/{_path(slug)}",
            query=_query({"share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def react(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        emoji: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogReactResponse:
        """Create the react in a space (public reader blog t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/blog/t/{slug}/react``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/t/{_path(slug)}/react",
            query=_query({}, extra_query),
            body=_body({"emoji": emoji}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def comment(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        author_name: str,
        content: PublicBlogCommentParamsContent,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        parent_post_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogCommentResponse:
        """Create the comment in a space (blog)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/blog/t/{slug}/comment``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/t/{_path(slug)}/comment",
            query=_query({}, extra_query),
            body=_body({"authorName": author_name, "content": content, "parentPostId": parent_post_id, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicCardsResource:
    """``client.public.cards`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def social_card_png(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of social card

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/social-card.png``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/social-card.png",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def page_social_card_png(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of social card (pages)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/social-card.png``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/social-card.png",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def topic_social_card_png(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of social card (t)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/t/{topicId}/social-card.png``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/t/{_path(topic_id)}/social-card.png",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def topic_social_card(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the social card svg in a space (t)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/t/{topicId}/social-card.svg``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/t/{_path(topic_id)}/social-card.svg",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def social_card(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the social card svg in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/social-card.svg``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/social-card.svg",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def page_social_card(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the social card svg in a space (pages)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/social-card.svg``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/social-card.svg",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicCareersResource:
    """``client.public.careers`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def attach(
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
    ) -> PublicCareersAttachResponse:
        """Create an attachment in a space (careers)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/careers/attachments``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/attachments",
            query=_query({}, extra_query),
            body=_body({"file": file}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def apply(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        email: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        page_id: Union[str, NotGiven] = NOT_GIVEN,
        cover_letter: Union[str, NotGiven] = NOT_GIVEN,
        links: Union[str, NotGiven] = NOT_GIVEN,
        attachments: Union[List[PublicCareersApplyParamsAttachment], NotGiven] = NOT_GIVEN,
        website: Union[str, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicCareersApplyResponse:
        """Apply the career

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/careers/apply``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/apply",
            query=_query({}, extra_query),
            body=_body({"pageId": page_id, "name": name, "email": email, "coverLetter": cover_letter, "links": links, "attachments": attachments, "website": website, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicChangelogResource:
    """``client.public.changelog`` (8 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def comment(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        author_name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        parent_post_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicChangelogCommentResponse:
        """Create the comment in a space (changelog)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/changelog/t/{slug}/comment``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/t/{_path(slug)}/comment",
            query=_query({}, extra_query),
            body=_body({"authorName": author_name, "content": content, "parentPostId": parent_post_id, "captchaToken": captcha_token, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def piece_markdown(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read a changelog release as markdown

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog/t/{slug}.md``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/t/{_path(slug)}.md",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def release(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicChangelogReleaseResponse:
        """Read a changelog release

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog/t/{slug}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/t/{_path(slug)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def react(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        emoji: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicChangelogReactResponse:
        """Create the react in a space (public reader changelog t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/changelog/t/{slug}/react``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/t/{_path(slug)}/react",
            query=_query({}, extra_query),
            body=_body({"emoji": emoji}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def subscribe(
        self,
        org_id: str,
        space_id: str,
        *,
        email: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicChangelogSubscribeResponse:
        """Subscribe the changelog

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/changelog/subscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/subscribe",
            query=_query({}, extra_query),
            body=_body({"email": email, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        offset: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        year: Union[str, NotGiven] = NOT_GIVEN,
        since: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogArchiveEnveloped:
        """Get the changelog in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog``

        :param limit: Releases per page.
        :param offset: Where in the archive to start.
        :param since: Use an ISO date (2026-01-31) or date-time (2026-01-31T09:00:00Z).
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog",
            query=_query({"limit": limit, "offset": offset, "share": share, "year": year, "since": since, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        offset: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        year: Union[str, NotGiven] = NOT_GIVEN,
        since: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog",
            query=_query({"limit": limit, "offset": offset, "share": share, "year": year, "since": since}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def rss(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of the changelog

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/rss.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def json_feed(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """JSON feed of the changelog

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog/feed.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/feed.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicConsentResource:
    """``client.public.consent`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def resolved(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ResolvedConsentConfig:
        """Get the consent in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/consent``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/consent",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def record(
        self,
        org_id: str,
        space_id: str,
        *,
        subject_id: str,
        categories: Dict[str, Any],
        adapter_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        policy_version: Union[str, NotGiven] = NOT_GIVEN,
        receipt: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicConsentRecordResponse:
        """Create a receipt in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/consent/receipts``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/consent/receipts",
            query=_query({}, extra_query),
            body=_body({"subjectId": subject_id, "categories": categories, "adapterId": adapter_id, "policyVersion": policy_version, "receipt": receipt}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicContactResource:
    """``client.public.contact`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def exists(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicContactExistsResponse:
        """Get the contact in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/contact``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def submit(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        email: str,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        subject: Union[str, NotGiven] = NOT_GIVEN,
        department: Union[str, NotGiven] = NOT_GIVEN,
        attachments: Union[List[PublicContactSubmitParamsAttachment], NotGiven] = NOT_GIVEN,
        website: Union[str, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        fields: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicContactSubmitResponse:
        """Create the contact in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/contact``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact",
            query=_query({}, extra_query),
            body=_body({"name": name, "email": email, "subject": subject, "body": body, "department": department, "attachments": attachments, "website": website, "captchaToken": captcha_token, "fields": fields}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def attach(
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
    ) -> PublicContactAttachResponse:
        """Create an attachment in a space (contact)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/contact/attachments``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/attachments",
            query=_query({}, extra_query),
            body=_body({"file": file}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicCoursesResource:
    """``client.public.courses`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def outline(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseOutline:
        """Get the outline in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/course/outline``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/outline",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def verify(
        self,
        org_id: str,
        space_id: str,
        verify_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CertificateView:
        """Get the certificate

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/course/certificate/{verifyId}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/certificate/{_path(verify_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def pdf(
        self,
        org_id: str,
        space_id: str,
        verify_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the PDF in a space (course certificate)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/course/certificate/{verifyId}/pdf``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/certificate/{_path(verify_id)}/pdf",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicCustomEmojiResource:
    """``client.public.custom_emoji`` (1 operation)."""

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
    ) -> PublicCustomEmojiListResponse:
        """Get the custom emoji in an organization (public reader)

        ``GET /public/orgs/{orgId}/custom-emoji``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/custom-emoji",
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
    ) -> Iterator[PublicCustomEmojiListResponseEmojiItem]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/custom-emoji",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="emoji",
        )


class PublicDomainsResource:
    """``client.public.domains`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def primary(
        self,
        *,
        space: Union[str, NotGiven] = NOT_GIVEN,
        org: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicDomainsPrimaryResponse:
        """Get the primary

        ``GET /public/domains/primary``

        :param space: Space slug or id.
        :param org: Organization slug or id.
        """
        return self._client._request(
            "GET",
            f"/public/domains/primary",
            query=_query({"space": space, "org": org}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def resolve(
        self,
        *,
        path: Union[str, NotGiven] = NOT_GIVEN,
        host: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicDomainsResolveResponse:
        """Resolve the domain

        ``GET /public/domains/resolve``

        :param path: The request path; the longest registered prefix under it answers.
        :param host: The hostname to resolve, e.g.
        """
        return self._client._request(
            "GET",
            f"/public/domains/resolve",
            query=_query({"path": path, "host": host}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicEventsResource:
    """``client.public.events`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        scope: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicEventsListResponse:
        """List events in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events``

        :param limit: Events per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit, "scope": scope, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        scope: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[EventSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit, "scope": scope}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="events",
        )

    def feed(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of calendar

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/calendar.ics``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/calendar.ics",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> EventSummary:
        """Get the event (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def ics(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of calendar (for a named one)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/{handle}/calendar.ics``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/{_path(handle)}/calendar.ics",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicExtensionRegistryResource:
    """``client.public.extension_registry`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicExtensionRegistryListResponse:
        """List extensions

        ``GET /registry/extensions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/registry/extensions",
            query=_query({"q": q, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[RegistryListing]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/registry/extensions",
            query=_query({"q": q, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="extensions",
        )

    def get(
        self,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicExtensionRegistryGetResponse:
        """Get the extension

        ``GET /registry/extensions/{slug}``
        """
        return self._client._request(
            "GET",
            f"/registry/extensions/{_path(slug)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicFormsResource:
    """``client.public.forms`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def definition(
        self,
        org_id: str,
        form_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicFormsDefinitionResponse:
        """Get the form (public reader)

        ``GET /public/orgs/{orgId}/forms/{formId}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/forms/{_path(form_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def submit(
        self,
        org_id: str,
        form_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        body: Any = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicFormsSubmitResponse:
        """Create a submission in an organization

        ``POST /public/orgs/{orgId}/forms/{formId}/submissions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/forms/{_path(form_id)}/submissions",
            query=_query({}, extra_query),
            body=body,
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicForumDiscoveryResource:
    """``client.public.forum.discovery`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def permalink(
        self,
        org_id: str,
        space_id: str,
        *,
        path: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumDiscoveryPermalinkResponse:
        """Get the permalink in a space (forum)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/permalink``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/permalink",
            query=_query({"path": path}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def bookmarks(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumDiscoveryBookmarksResponse:
        """List bookmarks in a space (public reader forum)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/bookmarks``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/bookmarks",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def bookmarks_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicForumDiscoveryBookmarksResponseTopic]:
        """Iterate every item of ``bookmarks`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/bookmarks",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="topics",
        )

    def mention_suggest(
        self,
        org_id: str,
        space_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumDiscoveryMentionSuggestResponse:
        """Get the mention suggest in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/mention-suggest``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/mention-suggest",
            query=_query({"q": q, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def mention_suggest_all(
        self,
        org_id: str,
        space_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicForumDiscoveryMentionSuggestResponseSuggestion]:
        """Iterate every item of ``mention_suggest`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/mention-suggest",
            query=_query({"q": q, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="suggestions",
        )

    def resolve_refs(
        self,
        org_id: str,
        space_id: str,
        *,
        tokens: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumDiscoveryResolveRefsResponse:
        """List refs in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/refs``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/refs",
            query=_query({"tokens": tokens}, extra_query),
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
    ) -> PublicForumDiscoverySearchResponse:
        """Get the search in a space (public reader forum)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/search``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/search",
            query=_query({"q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicForumFeedsResource:
    """``client.public.forum.feeds`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def rss(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of the forum

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/rss.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def latest_rss(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of latest

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/latest.rss``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/latest.rss",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def top_rss(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of top

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/top.rss``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/top.rss",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicForumPeopleResource:
    """``client.public.forum.people`` (8 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def directory(
        self,
        org_id: str,
        space_id: str,
        *,
        search: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumPeopleDirectoryResponse:
        """Get the directory in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/directory``

        :param page: Which page of results to return, 1-based.
        :param limit: Rows per page — the spelling used everywhere else in this API.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/directory",
            query=_query({"search": search, "page": page, "cursor": cursor, "limit": limit, "order": order, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def directory_all(
        self,
        org_id: str,
        space_id: str,
        *,
        search: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        order: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``directory`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/directory",
            query=_query({"search": search, "page": page, "limit": limit, "order": order, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="members",
        )

    def badges(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumPeopleBadgesResponse:
        """List badges in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/badges``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/badges",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def badges_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicForumPeopleBadgesResponseBadge]:
        """Iterate every item of ``badges`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/badges",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="badges",
        )

    def leaderboard(
        self,
        org_id: str,
        space_id: str,
        *,
        period: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumPeopleLeaderboardResponse:
        """Get the leaderboard in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/leaderboard``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/leaderboard",
            query=_query({"period": period}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def profile(
        self,
        org_id: str,
        space_id: str,
        user_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumPeopleProfileResponse:
        """Get the member

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/u/{userId}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/u/{_path(user_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def user_summary(
        self,
        org_id: str,
        space_id: str,
        user_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> UserSummary:
        """Get the summary in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/u/{userId}/summary``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/u/{_path(user_id)}/summary",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def user_actions_feed(
        self,
        org_id: str,
        space_id: str,
        user_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        before: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumPeopleUserActionsFeedResponse:
        """List actions in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/u/{userId}/actions``

        :param limit: Actions per page.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/u/{_path(user_id)}/actions",
            query=_query({"limit": limit, "type": type, "before": before}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def user_card(
        self,
        org_id: str,
        space_id: str,
        user_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumPeopleUserCardResponse:
        """Get the card in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/u/{userId}/card``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/u/{_path(user_id)}/card",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def online_roster(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumPeopleOnlineRosterResponse:
        """Get the online in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/presence/online``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/presence/online",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def online_roster_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicForumPeopleOnlineRosterResponseOnlineItem]:
        """Iterate every item of ``online_roster`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/presence/online",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="online",
        )


class PublicForumTaxonomyResource:
    """``client.public.forum.taxonomy`` (8 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def categories_list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTaxonomyCategoriesListResponse:
        """List categories in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/categories``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def categories_list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CategorySummary]:
        """Iterate every item of ``categories_list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="categories",
        )

    def category_form_template(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTaxonomyCategoryFormTemplateResponse:
        """Get the form template in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/categories/{categoryId}/form-template``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}/form-template",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def categories_overview(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTaxonomyCategoriesOverviewResponse:
        """Get the overview in a space (public reader forum categories)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/categories/overview``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/overview",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def categories_overview_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicForumTaxonomyCategoriesOverviewResponseCategory]:
        """Iterate every item of ``categories_overview`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/overview",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="categories",
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
    ) -> PublicForumTaxonomyTagsResponse:
        """List tags in a space (public reader forum)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/tags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tags",
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
    ) -> Iterator[PublicForumTaxonomyTagsResponseTag]:
        """Iterate every item of ``tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="tags",
        )

    def tag_about(
        self,
        org_id: str,
        space_id: str,
        tag: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTaxonomyTagAboutResponse:
        """Get the tag (public reader spaces forum)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/tags/{tag}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tags/{_path(tag)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def tag_intersection(
        self,
        org_id: str,
        space_id: str,
        a: str,
        b: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTaxonomyTagIntersectionResponse:
        """Get the intersection

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/tags/intersection/{a}/{b}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tags/intersection/{_path(a)}/{_path(b)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def category_rss(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of the category

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/categories/{slug}/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(slug)}/rss.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def tag_rss(
        self,
        org_id: str,
        space_id: str,
        tag: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of the tag

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/tags/{tag}/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tags/{_path(tag)}/rss.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicForumThreadsResource:
    """``client.public.forum.threads`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def stream(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the stream in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/stream``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/stream",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def stream_stream(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Stream ``stream`` as server-sent events, yielding each decoded event."""
        yield from self._client._stream(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/stream",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def piece_markdown(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read a forum topic as markdown

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}.md``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}.md",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def topic(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumThreadsTopicResponse:
        """Read a forum topic

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}",
            query=_query({"share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicForumTopicsResource:
    """``client.public.forum.topics`` (19 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def heartbeat(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        viewer_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        typing: Union[bool, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsHeartbeatResponse:
        """Create the heartbeat in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/heartbeat``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/heartbeat",
            query=_query({}, extra_query),
            body=_body({"viewerId": viewer_id, "typing": typing, "name": name}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reply(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        author_name: str,
        content: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        parent_post_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        whisper: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsReplyResponse:
        """Create the reply in a space (public reader forum t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/reply``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/reply",
            query=_query({}, extra_query),
            body=_body({"authorName": author_name, "content": content, "parentPostId": parent_post_id, "whisper": whisper}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reply_as_linked_topic(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        title: str,
        content: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsReplyAsLinkedTopicResponse:
        """Create the reply as linked topic in a space (public reader t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/reply-as-linked-topic``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/reply-as-linked-topic",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "categoryId": category_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def react(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        emoji: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsReactResponse:
        """Create the react in a space (public reader forum t posts)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/react``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/react",
            query=_query({}, extra_query),
            body=_body({"emoji": emoji}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reactors(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsReactorsResponse:
        """List reactions in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/reactions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/reactions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def reactors_all(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicForumTopicsReactorsResponseReaction]:
        """Iterate every item of ``reactors`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/reactions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="reactions",
        )

    def flag(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        flag_type: Union[str, NotGiven] = NOT_GIVEN,
        reason: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsFlagResponse:
        """Flag the post (public reader forum t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/flag``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/flag",
            query=_query({}, extra_query),
            body=_body({"flagType": flag_type, "reason": reason}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def flag_topic(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        flag_type: Union[str, NotGiven] = NOT_GIVEN,
        reason: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsFlagTopicResponse:
        """Flag the topic

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/flag``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/flag",
            query=_query({}, extra_query),
            body=_body({"flagType": flag_type, "reason": reason}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bookmark(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsBookmarkResponse:
        """Create the bookmark in a space (public reader forum t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/bookmark``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/bookmark",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bookmark_post(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsBookmarkPostResponse:
        """Create the bookmark in a space (public reader forum t posts)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/bookmark``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/bookmark",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bookmark_reminder(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        remind_at: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        preset: Union[str, NotGiven] = NOT_GIVEN,
        note: Union[Optional[str], NotGiven] = NOT_GIVEN,
        name: Union[Optional[str], NotGiven] = NOT_GIVEN,
        auto_delete: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsBookmarkReminderResponse:
        """Replace the reminder in a space (public reader t)

        ``PUT /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/bookmark/reminder``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/bookmark/reminder",
            query=_query({}, extra_query),
            body=_body({"remindAt": remind_at, "preset": preset, "note": note, "name": name, "autoDelete": auto_delete}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def answer(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        post_id: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsAnswerResponse:
        """Create the answer in a space (public reader forum t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/answer``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/answer",
            query=_query({}, extra_query),
            body=_body({"postId": post_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def offer_bounty(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        amount: int,
        days: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsOfferBountyResponse:
        """Create the bounty in a space (public reader t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/bounty``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/bounty",
            query=_query({}, extra_query),
            body=_body({"amount": amount, "days": days}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def withdraw_bounty(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Delete the bounty in a space (public reader t)

        ``DELETE /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/bounty``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/bounty",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def edit(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        content: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsEditResponse:
        """Create the edit in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/edit``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/edit",
            query=_query({}, extra_query),
            body=_body({"content": content}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def post_revisions(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsPostRevisionsResponse:
        """List revisions in a space (public reader forum t posts)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/revisions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/revisions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def post_revisions_all(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PostRevisionMeta]:
        """Iterate every item of ``post_revisions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/revisions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="revisions",
        )

    def post_revision_diff(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        revision: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsPostRevisionDiffResponse:
        """Get the revision (public reader forum t)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/revisions/{revision}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/revisions/{_path(revision)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def notify(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        level: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsNotifyResponse:
        """Create the notify in a space (public reader t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/notify``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/notify",
            query=_query({}, extra_query),
            body=_body({"level": level}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def related_topics(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsRelatedTopicsResponse:
        """Get the related in a space (public reader t)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/related``

        :param limit: Related topics returned.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/related",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def topic_posts_rss(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of posts

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts.rss``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts.rss",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicForumResource:
    """``client.public.forum`` (7 operations; discovery, feeds, people, taxonomy, threads, topics)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.discovery = PublicForumDiscoveryResource(client)
        self.feeds = PublicForumFeedsResource(client)
        self.people = PublicForumPeopleResource(client)
        self.taxonomy = PublicForumTaxonomyResource(client)
        self.threads = PublicForumThreadsResource(client)
        self.topics = PublicForumTopicsResource(client)

    def read_all(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumReadAllResponse:
        """Create the read all in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/read-all``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/read-all",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def dismiss_new(
        self,
        org_id: str,
        space_id: str,
        *,
        category: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumDismissNewResponse:
        """Dismiss new in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/dismiss-new``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/dismiss-new",
            query=_query({"category": category, "tag": tag}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def dismiss_unread(
        self,
        org_id: str,
        space_id: str,
        *,
        category: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumDismissUnreadResponse:
        """Dismiss unread in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/dismiss-unread``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/dismiss-unread",
            query=_query({"category": category, "tag": tag}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def embed_resolve(
        self,
        org_id: str,
        space_id: str,
        *,
        article_url: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumEmbedResolveResponse:
        """Resolve the embed

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/embed/resolve``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/embed/resolve",
            query=_query({}, extra_query),
            body=_body({"articleUrl": article_url, "title": title}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def upload(
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
    ) -> PublicForumUploadResponse:
        """Upload the forum

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/upload``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/upload",
            query=_query({}, extra_query),
            body=_body({"file": file}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def create_anon(
        self,
        org_id: str,
        space_id: str,
        *,
        author_name: str,
        title: str,
        content: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumCreateAnonResponse:
        """Create a topic in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/topics``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/topics",
            query=_query({}, extra_query),
            body=_body({"authorName": author_name, "title": title, "content": content, "kind": kind, "tags": tags, "categoryId": category_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def index(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        category: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        filter: Union[str, NotGiven] = NOT_GIVEN,
        period: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        solved: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumIndexResponse:
        """Get the forum in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum``

        :param limit: Topics per page.
        :param page: Which page of results to return, 1-based.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum",
            query=_query({"limit": limit, "tag": tag, "kind": kind, "category": category, "page": page, "share": share, "filter": filter, "period": period, "cursor": cursor, "solved": solved, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def index_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        category: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        filter: Union[str, NotGiven] = NOT_GIVEN,
        period: Union[str, NotGiven] = NOT_GIVEN,
        solved: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ArticleSummary]:
        """Iterate every item of ``index`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum",
            query=_query({"limit": limit, "tag": tag, "kind": kind, "category": category, "page": page, "share": share, "filter": filter, "period": period, "solved": solved, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="topics",
        )


class PublicIdentityResource:
    """``client.public.identity`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def unlock(
        self,
        org_id: str,
        space_id: str,
        *,
        password: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicIdentityUnlockResponse:
        """Unlock the space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/unlock``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/unlock",
            query=_query({}, extra_query),
            body=_body({"password": password}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unlock_jwt(
        self,
        org_id: str,
        space_id: str,
        *,
        jwt: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicIdentityUnlockJwtResponse:
        """Unlock JWT in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/unlock-jwt``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/unlock-jwt",
            query=_query({}, extra_query),
            body=_body({"jwt": jwt}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def signup_fields(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicIdentitySignupFieldsResponse:
        """List signup fields in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/signup-fields``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/signup-fields",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def signup_fields_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicIdentitySignupFieldsResponseField]:
        """Iterate every item of ``signup_fields`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/signup-fields",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="fields",
        )

    def register(
        self,
        org_id: str,
        space_id: str,
        *,
        email: str,
        name: str,
        password: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        fields: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        company: Union[str, NotGiven] = NOT_GIVEN,
        form_rendered_at: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicIdentityRegisterResponse:
        """Create the register in a space (public reader)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/register``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/register",
            query=_query({}, extra_query),
            body=_body({"email": email, "name": name, "password": password, "fields": fields, "company": company, "formRenderedAt": form_rendered_at}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def sign_in(
        self,
        org_id: str,
        space_id: str,
        *,
        email: str,
        password: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicIdentitySignInResponse:
        """Sign a reader in to a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/sign-in``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/sign-in",
            query=_query({}, extra_query),
            body=_body({"email": email, "password": password}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicInteractionsResource:
    """``client.public.interactions`` (9 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

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
    ) -> PublicInteractionsAskResponse:
        """Create the ask in a space (public reader)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/ask``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/ask",
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
        """Create the stream in a space (public reader)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/ask/stream``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/ask/stream",
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
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/ask/stream",
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
    ) -> PublicInteractionsAskFeedbackResponse:
        """Create the feedback in a space (public reader ask)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/ask/{queryId}/feedback``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/ask/{_path(query_id)}/feedback",
            query=_query({}, extra_query),
            body=_body({"helpful": helpful, "comment": comment}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_comments(
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
    ) -> PublicInteractionsListCommentsResponse:
        """List comments in a space (public reader pages)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/comments``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/comments",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_comments_all(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CommentSummary]:
        """Iterate every item of ``list_comments`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/comments",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="comments",
        )

    def post_comment(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        author_name: str,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        anchor: Union[Optional[PublicInteractionsPostCommentParamsAnchor], NotGiven] = NOT_GIVEN,
        suggestion: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicInteractionsPostCommentResponse:
        """Create a comment in a space (public reader pages)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/comments``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/comments",
            query=_query({}, extra_query),
            body=_body({"authorName": author_name, "body": body, "parentId": parent_id, "anchor": anchor, "suggestion": suggestion}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def react_to_comment(
        self,
        org_id: str,
        space_id: str,
        comment_id: str,
        *,
        emoji: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicInteractionsReactToCommentResponse:
        """Create the react in a space (public reader comments)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/comments/{commentId}/react``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/comments/{_path(comment_id)}/react",
            query=_query({}, extra_query),
            body=_body({"emoji": emoji}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ext_render(
        self,
        org_id: str,
        space_id: str,
        *,
        extension: str,
        block: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        props: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        context: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicInteractionsExtRenderResponse:
        """Render the ext

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/ext/render``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/ext/render",
            query=_query({}, extra_query),
            body=_body({"extension": extension, "block": block, "props": props, "context": context}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def ext_action(
        self,
        org_id: str,
        space_id: str,
        *,
        extension: str,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        block: Union[str, NotGiven] = NOT_GIVEN,
        props: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        inputs: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        context: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicInteractionsExtActionResponse:
        """Create the action in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/ext/action``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/ext/action",
            query=_query({}, extra_query),
            body=_body({"extension": extension, "block": block, "action": action, "props": props, "inputs": inputs, "context": context}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def feedback(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        rating: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        comment: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Create the feedback in a space (public reader pages)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/feedback``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/feedback",
            query=_query({}, extra_query),
            body=_body({"rating": rating, "comment": comment}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicLegalResource:
    """``client.public.legal`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalListResponse:
        """Get the legal in an organization (public reader)

        ``GET /public/orgs/{orgId}/legal``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def accept(
        self,
        org_id: str,
        kind: str,
        *,
        subject: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        subject_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalAcceptResponse:
        """Accept the legal (public reader)

        ``POST /public/orgs/{orgId}/legal/{kind}/accept``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/legal/{_path(kind)}/accept",
            query=_query({}, extra_query),
            body=_body({"subject": subject, "subjectToken": subject_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def versions(
        self,
        org_id: str,
        kind: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalVersionsResponse:
        """List versions in an organization

        ``GET /public/orgs/{orgId}/legal/{kind}/versions``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/{_path(kind)}/versions",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        kind: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalGetResponse:
        """Get the legal

        ``GET /public/orgs/{orgId}/legal/{kind}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/{_path(kind)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicLegalGateResource:
    """``client.public.legal_gate`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalGateStatusResponse:
        """What this space requires a reader to accept

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/legal-gate``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/legal-gate",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def accept(
        self,
        org_id: str,
        space_id: str,
        kind: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalGateAcceptResponse:
        """Record this reader’s acceptance of a required document

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/legal-gate/{kind}/accept``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/legal-gate/{_path(kind)}/accept",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicMcpResource:
    """``client.public.mcp`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def info(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicMcpInfoResponse:
        """Get the MCP server in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/mcp``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/mcp",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def rpc(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the MCP server in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/mcp``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/mcp",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def server_card(
        self,
        org_id: str,
        space_id: str,
        *,
        base: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the server card in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/mcp/server-card``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/mcp/server-card",
            query=_query({"base": base}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def ai_catalog(
        self,
        org_id: str,
        slug: str,
        *,
        base: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the AI catalog in an organization

        ``GET /public/orgs/{orgId}/sites/{slug}/ai-catalog``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/sites/{_path(slug)}/ai-catalog",
            query=_query({"base": base}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def server_card_mcp_discovery(
        self,
        org_id: str,
        slug: str,
        *,
        base: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the MCP server card in an organization

        ``GET /public/orgs/{orgId}/sites/{slug}/mcp-server-card``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/sites/{_path(slug)}/mcp-server-card",
            query=_query({"base": base}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicOneboxResource:
    """``client.public.onebox`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def onebox(
        self,
        org_id: str,
        *,
        url: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicOneboxOneboxResponse:
        """Get the onebox in an organization

        ``GET /public/orgs/{orgId}/onebox``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/onebox",
            query=_query({"url": url}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def inline(
        self,
        org_id: str,
        *,
        url: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicOneboxInlineResponse:
        """Get the inline in an organization

        ``GET /public/orgs/{orgId}/onebox/inline``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/onebox/inline",
            query=_query({"url": url}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def onebox_post(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[PublicOneboxOneboxPostParamsContent, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicOneboxOneboxPostResponse:
        """Create the post in an organization

        ``POST /public/orgs/{orgId}/onebox/post``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/onebox/post",
            query=_query({}, extra_query),
            body=_body({"content": content}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicOpenapiResource:
    """``client.public.openapi`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def forward(
        self,
        org_id: str,
        space_id: str,
        *,
        target_url: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        method: Union[str, NotGiven] = NOT_GIVEN,
        headers: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicOpenapiForwardResponse:
        """Create the OpenAPI proxy in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/openapi-proxy``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/openapi-proxy",
            query=_query({}, extra_query),
            body=_body({"targetUrl": target_url, "method": method, "headers": headers, "body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def languages(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicOpenapiLanguagesResponse:
        """List languages in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/sdk/languages``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/sdk/languages",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def languages_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicOpenapiLanguagesResponseLanguage]:
        """Iterate every item of ``languages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/sdk/languages",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="languages",
        )

    def download(
        self,
        org_id: str,
        space_id: str,
        language: str,
        *,
        spec_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicOpenapiDownloadResponse:
        """Get the SDK (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/sdk/{language}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/sdk/{_path(language)}",
            query=_query({"specId": spec_id}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def download_package(
        self,
        org_id: str,
        space_id: str,
        language: str,
        *,
        spec_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the package in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/sdk/{language}/package``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/sdk/{_path(language)}/package",
            query=_query({"specId": spec_id}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def collection(
        self,
        org_id: str,
        space_id: str,
        kind: str,
        *,
        spec_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the collection (public reader API export)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/api-export/collections/{kind}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/api-export/collections/{_path(kind)}",
            query=_query({"specId": spec_id}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def mock(
        self,
        org_id: str,
        space_id: str,
        *,
        spec_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the mock server in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/api-export/mock-server``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/api-export/mock-server",
            query=_query({"specId": spec_id}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicOrgsResource:
    """``client.public.orgs`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def script_origins(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicOrgsScriptOriginsResponse:
        """List script origins in an organization

        ``GET /public/orgs/{orgId}/script-origins``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/script-origins",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def script_origins_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``script_origins`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/script-origins",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="origins",
        )

    def get(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicOrgsGetResponse:
        """Get the org (public reader)

        ``GET /public/orgs/{orgId}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def about(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AboutStats:
        """Get the about in an organization

        ``GET /public/orgs/{orgId}/about``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/about",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicPreviewResource:
    """``client.public.preview`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def page(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PreviewPage:
        """A page as it will look when published

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/preview/pages/{pageId}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/preview/pages/{_path(page_id)}",
            query=_query({"token": token}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicReactionsResource:
    """``client.public.reactions`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def image(
        self,
        org_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the reaction

        ``GET /public/orgs/{orgId}/reactions/{slug}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/reactions/{_path(slug)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicReaderAuthResource:
    """``client.public.reader_auth`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def resolved(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicReaderAuthResolvedResponse:
        """Get the reader auth in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/reader-auth``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-auth",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicReaderPolicyResource:
    """``client.public.reader_policy`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def resolved(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicReaderPolicyResolvedResponse:
        """Get the reader policy in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/reader-policy``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-policy",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicRelationsResource:
    """``client.public.relations`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def resolve(
        self,
        org_id: str,
        *,
        ids: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRelationsResolveResponse:
        """List relations in an organization

        ``GET /public/orgs/{orgId}/relations``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/relations",
            query=_query({"ids": ids, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def resolve_all(
        self,
        org_id: str,
        *,
        ids: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ResolvedRelation]:
        """Iterate every item of ``resolve`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/relations",
            query=_query({"ids": ids, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="items",
        )


class PublicRoadmapResource:
    """``client.public.roadmap`` (9 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def submit(
        self,
        org_id: str,
        space_id: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        author_name: Union[str, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapSubmitResponse:
        """Create an item in a space (public reader roadmap)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/roadmap/items``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/items",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "authorName": author_name, "captchaToken": captcha_token, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def board(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapBoardResponse:
        """Get the roadmap in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap``

        :param limit: Items per LANE — not lanes.
        :param page: Which page of results to return, 1-based.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap",
            query=_query({"limit": limit, "cursor": cursor, "page": page, "share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def board_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicRoadmapBoardResponseLane]:
        """Iterate every item of ``board`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap",
            query=_query({"limit": limit, "page": page, "share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="lanes",
        )

    def rss(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of the roadmap

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/rss.xml",
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
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapSearchResponse:
        """Get the search in a space (public reader roadmap)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap/search``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/search",
            query=_query({"q": q, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def search_all(
        self,
        org_id: str,
        space_id: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicRoadmapSearchResponseHit]:
        """Iterate every item of ``search`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/search",
            query=_query({"q": q, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="hits",
        )

    def piece_markdown(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read a roadmap item as markdown

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}.md``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}.md",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def item(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapItemResponse:
        """Read a roadmap item

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}",
            query=_query({"share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def comment(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        author_name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        parent_post_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapCommentResponse:
        """Create the comment in a space (roadmap)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}/comment``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}/comment",
            query=_query({}, extra_query),
            body=_body({"authorName": author_name, "content": content, "parentPostId": parent_post_id, "captchaToken": captcha_token, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def watch(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        email: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapWatchResponse:
        """Create the watch in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}/watch``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}/watch",
            query=_query({}, extra_query),
            body=_body({"email": email, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def vote(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapVoteResponse:
        """Create the vote in a space (public reader roadmap t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}/vote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}/vote",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicSitesResource:
    """``client.public.sites`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def robots(
        self,
        org_id: str,
        site_slug: str,
        *,
        sitemap: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of robots (sites)

        ``GET /public/orgs/{orgId}/sites/{siteSlug}/robots.txt``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/sites/{_path(site_slug)}/robots.txt",
            query=_query({"sitemap": sitemap}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def overview(
        self,
        org_id: str,
        slug: str,
        *,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SitePublicOverview:
        """Get the site (public reader)

        ``GET /public/orgs/{orgId}/sites/{slug}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/sites/{_path(slug)}",
            query=_query({"preview": preview}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def search(
        self,
        org_id: str,
        slug: str,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicSitesSearchResponse:
        """Get the search in an organization (public reader sites)

        ``GET /public/orgs/{orgId}/sites/{slug}/search``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/sites/{_path(slug)}/search",
            query=_query({"q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def ask(
        self,
        org_id: str,
        slug: str,
        *,
        question: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicSitesAskResponse:
        """Create the ask in an organization (public reader sites)

        ``POST /public/orgs/{orgId}/sites/{slug}/ask``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/sites/{_path(slug)}/ask",
            query=_query({}, extra_query),
            body=_body({"question": question}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicSpacesResource:
    """``client.public.spaces`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicSpacesListResponse:
        """List spaces

        ``GET /public/spaces``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/spaces",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PublicSpacesListResponseSpace]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/spaces",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="spaces",
        )

    def address_index(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderAddressIndex:
        """Get the address index in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/address-index``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/address-index",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicStatusResource:
    """``client.public.status`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def subscribe(
        self,
        org_id: str,
        space_id: str,
        *,
        email: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicStatusSubscribeResponse:
        """Subscribe the status

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/status/subscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/subscribe",
            query=_query({}, extra_query),
            body=_body({"email": email}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def board(
        self,
        org_id: str,
        space_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicStatusBoard:
        """The published status board

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status",
            query=_query({"share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def badge(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the badge svg in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/badge.svg``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/badge.svg",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def summary(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusSummary:
        """Statuspage-compatible status summary

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/summary.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/summary.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def rss(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of the status

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/rss.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicThemeComponentRegistryResource:
    """``client.public.theme_component_registry`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def browse(
        self,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        outlet: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicThemeComponentRegistryBrowseResponse:
        """List theme components

        ``GET /registry/theme-components``

        :param featured: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/registry/theme-components",
            query=_query({"q": q, "tag": tag, "outlet": outlet, "featured": featured, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def detail(
        self,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicThemeComponentRegistryDetailResponse:
        """Get the theme component

        ``GET /registry/theme-components/{slug}``
        """
        return self._client._request(
            "GET",
            f"/registry/theme-components/{_path(slug)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def package(
        self,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicThemeComponentRegistryPackageResponse:
        """Get the package

        ``GET /registry/theme-components/{slug}/package``
        """
        return self._client._request(
            "GET",
            f"/registry/theme-components/{_path(slug)}/package",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicThemeRegistryResource:
    """``client.public.theme_registry`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def browse(
        self,
        *,
        q: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        space_type: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ThemeBrowseResult:
        """List themes

        ``GET /registry/themes``

        :param featured: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/registry/themes",
            query=_query({"q": q, "tag": tag, "spaceType": space_type, "featured": featured, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def detail(
        self,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicThemeRegistryDetailResponse:
        """Get the theme

        ``GET /registry/themes/{slug}``
        """
        return self._client._request(
            "GET",
            f"/registry/themes/{_path(slug)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def card(
        self,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the card svg

        ``GET /registry/themes/{slug}/card.svg``
        """
        return self._client._request(
            "GET",
            f"/registry/themes/{_path(slug)}/card.svg",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def bundle(
        self,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicThemeRegistryBundleResponse:
        """Get the bundle

        ``GET /registry/themes/{slug}/bundle``
        """
        return self._client._request(
            "GET",
            f"/registry/themes/{_path(slug)}/bundle",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicTranslationsResource:
    """``client.public.translations`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def catalog(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicTranslationsCatalogResponse:
        """The interface strings you can override

        ``GET /public/orgs/{orgId}/i18n/catalog``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/i18n/catalog",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def map(
        self,
        org_id: str,
        locale: str,
        *,
        space: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicTranslationsMapResponse:
        """Get the translation

        ``GET /public/orgs/{orgId}/i18n/{locale}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/i18n/{_path(locale)}",
            query=_query({"space": space}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicVisitorAuthResource:
    """``client.public.visitor_auth`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def redeem_jwt_get(
        self,
        org_id: str,
        space_id: str,
        *,
        return_to: Union[str, NotGiven] = NOT_GIVEN,
        jwt: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Get the JWT in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/reader-auth/jwt``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-auth/jwt",
            query=_query({"returnTo": return_to, "jwt": jwt}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def redeem_jwt_post(
        self,
        org_id: str,
        space_id: str,
        *,
        jwt: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        return_to: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicVisitorAuthRedeemJwtPostResponse:
        """Create the JWT in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/reader-auth/jwt``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-auth/jwt",
            query=_query({}, extra_query),
            body=_body({"jwt": jwt, "returnTo": return_to}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def start(
        self,
        org_id: str,
        space_id: str,
        *,
        method: Union[str, NotGiven] = NOT_GIVEN,
        return_to: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Start the visitor OIDC

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/visitor-oidc/start``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/visitor-oidc/start",
            query=_query({"method": method, "returnTo": return_to}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def callback(
        self,
        *,
        state: Union[str, NotGiven] = NOT_GIVEN,
        code: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Get the callback (public reader visitor OIDC)

        ``GET /public/visitor-oidc/callback``
        """
        return self._client._request(
            "GET",
            f"/public/visitor-oidc/callback",
            query=_query({"state": state, "code": code}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def adopt(
        self,
        *,
        t: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Adopt the visitor OIDC

        ``GET /public/visitor-oidc/adopt``
        """
        return self._client._request(
            "GET",
            f"/public/visitor-oidc/adopt",
            query=_query({"t": t}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicResource:
    """``client.public`` (29 operations; blog, cards, careers, changelog, consent, contact, courses, custom_emoji, domains, events, extension_registry, forms, forum, identity, interactions, legal, legal_gate, mcp, onebox, openapi, orgs, preview, reactions, reader_auth, reader_policy, relations, roadmap, sites, spaces, status, theme_component_registry, theme_registry, translations, visitor_auth)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.blog = PublicBlogResource(client)
        self.cards = PublicCardsResource(client)
        self.careers = PublicCareersResource(client)
        self.changelog = PublicChangelogResource(client)
        self.consent = PublicConsentResource(client)
        self.contact = PublicContactResource(client)
        self.courses = PublicCoursesResource(client)
        self.custom_emoji = PublicCustomEmojiResource(client)
        self.domains = PublicDomainsResource(client)
        self.events = PublicEventsResource(client)
        self.extension_registry = PublicExtensionRegistryResource(client)
        self.forms = PublicFormsResource(client)
        self.forum = PublicForumResource(client)
        self.identity = PublicIdentityResource(client)
        self.interactions = PublicInteractionsResource(client)
        self.legal = PublicLegalResource(client)
        self.legal_gate = PublicLegalGateResource(client)
        self.mcp = PublicMcpResource(client)
        self.onebox = PublicOneboxResource(client)
        self.openapi = PublicOpenapiResource(client)
        self.orgs = PublicOrgsResource(client)
        self.preview = PublicPreviewResource(client)
        self.reactions = PublicReactionsResource(client)
        self.reader_auth = PublicReaderAuthResource(client)
        self.reader_policy = PublicReaderPolicyResource(client)
        self.relations = PublicRelationsResource(client)
        self.roadmap = PublicRoadmapResource(client)
        self.sites = PublicSitesResource(client)
        self.spaces = PublicSpacesResource(client)
        self.status = PublicStatusResource(client)
        self.theme_component_registry = PublicThemeComponentRegistryResource(client)
        self.theme_registry = PublicThemeRegistryResource(client)
        self.translations = PublicTranslationsResource(client)
        self.visitor_auth = PublicVisitorAuthResource(client)

    def captcha(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicCaptcha:
        """Get the captcha in an organization (public reader)

        ``GET /public/orgs/{orgId}/captcha``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/captcha",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def gate(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicGateResponse:
        """Get the gate in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/gate``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/gate",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def hub_intro(
        self,
        org_id: str,
        space_id: str,
        kind: str,
        key: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicHubIntroResponse:
        """Get the hub

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/hubs/{kind}/{key}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/hubs/{_path(kind)}/{_path(key)}",
            query=_query({"share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def search(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicSearchResponse:
        """Get the search in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/search``

        :param limit: How many hits to return.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/search",
            query=_query({"limit": limit, "q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def pdf(
        self,
        org_id: str,
        space_id: str,
        *,
        locale: str,
        version: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the PDF in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/pdf``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pdf",
            query=_query({"locale": locale, "version": version}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def page_pdf(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the PDF in a space (pages)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/pdf``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/pdf",
            query=_query({"share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def faq(
        self,
        org_id: str,
        space_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderFaq:
        """Get the FAQ in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/faq``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/faq",
            query=_query({"share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def api_origins(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicApiOriginsResponse:
        """List API origins in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/api-origins``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/api-origins",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def api_origins_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``api_origins`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/api-origins",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="origins",
        )

    def script_origins(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicScriptOriginsResponse:
        """List script origins in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/script-origins``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/script-origins",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def script_origins_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``script_origins`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/script-origins",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="origins",
        )

    def style_origins(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicStyleOriginsResponse:
        """List style origins in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/style-origins``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/style-origins",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def seo(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpacePublicSeo:
        """List SEO settings in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/seo``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/seo",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def site_of(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicSiteOfResponse:
        """Get the site in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/site``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/site",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def chrome(
        self,
        org_id: str,
        space_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderChrome:
        """Get the chrome in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/chrome``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/chrome",
            query=_query({"share": share, "preview": preview}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def sitemap(
        self,
        org_id: str,
        space_id: str,
        *,
        x_forwarded_host: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of sitemap

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/sitemap.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/sitemap.xml",
            query=_query({}, extra_query),
            headers={**_query({"x-forwarded-host": x_forwarded_host}), **(extra_headers or {})},
            timeout=timeout,
        )

    def robots(
        self,
        org_id: str,
        space_id: str,
        *,
        x_forwarded_host: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of robots (spaces)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/robots.txt``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/robots.txt",
            query=_query({}, extra_query),
            headers={**_query({"x-forwarded-host": x_forwarded_host}), **(extra_headers or {})},
            timeout=timeout,
        )

    def updates_rss(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of updates

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/updates.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/updates.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def updates(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicUpdatesResponse:
        """List updates in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/updates``

        :param limit: Updates per page, newest last.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/updates",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def updates_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[SpaceUpdateRow]:
        """Iterate every item of ``updates`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/updates",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="updates",
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
        """File of llms (public reader orgs spaces)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/llms.txt``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/llms.txt",
            query=_query({}, extra_query),
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
        """File of llms full (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/llms-full.txt``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/llms-full.txt",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
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
        """File of skill (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/skill.md``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/skill.md",
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
    ) -> PublicTagsResponse:
        """List tags in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/tags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/tags",
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
    ) -> Iterator[PublicTagsResponseTag]:
        """Iterate every item of ``tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/tags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="tags",
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
    ) -> PublicTagPagesResponse:
        """Get the tag (public reader spaces)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/tags/{tag}``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/tags/{_path(tag)}",
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
    ) -> Iterator[PublicTagPagesResponsePage]:
        """Iterate every item of ``tag_pages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/tags/{_path(tag)}",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="pages",
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
        """Get the page (public reader orgs spaces markdown)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}.md``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}.md",
            query=_query({"form": form}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def overview(
        self,
        org_id: str,
        space_id: str,
        *,
        locale: str,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderOverview:
        """Get the space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}",
            query=_query({"locale": locale, "preview": preview, "share": share, "version": version}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def page_version(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicPageVersionResponse:
        """Get the version in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/version``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/version",
            query=_query({"share": share, "version": version, "locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def page(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        version: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderPage:
        """Get the page (public reader orgs spaces)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}",
            query=_query({"version": version, "locale": locale, "share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def export_all(
        self,
        org_id: str,
        space_id: str,
        *,
        locale: str,
        version: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceExport:
        """Export the space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/export``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/export",
            query=_query({"locale": locale, "version": version}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def view(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Create the view in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/view``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/view",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def viewer(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ViewerView:
        """Get the viewer in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/viewer``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/viewer",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
