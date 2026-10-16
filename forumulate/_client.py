from __future__ import annotations

import os
from typing import Any, Mapping, Optional

import requests

from ._core import ENVIRONMENTS, BaseClient, _base_url_from_env, _token_from_env
from .resources import (
    AiResource,
    AnalyticsResource,
    ApiActivityResource,
    AssetLibraryResource,
    AuditResource,
    AuthResource,
    BillingResource,
    BlogResource,
    BlogCommentsResource,
    BlogPostTranslationResource,
    BlogTaxonomyResource,
    CareersResource,
    CareersAtsResource,
    CareersIndexingResource,
    ChangelogResource,
    ChangelogImportResource,
    ChatResource,
    CommunityResource,
    ConnectorsResource,
    ConsentResource,
    ContactResource,
    ContactBlockResource,
    ContactPrivacyResource,
    ContentAiResource,
    ContentEntryLocalesResource,
    ContentLibraryResource,
    ContentLocalesResource,
    ContentModelResource,
    ContentStudioResource,
    ContentWorkflowResource,
    CourseAccessResource,
    CourseCommerceResource,
    CourseLearnerExtrasResource,
    CourseLearnersResource,
    CoursePathsResource,
    CoursesResource,
    CustomEmojiResource,
    CustomFieldsResource,
    DeliveryEntriesResource,
    DeliveryKeyResource,
    DeliveryKeysResource,
    DeliverySiteResource,
    DeployStatusResource,
    DeviceKeysResource,
    DocsResource,
    DraftsResource,
    EmbeddableHostsResource,
    EmbedFeedsResource,
    EntryCardResource,
    EntryDeliveryPreviewResource,
    EntryFieldsResource,
    EntryUsageResource,
    EnvironmentsResource,
    EventAgendaPublicResource,
    EventAttendeesResource,
    EventAttendeesPublicResource,
    EventMyAgendaResource,
    EventNoticesResource,
    EventPromoCodesResource,
    EventRsvpPrivacyResource,
    EventsResource,
    EventSeriesPublicResource,
    EventSessionsResource,
    EventSpeakersResource,
    EventTicketsResource,
    EventTicketsPublicResource,
    EventTicketWebhookResource,
    ExtensionsResource,
    FormsResource,
    ForumResource,
    ForumTopicTranslationResource,
    GoogleIndexingResource,
    GroupsResource,
    GrowthResource,
    HostedOutputResource,
    IconsResource,
    IntegrationsResource,
    InvitesResource,
    ItemsResource,
    LegalUpdatesResource,
    LibraryResource,
    LibraryAssetResource,
    LibraryDomainResource,
    LibraryItemResource,
    LibraryMediaResource,
    LibrarySdkResource,
    LibrarySiteResource,
    LibraryUsageResource,
    MailResource,
    MarkdownDialectResource,
    McpResource,
    MembersResource,
    MessagesResource,
    ModelIoResource,
    ModerationResource,
    MyActivityResource,
    MyCoursePathsResource,
    MyLearningResource,
    NewsletterResource,
    NotificationsResource,
    OnboardingResource,
    OrgImportJobResource,
    OrgPaymentsResource,
    OrgsResource,
    OrgSmsResource,
    PreviewExchangeResource,
    PreviewSessionsResource,
    PreviewStatusResource,
    PublicResource,
    QuestionsResource,
    ReaderAuthResource,
    ReaderDomainResource,
    ReaderImageSignResource,
    ReaderPolicyResource,
    ReaderSignOutResource,
    ReaderSignupsResource,
    ReferenceCandidatesResource,
    ReleaseReviewResource,
    ReleasesResource,
    ReleaseTranslationResource,
    RoadmapResource,
    RolesResource,
    ScimResource,
    SdksResource,
    SearchResource,
    SecretScanningResource,
    SectionLibraryResource,
    ServiceAccountsResource,
    SessionsResource,
    SiteFrontPageResource,
    SiteLabelsResource,
    SitePreviewResource,
    SitesResource,
    SpaceAuthorsResource,
    SpaceFrontPageResource,
    SpaceLabelsResource,
    SpacePiecePageResource,
    SpacesResource,
    SpaceTemplatesResource,
    SpaceTypesResource,
    SsoResource,
    StatusResource,
    StatusAccessResource,
    StatusIntegrationsResource,
    StatusMetricsResource,
    StatusTemplatesResource,
    StatusTranslationsResource,
    TemplatesResource,
    ThemesResource,
    TokensResource,
    TranslationsResource,
    UsersResource,
    VersioningResource,
    WebhooksResource,
)


