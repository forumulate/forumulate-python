from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class OrgLanguageSwitcherResource:
    """``client.org_language_switcher`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def get(
        self,
        org_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgLanguageSwitcherGetResponse:
        """Get the language switcher in an organization

        ``GET /orgs/{orgId}/language-switcher``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/language-switcher",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        placement: Union[str, NotGiven] = NOT_GIVEN,
        style: Union[str, NotGiven] = NOT_GIVEN,
        names: Union[str, NotGiven] = NOT_GIVEN,
        flags: Union[bool, NotGiven] = NOT_GIVEN,
        flag_countries: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        locales: Union[List[str], NotGiven] = NOT_GIVEN,
        custom_labels: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        missing: Union[str, NotGiven] = NOT_GIVEN,
        remember: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> OrgLanguageSwitcherSetResponse:
        """Replace the language switcher in an organization

        ``PUT /orgs/{orgId}/language-switcher``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/language-switcher",
            query=_query({}, extra_query),
            body=_body({"enabled": enabled, "placement": placement, "style": style, "names": names, "flags": flags, "flagCountries": flag_countries, "locales": locales, "customLabels": custom_labels, "missing": missing, "remember": remember}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
