from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator, List, Mapping, Optional, Union

from .._core import NOT_GIVEN, NotGiven, _body, _path, _query

if TYPE_CHECKING:
    from .._core import BaseClient
    from ..types import *  # noqa: F401,F403


class ForumAutomationsResource:
    """``client.forum.automations`` (7 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        *,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumAutomationsListResponse:
        """List forum automations in an organization

        ``GET /orgs/{orgId}/forum-automations``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/forum-automations",
            query=_query({"spaceId": space_id, "limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        *,
        space_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[AutomationSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/forum-automations",
            query=_query({"spaceId": space_id, "limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="automations",
        )

    def create(
        self,
        org_id: str,
        *,
        name: str,
        trigger: str,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        conditions: Union[List[ForumAutomationsCreateParamsCondition], NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create a forum automation in an organization

        ``POST /orgs/{orgId}/forum-automations``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/forum-automations",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "name": name, "enabled": enabled, "trigger": trigger, "conditions": conditions, "action": action, "config": config}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> AutomationEnvelope:
        """Get the forum automation

        ``GET /orgs/{orgId}/forum-automations/{id}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/forum-automations/{_path(id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        space_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, NotGiven] = NOT_GIVEN,
        trigger: Union[str, NotGiven] = NOT_GIVEN,
        conditions: Union[List[ForumAutomationsUpdateParamsCondition], NotGiven] = NOT_GIVEN,
        action: Union[str, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Update the forum automation

        ``PATCH /orgs/{orgId}/forum-automations/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/forum-automations/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"spaceId": space_id, "name": name, "enabled": enabled, "trigger": trigger, "conditions": conditions, "action": action, "config": config}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumAutomationsRemoveResponse:
        """Delete the forum automation

        ``DELETE /orgs/{orgId}/forum-automations/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/forum-automations/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def runs(
        self,
        org_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumAutomationsRunsResponse:
        """List runs in an organization

        ``GET /orgs/{orgId}/forum-automations/{id}/runs``

        :param limit: Runs listed, newest first.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/forum-automations/{_path(id)}/runs",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def runs_all(
        self,
        org_id: str,
        id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[AutomationRunSummary]:
        """Iterate every item of ``runs`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/forum-automations/{_path(id)}/runs",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="runs",
        )

    def invoke(
        self,
        org_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        payload: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Create the invoke in an organization

        ``POST /orgs/{orgId}/forum-automations/{id}/invoke``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/forum-automations/{_path(id)}/invoke",
            query=_query({}, extra_query),
            body=_body({"payload": payload}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ForumTaxonomyResource:
    """``client.forum.taxonomy`` (28 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list_categories(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyListCategoriesResponse:
        """List categories in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/categories``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_categories_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CategorySummary]:
        """Iterate every item of ``list_categories`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="categories",
        )

    def create_category(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        sort_order: Union[int, NotGiven] = NOT_GIVEN,
        default_notification_level: Union[str, NotGiven] = NOT_GIVEN,
        topic_template: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        minimum_required_tags: Union[int, NotGiven] = NOT_GIVEN,
        default_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        allowed_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        default_sort: Union[Optional[str], NotGiven] = NOT_GIVEN,
        logo_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        background_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        num_featured_topics: Union[Optional[int], NotGiven] = NOT_GIVEN,
        show_subcategory_list: Union[bool, NotGiven] = NOT_GIVEN,
        auto_close_hours: Union[Optional[int], NotGiven] = NOT_GIVEN,
        default_slow_mode_seconds: Union[Optional[int], NotGiven] = NOT_GIVEN,
        required_tag_groups: Union[List[ForumTaxonomyCreateCategoryParamsRequiredTagGroup], NotGiven] = NOT_GIVEN,
        navigate_to_first_post: Union[Any, NotGiven] = NOT_GIVEN,
        default_list_filter: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyCreateCategoryResponse:
        """Create a category in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/categories``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories",
            query=_query({}, extra_query),
            body=_body({"name": name, "description": description, "color": color, "parentId": parent_id, "sortOrder": sort_order, "defaultNotificationLevel": default_notification_level, "topicTemplate": topic_template, "minimumRequiredTags": minimum_required_tags, "defaultTags": default_tags, "allowedTags": allowed_tags, "defaultSort": default_sort, "logoUrl": logo_url, "backgroundUrl": background_url, "numFeaturedTopics": num_featured_topics, "showSubcategoryList": show_subcategory_list, "autoCloseHours": auto_close_hours, "defaultSlowModeSeconds": default_slow_mode_seconds, "requiredTagGroups": required_tag_groups, "navigateToFirstPost": navigate_to_first_post, "defaultListFilter": default_list_filter}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reorder_categories(
        self,
        org_id: str,
        space_id: str,
        *,
        ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyReorderCategoriesResponse:
        """Reorder the category

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/categories/reorder``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/reorder",
            query=_query({}, extra_query),
            body=_body({"ids": ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_category(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        parent_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        sort_order: Union[int, NotGiven] = NOT_GIVEN,
        default_notification_level: Union[str, NotGiven] = NOT_GIVEN,
        topic_template: Union[Optional[Dict[str, Any]], NotGiven] = NOT_GIVEN,
        minimum_required_tags: Union[int, NotGiven] = NOT_GIVEN,
        default_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        allowed_tags: Union[List[str], NotGiven] = NOT_GIVEN,
        default_sort: Union[Optional[str], NotGiven] = NOT_GIVEN,
        logo_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        background_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        num_featured_topics: Union[Optional[int], NotGiven] = NOT_GIVEN,
        show_subcategory_list: Union[bool, NotGiven] = NOT_GIVEN,
        auto_close_hours: Union[Optional[int], NotGiven] = NOT_GIVEN,
        default_slow_mode_seconds: Union[Optional[int], NotGiven] = NOT_GIVEN,
        required_tag_groups: Union[List[ForumTaxonomyUpdateCategoryParamsRequiredTagGroup], NotGiven] = NOT_GIVEN,
        navigate_to_first_post: Union[Any, NotGiven] = NOT_GIVEN,
        default_list_filter: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyUpdateCategoryResponse:
        """Update the category

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/forum/categories/{categoryId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "description": description, "color": color, "parentId": parent_id, "sortOrder": sort_order, "defaultNotificationLevel": default_notification_level, "topicTemplate": topic_template, "minimumRequiredTags": minimum_required_tags, "defaultTags": default_tags, "allowedTags": allowed_tags, "defaultSort": default_sort, "logoUrl": logo_url, "backgroundUrl": background_url, "numFeaturedTopics": num_featured_topics, "showSubcategoryList": show_subcategory_list, "autoCloseHours": auto_close_hours, "defaultSlowModeSeconds": default_slow_mode_seconds, "requiredTagGroups": required_tag_groups, "navigateToFirstPost": navigate_to_first_post, "defaultListFilter": default_list_filter}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_category(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        *,
        force: Union[bool, NotGiven] = NOT_GIVEN,
        move_to: Union[str, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyRemoveCategoryResponse:
        """Delete the category

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/categories/{categoryId}``

        :param force: Delete a category that still holds topics and leave those topics uncategorised.
        :param move_to: Re-file this category's topics under this category (which must be in the same space) before deleting it.
        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}",
            query=_query({"force": force, "moveTo": move_to}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def email_in(
        self,
        org_id: str,
        space_id: str,
        *,
        category_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyEmailInResponse:
        """The inbound email address for a forum space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/email-in``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/email-in",
            query=_query({"categoryId": category_id}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_shared_drafts(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyListSharedDraftsResponse:
        """List shared drafts in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/shared-drafts``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/shared-drafts",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_shared_drafts_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[SharedDraftSummary]:
        """Iterate every item of ``list_shared_drafts`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/shared-drafts",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="drafts",
        )

    def create_shared_draft(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ForumTaxonomyCreateSharedDraftParamsContent, NotGiven] = NOT_GIVEN,
        category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyCreateSharedDraftResponse:
        """Create a shared draft in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/shared-drafts``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/shared-drafts",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "categoryId": category_id, "tags": tags, "kind": kind, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_shared_draft(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ForumTaxonomyUpdateSharedDraftParamsContent, NotGiven] = NOT_GIVEN,
        category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyUpdateSharedDraftResponse:
        """Update the shared draft

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/forum/shared-drafts/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/shared-drafts/{_path(id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "categoryId": category_id, "tags": tags, "kind": kind, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_shared_draft(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyRemoveSharedDraftResponse:
        """Delete the shared draft

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/shared-drafts/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/shared-drafts/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def publish_shared_draft(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyPublishSharedDraftResponse:
        """Publish the shared draft

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/shared-drafts/{id}/publish``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/shared-drafts/{_path(id)}/publish",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_permalinks(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyListPermalinksResponse:
        """List permalinks in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/permalinks``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/permalinks",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_permalinks_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PermalinkRow]:
        """Iterate every item of ``list_permalinks`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/permalinks",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="permalinks",
        )

    def create_permalink(
        self,
        org_id: str,
        space_id: str,
        *,
        from_path: str,
        target_type: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        target_topic_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        target_category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        target_user_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        target_tag: Union[Optional[str], NotGiven] = NOT_GIVEN,
        external_url: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyCreatePermalinkResponse:
        """Create a permalink in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/permalinks``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/permalinks",
            query=_query({}, extra_query),
            body=_body({"fromPath": from_path, "targetType": target_type, "targetTopicId": target_topic_id, "targetCategoryId": target_category_id, "targetUserId": target_user_id, "targetTag": target_tag, "externalUrl": external_url}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def import_permalinks(
        self,
        org_id: str,
        space_id: str,
        *,
        permalinks: List[ForumTaxonomyImportPermalinksParamsPermalink],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyImportPermalinksResponse:
        """Import the permalink

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/permalinks/import``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/permalinks/import",
            query=_query({}, extra_query),
            body=_body({"permalinks": permalinks}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_permalink(
        self,
        org_id: str,
        space_id: str,
        id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyRemovePermalinkResponse:
        """Delete the permalink

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/permalinks/{id}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/permalinks/{_path(id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_category_perms(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyListCategoryPermsResponse:
        """List permissions in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/categories/{categoryId}/permissions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}/permissions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_category_perms_all(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CategoryPermissionRow]:
        """Iterate every item of ``list_category_perms`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}/permissions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="permissions",
        )

    def set_category_perms(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        *,
        grants: List[ForumTaxonomySetCategoryPermsParamsGrant],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomySetCategoryPermsResponse:
        """Replace permissions in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/forum/categories/{categoryId}/permissions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}/permissions",
            query=_query({}, extra_query),
            body=_body({"grants": grants}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_category_mods(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyListCategoryModsResponse:
        """List moderators in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/categories/{categoryId}/moderators``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}/moderators",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_category_mods_all(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[CategoryModeratorRow]:
        """Iterate every item of ``list_category_mods`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}/moderators",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="moderators",
        )

    def add_category_mod(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        *,
        user_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyAddCategoryModResponse:
        """Create a moderator in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/categories/{categoryId}/moderators``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}/moderators",
            query=_query({}, extra_query),
            body=_body({"userId": user_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_category_mod(
        self,
        org_id: str,
        space_id: str,
        category_id: str,
        user_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyRemoveCategoryModResponse:
        """Delete the moderator

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/categories/{categoryId}/moderators/{userId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/categories/{_path(category_id)}/moderators/{_path(user_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_tag_groups(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyListTagGroupsResponse:
        """List tag groups in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/tag-groups``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-groups",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_tag_groups_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[TagGroupSummary]:
        """Iterate every item of ``list_tag_groups`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-groups",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="tagGroups",
        )

    def create_tag_group(
        self,
        org_id: str,
        space_id: str,
        *,
        name: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        category_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyCreateTagGroupResponse:
        """Create a tag group in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/tag-groups``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-groups",
            query=_query({}, extra_query),
            body=_body({"name": name, "mode": mode, "tags": tags, "categoryIds": category_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update_tag_group(
        self,
        org_id: str,
        space_id: str,
        group_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        name: Union[str, NotGiven] = NOT_GIVEN,
        mode: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        category_ids: Union[List[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyUpdateTagGroupResponse:
        """Update the tag group

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/forum/tag-groups/{groupId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-groups/{_path(group_id)}",
            query=_query({}, extra_query),
            body=_body({"name": name, "mode": mode, "tags": tags, "categoryIds": category_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_tag_group(
        self,
        org_id: str,
        space_id: str,
        group_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyRemoveTagGroupResponse:
        """Delete the tag group

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/tag-groups/{groupId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-groups/{_path(group_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def list_tag_info(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyListTagInfoResponse:
        """Get the tag info in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/tag-info``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-info",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_tag_info_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[TagInfoRow]:
        """Iterate every item of ``list_tag_info`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-info",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="tagInfo",
        )

    def set_tag_info(
        self,
        org_id: str,
        space_id: str,
        *,
        tag: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        description: Union[Optional[str], NotGiven] = NOT_GIVEN,
        canonical: Union[Optional[str], NotGiven] = NOT_GIVEN,
        staff_only: Union[bool, NotGiven] = NOT_GIVEN,
        min_trust_level: Union[Optional[int], NotGiven] = NOT_GIVEN,
        color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        text_color: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomySetTagInfoResponse:
        """Create the tag info in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/tag-info``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-info",
            query=_query({}, extra_query),
            body=_body({"tag": tag, "description": description, "canonical": canonical, "staffOnly": staff_only, "minTrustLevel": min_trust_level, "color": color, "textColor": text_color}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_tag_info(
        self,
        org_id: str,
        space_id: str,
        tag: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomyRemoveTagInfoResponse:
        """Delete the tag info

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/tag-info/{tag}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-info/{_path(tag)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_topic_category(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        category_id: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTaxonomySetTopicCategoryResponse:
        """Create the category in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/category``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/category",
            query=_query({}, extra_query),
            body=_body({"categoryId": category_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ForumToolsResource:
    """``client.forum.tools`` (36 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def summarize(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsSummarizeResponse:
        """Create the summarize in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/summarize``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/summarize",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def unanswered_experts(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsUnansweredExpertsResponse:
        """List experts in a space (unanswered)

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/unanswered/experts``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/unanswered/experts",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def unanswered_experts_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ForumToolsUnansweredExpertsResponseItem]:
        """Iterate every item of ``unanswered_experts`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/unanswered/experts",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="items",
        )

    def experts(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsExpertsResponse:
        """List experts in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/experts``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/experts",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def experts_all(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ExpertSuggestion]:
        """Iterate every item of ``experts`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/experts",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="experts",
        )

    def notify_experts(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsNotifyExpertsResponse:
        """Create the notify in a space (experts)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/experts/notify``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/experts/notify",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def get_timer(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsGetTimerResponse:
        """Get the timer in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/timer``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/timer",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_timer(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        run_at: Union[str, NotGiven] = NOT_GIVEN,
        based_on_last_post: Union[bool, NotGiven] = NOT_GIVEN,
        duration_minutes: Union[int, NotGiven] = NOT_GIVEN,
        target_category_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsSetTimerResponse:
        """Create the timer in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/timer``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/timer",
            query=_query({}, extra_query),
            body=_body({"action": action, "runAt": run_at, "basedOnLastPost": based_on_last_post, "durationMinutes": duration_minutes, "targetCategoryId": target_category_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def clear_timer(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsClearTimerResponse:
        """Delete the timer in a space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/timer``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/timer",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def recover(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsRecoverResponse:
        """Create the recover in a space (forum)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/recover``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/recover",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bump(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsBumpResponse:
        """Create the bump in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/bump``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/bump",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def split(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        post_ids: List[str],
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsSplitResponse:
        """Split the forum

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/split``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/split",
            query=_query({}, extra_query),
            body=_body({"postIds": post_ids, "title": title}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def merge(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        target_topic_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsMergeResponse:
        """Merge the forum

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/merge``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/merge",
            query=_query({}, extra_query),
            body=_body({"targetTopicId": target_topic_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def promote_to_docs(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        target_space_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        collection_id: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsPromoteToDocsResponse:
        """Promote the forum

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/promote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/promote",
            query=_query({}, extra_query),
            body=_body({"targetSpaceId": target_space_id, "collectionId": collection_id, "title": title}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def move_posts(
        self,
        org_id: str,
        space_id: str,
        *,
        post_ids: List[str],
        target_topic_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsMovePostsResponse:
        """Move the post

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/posts/move``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/move",
            query=_query({}, extra_query),
            body=_body({"postIds": post_ids, "targetTopicId": target_topic_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def change_owner(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        post_ids: List[str],
        new_owner_id: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsChangeOwnerResponse:
        """Create the change owner in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/change-owner``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/change-owner",
            query=_query({}, extra_query),
            body=_body({"postIds": post_ids, "newOwnerId": new_owner_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def edit_post(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ForumToolsEditPostParamsContent, NotGiven] = NOT_GIVEN,
        edit_reason: Union[str, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsEditPostResponse:
        """Update the post (forum)

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/forum/posts/{postId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}",
            query=_query({}, extra_query),
            body=_body({"content": content, "editReason": edit_reason, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def delete_post(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsDeletePostResponse:
        """Delete the post (forum)

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/posts/{postId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def revisions(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsRevisionsResponse:
        """List revisions in a space (forum posts)

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/posts/{postId}/revisions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}/revisions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def revisions_all(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[PostRevisionMeta]:
        """Iterate every item of ``revisions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}/revisions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="revisions",
        )

    def revision_diff(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        revision: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsRevisionDiffResponse:
        """Get the revision (forum)

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/posts/{postId}/revisions/{revision}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}/revisions/{_path(revision)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def vote(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsVoteResponse:
        """Create the vote in a space (forum posts)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/posts/{postId}/vote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}/vote",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def react(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        emoji: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        anonymous: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsReactResponse:
        """Create the react in a space (forum posts)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/posts/{postId}/react``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}/react",
            query=_query({}, extra_query),
            body=_body({"emoji": emoji, "anonymous": anonymous}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bookmark(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsBookmarkResponse:
        """Create the bookmark in a space (forum)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/bookmark``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/bookmark",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bookmark_reminder(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        remind_at: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        preset: Union[str, NotGiven] = NOT_GIVEN,
        note: Union[Optional[str], NotGiven] = NOT_GIVEN,
        name: Union[Optional[str], NotGiven] = NOT_GIVEN,
        auto_delete: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsBookmarkReminderResponse:
        """Replace the reminder in a space

        ``PUT /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/bookmark/reminder``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PUT",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/bookmark/reminder",
            query=_query({}, extra_query),
            body=_body({"remindAt": remind_at, "preset": preset, "note": note, "name": name, "autoDelete": auto_delete}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def flag(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        reason: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        flag_type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsFlagResponse:
        """Flag the post (forum)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/posts/{postId}/flag``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}/flag",
            query=_query({}, extra_query),
            body=_body({"reason": reason, "flagType": flag_type}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def flag_topic(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        reason: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        flag_type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsFlagTopicResponse:
        """Flag the forum

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/flag``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/flag",
            query=_query({}, extra_query),
            body=_body({"reason": reason, "flagType": flag_type}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def answer(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        post_id: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsAnswerResponse:
        """Create the answer in a space (forum)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/answer``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/answer",
            query=_query({}, extra_query),
            body=_body({"postId": post_id}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def offer_bounty(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        amount: int,
        days: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsOfferBountyResponse:
        """Create the bounty in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/bounty``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/bounty",
            query=_query({}, extra_query),
            body=_body({"amount": amount, "days": days}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def withdraw_bounty(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ErrorEnvelope:
        """Delete the bounty in a space

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/bounty``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/bounty",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bounty_history(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsBountyHistoryResponse:
        """List bounties in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/bounties``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/bounties",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def bounty_history_all(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[BountyView]:
        """Iterate every item of ``bounty_history`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/bounties",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="bounties",
        )

    def set_state(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        state: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsSetStateResponse:
        """Create the state in a space (forum)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/state``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/state",
            query=_query({}, extra_query),
            body=_body({"state": state}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_kind(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        kind: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsSetKindResponse:
        """Create the kind in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/kind``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/kind",
            query=_query({}, extra_query),
            body=_body({"kind": kind}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def pin(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        pinned: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsPinResponse:
        """Pin the forum

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/pin``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/pin",
            query=_query({}, extra_query),
            body=_body({"pinned": pinned}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def pin_advanced(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        pinned: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        until: Union[Optional[str], NotGiven] = NOT_GIVEN,
        global_: Union[bool, NotGiven] = NOT_GIVEN,
        banner: Union[bool, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsPinAdvancedResponse:
        """Pin advanced in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/pin-advanced``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/pin-advanced",
            query=_query({}, extra_query),
            body=_body({"pinned": pinned, "until": until, "global": global_, "banner": banner}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def slow_mode(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        seconds: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsSlowModeResponse:
        """Create the slow mode in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/slow-mode``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/slow-mode",
            query=_query({}, extra_query),
            body=_body({"seconds": seconds}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def dismiss_pin(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsDismissPinResponse:
        """Dismiss pin in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/dismiss-pin``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/dismiss-pin",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_listed(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        listed: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsSetListedResponse:
        """Create the listed in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/listed``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/listed",
            query=_query({}, extra_query),
            body=_body({"listed": listed}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_post_status(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        status: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumToolsSetPostStatusResponse:
        """Create the status in a space (forum posts)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/posts/{postId}/status``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}/status",
            query=_query({}, extra_query),
            body=_body({"status": status}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ForumTopicsResource:
    """``client.forum.topics`` (16 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def list(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        category: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        assigned: Union[str, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumListEnveloped:
        """Get the forum in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum``

        :param limit: Topics per page.
        :param page: Which page of results to return, 1-based.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum",
            query=_query({"limit": limit, "tag": tag, "q": q, "category": category, "page": page, "assigned": assigned, "cursor": cursor, "kind": kind, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def list_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        tag: Union[str, NotGiven] = NOT_GIVEN,
        q: Union[str, NotGiven] = NOT_GIVEN,
        category: Union[str, NotGiven] = NOT_GIVEN,
        page: Union[int, NotGiven] = NOT_GIVEN,
        assigned: Union[str, NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        sort: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ArticleSummary]:
        """Iterate every item of ``list`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum",
            query=_query({"limit": limit, "tag": tag, "q": q, "category": category, "page": page, "assigned": assigned, "kind": kind, "sort": sort}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="topics",
        )

    def create(
        self,
        org_id: str,
        space_id: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ForumTopicsCreateParamsContent, NotGiven] = NOT_GIVEN,
        kind: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        featured_link: Union[Optional[str], NotGiven] = NOT_GIVEN,
        poll: Union[ForumTopicsCreateParamsPoll, NotGiven] = NOT_GIVEN,
        anonymous: Union[bool, NotGiven] = NOT_GIVEN,
        customization: Union[Optional[ForumTopicsCreateParamsCustomization], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsCreateResponse:
        """Create the forum in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "kind": kind, "tags": tags, "categoryId": category_id, "featuredLink": featured_link, "poll": poll, "anonymous": anonymous, "customization": customization, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def banner(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsBannerResponse:
        """Get the banner in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/banner``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/banner",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def get(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsGetResponse:
        """Get the forum

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def related(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsRelatedResponse:
        """Get the related in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/related``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/related",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def timeline(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsTimelineResponse:
        """Get the timeline in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/timeline``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/timeline",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def reply_as_linked_topic(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        post_id: str,
        *,
        title: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ForumTopicsReplyAsLinkedTopicParamsContent, NotGiven] = NOT_GIVEN,
        category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsReplyAsLinkedTopicResponse:
        """Create the reply as linked topic in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/posts/{postId}/reply-as-linked-topic``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/posts/{_path(post_id)}/reply-as-linked-topic",
            query=_query({}, extra_query),
            body=_body({"title": title, "content": content, "categoryId": category_id, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def add_poll(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        question: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        options: Union[List[str], NotGiven] = NOT_GIVEN,
        allow_multiple: Union[bool, NotGiven] = NOT_GIVEN,
        type: Union[str, NotGiven] = NOT_GIVEN,
        ranked: Union[bool, NotGiven] = NOT_GIVEN,
        public: Union[bool, NotGiven] = NOT_GIVEN,
        min_value: Union[int, NotGiven] = NOT_GIVEN,
        max_value: Union[int, NotGiven] = NOT_GIVEN,
        step: Union[int, NotGiven] = NOT_GIVEN,
        allowed_group_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        closes_at: Union[Optional[str], NotGiven] = NOT_GIVEN,
        results_visibility: Union[str, NotGiven] = NOT_GIVEN,
        min_choices: Union[Optional[int], NotGiven] = NOT_GIVEN,
        max_choices: Union[Optional[int], NotGiven] = NOT_GIVEN,
        chart_type: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsAddPollResponse:
        """Create the poll in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/poll``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/poll",
            query=_query({}, extra_query),
            body=_body({"question": question, "options": options, "allowMultiple": allow_multiple, "type": type, "ranked": ranked, "public": public, "minValue": min_value, "maxValue": max_value, "step": step, "allowedGroupId": allowed_group_id, "closesAt": closes_at, "resultsVisibility": results_visibility, "minChoices": min_choices, "maxChoices": max_choices, "chartType": chart_type}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def vote_poll(
        self,
        org_id: str,
        space_id: str,
        poll_id: str,
        *,
        option_ids: List[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsVotePollResponse:
        """Create the vote in a space (forum polls)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/polls/{pollId}/vote``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/polls/{_path(poll_id)}/vote",
            query=_query({}, extra_query),
            body=_body({"optionIds": option_ids}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def poll_voters(
        self,
        org_id: str,
        space_id: str,
        poll_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> PollVoterBreakdown:
        """List voters in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/polls/{pollId}/voters``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/polls/{_path(poll_id)}/voters",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def close_poll(
        self,
        org_id: str,
        space_id: str,
        poll_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsClosePollResponse:
        """Close the poll

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/polls/{pollId}/close``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/polls/{_path(poll_id)}/close",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reopen_poll(
        self,
        org_id: str,
        space_id: str,
        poll_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsReopenPollResponse:
        """Reopen the poll

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/polls/{pollId}/reopen``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/polls/{_path(poll_id)}/reopen",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def remove_poll(
        self,
        org_id: str,
        space_id: str,
        poll_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsRemovePollResponse:
        """Delete the poll

        ``DELETE /orgs/{orgId}/spaces/{spaceId}/forum/polls/{pollId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "DELETE",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/polls/{_path(poll_id)}",
            query=_query({}, extra_query),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def reply(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        content: Union[ForumTopicsReplyParamsContent, NotGiven] = NOT_GIVEN,
        parent_post_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        whisper: Union[bool, NotGiven] = NOT_GIVEN,
        anonymous: Union[bool, NotGiven] = NOT_GIVEN,
        markdown: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsReplyResponse:
        """Create a reply in a space (forum)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/replies``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/replies",
            query=_query({}, extra_query),
            body=_body({"content": content, "parentPostId": parent_post_id, "whisper": whisper, "anonymous": anonymous, "markdown": markdown}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_wiki(
        self,
        org_id: str,
        space_id: str,
        post_id: str,
        *,
        wiki: bool,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsSetWikiResponse:
        """Create the wiki in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/posts/{postId}/wiki``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/posts/{_path(post_id)}/wiki",
            query=_query({}, extra_query),
            body=_body({"wiki": wiki}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def update(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        title: Union[str, NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        featured_link: Union[Optional[str], NotGiven] = NOT_GIVEN,
        slug: Union[str, NotGiven] = NOT_GIVEN,
        customization: Union[Optional[ForumTopicsUpdateParamsCustomization], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTopicsUpdateResponse:
        """Update the forum

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}",
            query=_query({}, extra_query),
            body=_body({"title": title, "tags": tags, "featuredLink": featured_link, "slug": slug, "customization": customization}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ForumTranslationsResource:
    """``client.forum.translations`` (2 operations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client

    def translate_topic(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        *,
        locale: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTranslationsTranslateTopicResponse:
        """Create the translate in a space (public reader forum t)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/translate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/translate",
            query=_query({}, extra_query),
            body=_body({"locale": locale}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def translate_post(
        self,
        org_id: str,
        space_id: str,
        slug: str,
        post_id: str,
        *,
        locale: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTranslationsTranslatePostResponse:
        """Create the translate in a space (public reader forum t posts)

        ``POST /public/orgs/{orgId}/spaces/{spaceId}/forum/t/{slug}/posts/{postId}/translate``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/public/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/t/{_path(slug)}/posts/{_path(post_id)}/translate",
            query=_query({}, extra_query),
            body=_body({"locale": locale}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )


class ForumResource:
    """``client.forum`` (16 operations; automations, taxonomy, tools, topics, translations)."""

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        self.automations = ForumAutomationsResource(client)
        self.taxonomy = ForumTaxonomyResource(client)
        self.tools = ForumToolsResource(client)
        self.topics = ForumTopicsResource(client)
        self.translations = ForumTranslationsResource(client)

    def space_level(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumSpaceLevelResponse:
        """List notifications in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/notifications``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/notifications",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def set_space_level(
        self,
        org_id: str,
        space_id: str,
        *,
        level: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumSetSpaceLevelResponse:
        """Create a notification in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/notifications``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/notifications",
            query=_query({}, extra_query),
            body=_body({"level": level}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def mark_read(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        post_number: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumMarkReadResponse:
        """Create the read in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/read``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/read",
            query=_query({}, extra_query),
            body=_body({"postNumber": post_number}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def read_time(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        seconds: int,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumReadTimeResponse:
        """Create the read time in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/read-time``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/read-time",
            query=_query({}, extra_query),
            body=_body({"seconds": seconds}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def set_topic_level(
        self,
        org_id: str,
        space_id: str,
        topic_id: str,
        *,
        level: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumSetTopicLevelResponse:
        """Create a notification in a space (for a topic)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/{topicId}/notifications``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/{_path(topic_id)}/notifications",
            query=_query({}, extra_query),
            body=_body({"level": level}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def tag_subscriptions(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTagSubscriptionsResponse:
        """List tag subscriptions in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/tag-subscriptions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-subscriptions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def tag_subscriptions_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ForumTagSubscriptionsResponseSubscription]:
        """Iterate every item of ``tag_subscriptions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-subscriptions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="subscriptions",
        )

    def set_tag_subscription(
        self,
        org_id: str,
        space_id: str,
        *,
        tag: str,
        level: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumSetTagSubscriptionResponse:
        """Create a tag subscription in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/tag-subscriptions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tag-subscriptions",
            query=_query({}, extra_query),
            body=_body({"tag": tag, "level": level}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def category_subscriptions(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumCategorySubscriptionsResponse:
        """List category subscriptions in a space

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/category-subscriptions``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/category-subscriptions",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def category_subscriptions_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ForumCategorySubscriptionsResponseSubscription]:
        """Iterate every item of ``category_subscriptions`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/category-subscriptions",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="subscriptions",
        )

    def set_category_subscription(
        self,
        org_id: str,
        space_id: str,
        *,
        category_id: str,
        level: Optional[str],
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumSetCategorySubscriptionResponse:
        """Create a category subscription in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/category-subscriptions``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/category-subscriptions",
            query=_query({}, extra_query),
            body=_body({"categoryId": category_id, "level": level}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def tags(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumTagsResponse:
        """List tags in a space (forum)

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/tags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tags",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def tags_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[ForumTagsResponseTag]:
        """Iterate every item of ``tags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/tags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="tags",
        )

    def get_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumGetSettingsResponse:
        """List settings in a space (forum)

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/settings``
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/settings",
            query=_query({}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def update_settings(
        self,
        org_id: str,
        space_id: str,
        *,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        who_can_post: Union[Optional[str], NotGiven] = NOT_GIVEN,
        moderate_comments: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        moderate_anonymous: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        allow_anonymous: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        anonymous_captcha: Union[Optional[str], NotGiven] = NOT_GIVEN,
        default_sort: Union[Optional[str], NotGiven] = NOT_GIVEN,
        reactions_enabled: Union[Optional[bool], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumUpdateSettingsResponse:
        """Update settings in a space (forum)

        ``PATCH /orgs/{orgId}/spaces/{spaceId}/forum/settings``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "PATCH",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/settings",
            query=_query({}, extra_query),
            body=_body({"whoCanPost": who_can_post, "moderateComments": moderate_comments, "moderateAnonymous": moderate_anonymous, "allowAnonymous": allow_anonymous, "anonymousCaptcha": anonymous_captcha, "defaultSort": default_sort, "reactionsEnabled": reactions_enabled}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def flags(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        cursor: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumFlagsResponse:
        """List flags in a space (forum)

        ``GET /orgs/{orgId}/spaces/{spaceId}/forum/flags``

        :param limit: Rows per page.
        :param cursor: Where to continue from: pass back the `page.nextCursor` of the previous answer.
        """
        return self._client._request(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/flags",
            query=_query({"limit": limit, "cursor": cursor}, extra_query),
            headers=extra_headers,
            timeout=timeout,
        )

    def flags_all(
        self,
        org_id: str,
        space_id: str,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[FlagRow]:
        """Iterate every item of ``flags`` across all pages, following ``cursor``."""
        yield from self._client._paginate(
            "GET",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/flags",
            query=_query({"limit": limit}, extra_query),
            headers=extra_headers,
            timeout=timeout,
            page_param="cursor",
            items_key="flags",
        )

    def resolve_flag(
        self,
        org_id: str,
        space_id: str,
        flag_id: str,
        *,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumResolveFlagResponse:
        """Resolve the flag (forum)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/flags/{flagId}/resolve``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/flags/{_path(flag_id)}/resolve",
            query=_query({}, extra_query),
            body=_body({"action": action}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def bulk_moderate(
        self,
        org_id: str,
        space_id: str,
        *,
        topic_ids: List[str],
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        category_id: Union[Optional[str], NotGiven] = NOT_GIVEN,
        tags: Union[List[str], NotGiven] = NOT_GIVEN,
        level: Union[Optional[str], NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumBulkModerateResponse:
        """Create the bulk in a space

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/bulk``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/bulk",
            query=_query({}, extra_query),
            body=_body({"topicIds": topic_ids, "action": action, "categoryId": category_id, "tags": tags, "level": level}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )

    def review_flag(
        self,
        org_id: str,
        space_id: str,
        flag_id: str,
        *,
        action: str,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> ForumReviewFlagResponse:
        """Create the review in a space (forum flags)

        ``POST /orgs/{orgId}/spaces/{spaceId}/forum/flags/{flagId}/review``

        :param idempotency_key: Makes this write safe to retry.
        """
        return self._client._request(
            "POST",
            f"/orgs/{_path(org_id)}/spaces/{_path(space_id)}/forum/flags/{_path(flag_id)}/review",
            query=_query({}, extra_query),
            body=_body({"action": action}, extra_body),
            headers={**_query({"Idempotency-Key": idempotency_key}), **(extra_headers or {})},
            timeout=timeout,
        )
