from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ContactBlockResource:
    """``client.contact_block`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def submit(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        body: Any = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContactBlockSubmitResponse:
        """Create a submission in a space

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/contact/submissions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/contact/submissions",
            query=_query({}, extra_query),
            body=body,
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
