from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ReaderImageSignResource:
    """``client.reader_image_sign`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def sign(
        self,
        org_id: str,
        *,
        urls: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderImageSignSignResponse:
        """Sign external image addresses for the live reader

        ``POST /public/orgs/{orgId}/me/images/sign``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/me/images/sign",
            query=_query({}, extra_query),
            body=_body({"urls": urls}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
