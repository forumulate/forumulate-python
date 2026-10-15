from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class OrgImportJobResource:
    """``client.org_import_job`` (4 operations)."""

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
    ) -> OrgImportJobListResponse:
        """List imports in an organization

        ``GET /orgs/{orgId}/imports``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/imports",
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
            f"/orgs/{_path(org_id)}/imports",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def enqueue(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        format: Union[str, NotGiven] = NOT_GIVEN,
        version: Union[int, NotGiven] = NOT_GIVEN,
        exported_at: Union[str, NotGiven] = NOT_GIVEN,
        organization: Union[Any, NotGiven] = NOT_GIVEN,
        members: Union[List[OrgImportJobEnqueueParamsMember], NotGiven] = NOT_GIVEN,
        spaces: Union[List[OrgImportJobEnqueueParamsSpace], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Queue an import of an export document

        ``POST /orgs/{orgId}/imports``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/imports",
            query=_query({}, extra_query),
            body=_body({"format": format, "version": version, "exportedAt": exported_at, "organization": organization, "members": members, "spaces": spaces}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def enqueue_roadmap(
        self,
        org_id: str,
        *,
        source: str,
        data: Any,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space: Union[OrgImportJobEnqueueRoadmapParamsSpace, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Queue a Canny or Featurebase roadmap import

        ``POST /orgs/{orgId}/imports/roadmap``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/imports/roadmap",
            query=_query({}, extra_query),
            body=_body({"source": source, "data": data, "space": space}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        job_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgImportJobGetResponse:
        """Get the import

        ``GET /orgs/{orgId}/imports/{jobId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/imports/{_path(job_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