class Forumulate(BaseClient):
    """Client for the Forumulate (v1.1.0).

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
        self.asset_library = AssetLibraryResource(self)
        self.audit = AuditResource(self)
        self.auth = AuthResource(self)
        self.billing = BillingResource(self)
        self.blog = BlogResource(self)
        self.blog_comments = BlogCommentsResource(self)
        self.blog_post_translation = BlogPostTranslationResource(self)
        self.blog_taxonomy = BlogTaxonomyResource(self)
        self.careers = CareersResource(self)
        self.careers_ats = CareersAtsResource(self)
        self.careers_indexing = CareersIndexingResource(self)
        self.changelog = ChangelogResource(self)
        self.changelog_import = ChangelogImportResource(self)
        self.chat = ChatResource(self)
        self.community = CommunityResource(self)
        self.connectors = ConnectorsResource(self)
        self.consent = ConsentResource(self)
        self.contact = ContactResource(self)
        self.contact_block = ContactBlockResource(self)
        self.contact_privacy = ContactPrivacyResource(self)
        self.content_ai = ContentAiResource(self)
        self.content_entry_locales = ContentEntryLocalesResource(self)
        self.content_library = ContentLibraryResource(self)
        self.content_locales = ContentLocalesResource(self)
        self.content_model = ContentModelResource(self)
        self.content_studio = ContentStudioResource(self)
        self.content_workflow = ContentWorkflowResource(self)
        self.course_access = CourseAccessResource(self)
        self.course_commerce = CourseCommerceResource(self)
        self.course_learner_extras = CourseLearnerExtrasResource(self)
        self.course_learners = CourseLearnersResource(self)
        self.course_paths = CoursePathsResource(self)
        self.courses = CoursesResource(self)
        self.custom_emoji = CustomEmojiResource(self)
        self.custom_fields = CustomFieldsResource(self)
        self.delivery_entries = DeliveryEntriesResource(self)
        self.delivery_key = DeliveryKeyResource(self)
        self.delivery_keys = DeliveryKeysResource(self)
        self.delivery_site = DeliverySiteResource(self)
        self.deploy_status = DeployStatusResource(self)
        self.device_keys = DeviceKeysResource(self)
        self.docs = DocsResource(self)
        self.drafts = DraftsResource(self)
        self.embeddable_hosts = EmbeddableHostsResource(self)
        self.embed_feeds = EmbedFeedsResource(self)
        self.entry_card = EntryCardResource(self)
        self.entry_delivery_preview = EntryDeliveryPreviewResource(self)
        self.entry_fields = EntryFieldsResource(self)
        self.entry_usage = EntryUsageResource(self)
        self.environments = EnvironmentsResource(self)
        self.event_agenda_public = EventAgendaPublicResource(self)
        self.event_attendees = EventAttendeesResource(self)
        self.event_attendees_public = EventAttendeesPublicResource(self)
        self.event_my_agenda = EventMyAgendaResource(self)
        self.event_notices = EventNoticesResource(self)
        self.event_promo_codes = EventPromoCodesResource(self)
        self.event_rsvp_privacy = EventRsvpPrivacyResource(self)
        self.events = EventsResource(self)
        self.event_series_public = EventSeriesPublicResource(self)
        self.event_sessions = EventSessionsResource(self)
        self.event_speakers = EventSpeakersResource(self)
        self.event_tickets = EventTicketsResource(self)
        self.event_tickets_public = EventTicketsPublicResource(self)
        self.event_ticket_webhook = EventTicketWebhookResource(self)
        self.extensions = ExtensionsResource(self)
        self.forms = FormsResource(self)
        self.forum = ForumResource(self)
        self.forum_topic_translation = ForumTopicTranslationResource(self)
        self.google_indexing = GoogleIndexingResource(self)
        self.groups = GroupsResource(self)
        self.growth = GrowthResource(self)
        self.hosted_output = HostedOutputResource(self)
        self.icons = IconsResource(self)
        self.integrations = IntegrationsResource(self)
        self.invites = InvitesResource(self)
        self.items = ItemsResource(self)
        self.legal_updates = LegalUpdatesResource(self)
        self.library = LibraryResource(self)
        self.library_asset = LibraryAssetResource(self)
        self.library_domain = LibraryDomainResource(self)
        self.library_item = LibraryItemResource(self)
        self.library_media = LibraryMediaResource(self)
        self.library_sdk = LibrarySdkResource(self)
        self.library_site = LibrarySiteResource(self)
        self.library_usage = LibraryUsageResource(self)
        self.mail = MailResource(self)
        self.markdown_dialect = MarkdownDialectResource(self)
        self.mcp = McpResource(self)
        self.members = MembersResource(self)
        self.messages = MessagesResource(self)
        self.model_io = ModelIoResource(self)
        self.moderation = ModerationResource(self)
        self.my_activity = MyActivityResource(self)
        self.my_course_paths = MyCoursePathsResource(self)
        self.my_learning = MyLearningResource(self)
        self.newsletter = NewsletterResource(self)
        self.notifications = NotificationsResource(self)
        self.onboarding = OnboardingResource(self)
        self.org_import_job = OrgImportJobResource(self)
        self.org_payments = OrgPaymentsResource(self)
        self.orgs = OrgsResource(self)
        self.org_sms = OrgSmsResource(self)
        self.preview_exchange = PreviewExchangeResource(self)
        self.preview_sessions = PreviewSessionsResource(self)
        self.preview_status = PreviewStatusResource(self)
        self.public = PublicResource(self)
        self.questions = QuestionsResource(self)
        self.reader_auth = ReaderAuthResource(self)
        self.reader_domain = ReaderDomainResource(self)
        self.reader_image_sign = ReaderImageSignResource(self)
        self.reader_policy = ReaderPolicyResource(self)
        self.reader_sign_out = ReaderSignOutResource(self)
        self.reader_signups = ReaderSignupsResource(self)
        self.reference_candidates = ReferenceCandidatesResource(self)
        self.release_review = ReleaseReviewResource(self)
        self.releases = ReleasesResource(self)
        self.release_translation = ReleaseTranslationResource(self)
        self.roadmap = RoadmapResource(self)
        self.roles = RolesResource(self)
        self.scim = ScimResource(self)
        self.sdks = SdksResource(self)
        self.search = SearchResource(self)
        self.secret_scanning = SecretScanningResource(self)
        self.section_library = SectionLibraryResource(self)
        self.service_accounts = ServiceAccountsResource(self)
        self.sessions = SessionsResource(self)
        self.site_front_page = SiteFrontPageResource(self)
        self.site_labels = SiteLabelsResource(self)
        self.site_preview = SitePreviewResource(self)
        self.sites = SitesResource(self)
        self.space_authors = SpaceAuthorsResource(self)
        self.space_front_page = SpaceFrontPageResource(self)
        self.space_labels = SpaceLabelsResource(self)
        self.space_piece_page = SpacePiecePageResource(self)
        self.spaces = SpacesResource(self)
        self.space_templates = SpaceTemplatesResource(self)
        self.space_types = SpaceTypesResource(self)
        self.sso = SsoResource(self)
        self.status = StatusResource(self)
        self.status_access = StatusAccessResource(self)
        self.status_integrations = StatusIntegrationsResource(self)
        self.status_metrics = StatusMetricsResource(self)
        self.status_templates = StatusTemplatesResource(self)
        self.status_translations = StatusTranslationsResource(self)
        self.templates = TemplatesResource(self)
        self.themes = ThemesResource(self)
        self.tokens = TokensResource(self)
        self.translations = TranslationsResource(self)
        self.users = UsersResource(self)
        self.versioning = VersioningResource(self)
        self.webhooks = WebhooksResource(self)

    @classmethod
    def from_env(cls, env: Optional[Mapping[str, str]] = None, **kwargs: Any) -> "Forumulate":
        """A client configured from ``env`` (default: ``os.environ``); keyword arguments win."""
        return cls(env=env, **kwargs)
