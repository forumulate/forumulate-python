from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SpaceAuthorsResource:
    """``client.space_authors`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list_authors(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceAuthorsListAuthorsResponse:
        """List authors in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/authors``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/authors",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_authors_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_authors`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/authors",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def put_author(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        role: Union[Optional[str], NotGiven] = NOT_GIVEN,
        bio: Union[Optional[str], NotGiven] = NOT_GIVEN,
        avatar_url: Union[Any, NotGiven] = NOT_GIVEN,
        url: Union[Any, NotGiven] = NOT_GIVEN,
        handle: Union[Any, NotGiven] = NOT_GIVEN,
        links: Union[List[SpaceAuthorsPutAuthorParamsLink], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceAuthorsPutAuthorResponse:
        """Replace the author

        ``PUT /orgs/{orgId}/spaces/{spaceId}/authors/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/authors/{_path(key)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "role": role, "bio": bio, "avatarUrl": avatar_url, "url": url, "handle": handle, "links": links}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_author(
        self,
        org_id: str,
        space_id: str,
        key: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SpaceAuthorsRemoveAuthorResponse:
        """Delete the author

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/authors/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/authors/{_path(key)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
