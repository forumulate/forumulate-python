from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ModelIoResource:
    """``client.model_io`` (3 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def export(
        self,
        org_id: str,
        library_id: str,
        *,
        format: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ContentModelExport:
        """Download the content model as a file

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/model/export``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/model/export",
            query=_query({"format": format}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def import_(
        self,
        org_id: str,
        library_id: str,
        *,
        format: str,
        content: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        dry_run: Union[bool, NotGiven] = NOT_GIVEN,
        base_version: Union[int, NotGiven] = NOT_GIVEN,
        force: Union[bool, NotGiven] = NOT_GIVEN,
        ops: Union[List[ModelIoImportParamsOp], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Push a content model file (diff, dry run, apply)

        ``POST /orgs/{orgId}/content/libraries/{libraryId}/model/import``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/model/import",
            query=_query({}, extra_query),
            body=_body({"format": format, "content": content, "dryRun": dry_run, "baseVersion": base_version, "force": force, "ops": ops}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def schema(
        self,
        org_id: str,
        library_id: str,
        *,
        audience: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """The library's delivery JSON Schema

        ``GET /orgs/{orgId}/content/libraries/{libraryId}/model/schema.json``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/content/libraries/{_path(library_id)}/model/schema.json",
            query=_query({"audience": audience}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )
