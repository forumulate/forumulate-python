from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class BlogArticlesResource:
    """``client.blog.articles`` (16 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        author_id: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        state: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesListResponse:
        """Get the blog in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog``

        :param limit: Posts per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog",
            query=_query({"limit": limit, "tag": tag, "authorId": author_id, "cursor": cursor, "sort": sort, "state": state}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        author_id: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        state: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog",
            query=_query({"limit": limit, "tag": tag, "authorId": author_id, "sort": sort, "state": state}, extra_query),
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
        slug: Union[str, NotGiven] = NOT_GIVEN,
        published_at: Union[str, NotGiven] = NOT_GIVEN,
        byline: Union[Optional[BlogArticlesCreateParamsByline], NotGiven] = NOT_GIVEN,
        author: Union[Optional[str], NotGiven] = NOT_GIVEN,
        bylines: Union[Optional[List[BlogArticlesCreateParamsByline2]], NotGiven] = NOT_GIVEN,
        subtitle: Union[Optional[str], NotGiven] = NOT_GIVEN,
        content: Union[BlogArticlesCreateParamsContent, NotGiven] = NOT_GIVEN,
        sections: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        excerpt: Union[str, NotGiven] = NOT_GIVEN,
        cover_url: Union[Any, NotGiven] = NOT_GIVEN,
        cover_alt: Union[Optional[str], NotGiven] = NOT_GIVEN,
        series: Union[Optional[str], NotGiven] = NOT_GIVEN,
        social_image_url: Union[Any, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        seo: Union[BlogArticlesCreateParamsSeo, NotGiven] = NOT_GIVEN,
        further_reading: Union[List[BlogArticlesCreateParamsFurtherReadingItem], NotGiven] = NOT_GIVEN,
        comments_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        on_this_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[BlogArticlesCreateParamsCustomization], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesCreateResponse:
        """Create the blog in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog",
            query=_query({}, extra_query),
            body=_body({"title": title, "slug": slug, "publishedAt": published_at, "byline": byline, "author": author, "bylines": bylines, "subtitle": subtitle, "content": content, "sections": sections, "excerpt": excerpt, "coverUrl": cover_url, "coverAlt": cover_alt, "series": series, "socialImageUrl": social_image_url, "tags": tags, "seo": seo, "furtherReading": further_reading, "commentsEnabled": comments_enabled, "onThisPage": on_this_page, "customization": customization, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesGetResponse:
        """Get the blog

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        published_at: Union[str, NotGiven] = NOT_GIVEN,
        byline: Union[Optional[BlogArticlesUpdateParamsByline], NotGiven] = NOT_GIVEN,
        author: Union[Optional[str], NotGiven] = NOT_GIVEN,
        bylines: Union[Optional[List[BlogArticlesUpdateParamsByline2]], NotGiven] = NOT_GIVEN,
        subtitle: Union[Optional[str], NotGiven] = NOT_GIVEN,
        content: Union[BlogArticlesUpdateParamsContent, NotGiven] = NOT_GIVEN,
        sections: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        excerpt: Union[str, NotGiven] = NOT_GIVEN,
        cover_url: Union[Any, NotGiven] = NOT_GIVEN,
        cover_alt: Union[Optional[str], NotGiven] = NOT_GIVEN,
        series: Union[Optional[str], NotGiven] = NOT_GIVEN,
        social_image_url: Union[Any, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        seo: Union[BlogArticlesUpdateParamsSeo, NotGiven] = NOT_GIVEN,
        further_reading: Union[List[BlogArticlesUpdateParamsFurtherReadingItem], NotGiven] = NOT_GIVEN,
        comments_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        on_this_page: Union[Optional[str], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[BlogArticlesUpdateParamsCustomization], NotGiven] = NOT_GIVEN,
        edit_reason: Union[str, NotGiven] = NOT_GIVEN,
        pinned: Union[bool, NotGiven] = NOT_GIVEN,
        featured: Union[bool, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesUpdateResponse:
        """Update the blog

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "slug": slug, "publishedAt": published_at, "byline": byline, "author": author, "bylines": bylines, "subtitle": subtitle, "content": content, "sections": sections, "excerpt": excerpt, "coverUrl": cover_url, "coverAlt": cover_alt, "series": series, "socialImageUrl": social_image_url, "tags": tags, "seo": seo, "furtherReading": further_reading, "commentsEnabled": comments_enabled, "onThisPage": on_this_page, "customization": customization, "editReason": edit_reason, "pinned": pinned, "featured": featured, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesRemoveResponse:
        """Delete the blog

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def slug_history(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesSlugHistoryResponse:
        """Get the history in a space (blog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/slug/history``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/slug/history",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def slug_history_all(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``slug_history`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/slug/history",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def schedule(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        publish_at: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesScheduleResponse:
        """Create the schedule in a space (blog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/schedule``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/schedule",
            query=_query({}, extra_query),
            body=_body({"publishAt": publish_at}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unschedule(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesUnscheduleResponse:
        """Delete the schedule in a space (blog)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/schedule``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/schedule",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_authors(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        user_ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesSetAuthorsResponse:
        """Create an author in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/authors``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/authors",
            query=_query({}, extra_query),
            body=_body({"userIds": user_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_comments(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        enabled: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesSetCommentsResponse:
        """Create a comment in a space (blog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/comments``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/comments",
            query=_query({}, extra_query),
            body=_body({"enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def publish(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        notify: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesPublishResponse:
        """Publish the blog

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/publish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/publish",
            query=_query({}, extra_query),
            body=_body({"notify": notify}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_state(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        state: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesSetStateResponse:
        """Create the state in a space (blog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/state``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/state",
            query=_query({}, extra_query),
            body=_body({"state": state}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def pin(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        pinned: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesPinResponse:
        """Pin the blog

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/pin``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/pin",
            query=_query({}, extra_query),
            body=_body({"pinned": pinned}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reply(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[BlogArticlesReplyParamsContent, NotGiven] = NOT_GIVEN,
        parent_post_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesReplyResponse:
        """Create a reply in a space (blog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/replies``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/replies",
            query=_query({}, extra_query),
            body=_body({"content": content, "parentPostId": parent_post_id, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bookmark(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesBookmarkResponse:
        """Create the bookmark in a space (blog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/bookmark``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/bookmark",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def recover_article(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogArticlesRecoverArticleResponse:
        """Create the recover in a space (blog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/{topicId}/recover``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/{_path(topic_id)}/recover",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class BlogModerationResource:
    """``client.blog.moderation`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def flags(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogModerationFlagsResponse:
        """List flags in a space (blog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/flags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/flags",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def flags_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``flags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/flags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def review_flag(
        self,
        org_id: str,
        space_id: str,
        flag_id: str,
        *,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogModerationReviewFlagResponse:
        """Create the review in a space (blog flags)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/flags/{flagId}/review``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/flags/{_path(flag_id)}/review",
            query=_query({}, extra_query),
            body=_body({"action": action}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def resolve_flag(
        self,
        org_id: str,
        space_id: str,
        flag_id: str,
        *,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogModerationResolveFlagResponse:
        """Resolve the flag (blog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/flags/{flagId}/resolve``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/flags/{_path(flag_id)}/resolve",
            query=_query({}, extra_query),
            body=_body({"action": action}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class BlogNewsletterResource:
    """``client.blog.newsletter`` (6 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def subscribers(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogNewsletterSubscribersResponse:
        """List subscribers in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/subscribers``

        :param limit: Subscribers per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/subscribers",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def subscribers_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``subscribers`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/subscribers",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def subscribers_csv(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """File of subscribers

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/subscribers.csv``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/subscribers.csv",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def broadcasts(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogNewsletterBroadcastsResponse:
        """List broadcasts in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/broadcasts``

        :param limit: Broadcasts per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/broadcasts",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def broadcasts_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``broadcasts`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/broadcasts",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def send_broadcast(
        self,
        org_id: str,
        space_id: str,
        *,
        subject: str,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        segment: Union[BlogNewsletterSendBroadcastParamsSegment, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogNewsletterSendBroadcastResponse:
        """Create a broadcast in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/broadcasts``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/broadcasts",
            query=_query({}, extra_query),
            body=_body({"subject": subject, "body": body, "segment": segment}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_subscriber_tags(
        self,
        org_id: str,
        space_id: str,
        subscriber_id: str,
        *,
        tags: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogNewsletterSetSubscriberTagsResponse:
        """Replace tags in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/blog/subscribers/{subscriberId}/tags``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/subscribers/{_path(subscriber_id)}/tags",
            query=_query({}, extra_query),
            body=_body({"tags": tags}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def subscriber_tags(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogNewsletterSubscriberTagsResponse:
        """List subscriber tags in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/subscriber-tags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/subscriber-tags",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def subscriber_tags_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``subscriber_tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/subscriber-tags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )


class BlogResource:
    """``client.blog`` (5 operations; articles, moderation, newsletter)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.articles = BlogArticlesResource(client)
        self.moderation = BlogModerationResource(client)
        self.newsletter = BlogNewsletterResource(client)

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
    ) -> BlogTagsResponse:
        """List tags in a space (blog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/tags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags",
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
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogSearchResponse:
        """Get the search in a space (blog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/search``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/search",
            query=_query({"q": q}, extra_query),
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
    ) -> BlogBookmarksResponse:
        """List bookmarks in a space (blog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/bookmarks``

        :param limit: Bookmarks per page, once a version is stated.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/bookmarks",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/bookmarks",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def get_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogGetSettingsResponse:
        """List settings in a space (blog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/settings``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/settings",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        who_can_post: Union[Optional[str], NotGiven] = NOT_GIVEN,
        moderate_comments: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        moderate_anonymous: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        allow_anonymous: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        anonymous_captcha: Union[Optional[str], NotGiven] = NOT_GIVEN,
        default_sort: Union[Optional[str], NotGiven] = NOT_GIVEN,
        reactions_enabled: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        default_byline: Union[Optional[str], NotGiven] = NOT_GIVEN,
        reaction_emojis: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogUpdateSettingsResponse:
        """Update settings in a space (blog)

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/blog/settings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/settings",
            query=_query({}, extra_query),
            body=_body({"whoCanPost": who_can_post, "moderateComments": moderate_comments, "moderateAnonymous": moderate_anonymous, "allowAnonymous": allow_anonymous, "anonymousCaptcha": anonymous_captcha, "defaultSort": default_sort, "reactionsEnabled": reactions_enabled, "defaultByline": default_byline, "reactionEmojis": reaction_emojis}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
