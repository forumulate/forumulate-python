from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ReleaseReviewResource:
    """``client.release_review`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def request(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        note: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReleaseReviewRequestResponse:
        """Create the review in a space (changelog)

        ``POST /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/review``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/review",
            query=_query({}, extra_query),
            body=_body({"note": note}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def withdraw(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReleaseReviewWithdrawResponse:
        """Delete the review in a space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/review``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/review",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def approve(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        note: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReleaseReviewApproveResponse:
        """Approve the review

        ``POST /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/review/approve``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/review/approve",
            query=_query({}, extra_query),
            body=_body({"note": note}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def request_changes(
        self,
        org_id: str,
        space_id: str,
        release_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        note: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReleaseReviewRequestChangesResponse:
        """Create a request change in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/changelog/{releaseId}/review/request-changes``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/{_path(release_id)}/review/request-changes",
            query=_query({}, extra_query),
            body=_body({"note": note}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
