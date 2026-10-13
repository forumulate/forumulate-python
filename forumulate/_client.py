from __future__ import annotations

import os
from typing import Any, Mapping, Optional

import requests

from ._core import ENVIRONMENTS, BaseClient, _base_url_from_env, _token_from_env
from .resources import (
    AiResource,
    AnalyticsResource,
    ApiActivityResource,
    AuditResource,
    AuthResource,
    BillingResource,
    BlogResource,
    CareersResource,
    ChangelogResource,
    ChatResource,
    CommunityResource,
    ConnectorsResource,
    ConsentResource,
    ContactResource,
    CoursesResource,
    CustomEmojiResource,
    CustomFieldsResource,
    DeviceKeysResource,
    DocsResource,
    DraftsResource,
    EmbeddableHostsResource,
    EmbedFeedsResource,
    EventsResource,
    ExtensionsResource,
    FormsResource,
    ForumResource,
    GroupsResource,
    IntegrationsResource,
    InvitesResource,
    ItemsResource,
    LibraryResource,
    MailResource,
    McpResource,
    MembersResource,
    MessagesResource,
    ModerationResource,
    NewsletterResource,
    NotificationsResource,
    OnboardingResource,
    OrgsResource,
    PublicResource,
    QuestionsResource,
    ReaderAuthResource,
    ReaderDomainResource,
    ReaderPolicyResource,
    ReaderSignupsResource,
    RoadmapResource,
    RolesResource,
    ScimResource,
    SdksResource,
    SearchResource,
    ServiceAccountsResource,
    SessionsResource,
    SitesResource,
    SpacesResource,
    SpaceTemplatesResource,
    SpaceTypesResource,
    SsoResource,
    StatusResource,
    TemplatesResource,
    ThemesResource,
    TokensResource,
    TranslationsResource,
    UsersResource,
    WebhooksResource,
)


class Forumulate(BaseClient):
    """Client for the Forumulate (v1.0.0).

    With no arguments it reads its configuration from the environment
    (see ``from_env``). One pooled HTTP session serves every call; use it as a
    context manager, or call ``close()``, to release it. Rate limits (429) and
    server errors (5xx) are retried with backoff, honouring ``Retry-After``.
    """

    def __init__(
        self,
        *,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        environment: Optional[str] = None,
        timeout: float = 30.0,
        max_retries: int = 2,
        default_headers: Optional[Mapping[str, str]] = None,
        http_session: Optional[requests.Session] = None,
        env: Optional[Mapping[str, str]] = None,
    ) -> None:
        source = os.environ if env is None else env
        resolved = base_url or (ENVIRONMENTS.get(environment) if environment else None) or _base_url_from_env(source)
        super().__init__(
            base_url=resolved,
            token=token if token is not None else _token_from_env(source),
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            http_session=http_session,
        )
        self.ai = AiResource(self)
        self.analytics = AnalyticsResource(self)
        self.api_activity = ApiActivityResource(self)
        self.audit = AuditResource(self)
        self.auth = AuthResource(self)
        self.billing = BillingResource(self)
        self.blog = BlogResource(self)
        self.careers = CareersResource(self)
        self.changelog = ChangelogResource(self)
        self.chat = ChatResource(self)
        self.community = CommunityResource(self)
        self.connectors = ConnectorsResource(self)
        self.consent = ConsentResource(self)
        self.contact = ContactResource(self)
        self.courses = CoursesResource(self)
        self.custom_emoji = CustomEmojiResource(self)
        self.custom_fields = CustomFieldsResource(self)
        self.device_keys = DeviceKeysResource(self)
        self.docs = DocsResource(self)
        self.drafts = DraftsResource(self)
        self.embeddable_hosts = EmbeddableHostsResource(self)
        self.embed_feeds = EmbedFeedsResource(self)
        self.events = EventsResource(self)
        self.extensions = ExtensionsResource(self)
        self.forms = FormsResource(self)
        self.forum = ForumResource(self)
        self.groups = GroupsResource(self)
        self.integrations = IntegrationsResource(self)
        self.invites = InvitesResource(self)
        self.items = ItemsResource(self)
        self.library = LibraryResource(self)
        self.mail = MailResource(self)
        self.mcp = McpResource(self)
        self.members = MembersResource(self)
        self.messages = MessagesResource(self)
        self.moderation = ModerationResource(self)
        self.newsletter = NewsletterResource(self)
        self.notifications = NotificationsResource(self)
        self.onboarding = OnboardingResource(self)
        self.orgs = OrgsResource(self)
        self.public = PublicResource(self)
        self.questions = QuestionsResource(self)
        self.reader_auth = ReaderAuthResource(self)
        self.reader_domain = ReaderDomainResource(self)
        self.reader_policy = ReaderPolicyResource(self)
        self.reader_signups = ReaderSignupsResource(self)
        self.roadmap = RoadmapResource(self)
        self.roles = RolesResource(self)
        self.scim = ScimResource(self)
        self.sdks = SdksResource(self)
        self.search = SearchResource(self)
        self.service_accounts = ServiceAccountsResource(self)
        self.sessions = SessionsResource(self)
        self.sites = SitesResource(self)
        self.spaces = SpacesResource(self)
        self.space_templates = SpaceTemplatesResource(self)
        self.space_types = SpaceTypesResource(self)
        self.sso = SsoResource(self)
        self.status = StatusResource(self)
        self.templates = TemplatesResource(self)
        self.themes = ThemesResource(self)
        self.tokens = TokensResource(self)
        self.translations = TranslationsResource(self)
        self.users = UsersResource(self)
        self.webhooks = WebhooksResource(self)

    @classmethod
    def from_env(cls, env: Optional[Mapping[str, str]] = None, **kwargs: Any) -> "Forumulate":
        """A client configured from ``env`` (default: ``os.environ``); keyword arguments win."""
        return cls(env=env, **kwargs)
