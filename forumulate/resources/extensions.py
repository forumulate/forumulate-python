from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ExtensionsApiResource:
    """``client.extensions.api`` (8 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def me(
        self,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsApiMeResponse:
        """The signed-in account, for an extension

        ``GET /ext/v1/me``
        """
        return self._client._request(
            "GET",
            f"/ext/v1/me",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def page(
        self,
        page_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsApiPageResponse:
        """Get the page (ext v1)

        ``GET /ext/v1/pages/{pageId}``
        """
        return self._client._request(
            "GET",
            f"/ext/v1/pages/{_path(page_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def space_pages(
        self,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsApiSpacePagesResponse:
        """List pages in a space (ext v1)

        ``GET /ext/v1/spaces/{spaceId}/pages``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/ext/v1/spaces/{_path(space_id)}/pages",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def space_pages_all(
        self,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ExtPageSummary]:
        """Iterate every item of ``space_pages`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/ext/v1/spaces/{_path(space_id)}/pages",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="pages",
        )

    def save_draft(
        self,
        page_id: str,
        *,
        title: str,
        content: Dict[str, Any],
        if_match: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsApiSaveDraftResponse:
        """List draft pages

        ``POST /ext/v1/pages/{pageId}/draft``

        :param if_match: The content tag you believe this resource is at: the `ETag` header where the matching read sets one, otherwise the `contentHash` that read returned.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/ext/v1/pages/{_path(page_id)}/draft",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content}, extra_body),
            headers={**_query({"If-Match": if_match, "Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def comments(
        self,
        page_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsApiCommentsResponse:
        """List comments

        ``GET /ext/v1/pages/{pageId}/comments``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/ext/v1/pages/{_path(page_id)}/comments",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def comments_all(
        self,
        page_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ExtComment]:
        """Iterate every item of ``comments`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/ext/v1/pages/{_path(page_id)}/comments",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="comments",
        )

    def post_comment(
        self,
        page_id: str,
        *,
        body: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        author_name: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsApiPostCommentResponse:
        """Create a comment

        ``POST /ext/v1/pages/{pageId}/comments``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/ext/v1/pages/{_path(page_id)}/comments",
            query=_query({}, extra_query),
            body=_body({"body": body, "authorName": author_name}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def members(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsApiMembersResponse:
        """List members

        ``GET /ext/v1/members``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/ext/v1/members",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def members_all(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ExtMember]:
        """Iterate every item of ``members`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/ext/v1/members",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="members",
        )

    def analytics(
        self,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsApiAnalyticsResponse:
        """List analytics in a space (ext v1)

        ``GET /ext/v1/spaces/{spaceId}/analytics``
        """
        return self._client._request(
            "GET",
            f"/ext/v1/spaces/{_path(space_id)}/analytics",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )


class ExtensionsRegistryResource:
    """``client.extensions.registry`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def publish(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRegistryPublishResponse:
        """Publish the extension

        ``POST /orgs/{orgId}/extensions/{id}/publish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}/publish",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unpublish(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRegistryUnpublishResponse:
        """Unpublish the extension

        ``POST /orgs/{orgId}/extensions/{id}/unpublish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}/unpublish",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def install(
        self,
        org_id: str,
        *,
        slug: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Install registry in an organization

        ``POST /orgs/{orgId}/extensions/install-registry``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/install-registry",
            query=_query({}, extra_query),
            body=_body({"slug": slug, "config": config}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def rate(
        self,
        org_id: str,
        *,
        slug: str,
        rating: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        review: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRegistryRateResponse:
        """Create the rate in an organization

        ``POST /orgs/{orgId}/extensions/rate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/rate",
            query=_query({}, extra_query),
            body=_body({"slug": slug, "rating": rating, "review": review}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def submit(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRegistrySubmitResponse:
        """Submit review in an organization

        ``POST /orgs/{orgId}/extensions/{id}/submit-review``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}/submit-review",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def pricing(
        self,
        org_id: str,
        id: str,
        *,
        pricing: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        price_cents: Union[int, NotGiven] = NOT_GIVEN,
        currency: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRegistryPricingResponse:
        """Create the pricing in an organization

        ``POST /orgs/{orgId}/extensions/{id}/pricing``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}/pricing",
            query=_query({}, extra_query),
            body=_body({"pricing": pricing, "priceCents": price_cents, "currency": currency}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def purchase(
        self,
        org_id: str,
        *,
        slug: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRegistryPurchaseResponse:
        """Create the purchase in an organization (extensions)

        ``POST /orgs/{orgId}/extensions/purchase``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/purchase",
            query=_query({}, extra_query),
            body=_body({"slug": slug}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ExtensionsRenderResource:
    """``client.extensions.render`` (4 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def render_block(
        self,
        org_id: str,
        *,
        extension: str,
        block: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        props: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        context: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRenderRenderBlockResponse:
        """Render the extension

        ``POST /orgs/{orgId}/extensions/render``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/render",
            query=_query({}, extra_query),
            body=_body({"extension": extension, "block": block, "props": props, "context": context}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def action(
        self,
        org_id: str,
        *,
        extension: str,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        block: Union[str, NotGiven] = NOT_GIVEN,
        props: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        inputs: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        context: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRenderActionResponse:
        """Create the action in an organization

        ``POST /orgs/{orgId}/extensions/action``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/action",
            query=_query({}, extra_query),
            body=_body({"extension": extension, "block": block, "action": action, "props": props, "inputs": inputs, "context": context}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def render_surface(
        self,
        org_id: str,
        *,
        extension: str,
        surface: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        context: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRenderRenderSurfaceResponse:
        """Create the surface in an organization

        ``POST /orgs/{orgId}/extensions/surface``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/surface",
            query=_query({}, extra_query),
            body=_body({"extension": extension, "surface": surface, "context": context}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def surface_action(
        self,
        org_id: str,
        *,
        extension: str,
        surface: str,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        inputs: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        context: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRenderSurfaceActionResponse:
        """Create the surface action in an organization

        ``POST /orgs/{orgId}/extensions/surface-action``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/surface-action",
            query=_query({}, extra_query),
            body=_body({"extension": extension, "surface": surface, "action": action, "inputs": inputs, "context": context}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ExtensionsResource:
    """``client.extensions`` (9 operations; api, registry, render)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.api = ExtensionsApiResource(client)
        self.registry = ExtensionsRegistryResource(client)
        self.render = ExtensionsRenderResource(client)

    def list(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsListResponse:
        """List extensions in an organization

        ``GET /orgs/{orgId}/extensions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/extensions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[InstalledExtensionSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/extensions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="installed",
        )

    def available(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsAvailableResponse:
        """Get the available in an organization

        ``GET /orgs/{orgId}/extensions/available``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/extensions/available",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def available_all(
        self,
        org_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[AvailableExtension]:
        """Iterate every item of ``available`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/extensions/available",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="available",
        )

    def install(
        self,
        org_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        manifest_url: Union[str, NotGiven] = NOT_GIVEN,
        manifest: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Install the extension

        ``POST /orgs/{orgId}/extensions/install``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/install",
            query=_query({}, extra_query),
            body=_body({"manifestUrl": manifest_url, "manifest": manifest, "config": config}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        events: Union[List[str], NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsUpdateResponse:
        """Update the extension

        ``PATCH /orgs/{orgId}/extensions/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"config": config, "events": events, "enabled": enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def uninstall(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsUninstallResponse:
        """Delete the extension

        ``DELETE /orgs/{orgId}/extensions/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def test(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsTestResponse:
        """Test the extension

        ``POST /orgs/{orgId}/extensions/{id}/test``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}/test",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def deliveries(
        self,
        org_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsDeliveriesResponse:
        """List deliveries in an organization (extensions)

        ``GET /orgs/{orgId}/extensions/{id}/deliveries``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}/deliveries",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def deliveries_all(
        self,
        org_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ExtensionDelivery]:
        """Iterate every item of ``deliveries`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}/deliveries",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="deliveries",
        )

    def rotate(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsRotateResponse:
        """Rotate the extension

        ``POST /orgs/{orgId}/extensions/{id}/rotate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}/rotate",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def upgrade(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ExtensionsUpgradeResponse:
        """Create the upgrade in an organization

        ``POST /orgs/{orgId}/extensions/{id}/upgrade``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/extensions/{_path(id)}/upgrade",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
