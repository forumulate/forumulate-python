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
        scope: Union[PublicBlogSubscribeParamsScope, NotGiven] = NOT_GIVEN,
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
            body=_body({"email": email, "captchaToken": captcha_token, "scope": scope}, extra_body),
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
        pinned: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[str, NotGiven] = NOT_GIVEN,
        tag_match: Union[str, NotGiven] = NOT_GIVEN,
        exclude: Union[List[str], NotGiven] = NOT_GIVEN,
        offset: Union[int, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogIndexResponse:
        """Get the blog in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog``

        :param limit: Articles per page.
        :param page: Which page of results to return, 1-based.
        :param pinned: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param featured: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param exclude: Comma-separated post ids to leave out — a front page’s feeds de-duplicating each other.
        :param offset: Skip this many posts before the page starts (added to the page’s own offset).
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog",
            query=_query({"limit": limit, "tag": tag, "authorId": author_id, "author": author, "series": series, "month": month, "page": page, "cursor": cursor, "share": share, "pinned": pinned, "featured": featured, "preview": preview, "tags": tags, "tagMatch": tag_match, "exclude": exclude, "offset": offset, "locale": locale, "sort": sort}, extra_query),
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
        pinned: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[str, NotGiven] = NOT_GIVEN,
        tag_match: Union[str, NotGiven] = NOT_GIVEN,
        exclude: Union[List[str], NotGiven] = NOT_GIVEN,
        offset: Union[int, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``index`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog",
            query=_query({"limit": limit, "tag": tag, "authorId": author_id, "author": author, "series": series, "month": month, "page": page, "share": share, "pinned": pinned, "featured": featured, "preview": preview, "tags": tags, "tagMatch": tag_match, "exclude": exclude, "offset": offset, "locale": locale, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``search`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/search",
            query=_query({"q": q, "limit": limit}, extra_query),
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
    ) -> Iterator[Any]:
        """Iterate every item of ``archive`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/archive",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
        """List series in a space (blog)

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
    ) -> Iterator[Any]:
        """Iterate every item of ``series`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/series",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def piece_markdown(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"locale": locale}, extra_query),
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
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"share": share, "locale": locale}, extra_query),
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


