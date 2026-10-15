from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class BlogTaxonomyResource:
    """``client.blog_taxonomy`` (9 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list_tags(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogTaxonomyListTagsResponse:
        """Get the tag info in a space (blog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/tag-info``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tag-info",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_tags_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list_tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tag-info",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def set_tag(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        label: Union[Optional[str], NotGiven] = NOT_GIVEN,
        color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        text_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        color_dark: Union[Optional[str], NotGiven] = NOT_GIVEN,
        text_color_dark: Union[Optional[str], NotGiven] = NOT_GIVEN,
        gradient: Union[Optional[List[str]], NotGiven] = NOT_GIVEN,
        description: Union[Optional[str], NotGiven] = NOT_GIVEN,
        page_scheme: Union[Optional[str], NotGiven] = NOT_GIVEN,
        page_palette: Union[Optional[BlogTaxonomySetTagParamsPagePalette], NotGiven] = NOT_GIVEN,
        cover_url: Union[Any, NotGiven] = NOT_GIVEN,
        icon: Union[Optional[HeaderIconName], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogTaxonomySetTagResponse:
        """Replace the tag

        ``PUT /orgs/{orgId}/spaces/{spaceId}/blog/tags/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags/{_path(slug)}",
            query=_query({}, extra_query),
            body=_body({"label": label, "color": color, "textColor": text_color, "colorDark": color_dark, "textColorDark": text_color_dark, "gradient": gradient, "description": description, "pageScheme": page_scheme, "pagePalette": page_palette, "coverUrl": cover_url, "icon": icon}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def clear_tag(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogTaxonomyClearTagResponse:
        """Delete the tag

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/blog/tags/{slug}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags/{_path(slug)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_tag_page(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogTaxonomyGetTagPageResponse:
        """Get the page in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/tags/{slug}/page``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags/{_path(slug)}/page",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_tag_page(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        doc: BlogTaxonomySetTagPageParamsDoc,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        sidebar: Union[Optional[BlogTaxonomySetTagPageParamsSidebar], NotGiven] = NOT_GIVEN,
        aside: Union[Optional[BlogTaxonomySetTagPageParamsAside], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[BlogTaxonomySetTagPageParamsCustomization], NotGiven] = NOT_GIVEN,
        preset: Union[Optional[str], NotGiven] = NOT_GIVEN,
        hide_title: Union[Any, NotGiven] = NOT_GIVEN,
        width: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        gap: Union[Optional[str], NotGiven] = NOT_GIVEN,
        padding_top: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        padding_bottom: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogTaxonomySetTagPageResponse:
        """Replace the page in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/blog/tags/{slug}/page``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags/{_path(slug)}/page",
            query=_query({}, extra_query),
            body=_body({"doc": doc, "sidebar": sidebar, "aside": aside, "customization": customization, "preset": preset, "hideTitle": hide_title, "width": width, "gap": gap, "paddingTop": padding_top, "paddingBottom": padding_bottom}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_tag_page(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogTaxonomyRemoveTagPageResponse:
        """Delete the page in a space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/blog/tags/{slug}/page``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/tags/{_path(slug)}/page",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

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
    ) -> BlogTaxonomyListAuthorsResponse:
        """List authors in a space (blog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/blog/authors``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/authors",
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
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/authors",
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
        links: Union[List[BlogTaxonomyPutAuthorParamsLink], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> BlogTaxonomyPutAuthorResponse:
        """Replace the author (blog)

        ``PUT /orgs/{orgId}/spaces/{spaceId}/blog/authors/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/authors/{_path(key)}",
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
    ) -> BlogTaxonomyRemoveAuthorResponse:
        """Delete the author (blog)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/blog/authors/{key}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/blog/authors/{_path(key)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
