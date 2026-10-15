from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SiteFrontPageResource:
    """``client.site_front_page`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        site_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SiteFrontPageGetResponse:
        """Get the front page in an organization

        ``GET /orgs/{orgId}/sites/{siteId}/front-page``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/front-page",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        site_id: str,
        *,
        doc: SiteFrontPageSetParamsDoc,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        sidebar: Union[Optional[SiteFrontPageSetParamsSidebar], NotGiven] = NOT_GIVEN,
        aside: Union[Optional[SiteFrontPageSetParamsAside], NotGiven] = NOT_GIVEN,
        customization: Union[Optional[SiteFrontPageSetParamsCustomization], NotGiven] = NOT_GIVEN,
        preset: Union[Optional[str], NotGiven] = NOT_GIVEN,
        hide_title: Union[Any, NotGiven] = NOT_GIVEN,
        width: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        gap: Union[Optional[str], NotGiven] = NOT_GIVEN,
        padding_top: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        padding_bottom: Union[Optional[Any], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        body: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SiteFrontPageSetResponse:
        """Replace the front page in an organization

        ``PUT /orgs/{orgId}/sites/{siteId}/front-page``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/front-page",
            query=_query({}, extra_query),
            body=_body({"doc": doc, "sidebar": sidebar, "aside": aside, "customization": customization, "preset": preset, "hideTitle": hide_title, "width": width, "gap": gap, "paddingTop": padding_top, "paddingBottom": padding_bottom, "markdown": markdown, "body": body}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        site_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> SiteFrontPageRemoveResponse:
        """Delete the front page in an organization

        ``DELETE /orgs/{orgId}/sites/{siteId}/front-page``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/sites/{_path(site_id)}/front-page",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
