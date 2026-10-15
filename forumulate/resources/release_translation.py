from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ReleaseTranslationResource:
    """``client.release_translation`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReleaseTranslationListResponse:
        """List translations in a space (changelog)

        ``GET /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/translations``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/translations",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/translations",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        locale: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReleaseTranslationGetResponse:
        """Get the translation (spaces changelog translations)

        ``GET /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/translations/{locale}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/translations/{_path(locale)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def put(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        locale: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        excerpt: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        published: Union[bool, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReleaseTranslationPutResponse:
        """Replace the translation (changelog)

        ``PUT /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/translations/{locale}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/translations/{_path(locale)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "excerpt": excerpt, "content": content, "published": published, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        locale: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Delete the translation (changelog)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/translations/{locale}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/translations/{_path(locale)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def auto(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        locale: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        force: Union[bool, NotGiven] = NOT_GIVEN,
        published: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReleaseTranslationAutoResponse:
        """Create the auto in a space (changelog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/translations/{locale}/auto``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/translations/{_path(locale)}/auto",
            query=_query({}, extra_query),
            body=_body({"force": force, "published": published}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
