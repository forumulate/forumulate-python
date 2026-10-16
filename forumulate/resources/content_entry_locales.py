from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ContentEntryLocalesResource:
    """``client.content_entry_locales`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def read(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        fallback: Union[str, NotGiven] = NOT_GIVEN,
        draft: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Read an entry's fields in a locale

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/locales``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/locales",
            query=_query({"locale": locale, "fallback": fallback, "draft": draft}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def write(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        locale: str,
        *,
        fields: Dict[str, Any],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Write an entry's localized fields in a locale

        ``PUT /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/locales/{locale}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/locales/{_path(locale)}",
            query=_query({}, extra_query),
            body=_body({"fields": fields}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
