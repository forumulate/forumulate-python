from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ChangelogImportResource:
    """``client.changelog_import`` (1 operation)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def import_(
        self,
        org_id: str,
        space_id: str,
        *,
        source: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        publish: Union[bool, NotGiven] = NOT_GIVEN,
        dry_run: Union[bool, NotGiven] = NOT_GIVEN,
        repo: Union[str, NotGiven] = NOT_GIVEN,
        token: Union[str, NotGiven] = NOT_GIVEN,
        include_prereleases: Union[bool, NotGiven] = NOT_GIVEN,
        data: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Import the changelog

        ``POST /orgs/{orgId}/spaces/{spaceId}/changelog/import``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/changelog/import",
            query=_query({}, extra_query),
            body=_body({"source": source, "markdown": markdown, "publish": publish, "dryRun": dry_run, "repo": repo, "token": token, "includePrereleases": include_prereleases, "data": data}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
