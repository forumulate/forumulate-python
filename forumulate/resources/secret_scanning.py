from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class SecretScanningResource:
    """``client.secret_scanning`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def github(
        self,
        *,
        token: str,
        type: str,
        github_public_key_identifier: Union[str, NotGiven] = NOT_GIVEN,
        github_public_key_signature: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        url: Union[str, NotGiven] = NOT_GIVEN,
        source: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> List[TokenFeedback]:
        """Receive a GitHub secret scanning report

        ``POST /secret-scanning/github``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/secret-scanning/github",
            query=_query({}, extra_query),
            body=_body({"token": token, "type": type, "url": url, "source": source}, extra_body),
            headers={**_query({"github-public-key-identifier": github_public_key_identifier, "github-public-key-signature": github_public_key_signature, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
