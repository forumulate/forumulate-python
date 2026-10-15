from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ReaderSignOutResource:
    """``client.reader_sign_out`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def sign_out(
        self,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        org_id: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        return_to: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ReaderSignOutSignOutResponse:
        """Sign a reader out on this host

        ``POST /public/reader/sign-out``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/reader/sign-out",
            query=_query({}, extra_query),
            body=_body({"orgId": org_id, "spaceId": space_id, "returnTo": return_to}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
