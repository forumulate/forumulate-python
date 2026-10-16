from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ContentLocalesResource:
    """``client.content_locales`` (5 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryLocales:
        """List locales in an organization

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/locales``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/locales",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def add(
        self,
        org_id: str,
        library_id: str,
        *,
        code: Any,
        label: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a locale in an organization

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/locales``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/locales",
            query=_query({}, extra_query),
            body=_body({"code": code, "label": label}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def settings(
        self,
        org_id: str,
        library_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        source_locale: Union[Any, NotGiven] = NOT_GIVEN,
        locale_fallbacks: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update locales in an organization

        ``PATCH /orgs/{orgId}/content/libraries/{libraryId}/locales``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/locales",
            query=_query({}, extra_query),
            body=_body({"sourceLocale": source_locale, "localeFallbacks": locale_fallbacks}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def relabel(
        self,
        org_id: str,
        library_id: str,
        code: str,
        *,
        label: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update the locale (content libraries)

        ``PATCH /orgs/{orgId}/content/libraries/{libraryId}/locales/{code}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/locales/{_path(code)}",
            query=_query({}, extra_query),
            body=_body({"label": label}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        library_id: str,
        code: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> LibraryLocales:
        """Delete the locale (content libraries)

        ``DELETE /orgs/{orgId}/content/libraries/{libraryId}/locales/{code}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/locales/{_path(code)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
