from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ContentAiResource:
    """``client.content_ai`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def status(
        self,
        org_id: str,
        library_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AiContentStatus:
        """Whether AI for content is available

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/ai/status``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/ai/status",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def translate(
        self,
        org_id: str,
        library_id: str,
        *,
        entry_ids: List[str],
        locale: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Translate entries with the organization’s AI provider

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/ai/translate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/ai/translate",
            query=_query({}, extra_query),
            body=_body({"entryIds": entry_ids, "locale": locale}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def seo(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        locale: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Suggest an SEO title and description

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/ai/seo``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/ai/seo",
            query=_query({}, extra_query),
            body=_body({"locale": locale}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def draft(
        self,
        org_id: str,
        library_id: str,
        entry_id: str,
        *,
        field_key: str,
        brief: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Draft a blocks field from a brief

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/entries/{entryId}/ai/draft``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/entries/{_path(entry_id)}/ai/draft",
            query=_query({}, extra_query),
            body=_body({"fieldKey": field_key, "brief": brief}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
