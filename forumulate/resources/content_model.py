from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ContentModelResource:
    """``client.content_model`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentModelGetResponse:
        """Get the model in an organization

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/model``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/model",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def put(
        self,
        org_id: str,
        library_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        shape: Union[ContentModelPutParamsShape, NotGiven] = NOT_GIVEN,
        types: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        ops: Union[List[ContentModelPutParamsOp], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentModelPutResponse:
        """Replace the library's content model

        ``PUT /orgs/{orgId}/content/libraries/{libraryId}/model``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/model",
            query=_query({}, extra_query),
            body=_body({"shape": shape, "types": types, "ops": ops}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def versions(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentModelVersionsResponse:
        """List versions in an organization (content libraries model)

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/model/versions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/model/versions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def versions_all(
        self,
        org_id: str,
        library_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``versions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/model/versions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )
