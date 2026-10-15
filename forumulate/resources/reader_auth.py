from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ReaderAuthResource:
    """``client.reader_auth`` (9 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get_org(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """The organization's reader sign-in registry

        ``GET /orgs/{orgId}/reader-auth``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/reader-auth",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_org(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        source_of_truth: Union[str, NotGiven] = NOT_GIVEN,
        providers: Union[List[ReaderAuthSetOrgParamsProvider], NotGiven] = NOT_GIVEN,
        approve_new_members: Union[bool, NotGiven] = NOT_GIVEN,
        hosted_signup: Union[bool, NotGiven] = NOT_GIVEN,
        sign_in_url: Union[str, NotGiven] = NOT_GIVEN,
        sign_out_url: Union[str, NotGiven] = NOT_GIVEN,
        outbound_sync: Union[ReaderAuthSetOrgParamsOutboundSync, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace the organization's reader sign-in registry

        ``PUT /orgs/{orgId}/reader-auth``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/reader-auth",
            query=_query({}, extra_query),
            body=_body({"sourceOfTruth": source_of_truth, "providers": providers, "approveNewMembers": approve_new_members, "hostedSignup": hosted_signup, "signInUrl": sign_in_url, "signOutUrl": sign_out_url, "outboundSync": outbound_sync}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def patch_org(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        source_of_truth: Union[Optional[str], NotGiven] = NOT_GIVEN,
        providers: Union[List[ReaderAuthPatchOrgParamsProvider], NotGiven] = NOT_GIVEN,
        approve_new_members: Union[Any, NotGiven] = NOT_GIVEN,
        hosted_signup: Union[Any, NotGiven] = NOT_GIVEN,
        sign_in_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        sign_out_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        outbound_sync: Union[Optional[ReaderAuthPatchOrgParamsOutboundSync], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderAuthPatchOrgResponse:
        """Change part of the organization's reader sign-in registry

        ``PATCH /orgs/{orgId}/reader-auth``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/reader-auth",
            query=_query({}, extra_query),
            body=_body({"sourceOfTruth": source_of_truth, "providers": providers, "approveNewMembers": approve_new_members, "hostedSignup": hosted_signup, "signInUrl": sign_in_url, "signOutUrl": sign_out_url, "outboundSync": outbound_sync}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def setup_org(
        self,
        org_id: str,
        *,
        method: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderAuthSetup:
        """Values to register at your IdP for ORG-WIDE reader sign-in

        ``GET /orgs/{orgId}/reader-auth/setup``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/reader-auth/setup",
            query=_query({"method": method}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def setup(
        self,
        org_id: str,
        space_id: str,
        *,
        method: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderAuthSetup:
        """Values to register at your IdP for one space

        ``GET /orgs/{orgId}/spaces/{spaceId}/reader-auth/setup``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-auth/setup",
            query=_query({"method": method}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get_space(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderAuthSpaceOverrideView:
        """One space's reader sign-in override

        ``GET /orgs/{orgId}/spaces/{spaceId}/reader-auth``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-auth",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_space(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        source_of_truth: Union[str, NotGiven] = NOT_GIVEN,
        providers: Union[List[ReaderAuthSetSpaceParamsProvider], NotGiven] = NOT_GIVEN,
        approve_new_members: Union[bool, NotGiven] = NOT_GIVEN,
        hosted_signup: Union[bool, NotGiven] = NOT_GIVEN,
        sign_in_url: Union[str, NotGiven] = NOT_GIVEN,
        sign_out_url: Union[str, NotGiven] = NOT_GIVEN,
        outbound_sync: Union[ReaderAuthSetSpaceParamsOutboundSync, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Replace one space's reader sign-in override

        ``PUT /orgs/{orgId}/spaces/{spaceId}/reader-auth``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-auth",
            query=_query({}, extra_query),
            body=_body({"sourceOfTruth": source_of_truth, "providers": providers, "approveNewMembers": approve_new_members, "hostedSignup": hosted_signup, "signInUrl": sign_in_url, "signOutUrl": sign_out_url, "outboundSync": outbound_sync}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def patch_space(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        source_of_truth: Union[Optional[str], NotGiven] = NOT_GIVEN,
        providers: Union[List[ReaderAuthPatchSpaceParamsProvider], NotGiven] = NOT_GIVEN,
        approve_new_members: Union[Any, NotGiven] = NOT_GIVEN,
        hosted_signup: Union[Any, NotGiven] = NOT_GIVEN,
        sign_in_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        sign_out_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        outbound_sync: Union[Optional[ReaderAuthPatchSpaceParamsOutboundSync], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Change part of one space's reader sign-in override

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/reader-auth``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-auth",
            query=_query({}, extra_query),
            body=_body({"sourceOfTruth": source_of_truth, "providers": providers, "approveNewMembers": approve_new_members, "hostedSignup": hosted_signup, "signInUrl": sign_in_url, "signOutUrl": sign_out_url, "outboundSync": outbound_sync}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_space(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderAuthDeleteSpaceResponse:
        """Remove one space's reader sign-in override

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/reader-auth``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/reader-auth",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