class PublicBlogMediaResource:
    """``client.public.blog_media`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def media_zip(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """A published post's library media as one zip

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/t/{slug}/media.zip``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/t/{_path(slug)}/media.zip",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicBlogTaxonomyResource:
    """``client.public.blog_taxonomy`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def tag(
        self,
        org_id: str,
        space_id: str,
        tag: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogTaxonomyTagResponse:
        """Get the tag (public reader spaces blog)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/tags/{tag}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags/{_path(tag)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def author_list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogTaxonomyAuthorListResponse:
        """List authors in a space (public reader blog)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/authors``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/authors",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def author_list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``author_list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/authors",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def author(
        self,
        org_id: str,
        space_id: str,
        ref: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicBlogTaxonomyAuthorResponse:
        """Get the author (blog)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/blog/authors/{ref}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/authors/{_path(ref)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicCardsResource:
    """``client.public.cards`` (7 operations)."""

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

    def collection_social_card_png(
        self,
        org_id: str,
        space_id: str,
        collection: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of social card (c)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/c/{collection}/social-card.png``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/c/{_path(collection)}/social-card.png",
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
    """``client.public.careers`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def form(
        self,
        org_id: str,
        space_id: str,
        *,
        page_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicCareersFormResponse:
        """Get the form in a space (public reader careers)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/careers/form``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/form",
            query=_query({"pageId": page_id}, extra_query),
            headers=extra_headers,
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
        answers: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        eeo: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        consent: Union[bool, NotGiven] = NOT_GIVEN,
        source: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
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
            body=_body({"pageId": page_id, "name": name, "email": email, "coverLetter": cover_letter, "links": links, "attachments": attachments, "website": website, "captchaToken": captcha_token, "answers": answers, "eeo": eeo, "consent": consent, "source": source}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicChangelogResource:
    """``client.public.changelog`` (9 operations)."""

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
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def release(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        more: Union[float, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"more": more, "locale": locale}, extra_query),
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
        scope: Union[PublicChangelogSubscribeParamsScope, NotGiven] = NOT_GIVEN,
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
            body=_body({"email": email, "captchaToken": captcha_token, "scope": scope}, extra_body),
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
        match: Union[str, NotGiven] = NOT_GIVEN,
        month: Union[str, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        channel: Union[str, NotGiven] = NOT_GIVEN,
        family: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        breaking: Union[str, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        pinned: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogArchiveEnveloped:
        """Get the changelog in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog``

        :param limit: Releases per page.
        :param offset: Where in the archive to start.
        :param since: Use an ISO date (2026-01-31) or date-time (2026-01-31T09:00:00Z).
        :param breaking: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param pinned: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param featured: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog",
            query=_query({"limit": limit, "offset": offset, "share": share, "year": year, "since": since, "cursor": cursor, "match": match, "month": month, "version": version, "type": type, "channel": channel, "family": family, "from": from_, "to": to, "breaking": breaking, "q": q, "pinned": pinned, "featured": featured, "sort": sort, "preview": preview, "locale": locale, "tag": tag}, extra_query),
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
        match: Union[str, NotGiven] = NOT_GIVEN,
        month: Union[str, NotGiven] = NOT_GIVEN,
        version: Union[str, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        channel: Union[str, NotGiven] = NOT_GIVEN,
        family: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        breaking: Union[str, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        pinned: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog",
            query=_query({"limit": limit, "offset": offset, "share": share, "year": year, "since": since, "match": match, "month": month, "version": version, "type": type, "channel": channel, "family": family, "from": from_, "to": to, "breaking": breaking, "q": q, "pinned": pinned, "featured": featured, "sort": sort, "preview": preview, "locale": locale, "tag": tag}, extra_query),
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

    def atom(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Atom feed of the changelog

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog/atom.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/atom.xml",
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


class PublicChangelogMarkdownResource:
    """``client.public.changelog_markdown`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def whole(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read the whole changelog as markdown

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog/changelog.md``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/changelog.md",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicChangelogWidgetResource:
    """``client.public.changelog_widget`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[float, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ChangelogWidgetResponse:
        """Get the widget in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog/widget``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/widget",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def hit(
        self,
        org_id: str,
        space_id: str,
        *,
        event: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Create the hit in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/changelog/widget/hit``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/widget/hit",
            query=_query({}, extra_query),
            body=_body({"event": event, "slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def watching(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicChangelogWidgetWatchingResponse:
        """Get the watch in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/changelog/watch``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/watch",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def watch(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicChangelogWidgetWatchResponse:
        """Replace the watch in a space

        ``PUT /public/orgs/{orgId}/spaces/{spaceId}/changelog/watch``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/watch",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unwatch(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicChangelogWidgetUnwatchResponse:
        """Delete the watch in a space

        ``DELETE /public/orgs/{orgId}/spaces/{spaceId}/changelog/watch``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/watch",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
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
        preview: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"preview": preview}, extra_query),
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
        source: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
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
            body=_body({"name": name, "email": email, "subject": subject, "body": body, "department": department, "attachments": attachments, "website": website, "captchaToken": captcha_token, "fields": fields, "source": source}, extra_body),
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


class PublicCourseCatalogResource:
    """``client.public.course_catalog`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def courses(
        self,
        org_id: str,
        *,
        path: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicCourseCatalogCoursesResponse:
        """List courses in an organization (public reader)

        ``GET /public/orgs/{orgId}/courses``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/courses",
            query=_query({"path": path, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def courses_all(
        self,
        org_id: str,
        *,
        path: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``courses`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/courses",
            query=_query({"path": path, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def paths(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicCourseCatalogPathsResponse:
        """List course paths in an organization (public reader)

        ``GET /public/orgs/{orgId}/course-paths``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/course-paths",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def paths_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``paths`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/course-paths",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )


class PublicCourseCommerceResource:
    """``client.public.course_commerce`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def quote(
        self,
        org_id: str,
        space_id: str,
        *,
        coupon: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> CourseQuote:
        """Get the quote in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/course/commerce/quote``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/course/commerce/quote",
            query=_query({"coupon": coupon}, extra_query),
            headers=extra_headers,
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
    ) -> GatedOutline:
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
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/custom-emoji",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )


class PublicDomainsResource:
    """``client.public.domains`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def primary(
        self,
        *,
        library: Union[str, NotGiven] = NOT_GIVEN,
        space: Union[str, NotGiven] = NOT_GIVEN,
        org: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicDomainsPrimaryResponse:
        """Get the primary

        ``GET /public/domains/primary``

        :param library: Content library id, for its hosted output (`/h/…`): its own domain first, else the site it feeds, at the library’s slug.
        :param space: Space slug or id.
        :param org: Organization slug or id.
        """
        return self._client._request(
            "GET",
            f"/public/domains/primary",
            query=_query({"library": library, "space": space, "org": org}, extra_query),
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
    """``client.public.events`` (8 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        scope: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicEventsListResponse:
        """List events in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events``

        :param limit: Events per page, once a version is stated.
        :param from_: Use an ISO date (2026-01-31) or date-time (2026-01-31T09:00:00Z).
        :param to: Use an ISO date (2026-01-31) or date-time (2026-01-31T09:00:00Z).
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit, "scope": scope, "tag": tag, "mode": mode, "from": from_, "to": to, "cursor": cursor, "share": share}, extra_query),
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
        tag: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events",
            query=_query({"limit": limit, "scope": scope, "tag": tag, "mode": mode, "from": from_, "to": to, "share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def feed(
        self,
        org_id: str,
        space_id: str,
        *,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"tag": tag, "share": share}, extra_query),
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
        """RSS feed of the event

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/rss.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def atom(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Atom feed of the event

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/atom.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/atom.xml",
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
        """JSON feed of the event

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/events/feed.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/feed.json",
            query=_query({}, extra_query),
            headers=extra_headers,
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
        scope: Union[PublicEventsSubscribeParamsScope, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicEventsSubscribeResponse:
        """Subscribe the event

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/events/subscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/events/subscribe",
            query=_query({}, extra_query),
            body=_body({"email": email, "captchaToken": captcha_token, "scope": scope}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def ics(
        self,
        org_id: str,
        space_id: str,
        handle: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"share": share}, extra_query),
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
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/registry/extensions",
            query=_query({"q": q, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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


class PublicFaqFollowResource:
    """``client.public.faq_follow`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def follow(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        email: Union[str, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        section: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicFaqFollowFollowResponse:
        """Follow the FAQ

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/faq/follow``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/faq/follow",
            query=_query({}, extra_query),
            body=_body({"email": email, "captchaToken": captcha_token, "section": section}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
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
    ) -> Iterator[Any]:
        """Iterate every item of ``bookmarks`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/bookmarks",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``mention_suggest`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/mention-suggest",
            query=_query({"q": q, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    """``client.public.forum.feeds`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def new_count(
        self,
        org_id: str,
        space_id: str,
        *,
        since: Union[str, NotGiven] = NOT_GIVEN,
        category: Union[str, NotGiven] = NOT_GIVEN,
        include_subcategories: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumFeedsNewCountResponse:
        """Get the new count in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/new-count``

        :param since: Use an ISO date (2026-01-31) or date-time (2026-01-31T09:00:00Z).
        :param include_subcategories: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/new-count",
            query=_query({"since": since, "category": category, "includeSubcategories": include_subcategories}, extra_query),
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
    """``client.public.forum.people`` (7 operations)."""

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
        scope: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"search": search, "page": page, "cursor": cursor, "limit": limit, "scope": scope, "order": order, "sort": sort}, extra_query),
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
        scope: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"search": search, "page": page, "limit": limit, "scope": scope, "order": order, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``badges`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/badges",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``online_roster`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/presence/online",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )


class PublicForumTaxonomyResource:
    """``client.public.forum.taxonomy`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def categories_list(
        self,
        org_id: str,
        space_id: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTaxonomyCategoriesListResponse:
        """List categories in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/categories``

        :param locale: Answer each category in this language: its `name` and `description` are replaced by the entry in its `translations` map for this code (exact, then by language: `pt-BR` → `pt`).
        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories",
            query=_query({"locale": locale, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def categories_list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``categories_list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories",
            query=_query({"locale": locale, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
        latest: Union[float, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTaxonomyCategoriesOverviewResponse:
        """Get the overview in a space (public reader forum categories)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/categories/overview``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/overview",
            query=_query({"latest": latest}, extra_query),
            headers=extra_headers,
            timeout=timeout,
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
    """``client.public.forum.threads`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def summary(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumThreadsSummaryResponse:
        """Create the summary in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/summary``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/summary",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

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
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def view(
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
        """Create the view in a space (forum t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/view``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/view",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def topic(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"share": share, "locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicForumTopicsResource:
    """``client.public.forum.topics`` (17 operations)."""

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

    def vote(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        value: float,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumTopicsVoteResponse:
        """Replace the vote in a space (public reader t)

        ``PUT /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/vote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/vote",
            query=_query({}, extra_query),
            body=_body({"value": value}, extra_body),
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
        """List reactions in a space (forum)

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
    ) -> Iterator[Any]:
        """Iterate every item of ``reactors`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/reactions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``post_revisions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/revisions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
        pinned: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        bountied: Union[str, NotGiven] = NOT_GIVEN,
        include_subcategories: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[str, NotGiven] = NOT_GIVEN,
        media: Union[str, NotGiven] = NOT_GIVEN,
        previews: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        filter: Union[str, NotGiven] = NOT_GIVEN,
        period: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        tag_match: Union[str, NotGiven] = NOT_GIVEN,
        solved: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumIndexResponse:
        """Get the forum in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum``

        :param limit: Topics per page.
        :param pinned: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param featured: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param bountied: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param include_subcategories: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param media: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param page: Which page of results to return, 1-based.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum",
            query=_query({"limit": limit, "tag": tag, "kind": kind, "category": category, "pinned": pinned, "featured": featured, "bountied": bountied, "includeSubcategories": include_subcategories, "tags": tags, "media": media, "previews": previews, "page": page, "share": share, "filter": filter, "period": period, "cursor": cursor, "preview": preview, "locale": locale, "tagMatch": tag_match, "solved": solved, "sort": sort}, extra_query),
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
        pinned: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        bountied: Union[str, NotGiven] = NOT_GIVEN,
        include_subcategories: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[str, NotGiven] = NOT_GIVEN,
        media: Union[str, NotGiven] = NOT_GIVEN,
        previews: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        filter: Union[str, NotGiven] = NOT_GIVEN,
        period: Union[str, NotGiven] = NOT_GIVEN,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        tag_match: Union[str, NotGiven] = NOT_GIVEN,
        solved: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``index`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum",
            query=_query({"limit": limit, "tag": tag, "kind": kind, "category": category, "pinned": pinned, "featured": featured, "bountied": bountied, "includeSubcategories": include_subcategories, "tags": tags, "media": media, "previews": previews, "page": page, "share": share, "filter": filter, "period": period, "preview": preview, "locale": locale, "tagMatch": tag_match, "solved": solved, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )


class PublicForumAccountResource:
    """``client.public.forum_account`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        unread: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumAccountListResponse:
        """The signed-in reader's notifications, newest first

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/me/notifications``

        :param limit: Rows per page.
        :param unread: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/me/notifications",
            query=_query({"limit": limit, "unread": unread, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        unread: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/me/notifications",
            query=_query({"limit": limit, "unread": unread}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def mark_read(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumAccountMarkReadResponse:
        """Mark one of the reader’s notifications read

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/me/notifications/{id}/read``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/me/notifications/{_path(id)}/read",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def mark_all_read(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumAccountMarkAllReadResponse:
        """Mark every one of the reader’s notifications read

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/me/notifications/read-all``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/me/notifications/read-all",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicForumBookmarkResource:
    """``client.public.forum_bookmark`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

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
    ) -> PublicForumBookmarkBookmarkResponse:
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
    ) -> PublicForumBookmarkBookmarkPostResponse:
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
    ) -> PublicForumBookmarkBookmarkReminderResponse:
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

    def dismiss_pin(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumBookmarkDismissPinResponse:
        """Dismiss pin in a space (public reader t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/dismiss-pin``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/dismiss-pin",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicForumCategoryResource:
    """``client.public.forum_category`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def category(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumCategoryCategoryResponse:
        """Get the category

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/category/{slug}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/category/{_path(slug)}",
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
        level: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumCategoryNotifyResponse:
        """Create the notify in a space (public reader category)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/category/{slug}/notify``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/category/{_path(slug)}/notify",
            query=_query({}, extra_query),
            body=_body({"level": level}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def tags(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumCategoryTagsResponse:
        """List tags in a space (public reader forum)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/tags``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tags",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicForumProfileResource:
    """``client.public.forum_profile`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def user_summary(
        self,
        org_id: str,
        space_id: str,
        user_id: str,
        *,
        rail: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicUserSummary:
        """Get the summary in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/u/{userId}/summary``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/u/{_path(user_id)}/summary",
            query=_query({"rail": rail}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicForumSearchResource:
    """``client.public.forum_search`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def full(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        offset: Union[int, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicForumSearchFullResponse:
        """Search a public forum with Discourse operators (ranked, paged)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/forum/search/full``

        :param limit: Hits per page.
        :param offset: Hits skipped.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/search/full",
            query=_query({"limit": limit, "offset": offset, "q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def full_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ForumSearchHit]:
        """Iterate every item of ``full`` across all pages, following ``offset``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/search/full",
            query=_query({"limit": limit, "q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="offset",
            items_key="hits",
        )


class PublicGrowthResource:
    """``client.public.growth`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def goal(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        goal: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        ab: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicGrowthGoalResponse:
        """Create the goal in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/goal``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/goal",
            query=_query({}, extra_query),
            body=_body({"goal": goal, "kind": kind, "ab": ab}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def exposure(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        ab: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicGrowthExposureResponse:
        """Create the exposure in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageId}/exposure``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/exposure",
            query=_query({}, extra_query),
            body=_body({"ab": ab}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``signup_fields`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/signup-fields",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    """``client.public.interactions`` (10 operations)."""

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
    ) -> Iterator[Any]:
        """Iterate every item of ``list_comments`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_id)}/comments",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        rating: Union[str, NotGiven] = NOT_GIVEN,
        comment: Union[str, NotGiven] = NOT_GIVEN,
        score: Union[int, NotGiven] = NOT_GIVEN,
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
            body=_body({"rating": rating, "comment": comment, "score": score}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def faq_search_event(
        self,
        org_id: str,
        space_id: str,
        *,
        query: str,
        hits: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Create a search event in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/faq/search-events``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/faq/search-events",
            query=_query({}, extra_query),
            body=_body({"query": query, "hits": hits}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicLegalResource:
    """``client.public.legal`` (11 operations)."""

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
        """List versions in an organization (public reader legal)

        ``GET /public/orgs/{orgId}/legal/{kind}/versions``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/{_path(kind)}/versions",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def edition(
        self,
        org_id: str,
        kind: str,
        edition: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalEditionResponse:
        """Get the version

        ``GET /public/orgs/{orgId}/legal/{kind}/versions/{edition}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/{_path(kind)}/versions/{_path(edition)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def diff(
        self,
        org_id: str,
        kind: str,
        *,
        from_: Union[str, NotGiven] = NOT_GIVEN,
        to: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalDiffResponse:
        """Get the diff in an organization (public reader)

        ``GET /public/orgs/{orgId}/legal/{kind}/diff``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/{_path(kind)}/diff",
            query=_query({"from": from_, "to": to}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def rss(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """RSS feed of the legal

        ``GET /public/orgs/{orgId}/legal/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/rss.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def atom(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Atom feed of the legal

        ``GET /public/orgs/{orgId}/legal/atom.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/atom.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def json_feed(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """JSON feed of the legal

        ``GET /public/orgs/{orgId}/legal/feed.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/feed.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def trust(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalTrustResponse:
        """JSON feed of trust

        ``GET /public/orgs/{orgId}/legal/trust.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/trust.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def subprocessors(
        self,
        org_id: str,
        kind: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicLegalSubprocessorsResponse:
        """List subprocessors in an organization

        ``GET /public/orgs/{orgId}/legal/{kind}/subprocessors``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/legal/{_path(kind)}/subprocessors",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        kind: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"locale": locale}, extra_query),
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
    """``client.public.openapi`` (7 operations)."""

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
    ) -> Iterator[Any]:
        """Iterate every item of ``languages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/sdk/languages",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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

    def spec(
        self,
        org_id: str,
        space_id: str,
        *,
        spec_id: Union[str, NotGiven] = NOT_GIVEN,
        format: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the spec in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/api-export/spec``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/api-export/spec",
            query=_query({"specId": spec_id, "format": format}, extra_query),
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
            items_key=None,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``resolve`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/relations",
            query=_query({"ids": ids, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )


class PublicRoadmapResource:
    """``client.public.roadmap`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def board(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        share: Union[str, NotGiven] = NOT_GIVEN,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        pinned: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        status: Union[str, NotGiven] = NOT_GIVEN,
        mine: Union[str, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapBoardResponse:
        """Get the roadmap in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap``

        :param limit: Items per LANE — not lanes.
        :param page: Which page of results to return, 1-based.
        :param pinned: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param featured: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        :param mine: Use true or false (true/1/yes/on and false/0/no/off are accepted).
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap",
            query=_query({"limit": limit, "cursor": cursor, "page": page, "share": share, "preview": preview, "pinned": pinned, "featured": featured, "sort": sort, "tag": tag, "status": status, "mine": mine, "q": q}, extra_query),
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
        preview: Union[str, NotGiven] = NOT_GIVEN,
        pinned: Union[str, NotGiven] = NOT_GIVEN,
        featured: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        status: Union[str, NotGiven] = NOT_GIVEN,
        mine: Union[str, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``board`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap",
            query=_query({"limit": limit, "page": page, "share": share, "preview": preview, "pinned": pinned, "featured": featured, "sort": sort, "tag": tag, "status": status, "mine": mine, "q": q}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def votes(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapVotesResponse:
        """Your votes on a roadmap

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap/votes``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/votes",
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
    ) -> Iterator[Any]:
        """Iterate every item of ``search`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/search",
            query=_query({"q": q, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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


class PublicRoadmapItemResource:
    """``client.public.roadmap_item`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def voters(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapItemVotersResponse:
        """List voters in a space (public reader roadmap t)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}/voters``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}/voters",
            query=_query({}, extra_query),
            headers=extra_headers,
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
    ) -> PublicRoadmapItemReactResponse:
        """Create the react in a space (public reader roadmap t posts)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}/posts/{postId}/react``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}/posts/{_path(post_id)}/react",
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
    ) -> PublicRoadmapItemReactorsResponse:
        """List reactions in a space (roadmap)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}/posts/{postId}/reactions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}/posts/{_path(post_id)}/reactions",
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
    ) -> Iterator[Any]:
        """Iterate every item of ``reactors`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}/posts/{_path(post_id)}/reactions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )


class PublicRoadmapLanesResource:
    """``client.public.roadmap_lanes`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def lanes(
        self,
        org_id: str,
        space_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapLanesLanesResponse:
        """List lanes in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap/lanes``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/lanes",
            query=_query({"share": share}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicRoadmapVoteResource:
    """``client.public.roadmap_vote`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def vote(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        importance: Union[float, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapVoteVoteResponse:
        """Create the vote in a space (public reader roadmap t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}/vote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}/vote",
            query=_query({}, extra_query),
            body=_body({"importance": importance}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicRoadmapWriteResource:
    """``client.public.roadmap_write`` (7 operations)."""

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
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        theme: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapWriteSubmitResponse:
        """Create an item in a space (public reader roadmap)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/roadmap/items``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/items",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "authorName": author_name, "captchaToken": captcha_token, "tags": tags, "theme": theme, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def comment(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        author_name: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        parent_post_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapWriteCommentResponse:
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
    ) -> PublicRoadmapWriteWatchResponse:
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

    def follow_item(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        following: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapWriteFollowItemResponse:
        """Follow the topic

        ``PUT /public/orgs/{orgId}/spaces/{spaceId}/roadmap/t/{slug}/follow``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/t/{_path(slug)}/follow",
            query=_query({}, extra_query),
            body=_body({"following": following}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def board_follow_state(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapWriteBoardFollowStateResponse:
        """Follow the roadmap

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/roadmap/follow``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/follow",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def follow_board(
        self,
        org_id: str,
        space_id: str,
        *,
        following: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapWriteFollowBoardResponse:
        """Follow the roadmap (replace)

        ``PUT /public/orgs/{orgId}/spaces/{spaceId}/roadmap/follow``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/follow",
            query=_query({}, extra_query),
            body=_body({"following": following}, extra_body),
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
        scope: Union[PublicRoadmapWriteSubscribeParamsScope, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicRoadmapWriteSubscribeResponse:
        """Subscribe the roadmap

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/roadmap/subscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/roadmap/subscribe",
            query=_query({}, extra_query),
            body=_body({"email": email, "captchaToken": captcha_token, "scope": scope}, extra_body),
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


class PublicSpaceAuthorsResource:
    """``client.public.space_authors`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def author_list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicSpaceAuthorsAuthorListResponse:
        """List authors in a space (public reader)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/authors``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/authors",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def author_list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``author_list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/authors",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def author(
        self,
        org_id: str,
        space_id: str,
        ref: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicSpaceAuthorsAuthorResponse:
        """Get the author

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/authors/{ref}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/authors/{_path(ref)}",
            query=_query({}, extra_query),
            headers=extra_headers,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/spaces",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    """``client.public.status`` (8 operations)."""

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
        scope: Union[PublicStatusSubscribeParamsScope, NotGiven] = NOT_GIVEN,
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
            body=_body({"email": email, "captchaToken": captcha_token, "scope": scope}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def board(
        self,
        org_id: str,
        space_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        preview: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"share": share, "preview": preview, "locale": locale}, extra_query),
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
        """A status badge (SVG)

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

    def atom(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Atom feed of the status

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/atom.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/atom.xml",
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
        """JSON feed of the status

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/feed.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/feed.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def maintenance_ics(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of maintenance

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/maintenance.ics``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/maintenance.ics",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicStatusAccessResource:
    """``client.public.status_access`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def facts(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusAccessFacts:
        """Whether a status page is gated

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/access``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/access",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def check(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicStatusAccessCheckResponse:
        """May this reader read a status page?

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/access/check``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/access/check",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicStatusAlertsResource:
    """``client.public.status_alerts`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def options(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusReaderAlertOptions:
        """Which alert channels a reader can subscribe with

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/alerts``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/alerts",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def options_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``options`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/alerts",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def start(
        self,
        org_id: str,
        space_id: str,
        *,
        kind: str,
        target: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        scope: Union[PublicStatusAlertsStartParamsScope, NotGiven] = NOT_GIVEN,
        captcha_token: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicStatusAlertsStartResponse:
        """Subscribe a Slack hook, webhook or phone to this status page

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/status/alerts``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/alerts",
            query=_query({}, extra_query),
            body=_body({"kind": kind, "target": target, "scope": scope, "captchaToken": captcha_token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def verify(
        self,
        org_id: str,
        space_id: str,
        alert_id: str,
        *,
        code: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicStatusAlertsVerifyResponse:
        """Confirm a reader alert with the code it was sent

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/status/alerts/{alertId}/verify``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/alerts/{_path(alert_id)}/verify",
            query=_query({}, extra_query),
            body=_body({"code": code}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unsubscribe(
        self,
        org_id: str,
        space_id: str,
        alert_id: str,
        *,
        token: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicStatusAlertsUnsubscribeResponse:
        """Stop a reader alert, with the token every delivery carries

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/status/alerts/{alertId}/unsubscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/alerts/{_path(alert_id)}/unsubscribe",
            query=_query({}, extra_query),
            body=_body({"token": token}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicStatusEmbedsResource:
    """``client.public.status_embeds`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def day(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusDayHours:
        """One component's day, in hourly buckets

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/day.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/day.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def latency(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusLatency:
        """A status page's response times

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/latency``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/latency",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def metric_series(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusMetricsAnswer:
        """A status page's custom metric series

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/metrics``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/metrics",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def widget_json(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> StatusWidgetAnswer:
        """What is happening on a status page right now

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/widget.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/widget.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def widget_js(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Get the widget JS in a space

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/widget.js``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/widget.js",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicStatusHooksResource:
    """``client.public.status_hooks`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def receive(
        self,
        token: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        body: Any = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Receive a Datadog or PagerDuty alert for a status page

        ``POST /public/status-hooks/{token}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/status-hooks/{_path(token)}",
            query=_query({}, extra_query),
            body=body,
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class PublicStatusIncidentsResource:
    """``client.public.status_incidents`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def archive(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> IncidentArchivePage:
        """A status page's incident archive

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/incidents``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def one(
        self,
        org_id: str,
        space_id: str,
        incident_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicStatusIncidentsOneResponse:
        """One incident on a status page

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/incidents/{incidentId}``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/incidents/{_path(incident_id)}",
            query=_query({"share": share, "locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicStatuspageResource:
    """``client.public.statuspage`` (8 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def summary(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> V2Summary:
        """Statuspage-compatible summary (API v2)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/api/v2/summary.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/api/v2/summary.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def status(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> V2StatusAnswer:
        """Statuspage-compatible overall status (API v2)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/api/v2/status.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/api/v2/status.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def components(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> V2ComponentsAnswer:
        """Statuspage-compatible components and groups (API v2)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/api/v2/components.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/api/v2/components.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def incidents(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> V2IncidentsAnswer:
        """Statuspage-compatible incidents (API v2)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/api/v2/incidents.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/api/v2/incidents.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def unresolved(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> V2IncidentsAnswer:
        """Statuspage-compatible unresolved incidents (API v2)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/api/v2/incidents/unresolved.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/api/v2/incidents/unresolved.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def maintenances(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> V2MaintenancesAnswer:
        """Statuspage-compatible scheduled maintenances (API v2)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/api/v2/scheduled-maintenances.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/api/v2/scheduled-maintenances.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def upcoming(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> V2MaintenancesAnswer:
        """Statuspage-compatible upcoming maintenance (API v2)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/api/v2/scheduled-maintenances/upcoming.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/api/v2/scheduled-maintenances/upcoming.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def active(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> V2MaintenancesAnswer:
        """Statuspage-compatible maintenance under way (API v2)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/api/v2/scheduled-maintenances/active.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/api/v2/scheduled-maintenances/active.json",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class PublicStatusSiblingsResource:
    """``client.public.status_siblings`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def siblings(
        self,
        org_id: str,
        space_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicStatusSiblingsSiblingsResponse:
        """A status page's sibling pages

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/status/siblings``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/siblings",
            query=_query({"share": share, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def siblings_all(
        self,
        org_id: str,
        space_id: str,
        *,
        share: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``siblings`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/status/siblings",
            query=_query({"share": share, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
        """Get the translation (public reader i18n)

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
    """``client.public`` (34 operations; blog, blog_media, blog_taxonomy, cards, careers, changelog, changelog_markdown, changelog_widget, consent, contact, course_catalog, course_commerce, courses, custom_emoji, domains, events, extension_registry, faq_follow, forms, forum, forum_account, forum_bookmark, forum_category, forum_profile, forum_search, growth, identity, interactions, legal, legal_gate, mcp, onebox, openapi, orgs, preview, reactions, reader_auth, reader_policy, relations, roadmap, roadmap_item, roadmap_lanes, roadmap_vote, roadmap_write, sites, space_authors, spaces, status, status_access, status_alerts, status_embeds, status_hooks, status_incidents, statuspage, status_siblings, theme_component_registry, theme_registry, translations, visitor_auth)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.blog = PublicBlogResource(client)
        self.blog_media = PublicBlogMediaResource(client)
        self.blog_taxonomy = PublicBlogTaxonomyResource(client)
        self.cards = PublicCardsResource(client)
        self.careers = PublicCareersResource(client)
        self.changelog = PublicChangelogResource(client)
        self.changelog_markdown = PublicChangelogMarkdownResource(client)
        self.changelog_widget = PublicChangelogWidgetResource(client)
        self.consent = PublicConsentResource(client)
        self.contact = PublicContactResource(client)
        self.course_catalog = PublicCourseCatalogResource(client)
        self.course_commerce = PublicCourseCommerceResource(client)
        self.courses = PublicCoursesResource(client)
        self.custom_emoji = PublicCustomEmojiResource(client)
        self.domains = PublicDomainsResource(client)
        self.events = PublicEventsResource(client)
        self.extension_registry = PublicExtensionRegistryResource(client)
        self.faq_follow = PublicFaqFollowResource(client)
        self.forms = PublicFormsResource(client)
        self.forum = PublicForumResource(client)
        self.forum_account = PublicForumAccountResource(client)
        self.forum_bookmark = PublicForumBookmarkResource(client)
        self.forum_category = PublicForumCategoryResource(client)
        self.forum_profile = PublicForumProfileResource(client)
        self.forum_search = PublicForumSearchResource(client)
        self.growth = PublicGrowthResource(client)
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
        self.roadmap_item = PublicRoadmapItemResource(client)
        self.roadmap_lanes = PublicRoadmapLanesResource(client)
        self.roadmap_vote = PublicRoadmapVoteResource(client)
        self.roadmap_write = PublicRoadmapWriteResource(client)
        self.sites = PublicSitesResource(client)
        self.space_authors = PublicSpaceAuthorsResource(client)
        self.spaces = PublicSpacesResource(client)
        self.status = PublicStatusResource(client)
        self.status_access = PublicStatusAccessResource(client)
        self.status_alerts = PublicStatusAlertsResource(client)
        self.status_embeds = PublicStatusEmbedsResource(client)
        self.status_hooks = PublicStatusHooksResource(client)
        self.status_incidents = PublicStatusIncidentsResource(client)
        self.statuspage = PublicStatuspageResource(client)
        self.status_siblings = PublicStatusSiblingsResource(client)
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
    ) -> ReaderGate:
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
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"share": share, "locale": locale}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def search(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        collections: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"limit": limit, "collections": collections, "q": q}, extra_query),
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
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"share": share, "locale": locale}, extra_query),
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
            items_key=None,
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
            items_key=None,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``updates`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/updates",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
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
    ) -> Iterator[Any]:
        """Iterate every item of ``tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/tags",
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
    ) -> Iterator[Any]:
        """Iterate every item of ``tag_pages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/tags/{_path(tag)}",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def page_markdown(
        self,
        org_id: str,
        space_id: str,
        page_id: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
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
            query=_query({"locale": locale, "form": form}, extra_query),
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
        """Create the view in a space (pages)

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

    def updates_rss_public_updates_rss(
        self,
        org_id: str,
        space_id: str,
        page_ref: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """A docs page's Updates block as an RSS feed

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/pages/{pageRef}/updates.rss``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/pages/{_path(page_ref)}/updates.rss",
            query=_query({"locale": locale}, extra_query),
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
        """A careers board's open roles as RSS (`?tag=` narrows to one team)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/careers/rss.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/rss.xml",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def atom(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """A careers board's open roles as Atom (`?tag=` narrows to one team)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/careers/atom.xml``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/atom.xml",
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
        """A careers board's open roles as JSON Feed (`?tag=` narrows to one team)

        ``GET /public/orgs/{orgId}/spaces/{spaceId}/careers/feed.json``
        """
        return self._client._request(
            "GET",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/feed.json",
            query=_query({}, extra_query),
            headers=extra_headers,
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
        scope: Union[PublicSubscribeParamsScope, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PublicSubscribeResponse:
        """Join a careers board’s talent community (email when a role opens)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/careers/subscribe``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/careers/subscribe",
            query=_query({}, extra_query),
            body=_body({"email": email, "captchaToken": captcha_token, "scope": scope}, extra_body),
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
