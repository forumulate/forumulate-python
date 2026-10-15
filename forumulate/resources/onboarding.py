from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class OnboardingResource:
    """``client.onboarding`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def surfaces(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OnboardingSurfacesResponse:
        """List surfaces

        ``GET /onboarding/surfaces``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/onboarding/surfaces",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def surfaces_all(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[Any]:
        """Iterate every item of ``surfaces`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/onboarding/surfaces",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key=None,
        )

    def availability(
        self,
        *,
        subdomain: Union[str, NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Availability:
        """Get the availability

        ``GET /onboarding/availability``
        """
        return self._client._request(
            "GET",
            f"/onboarding/availability",
            query=_query({"subdomain": subdomain, "slug": slug}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def provision(
        self,
        *,
        org_name: str,
        slug: str,
        surfaces: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        subdomain: Union[str, NotGiven] = NOT_GIVEN,
        legal: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the onboarding

        ``POST /onboarding``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/onboarding",
            query=_query({}, extra_query),
            body=_body({"orgName": org_name, "slug": slug, "subdomain": subdomain, "surfaces": surfaces, "legal": legal}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
