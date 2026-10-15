from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class BlogCommentsResource:
    """``client.blog_comments`` (9 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def vote(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogCommentsVoteResponse:
        """Create the vote in a space (blog posts)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/posts/{postId}/vote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}/vote",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def react(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        emoji: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogCommentsReactResponse:
        """Create the react in a space (blog posts)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/posts/{postId}/react``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}/react",
            query=_query({}, extra_query),
            body=_body({"emoji": emoji}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def edit_post(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[BlogCommentsEditPostParamsContent, NotGiven] = NOT_GIVEN,
        edit_reason: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogCommentsEditPostResponse:
        """Update the post (blog)

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/blog/posts/{postId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}",
            query=_query({}, extra_query),
            body=_body({"content": content, "editReason": edit_reason, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_post(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogCommentsDeletePostResponse:
        """Delete the post (blog)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/blog/posts/{postId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revisions(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogCommentsRevisionsResponse:
        """List revisions in a space (blog posts)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/posts/{postId}/revisions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}/revisions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def revisions_all(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``revisions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}/revisions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def revision_diff(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        revision: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogCommentsRevisionDiffResponse:
        """Get the revision (blog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/posts/{postId}/revisions/{revision}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}/revisions/{_path(revision)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def flag(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        reason: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        flag_type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogCommentsFlagResponse:
        """Flag the post (blog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/posts/{postId}/flag``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}/flag",
            query=_query({}, extra_query),
            body=_body({"reason": reason, "flagType": flag_type}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_post_status(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        status: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogCommentsSetPostStatusResponse:
        """Create the status in a space (blog posts)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/posts/{postId}/status``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}/status",
            query=_query({}, extra_query),
            body=_body({"status": status}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def recover_post(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogCommentsRecoverPostResponse:
        """Create the recover in a space (blog posts)

        ``POST /orgs/{orgId}/spaces/{spaceId}/blog/posts/{postId}/recover``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/posts/{_path(post_id)}/recover",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
