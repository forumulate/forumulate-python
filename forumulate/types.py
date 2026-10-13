# Generated types.
from typing import Any, Dict, List, Literal, Optional, TypedDict, Union


class PatConstraintsDto(TypedDict, total=False):
    spaceIds: List[str]
    categoryIds: List[str]
    orgIds: List[str]


class CreatePatDto(TypedDict, total=False):
    name: str
    scopes: List[str]
    expiresInDays: int
    spaceIds: List[str]
    capabilities: List[str]
    scopeGrants: List[str]
    constraints: Any


class PatSummaryDto(TypedDict, total=False):
    id: str
    name: str
    scopes: List[str]
    createdAt: str
    expiresAt: Any
    lastUsedAt: Any
    spaceIds: List[str]
    capabilities: List[str]
    scopeGrants: Any
    constraints: Any
    applicationName: Any
    kind: str


class CreatedPatDto(TypedDict, total=False):
    token: str
    pat: "PatSummaryDto"


class PageInfoDto(TypedDict, total=False):
    limit: float
    hasMore: bool
    nextCursor: Any
    has_more: bool
    next_cursor: Any
    total: float


class PatListDto(TypedDict, total=False):
    pats: List["PatSummaryDto"]
    page: Any


class PatScopeDto(TypedDict, total=False):
    name: str
    description: str
    capabilities: List[str]


class PatScopeCatalogDto(TypedDict, total=False):
    scopes: List["PatScopeDto"]
    page: "PageInfo"


class CreateDeviceKeyDto(TypedDict, total=False):
    applicationName: str
    scopes: List[str]
    expiresInDays: int
    spaceIds: List[str]
    capabilities: List[str]
    scopeGrants: List[str]
    constraints: Any


class SlotRoleDto(TypedDict, total=False):
    id: str
    order: float
    gloss: str


class RoleVocabularyDto(TypedDict, total=False):
    version: str
    roles: List["SlotRoleDto"]
    unroledPolicy: str
    slotKeys: str


class OrgSummaryDto(TypedDict, total=False):
    id: str
    slug: str
    name: str
    createdAt: str


class OrgListDto(TypedDict, total=False):
    orgs: List["OrgSummaryDto"]
    page: Any


class SpaceSummaryDto(TypedDict, total=False):
    id: str
    type: str
    slug: str
    name: str
    visibility: str
    settings: Dict[str, Any]
    createdAt: str
    itemCount: float
    itemsUpdatedAt: Any
    url: Any


class SpaceCreatedDto(TypedDict, total=False):
    space: "SpaceSummaryDto"
    data: Any
    warnings: List[str]


class SpaceListDto(TypedDict, total=False):
    spaces: List["SpaceSummaryDto"]
    page: Any


class SpaceDetailDto(TypedDict, total=False):
    space: "SpaceSummaryDto"


class DnsRecordDto(TypedDict, total=False):
    name: str
    value: str


class VerificationFileDto(TypedDict, total=False):
    path: str
    contents: str


class VerificationMetaDto(TypedDict, total=False):
    tag: str


class DnsTargetDto(TypedDict, total=False):
    type: str
    name: str
    value: str


class DomainSummaryDto(TypedDict, total=False):
    id: str
    hostname: str
    basePath: str
    verified: bool
    active: bool
    verificationRecord: Any
    verificationFile: Any
    verificationMeta: "VerificationMetaDto"
    dnsTarget: Any
    createdAt: str


class DomainListDto(TypedDict, total=False):
    domains: List["DomainSummaryDto"]
    page: "PageInfo"


class DomainResponseDto(TypedDict, total=False):
    domain: "DomainSummaryDto"


class SetupDnsDto(TypedDict, total=False):
    found: List[str]
    expected: str
    reachesUs: bool
    cnameTarget: str


class SetupSnippetsDto(TypedDict, total=False):
    nginx: str
    caddy: str
    cloudflare: str


class SetupForwardDto(TypedDict, total=False):
    path: str
    origin: str
    snippets: "SetupSnippetsDto"


class DomainSetupDto(TypedDict, total=False):
    mode: str
    served: bool
    crawlerBlocked: bool
    message: str
    dns: "SetupDnsDto"
    forward: Any


class ExternalStandingDto(TypedDict, total=False):
    source: str
    label: str
    value: Any
    tier: Any
    profileUrl: Any
    iconUrl: Any
    updatedAt: str


class ExternalLeaderRowDto(TypedDict, total=False):
    userId: str
    standing: "ExternalStandingDto"


class ExternalLeaderboardDto(TypedDict, total=False):
    leaders: List["ExternalLeaderRowDto"]


class FreshnessDto(TypedDict, total=False):
    verifiedAt: Any
    ageDays: float
    stale: bool
    confidence: float


class ItemSummaryDto(TypedDict, total=False):
    id: str
    kind: str
    title: str
    slug: str
    published: bool
    group: str
    state: str
    updatedAt: str
    url: Any
    contentHash: str
    deleted: bool
    sections: Dict[str, Any]
    markdown: str
    contentIn: str
    freshness: Any


class ItemListLegacyDto(TypedDict, total=False):
    items: List["ItemSummaryDto"]


class SyncDto(TypedDict, total=False):
    checkpoint: str


class ItemPageDto(TypedDict, total=False):
    items: List["ItemSummaryDto"]
    page: "PageInfoDto"
    sync: "SyncDto"


class LevelProgressDto(TypedDict, total=False):
    level: float
    xp: float
    currentLevelXp: float
    nextLevelXp: Any
    xpIntoLevel: float
    xpForNextLevel: Any


class UserAttributesDto(TypedDict, total=False):
    progression: Dict[str, Any]
    points: float


class UserStateDto(TypedDict, total=False):
    attributes: "UserAttributesDto"
    entitlements: Dict[str, Any]
    directives: List[Dict[str, Any]]
    roles: List[str]


class SignalResultDto(TypedDict, total=False):
    track: str
    xp: float
    level: float
    levelChanged: bool
    delta: float


class InventoryItemDto(TypedDict, total=False):
    itemKey: str
    quantity: float
    name: Any


class WalletSummaryDto(TypedDict, total=False):
    balances: Dict[str, Any]
    inventory: List["InventoryItemDto"]


class CurrencyMovementResultDto(TypedDict, total=False):
    currency: str
    balance: float
    delta: float


class ItemMovementResultDto(TypedDict, total=False):
    itemKey: str
    quantity: float
    delta: float


class ErrorEnvelope(TypedDict, total=False):
    error: "ErrorEnvelopeError"
    requestId: str


class BlockNode(TypedDict, total=False):
    type: str
    attrs: Dict[str, Any]
    content: List["BlockNode"]
    text: str
    marks: List[Dict[str, Any]]


class BlockDoc(TypedDict, total=False):
    type: str
    content: List["BlockNode"]


class ConsentPreset(TypedDict, total=False):
    cbid: str
    dataDomainScript: str
    customerId: str
    websiteUuid: str


class ConsentConfig(TypedDict, total=False):
    provider: str
    preset: "ConsentPreset"
    custom: "ConsentConfigCustom"
    hosted: Dict[str, Any]
    policyVersion: str
    webhookSecret: str


SpaceConsentConfig = Any


class ConsentConfigView(TypedDict, total=False):
    provider: str
    preset: "ConsentPreset"
    policyVersion: str
    status: str
    reason: str
    webhookSecretSet: bool
    webhookConfigured: bool
    webhookVerifiedAt: Any
    webhookLastEventType: Any
    webhookUrl: str


class ResolvedConsentConfig(TypedDict, total=False):
    provider: str
    preset: "ConsentPreset"
    custom: Dict[str, Any]
    hosted: Dict[str, Any]
    policyVersion: str
    scriptSources: List[str]
    dryRun: bool
    status: str


class ConsentWebhookEvent(TypedDict, total=False):
    type: str
    data: Dict[str, Any]


class AboutStats(TypedDict, total=False):
    organization: "AboutStatsOrganization"
    staff: List["AboutStatsStaffItem"]
    stats: "AboutStatsStats"


class ActiveSession(TypedDict, total=False):
    createdAt: str
    current: bool
    expiresAt: str
    id: str
    ip: Any
    userAgent: Any


class ActivityItem(TypedDict, total=False):
    at: str
    excerpt: str
    kind: str
    spaceId: str
    spaceType: str
    topicId: str
    topicSlug: str
    topicTitle: str


class AgentEdit(TypedDict, total=False):
    slug: str
    summary: str
    tool: str


class AgentRunResult(TypedDict, total=False):
    calls: float
    edits: List["AgentEdit"]
    message: str
    truncated: bool
    turns: float


class AiInsights(TypedDict, total=False):
    answered: float
    helpful: float
    knowledgeGaps: List["QuestionCount"]
    notHelpful: float
    topQuestions: List["QuestionCount"]
    total: float
    unanswered: float
    unhelpfulAnswers: List["QuestionCount"]


class AiProviderStatus(TypedDict, total=False):
    keyHint: Any
    model: Any
    provider: Any
    providers: List["AiProviderStatusProvider"]
    verifiedAt: Any


class AiSourceSummary(TypedDict, total=False):
    id: str
    kind: str
    spaceId: Any
    title: str
    url: Any


class AnalyticsSummary(TypedDict, total=False):
    feedback: List["AnalyticsSummaryFeedbackItem"]
    noResultSearches: List["AnalyticsSummaryNoResultSearch"]
    pageViews: List["AnalyticsSummaryPageView"]
    topSearches: List["AnalyticsSummaryTopSearch"]
    totalViews: float
    viewsByDay: List["AnalyticsSummaryViewsByDayItem"]


class AnalyticsTags(TypedDict, total=False):
    customHead: str
    ga4: str
    gtm: str
    intercom: str
    segment: str


class AnswerResult(TypedDict, total=False):
    answer: str
    answered: bool
    citations: List["AnswerResultCitation"]
    citedRefs: List[str]
    citedTitles: List[str]


class ApiCall(TypedDict, total=False):
    at: str
    durationMs: float
    method: str
    route: str
    status: float


class ApplicationRow(TypedDict, total=False):
    assignedTo: Any
    assignedToName: Any
    attachments: List["ApplicationRowAttachment"]
    coverLetter: str
    createdAt: str
    email: str
    id: str
    links: str
    name: str
    pageId: Any
    repliedAt: Any
    replies: List["InboxReply"]
    roleTitle: str
    status: str


class ArticleDetail(TypedDict, total=False):
    answerPostId: Any
    assignedGroupId: Any
    assigneeId: Any
    authorId: Any
    authorName: Any
    authors: List["ArticleDetailAuthor"]
    authorUsername: str
    byline: Optional["Byline"]
    categoryId: Any
    commentsEnabled: bool
    coverUrl: Any
    customization: Optional["PieceCustomization"]
    excerpt: str
    featuredLink: Any
    fields: Dict[str, Any]
    furtherReading: List["ArticleDetailFurtherReadingItem"]
    id: str
    isNew: bool
    kind: str
    linkedTopics: List["LinkedTopic"]
    listed: bool
    mergedIntoId: Any
    onThisPage: Any
    op: "PostSummary"
    pinned: bool
    promotedPage: Any
    promotedPageId: Any
    publishedAt: Any
    readingMinutes: float
    releaseVersion: Any
    replies: List["PostSummary"]
    replyCount: float
    roadmapStatus: Any
    scheduledFor: Any
    seo: "ArticleDetailSeo"
    series: Any
    shippedTopicIds: List[str]
    slug: str
    state: str
    tags: List[str]
    title: str
    unread: float
    updatedAt: str
    viewCount: float
    voteCount: float


class ArticleSummary(TypedDict, total=False):
    answerPostId: Any
    authorId: Any
    authorName: Any
    authorUsername: str
    byline: Optional["Byline"]
    categoryId: Any
    commentsEnabled: bool
    coverUrl: Any
    customization: Optional["PieceCustomization"]
    excerpt: str
    featuredLink: Any
    furtherReading: List["ArticleSummaryFurtherReadingItem"]
    id: str
    isNew: bool
    kind: str
    listed: bool
    mergedIntoId: Any
    onThisPage: Any
    pinned: bool
    promotedPageId: Any
    publishedAt: Any
    readingMinutes: float
    releaseVersion: Any
    replyCount: float
    roadmapStatus: Any
    scheduledFor: Any
    series: Any
    shippedTopicIds: List[str]
    slug: str
    state: str
    tags: List[str]
    title: str
    unread: float
    updatedAt: str
    viewCount: float
    voteCount: float


class AssertionView(TypedDict, total=False):
    expects: Any
    id: str
    itemId: str
    kind: str
    lastCheckedAt: Any
    lastDetail: Any
    lastState: Any
    slot: str
    target: str


class AssetCatalog(TypedDict, total=False):
    assets: List["CatalogedAsset"]
    page: float
    pageSize: float
    total: float
    totalBytes: float


class AssetCopyNotice(TypedDict, total=False):
    path: str
    reason: str
    url: str


AtlasSyncResult = TypedDict("AtlasSyncResult", {"errors": List[str], "import": "AtlasSyncResultImport", "memberships": "AtlasSyncResultMemberships", "orgs": "AtlasSyncResultOrgs", "skipped": str}, total=False)


class AttachedComponent(TypedDict, total=False):
    enabled: bool
    id: str
    installed: bool
    name: Any
    settings: Dict[str, Any]
    slug: Any


class AuditPage(TypedDict, total=False):
    items: List["AuditRow"]
    nextCursor: Any


class AuditPageEnveloped(TypedDict, total=False):
    items: List["AuditRow"]
    page: "PageInfo"


class AuditRow(TypedDict, total=False):
    action: str
    actorUserId: Any
    after: Any
    before: Any
    createdAt: str
    id: str
    impersonatorUserId: Any
    source: str
    targetId: Any
    targetType: Any


class AuthorQuiz(TypedDict, total=False):
    id: str
    passingScore: float
    questions: List["QuizQuestion"]
    title: str


class AutomationCondition(TypedDict, total=False):
    field: str
    op: str
    value: Dict[str, Any]


class AutomationEnvelope(TypedDict, total=False):
    automation: "AutomationSummary"
    data: "AutomationSummary"


class AutomationRunEnvelope(TypedDict, total=False):
    data: "AutomationRunSummary"
    run: "AutomationRunSummary"


class AutomationRunSummary(TypedDict, total=False):
    createdAt: str
    detail: str
    id: str
    status: str
    topicId: Any
    trigger: str


class AutomationSummary(TypedDict, total=False):
    action: str
    conditions: List["AutomationCondition"]
    config: Dict[str, Any]
    createdAt: str
    enabled: bool
    id: str
    lastRunAt: Any
    name: str
    runCount: float
    spaceId: Any
    trigger: str


class Availability(TypedDict, total=False):
    platformDomain: str
    reason: str
    slugAvailable: bool
    subdomainAvailable: bool


class AvailableExtension(TypedDict, total=False):
    description: str
    icon: str
    name: str
    scopes: List[str]
    slug: str
    version: str


class Backlink(TypedDict, total=False):
    sourceId: str
    sourceKind: str
    spaceId: str
    title: str
    url: str


class BackupListing(TypedDict, total=False):
    backups: List["BackupObject"]
    configured: bool


class BackupObject(TypedDict, total=False):
    at: str
    bytes: float
    key: str


class BackupResult(TypedDict, total=False):
    bytes: float
    encrypted: bool
    key: Any
    manifestKey: str
    skipped: str


class BadgeSummary(TypedDict, total=False):
    counter: str
    description: str
    event: str
    grantCount: float
    grantedAt: str
    group: str
    icon: str
    multipleGrant: bool
    name: str
    slug: str
    threshold: float


class BillingView(TypedDict, total=False):
    configured: bool
    hasSubscription: bool
    plan: str


class BlockAttrSpec(TypedDict, total=False):
    accepts: List[str]
    name: str
    required: bool
    type: str
    values: List[Any]


class BlockChange(TypedDict, total=False):
    index: float
    op: str
    summary: str
    type: str


class BlockDiff(TypedDict, total=False):
    added: float
    blocks: List["BlockChange"]
    changed: bool
    removed: float


class BlockNodeSpec(TypedDict, total=False):
    attrs: List["BlockAttrSpec"]
    content: str
    contentRequired: bool
    type: str


class BountyView(TypedDict, total=False):
    amount: float
    awardedPostId: Any
    awardedTo: Any
    expiresAt: str
    id: str
    offeredBy: Any
    offeredByName: Any
    state: str


class BroadcastSummary(TypedDict, total=False):
    body: str
    clicks: float
    createdAt: str
    id: str
    opens: float
    recipientCount: float
    segment: Optional["Segment"]
    sentAt: Any
    status: str
    subject: str


class BrokenLink(TypedDict, total=False):
    pageSlug: str
    reason: str
    url: str


class BulkInviteResult(TypedDict, total=False):
    failed: float
    results: List["BulkInviteResultResult"]
    sent: float
    skipped: float


class BundleNotice(TypedDict, total=False):
    key: str
    reason: str


class Byline(TypedDict, total=False):
    avatarUrl: str
    name: str
    url: str


class CakedayRow(TypedDict, total=False):
    joinedAt: str
    name: str
    userId: str
    years: float


class Candidate(TypedDict, total=False):
    avatarUrl: Any
    name: str
    userId: str


class CannedReplyRow(TypedDict, total=False):
    body: "BlockDoc"
    createdAt: str
    id: str
    spaceId: Any
    title: str
    usageCount: float


class CatalogedAsset(TypedDict, total=False):
    contentType: str
    createdAt: str
    filename: str
    id: str
    size: float
    spaceId: Any
    uploaderId: Any
    url: str


class CategoryModeratorRow(TypedDict, total=False):
    createdAt: str
    email: str
    name: str
    userId: str


class CategoryPermissionRow(TypedDict, total=False):
    canCreate: bool
    canReply: bool
    canSee: bool
    groupId: str
    groupName: str


class CategorySummary(TypedDict, total=False):
    allowedTags: List[str]
    autoCloseHours: Any
    backgroundUrl: Any
    color: Any
    defaultListFilter: Any
    defaultNotificationLevel: str
    defaultSlowModeSeconds: Any
    defaultSort: Any
    defaultTags: List[str]
    description: str
    id: str
    logoUrl: Any
    minimumRequiredTags: float
    name: str
    navigateToFirstPost: Any
    numFeaturedTopics: Any
    parentId: Any
    requiredTagGroups: List["RequiredTagGroup"]
    showSubcategoryList: bool
    slug: str
    sortOrder: float
    topicCount: float
    topicTemplate: Any


class CertificateView(TypedDict, total=False):
    courseTitle: str
    issuedAt: str
    learnerName: str
    verifyId: str


class ChangelogArchiveEnveloped(TypedDict, total=False):
    changelog: str
    comments: "ChangelogArchiveEnvelopedComments"
    frontDoor: Dict[str, Any]
    homeDoc: Any
    page: "PageInfo"
    preset: str
    reactions: "ChangelogArchiveEnvelopedReactions"
    releases: List["ArticleDetail"]
    years: List["ChangelogArchiveEnvelopedYear"]


class ChangelogArchiveLegacy(TypedDict, total=False):
    changelog: str
    comments: "ChangelogArchiveLegacyComments"
    frontDoor: Dict[str, Any]
    homeDoc: Any
    page: "ChangelogArchiveLegacyPage"
    preset: str
    reactions: "ChangelogArchiveLegacyReactions"
    releases: List["ArticleDetail"]
    years: List["ChangelogArchiveLegacyYear"]


class ChangeRequestCommentCreated(TypedDict, total=False):
    body: str
    createdAt: str
    id: str


class ChangeRequestCommentRow(TypedDict, total=False):
    anchor: Optional["CommentAnchor"]
    authorId: Any
    body: str
    createdAt: str
    id: str
    pageId: Any
    parentCommentId: Any


class ChangeRequestDetail(TypedDict, total=False):
    changedPageIds: List[str]
    changeRequest: "ChangeRequestSummary"


class ChangeRequestSummary(TypedDict, total=False):
    authorId: Any
    createdAt: str
    id: str
    mergedAt: Any
    status: str
    title: str


class ChannelSummary(TypedDict, total=False):
    allowedGroupId: str
    archived: bool
    autoJoin: bool
    dmAvatarUrl: str
    dmName: str
    dmUserId: str
    id: str
    isDm: bool
    joined: bool
    lastMessageAt: str
    myMuted: bool
    myNotificationLevel: str
    name: str
    retentionDays: float
    slowModeSeconds: float
    slug: str
    spaceId: Any
    status: str
    unread: float
    visibility: str


class ChatAttachment(TypedDict, total=False):
    contentType: str
    name: str
    url: str


class ChatBookmarkSummary(TypedDict, total=False):
    authorName: str
    body: str
    channelId: str
    channelName: str
    createdAt: str
    id: str
    messageId: str
    name: Any
    note: Any
    remindAt: Any


class ChatMessageSummary(TypedDict, total=False):
    attachments: List["ChatAttachment"]
    authorId: Any
    authorName: str
    body: str
    channelId: str
    createdAt: str
    editedAt: Any
    id: str
    myReactions: List[str]
    parentId: Any
    pinnedAt: Any
    reactions: Dict[str, Any]
    replyCount: float


class ChatProviderDef(TypedDict, total=False):
    description: str
    docsUrl: str
    embed: "EmbedSpec"
    fields: List["ConnectorField"]
    icon: str
    id: str
    knowledge: "KnowledgeSpec"
    name: str
    source: str


class ChatSearchResult(TypedDict, total=False):
    messages: List["ChatMessageSummary"]
    minQueryLength: float


class Check(TypedDict, total=False):
    detail: str
    state: str


class ChromeFooter(TypedDict, total=False):
    cookieLinkPlacement: str
    css: str
    html: str
    htmlPlacement: str
    logo: Any
    logoMark: Any
    newsletter: "ChromeFooterNewsletter"


class ChromeHeader(TypedDict, total=False):
    blur: float
    border: str
    borderColor: str
    height: float
    logoHeight: float
    navCase: str
    navGap: float
    navSize: float
    navTracking: float
    navWeight: float
    opacity: float
    overlay: bool
    overlayInk: str
    shadow: str


class ChromeSecondaryCta(TypedDict, total=False):
    href: str
    label: str
    style: str


class Chunk(TypedDict, total=False):
    atomic: bool
    chunkId: str
    contentHash: str
    headingPath: List[str]
    role: str
    slot: str
    text: str
    tokens: float


class CollectionSummary(TypedDict, total=False):
    id: str
    isDefault: bool
    name: str
    slug: str
    sortKey: str


class CommentAnchor(TypedDict, total=False):
    blockIndex: float
    quote: str


class CommentSummary(TypedDict, total=False):
    anchor: Any
    authorName: str
    body: str
    createdAt: str
    id: str
    parentId: Any
    reactions: Dict[str, Any]
    resolved: bool
    status: str
    suggestion: Any


class CommunityAnalytics(TypedDict, total=False):
    activityByDay: List["CommunityAnalyticsActivityByDayItem"]
    needsAnswer: List["CommunityAnalyticsNeedsAnswerItem"]
    topContributors: List["CommunityAnalyticsTopContributor"]
    topTopics: List["CommunityAnalyticsTopTopic"]
    totals: "CommunityAnalyticsTotals"


class CommunityHit(TypedDict, total=False):
    slug: str
    snippet: str
    spaceId: str
    title: str
    topicId: str


class CommunitySettings(TypedDict, total=False):
    allowAnonymous: bool
    anonymousCaptcha: str
    defaultByline: str
    defaultSort: str
    moderateAnonymous: bool
    moderateComments: bool
    reactionsEnabled: bool
    whoCanPost: str


class CompiledRelease(TypedDict, total=False):
    content: "BlockDoc"
    mergedChangeRequests: List["CompiledReleaseMergedChangeRequest"]
    shippedItems: List["CompiledReleaseShippedItem"]
    since: Any
    title: str


class ComponentInstallItem(TypedDict, total=False):
    author: "ComponentInstallItemAuthor"
    component: "ComponentInstallItemComponent"
    createdAt: str
    description: Any
    enabled: bool
    id: str
    name: str
    placements: List["ComponentPlacement"]
    scripts: List[str]
    settings: "SettingValues"
    slug: str
    source: str
    sourceRef: Any
    updatedAt: str
    version: str


class ComponentInstallWrite(TypedDict, total=False):
    install: "ComponentInstallItem"
    strippedScripts: List["ComponentScriptNotice"]


class ComponentListing(TypedDict, total=False):
    author: "ComponentListingAuthor"
    description: Any
    featured: bool
    firstParty: bool
    hasCss: bool
    installs: float
    mine: bool
    name: str
    outlets: List[str]
    previewImages: List["ComponentListingPreviewImage"]
    publisherName: str
    settingsCount: float
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


class ComponentListingDetail(TypedDict, total=False):
    author: "ComponentListingDetailAuthor"
    component: "ComponentListingDetailComponent"
    description: Any
    featured: bool
    firstParty: bool
    hasCss: bool
    homepage: Any
    installs: float
    license: Any
    mine: bool
    name: str
    outlets: List[str]
    previewImages: List["ComponentListingDetailPreviewImage"]
    publisherName: str
    settingsCount: float
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


class ComponentMarketInstallResult(TypedDict, total=False):
    draft: Optional["ThemeDraftState"]
    install: "ComponentInstallItem"
    strippedScripts: List["ComponentScriptNotice"]


class ComponentPlacement(TypedDict, total=False):
    draftOnly: bool
    id: str
    kind: str
    name: str


class ComponentScriptNotice(TypedDict, total=False):
    path: str
    src: str


class ConfigField(TypedDict, total=False):
    help: str
    key: str
    label: str
    placeholder: str
    required: bool
    type: str


class ConflictDetail(TypedDict, total=False):
    base: Any
    draft: Any
    live: Any
    pageId: str
    title: str


class Conformance(TypedDict, total=False):
    conforms: bool
    duplicate: List[str]
    extra: List[str]
    missing: List[str]


class ConnectionSummary(TypedDict, total=False):
    autoExport: bool
    branch: str
    commitTemplate: Any
    lastSyncedAt: Any
    path: str
    provider: str
    repo: str
    webhookUrl: str


class ConnectorActivityEntry(TypedDict, total=False):
    action: str
    createdAt: str
    detail: Dict[str, Any]


class ConnectorAnswer(TypedDict, total=False):
    answer: str
    answered: bool
    citations: List["ConnectorAnswerCitation"]
    citedRefs: List[str]
    citedTitles: List[str]
    queryId: Any


class ConnectorChunkedItem(TypedDict, total=False):
    chunks: List["Chunk"]
    itemId: str
    title: str


class ConnectorChunksPage(TypedDict, total=False):
    items: List["ConnectorChunkedItem"]
    page: "PageInfo"
    policy: "ConnectorChunksPagePolicy"
    sync: "ConnectorChunksPageSync"


class ConnectorField(TypedDict, total=False):
    help: str
    key: str
    label: str
    placeholder: str
    required: bool
    type: str


class ConnectorManifest(TypedDict, total=False):
    auth: str
    capabilities: List[str]
    chunkPolicy: "ConnectorManifestChunkPolicy"
    endpoints: "ConnectorManifestEndpoints"
    provider: "ConnectorManifestProvider"
    rateLimit: "ConnectorManifestRateLimit"
    space: "ConnectorManifestSpace"


class ConnectorQuestionsIngested(TypedDict, total=False):
    accepted: float
    redacted: Dict[str, Any]


class ConnectorSearchResult(TypedDict, total=False):
    chunks: List["RetrievedChunk"]
    policy: "ConnectorSearchResultPolicy"


class ConnectorSummary(TypedDict, total=False):
    appearance: Dict[str, Any]
    canRegisterKnowledge: bool
    configuredFields: List[str]
    embedEnabled: bool
    hasToken: bool
    id: str
    knowledgeEnabled: bool
    knowledgeScopes: List[str]
    lastReadAt: Any
    lastWriteAt: Any
    missingFields: List[str]
    providerId: str
    providerName: str
    questionsIngested: float
    source: Any
    suggestionsMade: float
    themeSupport: List[str]
    tokenPrefix: Any


class ConnectorTestResult(TypedDict, total=False):
    embed: Any
    knowledge: Any


class ConnectorTokenMinted(TypedDict, total=False):
    scopes: List[str]
    token: str
    tokenPrefix: str


class ContactField(TypedDict, total=False):
    key: str
    label: str
    options: List[str]
    required: bool
    type: str


class ContentPoint(TypedDict, total=False):
    period: str
    posts: float
    topics: float


class ContentRule(TypedDict, total=False):
    enabled: bool
    id: str
    isRegex: bool
    message: str
    pattern: str
    severity: str


class ConversationDetail(TypedDict, total=False):
    archived: bool
    id: str
    messages: List["MessageView"]
    participants: List["ParticipantView"]
    subject: Any


class ConversationSummary(TypedDict, total=False):
    archived: bool
    id: str
    lastMessageAt: str
    others: List["ParticipantView"]
    snippet: str
    subject: Any
    unread: bool


class CourseLesson(TypedDict, total=False):
    completed: bool
    pageId: str
    quiz: "CourseQuizMarker"
    slug: str
    title: str


class CourseModule(TypedDict, total=False):
    id: str
    isDefault: bool
    lessons: List["CourseLesson"]
    name: str
    quiz: "CourseModuleQuiz"


class CourseOutline(TypedDict, total=False):
    modules: List["CourseModule"]
    order: List["CourseOutlineOrderItem"]
    progress: "CourseOutlineProgress"


class CourseQuizMarker(TypedDict, total=False):
    passed: bool
    passingScore: float
    quizId: str


class CreatedInviteLink(TypedDict, total=False):
    createdAt: str
    effect: str
    email: Any
    expiresAt: Any
    groupId: Any
    id: str
    maxUses: Any
    revokedAt: Any
    role: str
    spaceId: Any
    token: str
    url: str
    uses: float


class CurrencyMovementResult(TypedDict, total=False):
    balance: float
    currency: str
    delta: float


class CustomEmoji(TypedDict, total=False):
    imageUrl: str
    name: str
    shortcode: str
    token: str


class CustomReaction(TypedDict, total=False):
    contentType: str
    name: str
    slug: str
    token: str
    updatedAt: str


class CustomRoleView(TypedDict, total=False):
    capabilities: List[str]
    id: str
    name: str
    slug: str


class Department(TypedDict, total=False):
    email: str
    name: str


class DiffLine(TypedDict, total=False):
    op: str
    text: str


class DiscourseConnectView(TypedDict, total=False):
    allowedDomain: Any
    configured: bool
    defaultRole: str
    enabled: bool
    mode: str
    providerEndpoint: str
    providerUrl: Any


class DiscoveredOrigin(TypedDict, total=False):
    origin: str
    source: str
    via: str


class DndSummary(TypedDict, total=False):
    dailyEnd: Any
    dailyStart: Any
    endsAt: Any
    timezone: str


class DocDiff(TypedDict, total=False):
    added: float
    identical: bool
    lines: List["DiffLine"]
    removed: float


class DocLocale(TypedDict, total=False):
    code: str
    isDefault: bool
    label: str


class DocVersion(TypedDict, total=False):
    isDefault: bool
    key: str
    label: str


class DomainPreview(TypedDict, total=False):
    alreadyRegistered: bool
    basePath: str
    hostname: str
    otherAddressesOnHost: List[str]
    rule: str
    warnings: List[str]
    wholeHost: bool


class DomainSetup(TypedDict, total=False):
    crawlerBlocked: bool
    dns: "DomainSetupDns"
    edgeCache: "EdgeCacheFinding"
    forward: "DomainSetupForward"
    message: str
    mode: str
    served: bool


class DomainSummary(TypedDict, total=False):
    active: bool
    basePath: str
    createdAt: str
    dnsTarget: Any
    driftCheckedAt: Any
    driftedSince: Any
    hostname: str
    id: str
    ipAllowList: List[str]
    verificationFile: "DomainSummaryVerificationFile"
    verificationMeta: "DomainSummaryVerificationMeta"
    verificationRecord: "DomainSummaryVerificationRecord"
    verified: bool


class DraftSummary(TypedDict, total=False):
    draftKey: str
    preview: str
    updatedAt: str


class DraftView(TypedDict, total=False):
    conformance: "Conformance"
    content: "BlockDoc"
    preset: Any
    revisionId: str
    sections: Dict[str, Any]
    status: str
    title: str


class EdgeCacheFinding(TypedDict, total=False):
    age: Any
    cacheStatus: Any
    detail: str
    heldPastOurTtl: bool
    sMaxAge: Any
    verdict: str


class EffectiveShape(TypedDict, total=False):
    params: List["SpaceTypeField"]
    sections: List["SpaceTypeSection"]
    space: "SpaceShape"
    unknown: List[str]


class EffectiveSlotRole(TypedDict, total=False):
    declared: bool
    key: str
    rank: float
    role: str


class ElementStyleRule(TypedDict, total=False):
    declarations: Dict[str, Any]
    media: str
    page: str
    scheme: str
    selector: str
    state: str


class EmailPreview(TypedDict, total=False):
    html: str
    locale: Any
    preheader: str
    source: str
    subject: str
    text: str


class EmailTemplateDetail(TypedDict, total=False):
    audience: str
    defaults: "EmailTemplateDetailDefaults"
    description: str
    group: str
    key: str
    overrides: List["EmailTemplateOverride"]
    title: str
    variables: List["EmailVariableDef"]


class EmailTemplateOverride(TypedDict, total=False):
    blocks: List["EmailTemplateOverrideBlock"]
    id: str
    key: str
    locale: Any
    preheader: Any
    spaceId: Any
    subject: str
    updatedAt: str


class EmailTemplateSummary(TypedDict, total=False):
    audience: str
    description: str
    group: str
    key: str
    overrides: List["EmailTemplateSummaryOverride"]
    title: str


class EmailVariableDef(TypedDict, total=False):
    description: str
    example: Any
    optional: bool
    path: str
    type: str


class EmbedSpec(TypedDict, total=False):
    colorSchemeMap: "EmbedSpecColorSchemeMap"
    connectOrigins: List[str]
    consent: str
    initScript: str
    origin: str
    platformSafe: bool
    script: str
    src: str
    themeInit: "EmbedSpecThemeInit"
    themeSupport: List[str]


class EventCapacityState(TypedDict, total=False):
    capacity: Any
    full: bool
    going: float
    spotsLeft: Any
    waitlisted: float
    waitlistOpen: bool


class EventRsvpCleared(TypedDict, total=False):
    counts: "EventRsvpCounts"
    status: Any


class EventRsvpCounts(TypedDict, total=False):
    declined: float
    going: float
    interested: float
    waitlist: float


class EventRsvpResult(TypedDict, total=False):
    capacityState: "EventCapacityState"
    counts: "EventRsvpCounts"
    status: str
    waitlisted: bool


class EventSummary(TypedDict, total=False):
    capacity: Any
    capacityState: "EventCapacityState"
    counts: "EventRsvpCounts"
    coverUrl: Any
    customization: Optional["PieceCustomization"]
    description: str
    endsAt: Any
    id: str
    location: Any
    slug: str
    startsAt: str
    state: str
    timezone: str
    title: str
    topicId: Any
    url: Any


class ExpertSuggestion(TypedDict, total=False):
    name: str
    pageId: str
    pageTitle: str
    score: float
    spaceId: str
    userId: str


class ExplorerResult(TypedDict, total=False):
    columns: List[str]
    rowCount: float
    rows: List[Dict[str, Any]]
    truncated: bool


class ExportedSpace(TypedDict, total=False):
    collections: List["ExportedSpaceCollection"]
    id: str
    name: str
    pages: List["ExportedSpacePage"]
    settings: Dict[str, Any]
    slug: str
    topics: List["ExportedSpaceTopic"]
    type: str
    visibility: str


class ExtComment(TypedDict, total=False):
    authorName: str
    body: str
    createdAt: str
    id: str
    parentId: Any
    status: str


class ExtCommentRef(TypedDict, total=False):
    id: str
    status: str


class ExtensionDelivery(TypedDict, total=False):
    attempts: float
    completedAt: Any
    createdAt: str
    error: Any
    event: str
    id: str
    status: str
    statusCode: Any


class ExtensionInstallResult(TypedDict, total=False):
    accessToken: str
    integration: "InstalledExtensionSummary"


class ExternalStanding(TypedDict, total=False):
    iconUrl: Any
    label: str
    profileUrl: Any
    source: str
    tier: Any
    updatedAt: str
    value: Any


class ExtMember(TypedDict, total=False):
    name: str
    role: str
    userId: str


class ExtPage(TypedDict, total=False):
    content: "BlockDoc"
    metadata: Dict[str, Any]
    title: str


class ExtPageSummary(TypedDict, total=False):
    id: str
    published: bool
    slug: str
    title: str


class FailedJob(TypedDict, total=False):
    attemptsMade: float
    failedReason: str
    id: str
    name: str
    timestamp: Any


class FeaturedTopic(TypedDict, total=False):
    slug: str
    spaceId: str
    spaceType: str
    title: str
    topicId: str


class FieldDef(TypedDict, total=False):
    editableByUser: bool
    entityType: str
    id: str
    key: str
    label: str
    options: List[str]
    requiredAtSignup: bool
    showOnCard: bool
    sortOrder: float
    type: str
    visibility: str


class FieldValue(TypedDict, total=False):
    key: str
    label: str
    type: str
    value: str


class Finding(TypedDict, total=False):
    note: str
    pageId: str
    pageTitle: str
    severity: str


class FirstResponsePoint(TypedDict, total=False):
    avgHours: Any
    period: str


class FlagHistoryEntry(TypedDict, total=False):
    action: str
    actorName: str
    createdAt: str
    detail: Dict[str, Any]
    id: str


class FlagRow(TypedDict, total=False):
    authorName: str
    autoHidden: bool
    channelId: Any
    chatMessageId: Any
    claimedAt: Any
    claimedBy: Any
    claimedByName: Any
    createdAt: str
    flagType: str
    id: str
    postId: Any
    postStatus: str
    priority: str
    reason: str
    score: float
    target: str
    topicId: Any
    topicScope: bool


class FlagTypeCatalogueEntry(TypedDict, total=False):
    builtIn: bool
    description: str
    enabled: bool
    id: Any
    name: str
    surfaces: List[str]
    weight: float


class FontFace(TypedDict, total=False):
    display: str
    family: str
    format: str
    src: str
    style: str
    unicodeRange: str
    weight: str


class FormDefinition(TypedDict, total=False):
    consentText: Any
    createdAt: str
    fields: List["FormField"]
    id: str
    layout: str
    name: str
    notifyEmails: List[str]
    redirectUrl: Any
    status: str
    submitLabel: Any
    successMessage: Any
    updatedAt: str


class FormField(TypedDict, total=False):
    help: str
    label: str
    max: float
    min: float
    name: str
    options: List[str]
    pattern: str
    placeholder: str
    required: bool
    type: str
    value: str


class FormSubmissionRow(TypedDict, total=False):
    consentAt: Any
    consentText: Any
    createdAt: str
    data: Dict[str, Any]
    email: Any
    formId: str
    id: str
    pageUrl: Any
    spam: bool


class FormSummary(TypedDict, total=False):
    consentText: Any
    createdAt: str
    fields: List["FormField"]
    id: str
    lastSubmissionAt: Any
    layout: str
    name: str
    notifyEmails: List[str]
    redirectUrl: Any
    status: str
    submissionCount: float
    submitLabel: Any
    successMessage: Any
    updatedAt: str


class ForumListEnveloped(TypedDict, total=False):
    page: "PageInfo"
    topics: List["ArticleSummary"]
    unread: Dict[str, Any]


class ForumListLegacy(TypedDict, total=False):
    hasMore: bool
    page: float
    pageSize: float
    topics: List["ArticleSummary"]
    unread: Dict[str, Any]


class Freshness(TypedDict, total=False):
    ageDays: float
    confidence: float
    stale: bool
    verifiedAt: Any


class FreshnessIssue(TypedDict, total=False):
    description: str
    severity: str


class FreshnessReport(TypedDict, total=False):
    confidence: float
    isStale: bool
    issues: List["FreshnessIssue"]
    suggestions: List[str]


class FrontDoor(TypedDict, total=False):
    pass


class GenerateResult(TypedDict, total=False):
    generated: float
    pages: List["GenerateResultPage"]
    updated: float


class GithubAgentStatus(TypedDict, total=False):
    canPostComments: bool
    connected: bool
    repoFullName: Any


class GmailSettings(TypedDict, total=False):
    clientId: str
    mailbox: str


class GradedQuestion(TypedDict, total=False):
    correct: bool
    correctIndexes: List[float]
    explanation: str
    questionId: str
    selected: List[float]


class GradeResult(TypedDict, total=False):
    answersRevealed: bool
    correctCount: float
    passed: bool
    questions: List["GradedQuestion"]
    score: float
    total: float


class GraphSettings(TypedDict, total=False):
    clientId: str
    mailbox: str
    tenantId: str


class GroupDetail(TypedDict, total=False):
    autoJoinDomains: Any
    automatic: bool
    bio: Any
    categoryNotificationDefaults: Dict[str, Any]
    defaultNotificationLevel: str
    description: str
    flair: Any
    flairBgColor: Any
    flairColor: Any
    flairIcon: Any
    grantTrustLevel: Any
    id: str
    inboxEmail: Any
    inboxEnabled: bool
    isManager: bool
    isMember: bool
    joinPolicy: str
    memberCount: float
    members: List["GroupMemberSummary"]
    membersVisibility: str
    mentionableLevel: str
    messageableLevel: str
    name: str
    requestPending: bool
    slug: str
    tagNotificationDefaults: Dict[str, Any]
    title: Any
    visibility: str
    watchedCategoryIds: List[str]
    watchedTagIds: List[str]


class GroupGrantRow(TypedDict, total=False):
    createdAt: str
    customRoleId: Any
    effect: str
    groupId: str
    groupName: str
    id: str
    role: str
    spaceId: Any


class GroupMailboxStatus(TypedDict, total=False):
    configured: bool
    enabled: bool
    fromEmail: Any
    lastError: Any
    lastPolledAt: Any
    provider: Any
    secretsSet: Dict[str, Any]
    settings: Optional["ImapSettings"]


class GroupMemberSummary(TypedDict, total=False):
    email: str
    isManager: bool
    name: str
    userId: str


class GroupSummary(TypedDict, total=False):
    autoJoinDomains: Any
    automatic: bool
    bio: Any
    categoryNotificationDefaults: Dict[str, Any]
    defaultNotificationLevel: str
    description: str
    flair: Any
    flairBgColor: Any
    flairColor: Any
    flairIcon: Any
    grantTrustLevel: Any
    id: str
    inboxEmail: Any
    inboxEnabled: bool
    isManager: bool
    isMember: bool
    joinPolicy: str
    memberCount: float
    membersVisibility: str
    mentionableLevel: str
    messageableLevel: str
    name: str
    requestPending: bool
    slug: str
    tagNotificationDefaults: Dict[str, Any]
    title: Any
    visibility: str
    watchedCategoryIds: List[str]
    watchedTagIds: List[str]


class GrowthExtraReport(TypedDict, total=False):
    activeDaily: List["GrowthPoint"]
    bookmarksDaily: List["GrowthPoint"]
    flagsDaily: List["GrowthPoint"]
    likesDaily: List["GrowthPoint"]
    moderatorActivity: List["ModeratorActivityPoint"]
    noResultSearchTerms: List["SearchTermPoint"]
    pageViews: "GrowthExtraReportPageViews"
    postsDaily: List["GrowthPoint"]
    referrers: "GrowthExtraReportReferrers"
    searchesNoResultsDaily: List["GrowthPoint"]
    signupsDaily: List["GrowthPoint"]
    timeToFirstResponse: "GrowthExtraReportTimeToFirstResponse"
    topicsDaily: List["GrowthPoint"]
    topicsWithNoReplies: float
    topSearchTerms: List["SearchTermPoint"]
    window: "GrowthExtraReportWindow"


class GrowthPoint(TypedDict, total=False):
    count: float
    period: str


class GrowthReport(TypedDict, total=False):
    activeUsers: "GrowthReportActiveUsers"
    content: List["ContentPoint"]
    flags: List["GrowthPoint"]
    likes: List["GrowthPoint"]
    retention: List["RetentionCohort"]
    signups: List["GrowthPoint"]
    solved: List["GrowthPoint"]
    trustLevels: List["TrustLevelPoint"]
    window: "GrowthReportWindow"


class HealthReport(TypedDict, total=False):
    checkedAt: str
    problems: List["Problem"]
    usage: "StorageUsage"


class HostOriginPolicy(TypedDict, total=False):
    contributes: "HostOriginPolicyContributes"
    host: str
    kind: str
    notes: List[str]
    url: str


class IdentityOptions(TypedDict, total=False):
    adoptableTitles: List[str]
    current: "IdentityOptionsCurrent"
    primaryGroups: List["IdentityOptionsPrimaryGroup"]


class ImapSettings(TypedDict, total=False):
    imapFolder: str
    imapHost: str
    imapPort: float
    imapTls: bool
    imapUser: str
    smtpHost: str
    smtpPort: float
    smtpTls: bool
    smtpUser: str


class ImportOutcome(TypedDict, total=False):
    collisions: List[str]
    created: float
    dryRun: bool
    operations: float
    pageId: str
    pageIds: List[str]
    pages: float
    replaced: float
    skipped: float
    slug: str
    slugs: List[str]
    warnings: List[str]


class ImportResult(TypedDict, total=False):
    brokenLinks: List["ImportResultBrokenLink"]
    collection: "ImportResultCollection"
    collisions: List[str]
    created: float
    dryRun: bool
    failed: float
    failures: List["ImportResultFailure"]
    files: float
    imported: float
    plan: List["PlanEntry"]
    pruned: float
    prunedSlugs: List[str]
    redirects: List["ImportResultRedirect"]
    refused: List[str]
    replaced: float
    retired: List[str]
    skipped: float


class ImportSummary(TypedDict, total=False):
    collectionsCreated: float
    pagesCreated: float
    pagesSkipped: float
    spacesCreated: float
    spacesReused: float
    topicsCreated: float
    topicsSkipped: float


class InboxReply(TypedDict, total=False):
    authorName: str
    authorUserId: Any
    body: str
    createdAt: str
    id: str
    parentId: str


class IncidentSummary(TypedDict, total=False):
    body: Any
    fields: Dict[str, Any]
    id: str
    resolvedAt: Any
    scheduledFor: Any
    scheduledUntil: Any
    severity: str
    startedAt: str
    state: str
    title: str
    updatedAt: str
    updates: List["IncidentUpdate"]


class IncidentUpdate(TypedDict, total=False):
    body: str
    createdAt: str
    state: Any


class IncomingWebhookCreated(TypedDict, total=False):
    secret: str
    webhook: "IncomingWebhookSummary"


class IncomingWebhookSummary(TypedDict, total=False):
    channelId: str
    createdAt: str
    createdBy: Any
    id: str
    lastUsedAt: Any
    name: str
    revokedAt: Any
    url: str


class IngestedQuestion(TypedDict, total=False):
    askedAt: str
    citedChunks: List[str]
    id: str
    outcome: str
    source: str
    text: str


class InstalledExtensionSummary(TypedDict, total=False):
    availableEvents: List[str]
    blocks: List["InstalledExtensionSummaryBlock"]
    configFields: List["InstalledExtensionSummaryConfigField"]
    configuredFields: List[str]
    currency: str
    description: str
    enabled: bool
    events: List[str]
    extensionId: str
    icon: str
    id: str
    lastDispatchedAt: Any
    latestVersion: str
    name: str
    owned: bool
    priceCents: float
    pricing: str
    published: bool
    reviewNote: str
    reviewStatus: str
    scopes: List[str]
    slug: str
    surfaces: List["InstalledExtensionSummarySurface"]
    updateAvailable: bool
    verified: bool
    version: str


class InstalledSummary(TypedDict, total=False):
    configuredFields: List[str]
    enabled: bool
    events: List[str]
    id: str
    integrationId: str
    lastDispatchedAt: Any
    name: str


class IntegrationDef(TypedDict, total=False):
    category: str
    configFields: List["ConfigField"]
    delivery: "IntegrationDefDelivery"
    description: str
    events: List[str]
    id: str
    name: str


class InviteLinkRow(TypedDict, total=False):
    createdAt: str
    effect: str
    email: Any
    expiresAt: Any
    groupId: Any
    id: str
    maxUses: Any
    revokedAt: Any
    role: str
    spaceId: Any
    uses: float


class InviteRow(TypedDict, total=False):
    effect: str
    email: str
    expiresAt: str
    groupId: Any
    id: str
    role: str
    spaceId: Any


class ItemMovementResult(TypedDict, total=False):
    delta: float
    itemKey: str
    quantity: float


class ItemRead(TypedDict, total=False):
    conformance: "Conformance"
    contentHash: str
    contentIn: str
    id: str
    kind: str
    markdown: str
    preset: str
    sections: Dict[str, Any]
    slug: str
    title: str


class ItemRef(TypedDict, total=False):
    conformance: "Conformance"
    id: str
    kind: str
    preset: str
    slug: str
    title: str


class ItemSummary(TypedDict, total=False):
    contentHash: str
    contentIn: str
    deleted: bool
    freshness: "Freshness"
    group: str
    id: str
    kind: str
    markdown: str
    published: bool
    sections: Dict[str, Any]
    shapeKey: str
    slug: str
    state: str
    title: str
    updatedAt: str
    url: str


class JoinRequestRow(TypedDict, total=False):
    createdAt: str
    email: str
    id: str
    name: str
    userId: str


class KindSlot(TypedDict, total=False):
    key: str
    kind: str
    label: str
    required: bool
    role: str


class KnowledgeGap(TypedDict, total=False):
    kind: str
    lastSeenAt: Any
    occurrences: float
    score: float
    spaceId: str
    text: str
    topicId: str


class KnowledgeRegister(TypedDict, total=False):
    authHeader: str
    body: str
    endpoint: str
    idPath: str
    keyField: str
    method: str


class KnowledgeRegistration(TypedDict, total=False):
    provider: str
    registered: bool
    sourceId: Any


class KnowledgeSpec(TypedDict, total=False):
    capabilities: List[str]
    pull: bool
    register: "KnowledgeRegister"
    setupHint: str
    setupUrl: str


class LegalDocView(TypedDict, total=False):
    body: Any
    content: Any
    customization: "PieceCustomization"
    fields: Dict[str, Any]
    id: str
    kind: str
    onThisPage: Any
    pageId: Any
    required: bool
    seoDescription: Any
    spaceId: Any
    title: str
    updatedAt: str
    version: float


class LegalGateOverrideView(TypedDict, total=False):
    anonymous: str
    hasOverride: bool
    inherits: bool
    scope: str


class LegalStatus(TypedDict, total=False):
    documents: List["LegalStatusDocument"]
    pending: List[str]


class LevelProgress(TypedDict, total=False):
    currentLevelXp: float
    level: float
    nextLevelXp: Any
    xp: float
    xpForNextLevel: Any
    xpIntoLevel: float


class LinkedTopic(TypedDict, total=False):
    createdAt: str
    fromPostNumber: float
    id: str
    slug: str
    title: str


class LintFinding(TypedDict, total=False):
    code: str
    message: str
    severity: str
    where: str


class LintReport(TypedDict, total=False):
    counts: "LintReportCounts"
    findings: List["LintFinding"]
    grade: str
    operationCount: float
    score: float


class LtiConfigView(TypedDict, total=False):
    clientId: str
    configured: bool
    enabled: bool
    issuer: str


class MailLogRow(TypedDict, total=False):
    createdAt: str
    detail: Any
    email: str
    jobName: str
    status: str


class MailProviderView(TypedDict, total=False):
    domain: Any
    keyHint: Any
    provider: Any
    providers: List["MailProviderViewProvider"]
    region: Any
    verifiedAt: Any
    webhookUrl: str


class ManifestExtra(TypedDict, total=False):
    key: str
    kind: str
    space: str


class ManifestResult(TypedDict, total=False):
    dryRun: bool
    extras: List["ManifestExtra"]
    ok: bool
    summary: "ManifestResultSummary"
    units: List["ManifestUnitReport"]


class ManifestUnitReport(TypedDict, total=False):
    action: str
    changes: List[str]
    error: str
    key: str
    kind: str
    space: str
    status: str


class MarkSpec(TypedDict, total=False):
    attrs: List["BlockAttrSpec"]
    type: str


class MemberProfile(TypedDict, total=False):
    activity: List["ActivityItem"]
    badges: List["BadgeSummary"]
    cardBackgroundUrl: Any
    customFields: List["PublicFieldValue"]
    external: List["ExternalStanding"]
    featuredTopic: Optional["FeaturedTopic"]
    profileBackgroundUrl: Any
    trust: "TrustSummary"
    user: "MemberProfileUser"


class MemberRow(TypedDict, total=False):
    effect: str
    email: str
    externalId: Any
    externalProvider: Any
    name: str
    role: str
    spaceId: Any
    userId: str


class MergeRules(TypedDict, total=False):
    blockOnChangesRequested: bool
    requireAllReviewers: bool
    requiredApprovals: float


class MessageLink(TypedDict, total=False):
    anchor: str
    channelId: str
    messageId: str
    url: str


class MessageView(TypedDict, total=False):
    createdAt: str
    editedAt: Any
    id: str
    senderId: Any
    senderName: str
    text: str


class ModeratorActivityPoint(TypedDict, total=False):
    actorId: Any
    actorName: str
    count: float


class MonitorState(TypedDict, total=False):
    declaredState: Any
    failingChecks: float
    group: Any
    history: List[Any]
    historyUptime: List[Any]
    id: str
    latencyMs: Any
    name: str
    state: str
    status: str
    uptime: Any
    window: "UptimeWindow"


class MonitorSummary(TypedDict, total=False):
    alertsEnabled: bool
    bodyExpect: Any
    bodyPath: Any
    certExpiryDays: Any
    declaredState: Any
    expectStatus: Any
    failureThreshold: float
    group: Any
    id: str
    intervalSeconds: float
    keyword: Any
    kind: str
    lastPingAt: str
    maxLatencyMs: Any
    method: str
    name: str
    pingUrl: str
    requestBody: Any
    requestHeaderNames: List[str]
    successThreshold: float
    url: str
    visible: bool


class MyCertificate(TypedDict, total=False):
    certificate: Optional["CertificateView"]
    complete: bool
    progress: "MyCertificateProgress"


class NotificationSummary(TypedDict, total=False):
    actors: List[str]
    count: float
    createdAt: str
    data: Dict[str, Any]
    groupIds: List[str]
    id: str
    link: Any
    read: bool
    type: str


class OauthClientCreated(TypedDict, total=False):
    createdAt: Any
    id: str
    name: str
    redirectUris: List[str]
    scopes: List[str]
    secret: str
    type: str


class OauthClientView(TypedDict, total=False):
    createdAt: Any
    id: str
    name: str
    redirectUris: List[str]
    scopes: List[str]
    type: str


class OnboardingResult(TypedDict, total=False):
    organization: "OnboardingResultOrganization"
    publicUrl: Any
    spaceIds: List[str]


class Onebox(TypedDict, total=False):
    authorName: str
    description: Any
    embedHtml: str
    faviconUrl: Any
    imageUrl: Any
    providerName: str
    siteName: Any
    thumbnailUrl: str
    title: Any
    type: str
    url: str


class OpenApiOperation(TypedDict, total=False):
    baseUrl: str
    codeSamples: List["OpenApiOperationCodeSample"]
    description: str
    method: str
    operationId: str
    parameters: List["OpenApiParam"]
    path: str
    requestBody: "OpenApiOperationRequestBody"
    responses: List["OpenApiResponse"]
    security: "OpenApiSecurity"
    summary: str


OpenApiParam = TypedDict("OpenApiParam", {"description": str, "in": str, "name": str, "required": bool, "type": str}, total=False)


class OpenApiResponse(TypedDict, total=False):
    contentType: str
    description: str
    schema: str
    status: str


class OpenApiSecurity(TypedDict, total=False):
    optional: bool
    options: List[List[Any]]


class OrgAnswer(TypedDict, total=False):
    answer: str
    answered: bool
    citations: List["OrgAnswerCitation"]
    citedRefs: List[str]
    citedTitles: List[str]
    queryId: Any


class OrgCloudflareView(TypedDict, total=False):
    enabled: bool
    lastError: Any
    lastVerifiedAt: Any
    secretSet: bool
    zoneMode: Any


class OrgComponentListing(TypedDict, total=False):
    author: "OrgComponentListingAuthor"
    description: Any
    featured: bool
    firstParty: bool
    hasCss: bool
    installedId: Any
    installs: float
    mine: bool
    name: str
    outlets: List[str]
    previewImages: List["OrgComponentListingPreviewImage"]
    publisherName: str
    settingsCount: float
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


class OrgEventsReport(TypedDict, total=False):
    byDay: List["OrgEventsReportByDayItem"]
    byType: List["OrgEventsReportByTypeItem"]
    topSpaces: List["OrgEventsReportTopSpace"]
    total: float
    windowDays: float


class OrgExport(TypedDict, total=False):
    exportedAt: str
    format: str
    members: List["OrgExportMember"]
    organization: "OrgExportOrganization"
    spaces: List["ExportedSpace"]
    version: float


class OrgSearchHit(TypedDict, total=False):
    collectionId: str
    pageId: str
    rank: float
    slug: str
    snippet: str
    spaceId: str
    spaceName: str
    title: str
    updatedAt: str
    url: str


class OrgSummary(TypedDict, total=False):
    contentLanguage: Any
    createdAt: str
    id: str
    inboundEmailDomain: Any
    name: str
    slug: str


class OutageWindow(TypedDict, total=False):
    endedAt: Any
    failures: float
    monitorId: str
    monitorName: str
    ongoing: bool
    startedAt: str


class OutletSpec(TypedDict, total=False):
    context: List[str]
    description: str
    name: str
    repeats: bool
    surface: str
    wraps: bool


class OwnComponentListing(TypedDict, total=False):
    approvedAt: Any
    author: "OwnComponentListingAuthor"
    description: Any
    featured: bool
    firstParty: bool
    hasCss: bool
    installs: float
    live: bool
    mine: bool
    name: str
    outlets: List[str]
    pending: bool
    previewImages: List["OwnComponentListingPreviewImage"]
    publisherName: str
    reviewNote: str
    settingsCount: float
    slug: str
    sourceInstallId: Any
    spaceTypes: List[str]
    status: str
    submittedAt: Any
    tags: List[str]
    version: str


class OwnThemeListing(TypedDict, total=False):
    approvedAt: Any
    author: "OwnThemeListingAuthor"
    cardUrl: str
    currency: str
    description: Any
    featured: bool
    firstParty: bool
    installs: float
    live: bool
    mine: bool
    name: str
    pending: bool
    previewImages: List["OwnThemeListingPreviewImage"]
    priceCents: float
    pricing: str
    publisherName: str
    requiredOrigins: "OwnThemeListingRequiredOrigins"
    reviewNote: str
    slug: str
    sourceComponentId: Any
    spaceTypes: List[str]
    status: str
    submittedAt: Any
    tags: List[str]
    version: str


class PageDetail(TypedDict, total=False):
    collection: "PageDetailCollection"
    content: Dict[str, Any]
    contentHash: str
    draftUpdatedAt: Any
    hasDraft: bool
    id: str
    locale: str
    metadata: Dict[str, Any]
    parentId: Any
    slug: str
    status: str
    title: str
    updatedAt: str
    url: Any
    versionKey: str


class PageInventoryRow(TypedDict, total=False):
    collectionId: str
    collectionName: str
    enriched: bool
    id: str
    parentId: Any
    published: bool
    slug: str
    title: str
    updatedAt: str
    wordCount: float


class PageListRow(TypedDict, total=False):
    collectionId: str
    id: str
    parentId: Any
    slug: str
    sortKey: str
    status: str
    title: str
    updatedAt: str
    visibility: str


class PageNode(TypedDict, total=False):
    audience: Any
    children: List["PageNode"]
    externalUrl: Any
    fields: Dict[str, Any]
    hasLive: bool
    hideFromNav: bool
    icon: Any
    id: str
    parentId: Any
    shapeKey: Any
    shapeLabel: Any
    slug: str
    sortKey: str
    title: str
    updatedAt: str


class PageTrashRow(TypedDict, total=False):
    deletedAt: Any
    id: str
    slug: str
    title: str


class ParticipantView(TypedDict, total=False):
    avatarUrl: Any
    name: str
    userId: str


class PatScopeDefinition(TypedDict, total=False):
    capabilities: List[str]
    description: str
    name: str


class PatSummary(TypedDict, total=False):
    applicationName: Any
    capabilities: Any
    constraints: Any
    createdAt: str
    expiresAt: Any
    id: str
    kind: str
    lastUsedAt: Any
    name: str
    scopeGrants: Any
    scopes: List[str]
    spaceIds: Any


class PendingInvite(TypedDict, total=False):
    expiresAt: str
    id: str
    invitedBy: Any
    organizationId: str
    organizationName: str
    role: str


class PendingLegalDoc(TypedDict, total=False):
    acceptedVersion: Any
    kind: str
    title: str
    version: float


class PermalinkResolution(TypedDict, total=False):
    slug: Any
    targetType: str
    url: Any


class PermalinkRow(TypedDict, total=False):
    createdAt: str
    externalUrl: Any
    fromPath: str
    id: str
    targetCategoryId: Any
    targetTag: Any
    targetTopicId: Any
    targetType: str
    targetUserId: Any


class PieceCustomization(TypedDict, total=False):
    customCss: str
    jsonLd: str
    ogDescription: str
    ogTitle: str
    shareImageUrl: str
    theme: "PieceTheme"
    twitterCard: str


class PieceTheme(TypedDict, total=False):
    accentColor: str
    bodyFontFamily: str
    colorScheme: str
    components: "PieceThemeComponents"
    contentWidth: str
    customFontFamily: str
    font: str
    headingFontFamily: str
    layout: "PieceThemeLayout"
    monoFontFamily: str
    motion: "PieceThemeMotion"
    palette: "PieceThemePalette"
    paletteDark: "PieceThemePaletteDark"
    primaryColor: str


class PlanEntry(TypedDict, total=False):
    action: str
    collision: bool
    slug: str
    title: str


class PointsLeader(TypedDict, total=False):
    name: str
    points: float
    userId: str


class PollOptionResult(TypedDict, total=False):
    id: str
    text: str
    votes: float


class PollSummary(TypedDict, total=False):
    allowedGroupId: Any
    allowMultiple: bool
    average: Any
    chartType: str
    closed: bool
    closedAt: Any
    closesAt: Any
    id: str
    maxChoices: Any
    maxValue: Any
    minChoices: Any
    minValue: Any
    myVotes: List[str]
    options: List["PollOptionResult"]
    pollType: str
    public: bool
    question: str
    rankedResult: Optional["RankedResult"]
    resultsHidden: bool
    resultsVisibility: str
    step: Any
    totalVotes: float
    type: str
    voterCount: float


class PollVoterBreakdown(TypedDict, total=False):
    options: List["PollVoterBreakdownOption"]
    pollId: str
    public: bool


class PostRevisionDetail(TypedDict, total=False):
    content: "BlockDoc"
    createdAt: str
    diff: "DocDiff"
    editorId: Any
    editorName: Any
    editReason: Any
    id: str
    revision: float


class PostRevisionMeta(TypedDict, total=False):
    createdAt: str
    editorId: Any
    editorName: Any
    editReason: Any
    id: str
    revision: float


class PostSummary(TypedDict, total=False):
    actionCode: Any
    actionData: Any
    authorBadges: List["PostSummaryAuthorBadge"]
    authorFlair: "PostSummaryAuthorFlair"
    authorId: Any
    authorName: str
    authorTitle: str
    authorTrust: float
    authorUsername: str
    content: "BlockDoc"
    createdAt: str
    editedAt: Any
    flagCount: float
    id: str
    isOp: bool
    parentAuthorName: str
    parentPostId: Any
    parentPostNumber: float
    postNumber: float
    reactions: Dict[str, Any]
    status: str
    voteCount: float
    whisper: bool
    wiki: bool


class PrefsSummary(TypedDict, total=False):
    communitySummary: bool
    deliverEmail: str
    deliverPush: str
    digestHour: float
    mailingListMode: str
    messagesFrom: str
    mutedTypes: List[str]
    pushMutedTypes: List[str]
    quietEnd: Any
    quietStart: Any
    timezone: str


class PreviewLink(TypedDict, total=False):
    expiresAt: str
    token: str
    urls: List[str]
    windowSeconds: float


class PreviewPage(TypedDict, total=False):
    content: Any
    id: str
    metadata: Dict[str, Any]
    status: str
    title: str
    unpublished: bool


class Problem(TypedDict, total=False):
    detail: str
    id: str
    message: str
    severity: str


class PromotionResult(TypedDict, total=False):
    collectionId: str
    pageId: str
    pageSlug: str
    topicId: str


class ProposedDraft(TypedDict, total=False):
    fromQuestions: float
    itemId: str
    sections: Dict[str, Any]
    title: str
    unresolved: float
    written: str


class ProviderSpec(TypedDict, total=False):
    defaultDimensions: float
    defaultModel: str
    id: str
    name: str


class ProxyResponse(TypedDict, total=False):
    body: str
    headers: Dict[str, Any]
    status: float


class PublicCaptcha(TypedDict, total=False):
    provider: Any
    siteKey: Any


class PublicFieldValue(TypedDict, total=False):
    key: str
    label: str
    showOnCard: bool
    type: str
    value: str
    visibility: str


class PublicFormDefinition(TypedDict, total=False):
    consentText: Any
    fields: List["FormField"]
    id: str
    layout: str
    name: str
    redirectUrl: Any
    status: str
    submitLabel: Any
    successMessage: Any


class PublicLegalDoc(TypedDict, total=False):
    body: Any
    content: Any
    customization: "PieceCustomization"
    fields: Dict[str, Any]
    kind: str
    onThisPage: Any
    pageId: Any
    required: bool
    seoDescription: Any
    spaceId: Any
    title: str
    updatedAt: str
    version: float


class PublicStatusBoard(TypedDict, total=False):
    historyDays: List[str]
    homeDoc: Any
    incidents: List["IncidentSummary"]
    monitors: List["MonitorState"]
    outages: List["OutageWindow"]
    overall: str
    status: str
    window: "UptimeWindow"


class PublicUser(TypedDict, total=False):
    avatarSource: Any
    avatarUrl: Any
    bio: Any
    createdAt: str
    email: str
    emailVerified: bool
    id: str
    locale: Any
    location: Any
    name: str
    profileHidden: bool
    username: str
    websiteUrl: Any


class PublishedFrontDoorOption(TypedDict, total=False):
    choices: List[str]
    default: Any
    key: str
    kind: str


class PublishedPage(TypedDict, total=False):
    content: "BlockDoc"
    contributors: List["PublishedPageContributor"]
    metadata: Dict[str, Any]
    revisionId: str
    title: str
    updatedAt: str


class PublishedPreset(TypedDict, total=False):
    description: str
    label: str
    name: str
    recommended: bool


class PublishedShapePreset(TypedDict, total=False):
    description: str
    label: str
    layout: List["PublishedShapePresetLayoutItem"]
    name: str
    sections: List["PublishedShapePresetSection"]


class QuestionCluster(TypedDict, total=False):
    citedChunks: List[str]
    count: float
    label: str
    questions: List[str]
    unresolved: float


class QuestionCount(TypedDict, total=False):
    count: float
    question: str


class QueuedResync(TypedDict, total=False):
    jobId: str
    poll: str
    queued: bool
    spec: "StoredSpecSummary"


class QueueSummary(TypedDict, total=False):
    counts: Dict[str, Any]
    name: str


class QuizPolicy(TypedDict, total=False):
    cooldownSeconds: float
    maxAttempts: float
    reveal: str


class QuizQuestion(TypedDict, total=False):
    choices: List[str]
    correctIndexes: List[float]
    explanation: str
    id: str
    prompt: str


class QuotaStatus(TypedDict, total=False):
    limit: Any
    metric: str
    nearLimit: bool
    remaining: Any
    used: float


class RankedResult(TypedDict, total=False):
    rounds: List["RankedRound"]
    totalBallots: float
    winnerId: Any


class RankedRound(TypedDict, total=False):
    continuing: float
    eliminated: Any
    exhausted: float
    majority: bool
    round: float
    tallies: List["RankedRoundTally"]


class RankedRoundTally(TypedDict, total=False):
    optionId: str
    votes: float


class ReaderAddressIndex(TypedDict, total=False):
    asOf: str
    complete: bool
    slugs: List[str]


class ReaderAnalytics(TypedDict, total=False):
    customHead: str
    ga4: str
    gtm: str
    intercom: str
    segment: str


class ReaderAuthSetup(TypedDict, total=False):
    oneOfConfig: List[str]
    redirectUri: str
    requiredConfig: List[str]
    scope: str
    scopes: str
    startUrl: str
    supportedMethods: List[str]


class ReaderAuthSpaceOverrideSaved(TypedDict, total=False):
    approveNewMembers: bool
    hasOverride: bool
    hostedSignup: bool
    inherits: bool
    outboundSync: "ReaderAuthSpaceOverrideSavedOutboundSync"
    providers: List["ReaderAuthSpaceOverrideSavedProvider"]
    signInUrl: str
    sourceOfTruth: str


class ReaderAuthSpaceOverrideView(TypedDict, total=False):
    approveNewMembers: bool
    hasOverride: bool
    hostedSignup: bool
    inherits: bool
    outboundSync: "ReaderAuthSpaceOverrideViewOutboundSync"
    providers: List["ReaderAuthSpaceOverrideViewProvider"]
    signInUrl: str
    sourceOfTruth: str


class ReaderChrome(TypedDict, total=False):
    analytics: "ReaderAnalytics"
    announcement: Any
    chatWidgets: List["WidgetDescriptor"]
    chrome: Any
    inSite: Any
    languageSwitcher: bool
    name: str
    readerThemes: List["ReaderChromeReaderTheme"]
    redirects: List["RedirectRule"]
    theme: "ReaderChromeTheme"
    themeComponents: List["ReaderThemeComponent"]
    themeDraftApplied: bool
    whiteLabel: bool


class ReaderCollection(TypedDict, total=False):
    id: str
    isDefault: bool
    name: str
    pages: List["PageNode"]
    slug: str


class ReaderDomain(TypedDict, total=False):
    cnameTarget: Any
    cookieDomain: Any
    domainId: str
    host: str
    live: bool
    status: str


class ReaderFaq(TypedDict, total=False):
    contactPath: Any
    contactUrl: Any
    preset: str
    sections: List["ReaderFaqSection"]
    space: "ReaderFaqSpace"


class ReaderIdentityOverrideView(TypedDict, total=False):
    hasOverride: bool
    inherits: bool
    scope: str


class ReaderOverview(TypedDict, total=False):
    aiEnabled: bool
    analytics: "ReaderAnalytics"
    careersApplyUrl: Any
    chatWidgets: List["WidgetDescriptor"]
    collections: List["ReaderCollection"]
    commentsEnabled: bool
    frontDoor: "FrontDoor"
    glossary: List["ReaderOverviewGlossaryItem"]
    homeDoc: Optional["BlockDoc"]
    homePageId: Any
    locale: str
    locales: List["DocLocale"]
    organization: Any
    preset: str
    readerTools: "ReaderTools"
    seo: "SpacePublicSeo"
    shape: "EffectiveShape"
    space: "ReaderOverviewSpace"
    theme: "ReaderOverviewTheme"
    version: str
    versions: List["DocVersion"]


class ReaderPage(TypedDict, total=False):
    content: "BlockDoc"
    contributors: List["ReaderPageContributor"]
    id: str
    locale: str
    localeLinks: List["ReaderPageLocaleLink"]
    metadata: "ReaderPageMetadata"
    reusables: Dict[str, Any]
    shape: "ReaderPageShape"
    slug: str
    title: str
    updatedAt: str
    variables: Dict[str, Any]
    version: str
    versionLinks: List["ReaderPageVersionLink"]


class ReaderQuiz(TypedDict, total=False):
    best: Any
    id: str
    passingScore: float
    questions: List["ReaderQuizQuestion"]
    title: str


class ReaderSignupRow(TypedDict, total=False):
    createdAt: str
    email: str
    id: str
    name: str
    source: str
    status: str
    userId: str


class ReaderThemeComponent(TypedDict, total=False):
    css: str
    id: str
    outlets: "ReaderThemeComponentOutlets"
    settings: Dict[str, Any]
    slug: str
    strings: Dict[str, Any]
    values: "SettingValues"


class ReaderThemeOption(TypedDict, total=False):
    name: str
    theme: "ReaderThemeOptionTheme"


class ReaderTools(TypedDict, total=False):
    aiActions: bool
    copyMarkdown: bool
    mcp: bool
    pdf: bool
    search: bool


class Readiness(TypedDict, total=False):
    db: bool
    loopLagMs: float
    queue: bool
    queueDepth: "ReadinessQueueDepth"
    status: str


class ReadReceipt(TypedDict, total=False):
    lastReadAt: str
    name: str
    userId: str


class RecomputedTrust(TypedDict, total=False):
    after: "RecomputedTrustAfter"
    before: "RecomputedTrustBefore"
    userId: str


RedirectRule = TypedDict("RedirectRule", {"from": str, "match": "RedirectRuleMatch", "passQuery": bool, "status": Any, "to": str, "type": str}, total=False)


class ReferredPage(TypedDict, total=False):
    count: float
    pageId: str
    slug: str
    spaceSlug: Any


class ReferrerPoint(TypedDict, total=False):
    category: str
    count: float
    host: str


class ReferrersReport(TypedDict, total=False):
    byCategory: "ReferrersReportByCategory"
    top: List["ReferrersReportTopItem"]
    total: float
    windowDays: float


class RegistryListing(TypedDict, total=False):
    blocks: List["RegistryListingBlock"]
    configFields: List["RegistryListingConfigField"]
    currency: str
    description: str
    icon: str
    name: str
    priceCents: float
    pricing: str
    ratingAvg: float
    ratingCount: float
    scopes: List[str]
    slug: str
    verified: bool
    version: str
    versions: List["RegistryListingVersion"]


class RegistryTheme(TypedDict, total=False):
    description: Any
    installs: float
    mine: bool
    name: str
    publisherName: str
    slug: str
    theme: "RegistryThemeTheme"


class RegistryTokenStatus(TypedDict, total=False):
    lastError: Any
    lastVerifiedAt: Any
    registry: str
    secretSet: bool
    settings: Dict[str, Any]


class RelatedTopic(TypedDict, total=False):
    id: str
    lastActivityAt: str
    replyCount: float
    slug: str
    title: str
    voteCount: float


class RelationshipRow(TypedDict, total=False):
    expiresAt: Any
    mode: str
    name: str
    targetUserId: str


class RequiredTagGroup(TypedDict, total=False):
    minCount: float
    tagGroupId: str


class ResolvedLegalGate(TypedDict, total=False):
    anonymous: str
    anonymousSource: str
    scope: str
    scopeSource: str


class ResolvedReaderIdentity(TypedDict, total=False):
    scope: str
    scopeSource: str


class ResolvedRelation(TypedDict, total=False):
    id: str
    title: str
    url: Any


class ResyncOpenApiResult(TypedDict, total=False):
    collectionId: str
    created: float
    pruned: float
    redirected: float
    replaced: float


class ResyncResult(TypedDict, total=False):
    collectionId: str
    pruned: float
    redirected: float
    regenerated: "ImportOutcome"
    spec: "StoredSpecSummary"


class RetentionCohort(TypedDict, total=False):
    cohort: str
    rates: List[Any]
    size: float


class RetrievedChunk(TypedDict, total=False):
    chunkId: str
    freshness: "Freshness"
    itemId: str
    role: str
    score: float
    slot: str
    sourceKind: str
    spaceId: str
    text: str
    title: str
    url: Any


class ReusableSummary(TypedDict, total=False):
    content: Any
    id: str
    name: str


class Reviewable(TypedDict, total=False):
    authorName: Any
    channelId: str
    chatMessageId: str
    createdAt: str
    flagType: Any
    id: str
    kind: str
    postId: Any
    postStatus: str
    reason: Any
    score: float
    topicId: Any
    topicScope: bool


RevisionDiff = TypedDict("RevisionDiff", {"blocks": "BlockDiff", "diff": "DocDiff", "from": Optional["RevisionSummary"], "titleChanged": bool, "to": "RevisionSummary"}, total=False)


class RevisionSummary(TypedDict, total=False):
    authorId: Any
    authorName: str
    changeRequestId: Any
    createdAt: str
    id: str
    live: bool
    status: str
    title: str
    unchanged: bool


class RuleRunResult(TypedDict, total=False):
    badgeSlug: str
    granted: float
    matched: float
    revoked: float
    ruleId: str


class SamlConfigView(TypedDict, total=False):
    allowedDomain: Any
    configured: bool
    defaultRole: str
    enabled: bool
    idpEntryPoint: str


class SavedSearchRow(TypedDict, total=False):
    createdAt: str
    id: str
    name: str
    notify: bool
    query: str


class ScheduleSummary(TypedDict, total=False):
    days: Dict[str, Any]
    enabled: bool
    timezone: str


class ScheduleSummary2(TypedDict, total=False):
    pageId: str
    publishAt: str


class ScheduleWindow(TypedDict, total=False):
    end: float
    start: float


class ScimGroup(TypedDict, total=False):
    displayName: str
    id: str
    members: List["ScimGroupMember"]
    schemas: List[str]


class ScimTokenMinted(TypedDict, total=False):
    active: bool
    createdAt: Any
    id: str
    prefix: str
    token: str


class ScimTokenView(TypedDict, total=False):
    active: bool
    createdAt: Any
    id: str
    prefix: str


class ScimUser(TypedDict, total=False):
    active: bool
    emails: List["ScimUserEmail"]
    id: str
    name: "ScimUserName"
    schemas: List[str]
    userName: str


class ScreenedRow(TypedDict, total=False):
    action: str
    createdAt: str
    id: str
    kind: str
    note: Any
    pattern: str


class SdkFile(TypedDict, total=False):
    filename: str
    install: str
    label: str
    language: str
    source: str


class SearchHit(TypedDict, total=False):
    collectionId: str
    pageId: str
    rank: float
    slug: str
    snippet: str
    title: str
    url: str


class SearchTermPoint(TypedDict, total=False):
    count: float
    noResultCount: float
    term: str


class Segment(TypedDict, total=False):
    subscribedAfter: str
    subscribedBefore: str
    tags: List[str]


class SemanticHit(TypedDict, total=False):
    pageId: str
    score: float
    snippet: str
    sourceType: str
    spaceId: str
    spaceName: str
    title: str
    updatedAt: str
    url: str


class ServiceAccountSummary(TypedDict, total=False):
    createdAt: str
    id: str
    name: str
    role: str
    username: str


class SettingValues(TypedDict, total=False):
    pass


class SettingView(TypedDict, total=False):
    advanced: bool
    category: str
    default: Any
    description: str
    isDefault: bool
    key: str
    label: str
    max: float
    maxLength: float
    min: float
    options: List[str]
    type: str
    value: Any


class ShadowSnapshot(TypedDict, total=False):
    agree: float
    agreementRate: Any
    byCapability: Dict[str, Any]
    localAllowFgaDeny: float
    localDenyFgaAllow: float
    noAnswer: float
    total: float


class ShapeOverride(TypedDict, total=False):
    params: "ShapeOverrideParams"
    sections: "ShapeOverrideSections"
    space: "ShapeOverrideSpace"


class SharedDraftSummary(TypedDict, total=False):
    categoryId: Any
    content: "BlockDoc"
    createdBy: Any
    id: str
    kind: str
    tags: List[str]
    title: str
    updatedAt: str
    updatedBy: Any


class ShareLinkSummary(TypedDict, total=False):
    createdAt: str
    id: str
    label: Any
    revoked: bool


class SignalResult(TypedDict, total=False):
    delta: float
    level: float
    levelChanged: bool
    track: str
    xp: float


class SiteCollectionTree(TypedDict, total=False):
    id: str
    isDefault: bool
    name: str
    pages: List["PageNode"]
    slug: str


class SiteConfig(TypedDict, total=False):
    copyright: str
    cta: "SiteConfigCta"
    footer: "ChromeFooter"
    footerColumns: List["SiteConfigFooterColumn"]
    footerDescription: str
    footerLinks: List["SiteConfigFooterLink"]
    headerLinks: List["SiteConfigHeaderLink"]
    headerSpaceIds: List[str]
    mobileNav: str
    navMenu: "SiteConfigNavMenu"
    socialLinks: List["SiteConfigSocialLink"]
    tabs: List["SiteTab"]
    tagline: str
    theme: Dict[str, Any]
    themeToggle: "SiteConfigThemeToggle"


class SitePublicOverview(TypedDict, total=False):
    config: "SiteConfig"
    name: str
    sections: List["SiteSectionTree"]
    slug: str
    spaces: List["SiteSpaceRef"]
    tabs: List["SiteTabView"]
    themeComponents: List["ReaderThemeComponent"]


class SiteSectionTree(TypedDict, total=False):
    collections: List["SiteCollectionTree"]
    spaceId: str
    spaceName: str


class SiteSpaceRef(TypedDict, total=False):
    addresses: List["SiteSpaceRefAddress"]
    aiIngestion: bool
    indexable: bool
    name: str
    slug: str
    spaceId: str
    type: str
    updatedAt: str


class SiteSummary(TypedDict, total=False):
    config: "SiteConfig"
    createdAt: str
    id: str
    name: str
    slug: str
    spaceIds: List[str]
    staging: bool
    stagingToken: Any


class SiteTab(TypedDict, total=False):
    slug: str
    spaceIds: List[str]
    title: str


class SiteTabView(TypedDict, total=False):
    sections: List["SiteSectionTree"]
    slug: str
    title: str


class SlackStatus(TypedDict, total=False):
    connected: bool
    teamId: Any
    teamName: Any


class SlotMapDoc(TypedDict, total=False):
    slotKeys: str
    types: Dict[str, Any]
    unroledPolicy: str


class SlugHistoryEntry(TypedDict, total=False):
    createdAt: str
    slug: str


class SnapshotSummary(TypedDict, total=False):
    createdAt: str
    createdBy: Any
    id: str
    label: str
    pageCount: float


class SnapshotSummary2(TypedDict, total=False):
    authorId: Any
    authorName: Any
    createdAt: str
    id: str
    title: str


class SpaceAddress(TypedDict, total=False):
    checks: "SpaceAddressChecks"
    kind: str
    primary: bool
    url: str


class SpaceExport(TypedDict, total=False):
    pages: List["SpaceExportPage"]
    reusables: Dict[str, Any]
    space: "SpaceExportSpace"
    theme: "SpaceExportTheme"
    variables: Dict[str, Any]


class SpaceHubRoute(TypedDict, total=False):
    collection: str
    path: str


class SpaceLayoutPreset(TypedDict, total=False):
    description: str
    label: str
    name: str
    recommended: bool


class SpaceOverview(TypedDict, total=False):
    hostname: Any
    items: float
    lastActivityAt: Any
    spaceId: str


class SpacePublicSeo(TypedDict, total=False):
    contentLanguage: Any
    description: str
    noindex: bool
    socialCard: "SpacePublicSeoSocialCard"
    socialCardVersion: str
    socialImageUrl: str
    verification: "SpacePublicSeoVerification"


class SpaceShape(TypedDict, total=False):
    index: str
    nav: str
    order: str
    summary: List[str]
    whoCreates: str


class SpaceShapeView(TypedDict, total=False):
    base: "EffectiveShape"
    defaultKind: Any
    jsonSchema: Dict[str, Any]
    override: "ShapeOverride"
    presets: List["SpaceShapeViewPreset"]
    shape: "EffectiveShape"


class SpaceSummary(TypedDict, total=False):
    createdAt: str
    id: str
    itemCount: float
    itemsUpdatedAt: str
    name: str
    settings: Dict[str, Any]
    slug: str
    type: str
    url: str
    visibility: str


class SpaceTypeField(TypedDict, total=False):
    column: bool
    default: Dict[str, Any]
    hint: str
    internal: bool
    key: str
    label: str
    options: List[str]
    placeholder: str
    relationSpaceId: str
    required: bool
    schemaProperty: str
    type: str


class SpaceTypeSection(TypedDict, total=False):
    example: str
    hint: str
    key: str
    kind: str
    label: str
    render: str
    required: bool
    role: str
    schemaProperty: str


class SpaceTypeSpec(TypedDict, total=False):
    backing: str
    fields: List["SpaceTypeField"]
    icon: str
    name: str
    piecePresets: List["SpaceLayoutPreset"]
    pieceWriteCapability: str
    presets: List["SpaceLayoutPreset"]
    purpose: str
    readerTools: "SpaceTypeSpecReaderTools"
    route: "SpaceTypeSpecRoute"
    sections: List["SpaceTypeSection"]
    settings: "SpaceTypeSpecSettings"
    space: "SpaceShape"
    tabs: List[str]
    type: str
    vocabulary: "SpaceTypeSpecVocabulary"


class SpaceTypography(TypedDict, total=False):
    baseSize: float
    bodyWrap: str
    features: "SpaceTypographyFeatures"
    fluid: "SpaceTypographyFluid"
    headingTransform: str
    headingWrap: str
    levels: "SpaceTypographyLevels"
    opticalSizing: str
    scale: str
    variation: "SpaceTypographyVariation"


class SpaceUpdateRow(TypedDict, total=False):
    pageId: str
    slug: str
    title: str
    updatedAt: str


class SsoConfigView(TypedDict, total=False):
    allowedDomain: Any
    clientId: str
    configured: bool
    defaultRole: str
    enabled: bool
    issuer: str
    provider: str
    requireSso: bool


class SsoConnectionView(TypedDict, total=False):
    active: bool
    createdAt: Any
    domain: Any
    hasSecret: bool
    id: str
    name: Any
    organizationId: str
    type: str
    updatedAt: Any


class StaffActionSummary(TypedDict, total=False):
    action: str
    actorName: str
    createdAt: str
    detail: Dict[str, Any]
    id: str
    targetId: Any
    targetType: str


class StatusBoard(TypedDict, total=False):
    historyDays: List[str]
    incidents: List["IncidentSummary"]
    monitors: List["MonitorState"]
    outages: List["OutageWindow"]
    overall: str
    window: "UptimeWindow"


class StatusChannel(TypedDict, total=False):
    createdAt: str
    id: str
    kind: str
    label: str
    url: str


class StatusSummary(TypedDict, total=False):
    components: List["StatusSummaryComponent"]
    incidents: List["StatusSummaryIncident"]
    outages: List["OutageWindow"]
    page: "StatusSummaryPage"
    status: "StatusSummaryStatus"
    window: "UptimeWindow"


class StorageUsage(TypedDict, total=False):
    assets: float
    pages: float
    posts: float
    storageBytes: Any
    topics: float


class StoredSpecSummary(TypedDict, total=False):
    createdAt: str
    id: str
    lastSyncedAt: Any
    name: str
    sourceUrl: str


class SubmissionRow(TypedDict, total=False):
    assignedTo: Any
    assignedToName: Any
    attachments: List["SubmissionRowAttachment"]
    body: str
    createdAt: str
    department: Any
    email: str
    fields: Dict[str, Any]
    handledAt: Any
    id: str
    name: str
    repliedAt: Any
    replies: List["InboxReply"]
    subject: Any


class SubmittedComponentListing(TypedDict, total=False):
    component: "SubmittedComponentListingComponent"
    live: bool
    name: str
    publisherName: str
    slug: str
    submittedAt: Any
    version: str


class SubmittedExtension(TypedDict, total=False):
    id: str
    name: str
    reviewStatus: str
    slug: str
    version: str


class SubmittedThemeListing(TypedDict, total=False):
    bundle: "SubmittedThemeListingBundle"
    live: bool
    name: str
    publisherName: str
    slug: str
    submittedAt: Any
    version: str


class SubscriberSummary(TypedDict, total=False):
    confirmedAt: Any
    createdAt: str
    email: str
    id: str
    status: str
    tags: List[str]


class SuggestionResult(TypedDict, total=False):
    changeRequestId: str
    remainingToday: float
    title: str


class SummaryStats(TypedDict, total=False):
    daysVisited: float
    likesGiven: float
    likesReceived: float
    postsCreated: float
    solutions: float
    topicsCreated: float


class SuppressionRow(TypedDict, total=False):
    createdAt: str
    detail: Any
    email: str
    reason: str


class SuspensionSummary(TypedDict, total=False):
    active: bool
    createdAt: str
    expiresAt: Any
    id: str
    kind: str
    liftedAt: Any
    reason: str
    userId: str
    userName: str


class TagGroupSummary(TypedDict, total=False):
    categoryIds: List[str]
    id: str
    mode: str
    name: str
    tags: List[str]


class TagHub(TypedDict, total=False):
    counts: Dict[str, Any]
    items: List["TagHubItem"]
    tag: str


class TagHubItem(TypedDict, total=False):
    excerpt: str
    id: str
    sourceType: str
    spaceId: str
    spaceName: str
    title: str
    updatedAt: str
    url: str


class TagInfoRow(TypedDict, total=False):
    canonical: Any
    color: Any
    description: Any
    minTrustLevel: Any
    staffOnly: bool
    tag: str
    textColor: Any


class TargetComponents(TypedDict, total=False):
    draft: Any
    live: List["AttachedComponent"]


class TargetComponentsWrite(TypedDict, total=False):
    draft: Any
    live: List["AttachedComponent"]
    themeDraft: "ThemeDraftState"


class TemplateApplyFailure(TypedDict, total=False):
    code: str
    message: str
    slug: str


class TemplateApplyResult(TypedDict, total=False):
    created: float
    failed: List["TemplateApplyFailure"]
    skipped: List[str]


class TemplateSummary(TypedDict, total=False):
    createdAt: str
    id: str
    name: str
    orgWide: bool


class TemplateView(TypedDict, total=False):
    description: str
    id: str
    name: str
    pageCount: float
    published: bool
    source: str
    type: str


class ThemeBrowseResult(TypedDict, total=False):
    facets: "ThemeBrowseResultFacets"
    themes: List["ThemeListing"]


class ThemeBundleExport(TypedDict, total=False):
    bundle: "ThemeBundleExportBundle"
    stripped: List["BundleNotice"]


class ThemeComponentExport(TypedDict, total=False):
    _forumulate: "ThemeComponentExportForumulate"
    name: str
    theme: "ThemeComponentExportTheme"


class ThemeComponentSummary(TypedDict, total=False):
    createdAt: str
    enabled: bool
    id: str
    name: str
    parentThemeId: Any
    theme: "ThemeComponentSummaryTheme"


class ThemeDraftState(TypedDict, total=False):
    exists: bool
    stale: bool
    theme: Any
    updatedAt: Any
    updatedBy: Any


class ThemeDraftWrite(TypedDict, total=False):
    draft: "ThemeDraftState"
    stripped: List["BundleNotice"]


class ThemeFonts(TypedDict, total=False):
    faces: List["FontFace"]


class ThemeInstallResult(TypedDict, total=False):
    assets: List["AssetCopyNotice"]
    draft: Optional["ThemeDraftState"]
    stripped: List["BundleNotice"]
    theme: "ThemeLibraryItem"


class ThemeLibraryItem(TypedDict, total=False):
    createdAt: str
    description: Any
    enabled: bool
    id: str
    meta: Optional["ThemeLibraryMeta"]
    name: str
    parentThemeId: Any
    source: str
    sourceRef: Any
    theme: "ThemeLibraryItemTheme"
    updatedAt: str


class ThemeLibraryMeta(TypedDict, total=False):
    author: "ThemeLibraryMetaAuthor"
    homepage: str
    license: str
    previewImages: List["ThemeLibraryMetaPreviewImage"]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


class ThemeLibraryWrite(TypedDict, total=False):
    assets: List["AssetCopyNotice"]
    stripped: List["BundleNotice"]
    theme: "ThemeLibraryItem"


class ThemeListing(TypedDict, total=False):
    author: "ThemeListingAuthor"
    cardUrl: str
    currency: str
    description: Any
    featured: bool
    firstParty: bool
    installs: float
    mine: bool
    name: str
    previewImages: List["ThemeListingPreviewImage"]
    priceCents: float
    pricing: str
    publisherName: str
    requiredOrigins: "ThemeListingRequiredOrigins"
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


class ThemeListingDetail(TypedDict, total=False):
    author: "ThemeListingDetailAuthor"
    cardUrl: str
    currency: str
    description: Any
    featured: bool
    firstParty: bool
    homepage: Any
    installs: float
    license: Any
    mine: bool
    name: str
    previewImages: List["ThemeListingDetailPreviewImage"]
    priceCents: float
    pricing: str
    publisherName: str
    requiredOrigins: "ThemeListingDetailRequiredOrigins"
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    theme: "ThemeListingDetailTheme"
    version: str


class ThemePreset(TypedDict, total=False):
    description: str
    id: str
    name: str
    theme: "ThemePresetTheme"


class ThemeWarning(TypedDict, total=False):
    code: str
    key: str
    message: str


class TimerSummary(TypedDict, total=False):
    action: str
    basedOnLastPost: bool
    durationMinutes: Any
    executedAt: Any
    id: str
    runAt: str
    targetCategoryId: Any


class TitleDedupeResult(TypedDict, total=False):
    changed: float
    dryRun: bool
    matched: float
    pages: List["TitleDedupeResultPage"]
    scanned: float


class TopCategory(TypedDict, total=False):
    count: float
    id: str
    name: str
    slug: str


class TopicMap(TypedDict, total=False):
    createdAt: str
    lastPostAt: str
    links: float
    participantCount: float
    posts: float
    topParticipants: List["TopicMapTopParticipant"]


class TopicReadState(TypedDict, total=False):
    lastReadPostNumber: float
    level: str
    readTimeSeconds: float
    unreadCount: float


class TopicTimeline(TypedDict, total=False):
    lastPostAt: str
    markers: List["TopicTimelineMarker"]
    posts: float
    startedAt: str


class TopPost(TypedDict, total=False):
    likes: float
    snippet: str
    topicId: str
    topicSlug: str
    topicTitle: str


class TopTag(TypedDict, total=False):
    count: float
    tag: str


class TopTopic(TypedDict, total=False):
    replyCount: float
    slug: str
    title: str
    topicId: str
    voteCount: float


class TranslatedContent(TypedDict, total=False):
    cached: bool
    content: "BlockDoc"
    locale: str
    title: Any


class TranslationOverrideView(TypedDict, total=False):
    key: str
    locale: str
    updatedAt: str
    value: str


class TrustLevelPoint(TypedDict, total=False):
    count: float
    level: float


class TrustSummary(TypedDict, total=False):
    label: str
    level: float
    likesGiven: float
    likesReceived: float
    postsCreated: float
    solutions: float
    staff: bool
    topicsCreated: float
    userId: str


class TypeLevelSettings(TypedDict, total=False):
    lineHeight: float
    size: float
    tracking: float
    weight: float


class TypePrefEntry(TypedDict, total=False):
    email: bool
    inApp: bool
    type: str


class TypePrefsMatrix(TypedDict, total=False):
    preferences: List["TypePrefEntry"]
    types: List[str]


class TypePresets(TypedDict, total=False):
    frontDoor: List["PublishedFrontDoorOption"]
    piecePresets: List["PublishedPreset"]
    presets: List["PublishedPreset"]
    shapePresets: List["PublishedShapePreset"]


class TypeSlots(TypedDict, total=False):
    base: List["EffectiveSlotRole"]
    presets: Dict[str, Any]


class UncoveredThread(TypedDict, total=False):
    askedAt: str
    bestDocsScore: float
    title: str
    topicId: str
    url: str


class Unfurled(TypedDict, total=False):
    authorName: str
    description: Any
    embedHtml: str
    imageUrl: Any
    providerName: str
    siteName: Any
    thumbnailUrl: str
    title: Any
    type: str
    url: str


class UnifiedHit(TypedDict, total=False):
    createdAt: str
    id: str
    score: float
    snippet: str
    solved: bool
    sourceType: str
    spaceId: str
    spaceName: str
    title: str
    updatedAt: str
    url: str
    viewCount: float
    voteCount: float


class UnifiedSearchResult(TypedDict, total=False):
    facets: "UnifiedSearchResultFacets"
    hits: List["UnifiedHit"]
    minQueryLength: float
    offset: float
    total: float


class UploadedAsset(TypedDict, total=False):
    contentType: str
    filename: str
    id: str
    size: float
    url: str


class UptimeWindow(TypedDict, total=False):
    daysCovered: float
    firstCheckAt: Any
    lastCheckAt: Any
    reportedDays: float
    samples: float
    spanHours: float
    sufficient: bool


class UserActionItem(TypedDict, total=False):
    actor: "UserActionItemActor"
    at: str
    excerpt: str
    postId: str
    spaceId: str
    spaceType: str
    topicId: str
    topicSlug: str
    topicTitle: str
    type: str


class UserActionsPage(TypedDict, total=False):
    items: List["UserActionItem"]
    nextCursor: Any


class UserCard(TypedDict, total=False):
    cardBackgroundUrl: Any
    memberSince: Any
    posts: float
    status: Optional["UserStatus"]
    trustLevel: float
    user: "UserCardUser"
    viewerRelationship: Any


class UserNoteRow(TypedDict, total=False):
    authorName: str
    body: str
    createdAt: str
    id: str


class UserState(TypedDict, total=False):
    attributes: "UserStateAttributes"
    directives: List[Any]
    entitlements: Dict[str, Any]
    roles: List[str]


class UserStatus(TypedDict, total=False):
    emoji: Any
    message: Any
    until: Any


class UserSummary(TypedDict, total=False):
    badges: List["BadgeSummary"]
    stats: "SummaryStats"
    topCategories: List["TopCategory"]
    topPosts: List["TopPost"]
    topTags: List["TopTag"]
    topTopics: List["TopTopic"]


class VariableRow(TypedDict, total=False):
    key: str
    scope: str
    type: str
    value: str


class VerifyResult(TypedDict, total=False):
    bytes: float
    detail: str
    key: Any
    ok: bool


class ViewerView(TypedDict, total=False):
    canPost: bool
    canReply: bool
    name: Any
    signedIn: bool
    signInMethods: List[str]
    signInPath: Any
    signInWith: Any
    whoCreates: str


class WalletSummary(TypedDict, total=False):
    balances: Dict[str, Any]
    inventory: List["WalletSummaryInventoryItem"]


class WatchedUserRow(TypedDict, total=False):
    createdAt: str
    name: str
    reason: str
    userId: str
    username: str
    watchedByName: Any
    watchedByUserId: Any


class WatchedWordSummary(TypedDict, total=False):
    action: str
    caseSensitive: bool
    id: str
    isRegex: bool
    replacement: Any
    word: str


class WebhookSummary(TypedDict, total=False):
    active: bool
    bodyEncoding: str
    categoryIds: Any
    createdAt: str
    events: List[str]
    format: str
    groupIds: Any
    id: str
    signatureVersion: str
    spaceId: Any
    tagIds: Any
    url: str


class WidgetDescriptor(TypedDict, total=False):
    connectOrigins: List[str]
    consent: str
    origin: str
    placement: str
    providerId: str
    providerName: str
    script: str
    src: str
    theme: Dict[str, Any]


class PageInfo(TypedDict, total=False):
    limit: int
    hasMore: bool
    nextCursor: Any
    has_more: bool
    next_cursor: Any
    total: int


class PatListDtoLegacy(TypedDict, total=False):
    pats: List["PatSummaryDto"]


class OrgListDtoLegacy(TypedDict, total=False):
    orgs: List["OrgSummaryDto"]


class SpaceListDtoLegacy(TypedDict, total=False):
    spaces: List["SpaceSummaryDto"]


class ErrorEnvelopeError(TypedDict, total=False):
    code: str
    message: str
    details: Dict[str, Any]
    docs: str
    slugs: List[str]


class ConsentConfigCustom(TypedDict, total=False):
    mode: str
    settingsUrl: str
    stateUrl: str
    loaderUrl: str


class AboutStatsOrganization(TypedDict, total=False):
    createdAt: str
    name: str
    slug: str


class AboutStatsStaffItem(TypedDict, total=False):
    avatarUrl: Any
    name: str
    role: str
    userId: str
    username: str


class AboutStatsStats(TypedDict, total=False):
    activeThisWeek: float
    members: float
    newestMemberAt: Any
    oldestMemberAt: Any
    posts: float
    topics: float


class AiProviderStatusProvider(TypedDict, total=False):
    defaultModel: str
    id: str
    name: str


class AnalyticsSummaryFeedbackItem(TypedDict, total=False):
    down: float
    pageId: str
    up: float


class AnalyticsSummaryNoResultSearch(TypedDict, total=False):
    count: float
    query: str


class AnalyticsSummaryPageView(TypedDict, total=False):
    pageId: str
    views: float


class AnalyticsSummaryTopSearch(TypedDict, total=False):
    count: float
    query: str


class AnalyticsSummaryViewsByDayItem(TypedDict, total=False):
    day: str
    views: float


class AnswerResultCitation(TypedDict, total=False):
    anchor: str
    itemId: str
    slot: str
    title: str
    url: Any


class ApplicationRowAttachment(TypedDict, total=False):
    assetId: str
    filename: str
    size: float


class ArticleDetailAuthor(TypedDict, total=False):
    name: str
    userId: str


class ArticleDetailFurtherReadingItem(TypedDict, total=False):
    href: str
    label: str


class ArticleDetailSeo(TypedDict, total=False):
    noindex: bool
    seoDescription: str
    seoTitle: str


class ArticleSummaryFurtherReadingItem(TypedDict, total=False):
    href: str
    label: str


class AtlasSyncResultImport(TypedDict, total=False):
    imported: float
    linked: float
    unmapped: List[str]


class AtlasSyncResultMemberships(TypedDict, total=False):
    skipped: float
    synced: float


class AtlasSyncResultOrgs(TypedDict, total=False):
    alreadyLinked: float
    created: float
    failed: List[str]


class BulkInviteResultResult(TypedDict, total=False):
    email: str
    reason: str
    status: str


class ChangelogArchiveEnvelopedComments(TypedDict, total=False):
    enabled: bool


class ChangelogArchiveEnvelopedReactions(TypedDict, total=False):
    enabled: bool
    palette: List[str]


class ChangelogArchiveEnvelopedYear(TypedDict, total=False):
    count: float
    year: float


class ChangelogArchiveLegacyComments(TypedDict, total=False):
    enabled: bool


class ChangelogArchiveLegacyPage(TypedDict, total=False):
    hasMore: bool
    limit: float
    offset: float
    total: float


class ChangelogArchiveLegacyReactions(TypedDict, total=False):
    enabled: bool
    palette: List[str]


class ChangelogArchiveLegacyYear(TypedDict, total=False):
    count: float
    year: float


class ChromeFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class CommunityAnalyticsActivityByDayItem(TypedDict, total=False):
    day: str
    posts: float
    topics: float


class CommunityAnalyticsNeedsAnswerItem(TypedDict, total=False):
    askedAt: str
    slug: str
    title: str
    topicId: str


class CommunityAnalyticsTopContributor(TypedDict, total=False):
    name: str
    posts: float
    solutions: float
    userId: str


class CommunityAnalyticsTopTopic(TypedDict, total=False):
    replies: float
    slug: str
    title: str
    topicId: str
    views: float


class CommunityAnalyticsTotals(TypedDict, total=False):
    activeMembers: float
    posts: float
    solved: float
    topics: float
    unanswered: float


class CompiledReleaseMergedChangeRequest(TypedDict, total=False):
    id: str
    mergedAt: Any
    title: str


class CompiledReleaseShippedItem(TypedDict, total=False):
    id: str
    title: str


class ComponentInstallItemAuthor(TypedDict, total=False):
    name: str
    url: str


class ComponentInstallItemComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ComponentInstallItemComponentMetaPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class ComponentInstallItemComponentMeta(TypedDict, total=False):
    author: "ComponentInstallItemComponentMetaAuthor"
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List["ComponentInstallItemComponentMetaPreviewImage"]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


ComponentInstallItemComponentOutlets = TypedDict("ComponentInstallItemComponentOutlets", {"above-main": Any, "below-main": Any, "blog-index-above-list": Any, "blog-post-after": Any, "blog-post-before": Any, "careers-above-list": Any, "category-header": Any, "changelog-above-list": Any, "courses-above-list": Any, "docs-page-footer": Any, "docs-page-header": Any, "events-above-list": Any, "faq-above-list": Any, "footer-after": Any, "footer-before": Any, "forum-index-above-list": Any, "forum-index-below-list": Any, "forum-post-after-body": Any, "forum-sidebar-bottom": Any, "forum-sidebar-top": Any, "forum-topic-above-title": Any, "forum-topic-below-first-post": Any, "forum-topic-below-title": Any, "forum-topic-bottom": Any, "header-after": Any, "header-before": Any, "roadmap-above-board": Any, "status-above-board": Any, "user-card": Any}, total=False)


class ComponentInstallItemComponent(TypedDict, total=False):
    css: str
    format: str
    formatVersion: float
    meta: "ComponentInstallItemComponentMeta"
    outlets: "ComponentInstallItemComponentOutlets"
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ComponentListingAuthor(TypedDict, total=False):
    name: str
    url: str


class ComponentListingPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class ComponentListingDetailAuthor(TypedDict, total=False):
    name: str
    url: str


class ComponentListingDetailComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ComponentListingDetailComponentMetaPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class ComponentListingDetailComponentMeta(TypedDict, total=False):
    author: "ComponentListingDetailComponentMetaAuthor"
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List["ComponentListingDetailComponentMetaPreviewImage"]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


ComponentListingDetailComponentOutlets = TypedDict("ComponentListingDetailComponentOutlets", {"above-main": Any, "below-main": Any, "blog-index-above-list": Any, "blog-post-after": Any, "blog-post-before": Any, "careers-above-list": Any, "category-header": Any, "changelog-above-list": Any, "courses-above-list": Any, "docs-page-footer": Any, "docs-page-header": Any, "events-above-list": Any, "faq-above-list": Any, "footer-after": Any, "footer-before": Any, "forum-index-above-list": Any, "forum-index-below-list": Any, "forum-post-after-body": Any, "forum-sidebar-bottom": Any, "forum-sidebar-top": Any, "forum-topic-above-title": Any, "forum-topic-below-first-post": Any, "forum-topic-below-title": Any, "forum-topic-bottom": Any, "header-after": Any, "header-before": Any, "roadmap-above-board": Any, "status-above-board": Any, "user-card": Any}, total=False)


class ComponentListingDetailComponent(TypedDict, total=False):
    css: str
    format: str
    formatVersion: float
    meta: "ComponentListingDetailComponentMeta"
    outlets: "ComponentListingDetailComponentOutlets"
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ComponentListingDetailPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class ConnectorAnswerCitation(TypedDict, total=False):
    anchor: str
    itemId: str
    slot: str
    title: str
    url: Any


class ConnectorChunksPagePolicy(TypedDict, total=False):
    version: str


class ConnectorChunksPageSync(TypedDict, total=False):
    checkpoint: str


class ConnectorManifestChunkPolicy(TypedDict, total=False):
    note: str
    version: str


class ConnectorManifestEndpoints(TypedDict, total=False):
    ask: Any
    chunks: Any
    llms: Any
    manifest: str
    questions: Any
    search: Any
    suggestions: Any


class ConnectorManifestProvider(TypedDict, total=False):
    id: str
    name: str


class ConnectorManifestRateLimit(TypedDict, total=False):
    writesPerDay: float


class ConnectorManifestSpace(TypedDict, total=False):
    id: str
    name: str


class ConnectorSearchResultPolicy(TypedDict, total=False):
    version: str


class CourseModuleQuiz(TypedDict, total=False):
    passed: bool
    passingScore: float
    quizId: str
    title: str


class CourseOutlineOrderItem(TypedDict, total=False):
    slug: str
    title: str


class CourseOutlineProgress(TypedDict, total=False):
    completed: float
    percent: float
    total: float


class DomainSetupDns(TypedDict, total=False):
    expected: str
    found: List[str]
    reachesUs: bool


class DomainSetupForwardSnippets(TypedDict, total=False):
    caddy: str
    cloudflare: str
    nginx: str


class DomainSetupForward(TypedDict, total=False):
    origin: str
    path: str
    snippets: "DomainSetupForwardSnippets"


class DomainSummaryVerificationFile(TypedDict, total=False):
    contents: str
    path: str


class DomainSummaryVerificationMeta(TypedDict, total=False):
    tag: str


class DomainSummaryVerificationRecord(TypedDict, total=False):
    name: str
    value: str


class EmailTemplateDetailDefaultsBlock(TypedDict, total=False):
    align: str
    level: Any
    text: str
    type: str
    muted: bool
    label: str
    showUrl: bool
    url: str
    alt: str
    href: str
    src: str
    width: float
    size: str


class EmailTemplateDetailDefaults(TypedDict, total=False):
    blocks: List["EmailTemplateDetailDefaultsBlock"]
    preheader: str
    subject: str


class EmailTemplateOverrideBlock(TypedDict, total=False):
    align: str
    level: Any
    text: str
    type: str
    muted: bool
    label: str
    showUrl: bool
    url: str
    alt: str
    href: str
    src: str
    width: float
    size: str


class EmailTemplateSummaryOverride(TypedDict, total=False):
    id: str
    locale: Any
    spaceId: Any
    updatedAt: str


class EmbedSpecColorSchemeMap(TypedDict, total=False):
    dark: Any
    light: Any
    system: Any


class EmbedSpecThemeInit(TypedDict, total=False):
    colorScheme: Any
    greeting: Any
    position: Any
    primaryColor: Any


class ExportedSpaceCollection(TypedDict, total=False):
    id: str
    name: str
    slug: str


class ExportedSpacePage(TypedDict, total=False):
    collectionId: Any
    content: Any
    id: str
    slug: str
    title: str


class ExportedSpaceTopicPost(TypedDict, total=False):
    authorId: Any
    content: Any
    createdAt: str
    id: str
    isOp: bool


class ExportedSpaceTopic(TypedDict, total=False):
    id: str
    kind: str
    posts: List["ExportedSpaceTopicPost"]
    slug: str
    state: str
    tags: List[str]
    title: str


class GenerateResultPage(TypedDict, total=False):
    id: str
    slug: str
    title: str


class GrowthExtraReportPageViews(TypedDict, total=False):
    audienceSplitAvailable: bool
    available: bool
    daily: List["GrowthPoint"]


class GrowthExtraReportReferrers(TypedDict, total=False):
    available: bool
    top: List["ReferrerPoint"]
    topPages: List["ReferredPage"]


class GrowthExtraReportTimeToFirstResponse(TypedDict, total=False):
    avgHours: Any
    weekly: List["FirstResponsePoint"]


class GrowthExtraReportWindow(TypedDict, total=False):
    days: float
    weeks: float


class GrowthReportActiveUsers(TypedDict, total=False):
    daily: List["GrowthPoint"]
    monthly: List["GrowthPoint"]
    weekly: List["GrowthPoint"]


class GrowthReportWindow(TypedDict, total=False):
    days: float
    months: float
    weeks: float


HostOriginPolicyContributes = TypedDict("HostOriginPolicyContributes", {"font-src": Any, "frame-src": Any, "img-src": Any, "media-src": Any, "script-src": Any, "style-src": Any}, total=False)


class IdentityOptionsCurrent(TypedDict, total=False):
    primaryGroupId: Any
    title: Any


class IdentityOptionsPrimaryGroup(TypedDict, total=False):
    id: str
    name: str


class ImportResultBrokenLink(TypedDict, total=False):
    pageSlug: str
    url: str


class ImportResultCollection(TypedDict, total=False):
    created: bool
    exists: bool
    id: str
    name: str


class ImportResultFailure(TypedDict, total=False):
    file: str
    reason: str


ImportResultRedirect = TypedDict("ImportResultRedirect", {"from": str, "to": str}, total=False)


class InstalledExtensionSummaryBlockConfigField(TypedDict, total=False):
    help: str
    key: str
    label: str
    placeholder: str
    required: bool
    type: str


class InstalledExtensionSummaryBlock(TypedDict, total=False):
    configFields: List["InstalledExtensionSummaryBlockConfigField"]
    name: str
    type: str


class InstalledExtensionSummaryConfigField(TypedDict, total=False):
    help: str
    key: str
    label: str
    placeholder: str
    required: bool
    type: str


class InstalledExtensionSummarySurface(TypedDict, total=False):
    id: str
    target: str
    title: str


class IntegrationDefDelivery(TypedDict, total=False):
    format: str
    urlField: str


class LegalStatusDocument(TypedDict, total=False):
    accepted: bool
    body: Any
    content: Any
    customization: "PieceCustomization"
    fields: Dict[str, Any]
    id: str
    kind: str
    onThisPage: Any
    pageId: Any
    required: bool
    seoDescription: Any
    spaceId: Any
    title: str
    updatedAt: str
    version: float


class LintReportCounts(TypedDict, total=False):
    error: float
    info: float
    warn: float


class MailProviderViewProvider(TypedDict, total=False):
    id: str
    name: str
    needsDomain: bool


class ManifestResultSummary(TypedDict, total=False):
    applied: float
    create: float
    failed: float
    skipped: float
    unchanged: float
    update: float


class MemberProfileUser(TypedDict, total=False):
    avatarUrl: Any
    bio: Any
    id: str
    lastSeen: Any
    memberSince: Any
    name: str


class MyCertificateProgress(TypedDict, total=False):
    completed: float
    percent: float
    total: float


class OnboardingResultOrganization(TypedDict, total=False):
    id: str
    name: str
    slug: str


class OpenApiOperationCodeSample(TypedDict, total=False):
    label: str
    lang: str
    source: str


class OpenApiOperationRequestBodyField(TypedDict, total=False):
    description: str
    name: str
    required: bool
    type: str


class OpenApiOperationRequestBody(TypedDict, total=False):
    contentType: str
    description: str
    fields: List["OpenApiOperationRequestBodyField"]
    schema: str


OpenApiSecurityOptionItem = TypedDict("OpenApiSecurityOptionItem", {"bearerFormat": str, "description": str, "key": str, "type": str, "in": str, "name": str, "scopes": List[str], "detail": str}, total=False)


class OrgAnswerCitation(TypedDict, total=False):
    anchor: str
    itemId: str
    slot: str
    title: str
    url: Any


class OrgComponentListingAuthor(TypedDict, total=False):
    name: str
    url: str


class OrgComponentListingPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class OrgEventsReportByDayItem(TypedDict, total=False):
    day: str
    feedback: float
    search: float
    view: float


class OrgEventsReportByTypeItem(TypedDict, total=False):
    count: float
    type: str


class OrgEventsReportTopSpace(TypedDict, total=False):
    spaceId: str
    spaceName: str
    views: float


class OrgExportMember(TypedDict, total=False):
    email: str
    name: str
    role: str
    scopeSpaceId: Any
    userId: str


class OrgExportOrganization(TypedDict, total=False):
    id: str
    name: str
    slug: str


class OwnComponentListingAuthor(TypedDict, total=False):
    name: str
    url: str


class OwnComponentListingPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class OwnThemeListingAuthor(TypedDict, total=False):
    name: str
    url: str


class OwnThemeListingPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class OwnThemeListingRequiredOrigins(TypedDict, total=False):
    fonts: List[str]
    images: List[str]


class PageDetailCollection(TypedDict, total=False):
    id: str
    name: str


class PieceThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class PieceThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class PieceThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class PieceThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class PieceThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class PieceThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class PieceThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class PieceThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class PieceThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class PieceThemeComponents(TypedDict, total=False):
    button: "PieceThemeComponentsButton"
    code: "PieceThemeComponentsCode"
    focus: "PieceThemeComponentsFocus"
    input: "PieceThemeComponentsInput"
    radius: float
    scrollbar: "PieceThemeComponentsScrollbar"
    selection: "PieceThemeComponentsSelection"
    shadow: str
    spacing: "PieceThemeComponentsSpacing"
    syntax: "PieceThemeComponentsSyntax"
    syntaxDark: "PieceThemeComponentsSyntaxDark"


class PieceThemeLayout(TypedDict, total=False):
    measure: str


class PieceThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class PieceThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class PieceThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class PieceThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class PieceThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


PieceThemeMotionTargets = TypedDict("PieceThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class PieceThemeMotion(TypedDict, total=False):
    ambient: "PieceThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "PieceThemeMotionHeader"
    hover: "PieceThemeMotionHover"
    keyframes: List["PieceThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "PieceThemeMotionReveal"
    speed: float
    targets: "PieceThemeMotionTargets"


class PieceThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class PieceThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class PollVoterBreakdownOptionVoter(TypedDict, total=False):
    name: str
    userId: str


class PollVoterBreakdownOption(TypedDict, total=False):
    id: str
    text: str
    voters: List["PollVoterBreakdownOptionVoter"]


class PostSummaryAuthorBadge(TypedDict, total=False):
    icon: str
    name: str
    slug: str


class PostSummaryAuthorFlair(TypedDict, total=False):
    bgColor: Any
    color: Any
    icon: Any
    label: str


class PublishedPageContributor(TypedDict, total=False):
    avatarUrl: Any
    name: str


class PublishedShapePresetLayoutItemColumn(TypedDict, total=False):
    content: List[Dict[str, Any]]
    width: float


class PublishedShapePresetLayoutItem(TypedDict, total=False):
    block: str
    key: str
    columns: List["PublishedShapePresetLayoutItemColumn"]
    count: float
    level: Any


class PublishedShapePresetSection(TypedDict, total=False):
    key: str
    kind: str
    label: str
    required: bool
    role: str


class ReaderAuthSpaceOverrideSavedOutboundSync(TypedDict, total=False):
    deprovisionAction: str
    lastError: str
    scimBaseUrl: str
    scimBearerToken: str
    status: str
    targetId: str


class ReaderAuthSpaceOverrideSavedProvider(TypedDict, total=False):
    config: Dict[str, Any]
    label: str
    method: str
    order: float
    provisionIdentity: bool


class ReaderAuthSpaceOverrideViewOutboundSync(TypedDict, total=False):
    deprovisionAction: str
    lastError: str
    scimBaseUrl: str
    scimBearerToken: str
    status: str
    targetId: str


class ReaderAuthSpaceOverrideViewProvider(TypedDict, total=False):
    config: Dict[str, Any]
    label: str
    method: str
    order: float
    provisionIdentity: bool


class ReaderChromeReaderThemeThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ReaderChromeReaderThemeThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ReaderChromeReaderThemeThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: Dict[str, Any]
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List[Dict[str, Any]]
    footerDescription: str
    footerLinks: List[Dict[str, Any]]
    header: "ChromeHeader"
    headerLinks: List[Dict[str, Any]]
    height: str
    mobileNav: str
    navMenu: Dict[str, Any]
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List[Dict[str, Any]]
    sticky: bool
    themeToggle: Dict[str, Any]


class ReaderChromeReaderThemeThemeComponents(TypedDict, total=False):
    button: Dict[str, Any]
    code: Dict[str, Any]
    focus: Dict[str, Any]
    input: Dict[str, Any]
    radius: float
    scrollbar: Dict[str, Any]
    selection: Dict[str, Any]
    shadow: str
    spacing: Dict[str, Any]
    syntax: Dict[str, Any]
    syntaxDark: Dict[str, Any]


class ReaderChromeReaderThemeThemeLayout(TypedDict, total=False):
    measure: str


class ReaderChromeReaderThemeThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ReaderChromeReaderThemeThemeMotion(TypedDict, total=False):
    ambient: Dict[str, Any]
    easing: str
    enabled: bool
    header: Dict[str, Any]
    hover: Dict[str, Any]
    keyframes: List[Dict[str, Any]]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: Dict[str, Any]
    speed: float
    targets: Dict[str, Any]


class ReaderChromeReaderThemeThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List[Dict[str, Any]]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ReaderChromeReaderThemeThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ReaderChromeReaderThemeThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ReaderChromeReaderThemeTheme(TypedDict, total=False):
    accentColor: str
    ads: "ReaderChromeReaderThemeThemeAds"
    announcement: "ReaderChromeReaderThemeThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ReaderChromeReaderThemeThemeChrome"
    colorScheme: str
    componentInstalls: List[Dict[str, Any]]
    components: "ReaderChromeReaderThemeThemeComponents"
    contentWidth: str
    cssSnippets: List[Dict[str, Any]]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ReaderChromeReaderThemeThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ReaderChromeReaderThemeThemeMobile"
    monoFontFamily: str
    motion: "ReaderChromeReaderThemeThemeMotion"
    notFound: "ReaderChromeReaderThemeThemeNotFound"
    onThisPage: str
    palette: "ReaderChromeReaderThemeThemePalette"
    paletteDark: "ReaderChromeReaderThemeThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List[Dict[str, Any]]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ReaderChromeReaderTheme(TypedDict, total=False):
    name: str
    theme: "ReaderChromeReaderThemeTheme"


class ReaderChromeThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ReaderChromeThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ReaderChromeThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ReaderChromeThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ReaderChromeThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ReaderChromeThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ReaderChromeThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ReaderChromeThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ReaderChromeThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ReaderChromeThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ReaderChromeThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ReaderChromeThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ReaderChromeThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ReaderChromeThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ReaderChromeThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ReaderChromeThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ReaderChromeThemeChromeThemeToggle"


class ReaderChromeThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ReaderChromeThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ReaderChromeThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ReaderChromeThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ReaderChromeThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ReaderChromeThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ReaderChromeThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ReaderChromeThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ReaderChromeThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ReaderChromeThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ReaderChromeThemeComponents(TypedDict, total=False):
    button: "ReaderChromeThemeComponentsButton"
    code: "ReaderChromeThemeComponentsCode"
    focus: "ReaderChromeThemeComponentsFocus"
    input: "ReaderChromeThemeComponentsInput"
    radius: float
    scrollbar: "ReaderChromeThemeComponentsScrollbar"
    selection: "ReaderChromeThemeComponentsSelection"
    shadow: str
    spacing: "ReaderChromeThemeComponentsSpacing"
    syntax: "ReaderChromeThemeComponentsSyntax"
    syntaxDark: "ReaderChromeThemeComponentsSyntaxDark"


class ReaderChromeThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ReaderChromeThemeLayout(TypedDict, total=False):
    measure: str


class ReaderChromeThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ReaderChromeThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ReaderChromeThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ReaderChromeThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ReaderChromeThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ReaderChromeThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ReaderChromeThemeMotionTargets = TypedDict("ReaderChromeThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ReaderChromeThemeMotion(TypedDict, total=False):
    ambient: "ReaderChromeThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ReaderChromeThemeMotionHeader"
    hover: "ReaderChromeThemeMotionHover"
    keyframes: List["ReaderChromeThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ReaderChromeThemeMotionReveal"
    speed: float
    targets: "ReaderChromeThemeMotionTargets"


class ReaderChromeThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ReaderChromeThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ReaderChromeThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ReaderChromeThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ReaderChromeThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ReaderChromeThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ReaderChromeTheme(TypedDict, total=False):
    accentColor: str
    ads: "ReaderChromeThemeAds"
    announcement: "ReaderChromeThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ReaderChromeThemeChrome"
    colorScheme: str
    componentInstalls: List["ReaderChromeThemeComponentInstall"]
    components: "ReaderChromeThemeComponents"
    contentWidth: str
    cssSnippets: List["ReaderChromeThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ReaderChromeThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ReaderChromeThemeMobile"
    monoFontFamily: str
    motion: "ReaderChromeThemeMotion"
    notFound: "ReaderChromeThemeNotFound"
    onThisPage: str
    palette: "ReaderChromeThemePalette"
    paletteDark: "ReaderChromeThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ReaderChromeThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ReaderFaqSectionQuestion(TypedDict, total=False):
    answer: "BlockDoc"
    id: str
    question: str
    slug: str
    topic: str


class ReaderFaqSection(TypedDict, total=False):
    id: str
    isDefault: bool
    kind: str
    name: str
    questions: List["ReaderFaqSectionQuestion"]


class ReaderFaqSpace(TypedDict, total=False):
    name: str
    type: str


class ReaderOverviewGlossaryItem(TypedDict, total=False):
    definition: str
    term: str


class ReaderOverviewSpace(TypedDict, total=False):
    description: Any
    id: str
    name: str
    slug: str
    type: str


class ReaderOverviewThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ReaderOverviewThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ReaderOverviewThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ReaderOverviewThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ReaderOverviewThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ReaderOverviewThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ReaderOverviewThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ReaderOverviewThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ReaderOverviewThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ReaderOverviewThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ReaderOverviewThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ReaderOverviewThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ReaderOverviewThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ReaderOverviewThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ReaderOverviewThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ReaderOverviewThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ReaderOverviewThemeChromeThemeToggle"


class ReaderOverviewThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ReaderOverviewThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ReaderOverviewThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ReaderOverviewThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ReaderOverviewThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ReaderOverviewThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ReaderOverviewThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ReaderOverviewThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ReaderOverviewThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ReaderOverviewThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ReaderOverviewThemeComponents(TypedDict, total=False):
    button: "ReaderOverviewThemeComponentsButton"
    code: "ReaderOverviewThemeComponentsCode"
    focus: "ReaderOverviewThemeComponentsFocus"
    input: "ReaderOverviewThemeComponentsInput"
    radius: float
    scrollbar: "ReaderOverviewThemeComponentsScrollbar"
    selection: "ReaderOverviewThemeComponentsSelection"
    shadow: str
    spacing: "ReaderOverviewThemeComponentsSpacing"
    syntax: "ReaderOverviewThemeComponentsSyntax"
    syntaxDark: "ReaderOverviewThemeComponentsSyntaxDark"


class ReaderOverviewThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ReaderOverviewThemeLayout(TypedDict, total=False):
    measure: str


class ReaderOverviewThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ReaderOverviewThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ReaderOverviewThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ReaderOverviewThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ReaderOverviewThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ReaderOverviewThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ReaderOverviewThemeMotionTargets = TypedDict("ReaderOverviewThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ReaderOverviewThemeMotion(TypedDict, total=False):
    ambient: "ReaderOverviewThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ReaderOverviewThemeMotionHeader"
    hover: "ReaderOverviewThemeMotionHover"
    keyframes: List["ReaderOverviewThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ReaderOverviewThemeMotionReveal"
    speed: float
    targets: "ReaderOverviewThemeMotionTargets"


class ReaderOverviewThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ReaderOverviewThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ReaderOverviewThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ReaderOverviewThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ReaderOverviewThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ReaderOverviewThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ReaderOverviewTheme(TypedDict, total=False):
    accentColor: str
    ads: "ReaderOverviewThemeAds"
    announcement: "ReaderOverviewThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ReaderOverviewThemeChrome"
    colorScheme: str
    componentInstalls: List["ReaderOverviewThemeComponentInstall"]
    components: "ReaderOverviewThemeComponents"
    contentWidth: str
    cssSnippets: List["ReaderOverviewThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ReaderOverviewThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ReaderOverviewThemeMobile"
    monoFontFamily: str
    motion: "ReaderOverviewThemeMotion"
    notFound: "ReaderOverviewThemeNotFound"
    onThisPage: str
    palette: "ReaderOverviewThemePalette"
    paletteDark: "ReaderOverviewThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ReaderOverviewThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ReaderPageContributor(TypedDict, total=False):
    avatarUrl: Any
    name: str


class ReaderPageLocaleLink(TypedDict, total=False):
    code: str
    current: bool
    label: str
    pageId: Any


class ReaderPageMetadata(TypedDict, total=False):
    fields: Dict[str, Any]


class ReaderPageShape(TypedDict, total=False):
    sections: List["SpaceTypeSection"]


class ReaderPageVersionLink(TypedDict, total=False):
    current: bool
    key: str
    label: str
    pageId: Any


class ReaderQuizQuestion(TypedDict, total=False):
    choices: List[str]
    id: str
    multiple: bool
    prompt: str


ReaderThemeComponentOutlets = TypedDict("ReaderThemeComponentOutlets", {"above-main": Any, "below-main": Any, "blog-index-above-list": Any, "blog-post-after": Any, "blog-post-before": Any, "careers-above-list": Any, "category-header": Any, "changelog-above-list": Any, "courses-above-list": Any, "docs-page-footer": Any, "docs-page-header": Any, "events-above-list": Any, "faq-above-list": Any, "footer-after": Any, "footer-before": Any, "forum-index-above-list": Any, "forum-index-below-list": Any, "forum-post-after-body": Any, "forum-sidebar-bottom": Any, "forum-sidebar-top": Any, "forum-topic-above-title": Any, "forum-topic-below-first-post": Any, "forum-topic-below-title": Any, "forum-topic-bottom": Any, "header-after": Any, "header-before": Any, "roadmap-above-board": Any, "status-above-board": Any, "user-card": Any}, total=False)


class ReaderThemeOptionThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ReaderThemeOptionThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ReaderThemeOptionThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ReaderThemeOptionThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ReaderThemeOptionThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ReaderThemeOptionThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ReaderThemeOptionThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ReaderThemeOptionThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ReaderThemeOptionThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ReaderThemeOptionThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ReaderThemeOptionThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ReaderThemeOptionThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ReaderThemeOptionThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ReaderThemeOptionThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ReaderThemeOptionThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ReaderThemeOptionThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ReaderThemeOptionThemeChromeThemeToggle"


class ReaderThemeOptionThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ReaderThemeOptionThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ReaderThemeOptionThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ReaderThemeOptionThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ReaderThemeOptionThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ReaderThemeOptionThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ReaderThemeOptionThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ReaderThemeOptionThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ReaderThemeOptionThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ReaderThemeOptionThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ReaderThemeOptionThemeComponents(TypedDict, total=False):
    button: "ReaderThemeOptionThemeComponentsButton"
    code: "ReaderThemeOptionThemeComponentsCode"
    focus: "ReaderThemeOptionThemeComponentsFocus"
    input: "ReaderThemeOptionThemeComponentsInput"
    radius: float
    scrollbar: "ReaderThemeOptionThemeComponentsScrollbar"
    selection: "ReaderThemeOptionThemeComponentsSelection"
    shadow: str
    spacing: "ReaderThemeOptionThemeComponentsSpacing"
    syntax: "ReaderThemeOptionThemeComponentsSyntax"
    syntaxDark: "ReaderThemeOptionThemeComponentsSyntaxDark"


class ReaderThemeOptionThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ReaderThemeOptionThemeLayout(TypedDict, total=False):
    measure: str


class ReaderThemeOptionThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ReaderThemeOptionThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ReaderThemeOptionThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ReaderThemeOptionThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ReaderThemeOptionThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ReaderThemeOptionThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ReaderThemeOptionThemeMotionTargets = TypedDict("ReaderThemeOptionThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ReaderThemeOptionThemeMotion(TypedDict, total=False):
    ambient: "ReaderThemeOptionThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ReaderThemeOptionThemeMotionHeader"
    hover: "ReaderThemeOptionThemeMotionHover"
    keyframes: List["ReaderThemeOptionThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ReaderThemeOptionThemeMotionReveal"
    speed: float
    targets: "ReaderThemeOptionThemeMotionTargets"


class ReaderThemeOptionThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ReaderThemeOptionThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ReaderThemeOptionThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ReaderThemeOptionThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ReaderThemeOptionThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ReaderThemeOptionThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ReaderThemeOptionTheme(TypedDict, total=False):
    accentColor: str
    ads: "ReaderThemeOptionThemeAds"
    announcement: "ReaderThemeOptionThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ReaderThemeOptionThemeChrome"
    colorScheme: str
    componentInstalls: List["ReaderThemeOptionThemeComponentInstall"]
    components: "ReaderThemeOptionThemeComponents"
    contentWidth: str
    cssSnippets: List["ReaderThemeOptionThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ReaderThemeOptionThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ReaderThemeOptionThemeMobile"
    monoFontFamily: str
    motion: "ReaderThemeOptionThemeMotion"
    notFound: "ReaderThemeOptionThemeNotFound"
    onThisPage: str
    palette: "ReaderThemeOptionThemePalette"
    paletteDark: "ReaderThemeOptionThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ReaderThemeOptionThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ReadinessQueueDepth(TypedDict, total=False):
    active: float
    delayed: float
    failed: float
    waiting: float


class RecomputedTrustAfter(TypedDict, total=False):
    postsCreated: float
    solutions: float
    topicsCreated: float


class RecomputedTrustBefore(TypedDict, total=False):
    postsCreated: float
    solutions: float
    topicsCreated: float


class RedirectRuleMatch(TypedDict, total=False):
    query: Any


class ReferrersReportByCategory(TypedDict, total=False):
    other: float
    search: float
    social: float


class ReferrersReportTopItem(TypedDict, total=False):
    category: str
    count: float
    host: str


class RegistryListingBlock(TypedDict, total=False):
    name: str
    type: str


class RegistryListingConfigField(TypedDict, total=False):
    help: str
    key: str
    label: str
    placeholder: str
    required: bool
    type: str


class RegistryListingVersion(TypedDict, total=False):
    changelog: str
    publishedAt: str
    version: str


class RegistryThemeThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class RegistryThemeThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class RegistryThemeThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class RegistryThemeThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class RegistryThemeThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class RegistryThemeThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class RegistryThemeThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class RegistryThemeThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class RegistryThemeThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class RegistryThemeThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "RegistryThemeThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["RegistryThemeThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["RegistryThemeThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["RegistryThemeThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "RegistryThemeThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["RegistryThemeThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "RegistryThemeThemeChromeThemeToggle"


class RegistryThemeThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class RegistryThemeThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class RegistryThemeThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class RegistryThemeThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class RegistryThemeThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class RegistryThemeThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class RegistryThemeThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class RegistryThemeThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class RegistryThemeThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class RegistryThemeThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class RegistryThemeThemeComponents(TypedDict, total=False):
    button: "RegistryThemeThemeComponentsButton"
    code: "RegistryThemeThemeComponentsCode"
    focus: "RegistryThemeThemeComponentsFocus"
    input: "RegistryThemeThemeComponentsInput"
    radius: float
    scrollbar: "RegistryThemeThemeComponentsScrollbar"
    selection: "RegistryThemeThemeComponentsSelection"
    shadow: str
    spacing: "RegistryThemeThemeComponentsSpacing"
    syntax: "RegistryThemeThemeComponentsSyntax"
    syntaxDark: "RegistryThemeThemeComponentsSyntaxDark"


class RegistryThemeThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class RegistryThemeThemeLayout(TypedDict, total=False):
    measure: str


class RegistryThemeThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class RegistryThemeThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class RegistryThemeThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class RegistryThemeThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class RegistryThemeThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class RegistryThemeThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


RegistryThemeThemeMotionTargets = TypedDict("RegistryThemeThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class RegistryThemeThemeMotion(TypedDict, total=False):
    ambient: "RegistryThemeThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "RegistryThemeThemeMotionHeader"
    hover: "RegistryThemeThemeMotionHover"
    keyframes: List["RegistryThemeThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "RegistryThemeThemeMotionReveal"
    speed: float
    targets: "RegistryThemeThemeMotionTargets"


class RegistryThemeThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class RegistryThemeThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["RegistryThemeThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class RegistryThemeThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class RegistryThemeThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class RegistryThemeThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class RegistryThemeTheme(TypedDict, total=False):
    accentColor: str
    ads: "RegistryThemeThemeAds"
    announcement: "RegistryThemeThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "RegistryThemeThemeChrome"
    colorScheme: str
    componentInstalls: List["RegistryThemeThemeComponentInstall"]
    components: "RegistryThemeThemeComponents"
    contentWidth: str
    cssSnippets: List["RegistryThemeThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "RegistryThemeThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "RegistryThemeThemeMobile"
    monoFontFamily: str
    motion: "RegistryThemeThemeMotion"
    notFound: "RegistryThemeThemeNotFound"
    onThisPage: str
    palette: "RegistryThemeThemePalette"
    paletteDark: "RegistryThemeThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["RegistryThemeThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ScimGroupMember(TypedDict, total=False):
    display: str
    value: str


class ScimUserEmail(TypedDict, total=False):
    primary: bool
    value: str


class ScimUserName(TypedDict, total=False):
    formatted: str


class ShapeOverrideParams(TypedDict, total=False):
    add: List["SpaceTypeField"]
    omit: List[str]
    order: List[str]
    set: Dict[str, Any]


class ShapeOverrideSections(TypedDict, total=False):
    add: List["SpaceTypeSection"]
    omit: List[str]
    order: List[str]
    set: Dict[str, Any]


class ShapeOverrideSpace(TypedDict, total=False):
    index: str
    nav: str
    order: str
    summary: List[str]
    whoCreates: str


class SiteConfigCta(TypedDict, total=False):
    href: str
    label: str


class SiteConfigFooterColumnLink(TypedDict, total=False):
    href: str
    label: str


class SiteConfigFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SiteConfigFooterColumnLink"]


class SiteConfigFooterLink(TypedDict, total=False):
    href: str
    label: str


class SiteConfigHeaderLinkChildrenItem(TypedDict, total=False):
    badge: str
    description: str
    href: str
    icon: str
    label: str


class SiteConfigHeaderLinkPanelFeatured(TypedDict, total=False):
    href: str
    image: str
    text: str
    title: str


class SiteConfigHeaderLinkPanelFooter(TypedDict, total=False):
    cta: Dict[str, Any]
    links: List[Dict[str, Any]]


class SiteConfigHeaderLinkPanel(TypedDict, total=False):
    align: str
    columns: List[Dict[str, Any]]
    css: str
    featured: "SiteConfigHeaderLinkPanelFeatured"
    footer: "SiteConfigHeaderLinkPanelFooter"
    html: str
    width: str


class SiteConfigHeaderLink(TypedDict, total=False):
    children: List["SiteConfigHeaderLinkChildrenItem"]
    highlight: bool
    href: str
    label: str
    panel: "SiteConfigHeaderLinkPanel"
    style: str


class SiteConfigNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class SiteConfigSocialLink(TypedDict, total=False):
    href: str
    platform: str


class SiteConfigThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class SiteSpaceRefAddress(TypedDict, total=False):
    basePath: str
    hostname: str


class SpaceAddressChecks(TypedDict, total=False):
    certificate: "Check"
    dns: "Check"
    serving: "Check"


class SpaceExportPage(TypedDict, total=False):
    content: "BlockDoc"
    title: str


class SpaceExportSpace(TypedDict, total=False):
    name: str
    slug: str


class SpaceExportThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class SpaceExportThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class SpaceExportThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class SpaceExportThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class SpaceExportThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class SpaceExportThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class SpaceExportThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class SpaceExportThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class SpaceExportThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class SpaceExportThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "SpaceExportThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["SpaceExportThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["SpaceExportThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["SpaceExportThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "SpaceExportThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["SpaceExportThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "SpaceExportThemeChromeThemeToggle"


class SpaceExportThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpaceExportThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class SpaceExportThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpaceExportThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class SpaceExportThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpaceExportThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class SpaceExportThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SpaceExportThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class SpaceExportThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpaceExportThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpaceExportThemeComponents(TypedDict, total=False):
    button: "SpaceExportThemeComponentsButton"
    code: "SpaceExportThemeComponentsCode"
    focus: "SpaceExportThemeComponentsFocus"
    input: "SpaceExportThemeComponentsInput"
    radius: float
    scrollbar: "SpaceExportThemeComponentsScrollbar"
    selection: "SpaceExportThemeComponentsSelection"
    shadow: str
    spacing: "SpaceExportThemeComponentsSpacing"
    syntax: "SpaceExportThemeComponentsSyntax"
    syntaxDark: "SpaceExportThemeComponentsSyntaxDark"


class SpaceExportThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class SpaceExportThemeLayout(TypedDict, total=False):
    measure: str


class SpaceExportThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class SpaceExportThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class SpaceExportThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SpaceExportThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class SpaceExportThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class SpaceExportThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


SpaceExportThemeMotionTargets = TypedDict("SpaceExportThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class SpaceExportThemeMotion(TypedDict, total=False):
    ambient: "SpaceExportThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "SpaceExportThemeMotionHeader"
    hover: "SpaceExportThemeMotionHover"
    keyframes: List["SpaceExportThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "SpaceExportThemeMotionReveal"
    speed: float
    targets: "SpaceExportThemeMotionTargets"


class SpaceExportThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class SpaceExportThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["SpaceExportThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class SpaceExportThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpaceExportThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpaceExportThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class SpaceExportTheme(TypedDict, total=False):
    accentColor: str
    ads: "SpaceExportThemeAds"
    announcement: "SpaceExportThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "SpaceExportThemeChrome"
    colorScheme: str
    componentInstalls: List["SpaceExportThemeComponentInstall"]
    components: "SpaceExportThemeComponents"
    contentWidth: str
    cssSnippets: List["SpaceExportThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "SpaceExportThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "SpaceExportThemeMobile"
    monoFontFamily: str
    motion: "SpaceExportThemeMotion"
    notFound: "SpaceExportThemeNotFound"
    onThisPage: str
    palette: "SpaceExportThemePalette"
    paletteDark: "SpaceExportThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["SpaceExportThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class SpacePublicSeoSocialCard(TypedDict, total=False):
    accent: str
    accentBar: bool
    background: str
    backgroundTo: str
    eyebrowColor: str
    font: str
    footer: str
    logoUrl: str
    titleColor: str


class SpacePublicSeoVerification(TypedDict, total=False):
    bing: str
    google: str


class SpaceShapeViewPresetLayoutItem(TypedDict, total=False):
    block: str
    key: str
    columns: List[Dict[str, Any]]
    count: float
    level: Any


class SpaceShapeViewPreset(TypedDict, total=False):
    description: str
    label: str
    layout: List["SpaceShapeViewPresetLayoutItem"]
    name: str
    own: bool
    sections: List["KindSlot"]


class SpaceTypeSpecReaderTools(TypedDict, total=False):
    aiActions: bool
    copyMarkdown: bool
    mcp: bool
    pdf: bool
    search: bool


class SpaceTypeSpecRoute(TypedDict, total=False):
    content: str
    defaultSlug: str
    hubs: List["SpaceHubRoute"]
    orgIndexed: bool
    pieceAddressed: bool
    publicPrefix: str
    rootRedirectsToFirstPiece: bool


class SpaceTypeSpecSettings(TypedDict, total=False):
    advanced: List[str]
    essential: List[str]


class SpaceTypeSpecVocabularyEmpty(TypedDict, total=False):
    hint: str
    title: str


class SpaceTypeSpecVocabulary(TypedDict, total=False):
    container: List[str]
    empty: "SpaceTypeSpecVocabularyEmpty"
    piece: List[str]
    primaryAction: str


class SpaceTypographyFeatures(TypedDict, total=False):
    body: str
    code: str
    heading: str


class SpaceTypographyFluid(TypedDict, total=False):
    bodyMinScale: float
    enabled: bool
    maxViewport: float
    minScale: float
    minViewport: float


class SpaceTypographyLevels(TypedDict, total=False):
    body: "TypeLevelSettings"
    code: "TypeLevelSettings"
    h1: "TypeLevelSettings"
    h2: "TypeLevelSettings"
    h3: "TypeLevelSettings"
    h4: "TypeLevelSettings"
    h5: "TypeLevelSettings"
    h6: "TypeLevelSettings"
    small: "TypeLevelSettings"


class SpaceTypographyVariation(TypedDict, total=False):
    body: str
    code: str
    heading: str


class StatusSummaryComponent(TypedDict, total=False):
    name: str
    status: str
    uptime: Any
    window: "UptimeWindow"


class StatusSummaryIncident(TypedDict, total=False):
    name: str
    started_at: str
    status: str
    updated_at: str


class StatusSummaryPage(TypedDict, total=False):
    name: str


class StatusSummaryStatus(TypedDict, total=False):
    description: str
    indicator: str


class SubmissionRowAttachment(TypedDict, total=False):
    assetId: str
    filename: str
    size: float


class SubmittedComponentListingComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class SubmittedComponentListingComponentMetaPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class SubmittedComponentListingComponentMeta(TypedDict, total=False):
    author: "SubmittedComponentListingComponentMetaAuthor"
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List["SubmittedComponentListingComponentMetaPreviewImage"]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


SubmittedComponentListingComponentOutlets = TypedDict("SubmittedComponentListingComponentOutlets", {"above-main": Any, "below-main": Any, "blog-index-above-list": Any, "blog-post-after": Any, "blog-post-before": Any, "careers-above-list": Any, "category-header": Any, "changelog-above-list": Any, "courses-above-list": Any, "docs-page-footer": Any, "docs-page-header": Any, "events-above-list": Any, "faq-above-list": Any, "footer-after": Any, "footer-before": Any, "forum-index-above-list": Any, "forum-index-below-list": Any, "forum-post-after-body": Any, "forum-sidebar-bottom": Any, "forum-sidebar-top": Any, "forum-topic-above-title": Any, "forum-topic-below-first-post": Any, "forum-topic-below-title": Any, "forum-topic-bottom": Any, "header-after": Any, "header-before": Any, "roadmap-above-board": Any, "status-above-board": Any, "user-card": Any}, total=False)


class SubmittedComponentListingComponent(TypedDict, total=False):
    css: str
    format: str
    formatVersion: float
    meta: "SubmittedComponentListingComponentMeta"
    outlets: "SubmittedComponentListingComponentOutlets"
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class SubmittedThemeListingBundleComponentMeta(TypedDict, total=False):
    author: Dict[str, Any]
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List[Dict[str, Any]]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


SubmittedThemeListingBundleComponentOutlets = TypedDict("SubmittedThemeListingBundleComponentOutlets", {"above-main": Any, "below-main": Any, "blog-index-above-list": Any, "blog-post-after": Any, "blog-post-before": Any, "careers-above-list": Any, "category-header": Any, "changelog-above-list": Any, "courses-above-list": Any, "docs-page-footer": Any, "docs-page-header": Any, "events-above-list": Any, "faq-above-list": Any, "footer-after": Any, "footer-before": Any, "forum-index-above-list": Any, "forum-index-below-list": Any, "forum-post-after-body": Any, "forum-sidebar-bottom": Any, "forum-sidebar-top": Any, "forum-topic-above-title": Any, "forum-topic-below-first-post": Any, "forum-topic-below-title": Any, "forum-topic-bottom": Any, "header-after": Any, "header-before": Any, "roadmap-above-board": Any, "status-above-board": Any, "user-card": Any}, total=False)


class SubmittedThemeListingBundleComponent(TypedDict, total=False):
    css: str
    format: str
    formatVersion: float
    meta: "SubmittedThemeListingBundleComponentMeta"
    outlets: "SubmittedThemeListingBundleComponentOutlets"
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class SubmittedThemeListingBundleMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class SubmittedThemeListingBundleMetaPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class SubmittedThemeListingBundleMeta(TypedDict, total=False):
    author: "SubmittedThemeListingBundleMetaAuthor"
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List["SubmittedThemeListingBundleMetaPreviewImage"]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


class SubmittedThemeListingBundleRequiredOrigins(TypedDict, total=False):
    fonts: List[str]
    images: List[str]


class SubmittedThemeListingBundleThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class SubmittedThemeListingBundleThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class SubmittedThemeListingBundleThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class SubmittedThemeListingBundleThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "SubmittedThemeListingBundleThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List[Dict[str, Any]]
    footerDescription: str
    footerLinks: List[Dict[str, Any]]
    header: "ChromeHeader"
    headerLinks: List[Dict[str, Any]]
    height: str
    mobileNav: str
    navMenu: "SubmittedThemeListingBundleThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List[Dict[str, Any]]
    sticky: bool
    themeToggle: "SubmittedThemeListingBundleThemeChromeThemeToggle"


class SubmittedThemeListingBundleThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class SubmittedThemeListingBundleThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SubmittedThemeListingBundleThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class SubmittedThemeListingBundleThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SubmittedThemeListingBundleThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class SubmittedThemeListingBundleThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SubmittedThemeListingBundleThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class SubmittedThemeListingBundleThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SubmittedThemeListingBundleThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SubmittedThemeListingBundleThemeComponents(TypedDict, total=False):
    button: "SubmittedThemeListingBundleThemeComponentsButton"
    code: "SubmittedThemeListingBundleThemeComponentsCode"
    focus: "SubmittedThemeListingBundleThemeComponentsFocus"
    input: "SubmittedThemeListingBundleThemeComponentsInput"
    radius: float
    scrollbar: "SubmittedThemeListingBundleThemeComponentsScrollbar"
    selection: "SubmittedThemeListingBundleThemeComponentsSelection"
    shadow: str
    spacing: "SubmittedThemeListingBundleThemeComponentsSpacing"
    syntax: "SubmittedThemeListingBundleThemeComponentsSyntax"
    syntaxDark: "SubmittedThemeListingBundleThemeComponentsSyntaxDark"


class SubmittedThemeListingBundleThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class SubmittedThemeListingBundleThemeLayout(TypedDict, total=False):
    measure: str


class SubmittedThemeListingBundleThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class SubmittedThemeListingBundleThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class SubmittedThemeListingBundleThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SubmittedThemeListingBundleThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class SubmittedThemeListingBundleThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


SubmittedThemeListingBundleThemeMotionTargets = TypedDict("SubmittedThemeListingBundleThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class SubmittedThemeListingBundleThemeMotion(TypedDict, total=False):
    ambient: "SubmittedThemeListingBundleThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "SubmittedThemeListingBundleThemeMotionHeader"
    hover: "SubmittedThemeListingBundleThemeMotionHover"
    keyframes: List[Dict[str, Any]]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "SubmittedThemeListingBundleThemeMotionReveal"
    speed: float
    targets: "SubmittedThemeListingBundleThemeMotionTargets"


class SubmittedThemeListingBundleThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SubmittedThemeListingBundleThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SubmittedThemeListingBundleThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class SubmittedThemeListingBundleTheme(TypedDict, total=False):
    accentColor: str
    bodyFontFamily: str
    chrome: "SubmittedThemeListingBundleThemeChrome"
    colorScheme: str
    components: "SubmittedThemeListingBundleThemeComponents"
    contentWidth: str
    cssSnippets: List["SubmittedThemeListingBundleThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    elementStyles: List["ElementStyleRule"]
    font: str
    fonts: "ThemeFonts"
    headingFontFamily: str
    layout: "SubmittedThemeListingBundleThemeLayout"
    mobile: "SubmittedThemeListingBundleThemeMobile"
    monoFontFamily: str
    motion: "SubmittedThemeListingBundleThemeMotion"
    onThisPage: str
    palette: "SubmittedThemeListingBundleThemePalette"
    paletteDark: "SubmittedThemeListingBundleThemePaletteDark"
    primaryColor: str
    settings: Dict[str, Any]
    settingsSchema: List["SubmittedThemeListingBundleThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"


class SubmittedThemeListingBundle(TypedDict, total=False):
    components: List["SubmittedThemeListingBundleComponent"]
    format: str
    formatVersion: Any
    meta: "SubmittedThemeListingBundleMeta"
    requiredOrigins: "SubmittedThemeListingBundleRequiredOrigins"
    theme: "SubmittedThemeListingBundleTheme"


class ThemeBrowseResultFacetsSpaceType(TypedDict, total=False):
    count: float
    type: str


class ThemeBrowseResultFacetsTag(TypedDict, total=False):
    count: float
    tag: str


class ThemeBrowseResultFacets(TypedDict, total=False):
    spaceTypes: List["ThemeBrowseResultFacetsSpaceType"]
    tags: List["ThemeBrowseResultFacetsTag"]


class ThemeBundleExportBundleComponentMeta(TypedDict, total=False):
    author: Dict[str, Any]
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List[Dict[str, Any]]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


ThemeBundleExportBundleComponentOutlets = TypedDict("ThemeBundleExportBundleComponentOutlets", {"above-main": Any, "below-main": Any, "blog-index-above-list": Any, "blog-post-after": Any, "blog-post-before": Any, "careers-above-list": Any, "category-header": Any, "changelog-above-list": Any, "courses-above-list": Any, "docs-page-footer": Any, "docs-page-header": Any, "events-above-list": Any, "faq-above-list": Any, "footer-after": Any, "footer-before": Any, "forum-index-above-list": Any, "forum-index-below-list": Any, "forum-post-after-body": Any, "forum-sidebar-bottom": Any, "forum-sidebar-top": Any, "forum-topic-above-title": Any, "forum-topic-below-first-post": Any, "forum-topic-below-title": Any, "forum-topic-bottom": Any, "header-after": Any, "header-before": Any, "roadmap-above-board": Any, "status-above-board": Any, "user-card": Any}, total=False)


class ThemeBundleExportBundleComponent(TypedDict, total=False):
    css: str
    format: str
    formatVersion: float
    meta: "ThemeBundleExportBundleComponentMeta"
    outlets: "ThemeBundleExportBundleComponentOutlets"
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ThemeBundleExportBundleMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemeBundleExportBundleMetaPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class ThemeBundleExportBundleMeta(TypedDict, total=False):
    author: "ThemeBundleExportBundleMetaAuthor"
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List["ThemeBundleExportBundleMetaPreviewImage"]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


class ThemeBundleExportBundleRequiredOrigins(TypedDict, total=False):
    fonts: List[str]
    images: List[str]


class ThemeBundleExportBundleThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ThemeBundleExportBundleThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ThemeBundleExportBundleThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ThemeBundleExportBundleThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ThemeBundleExportBundleThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List[Dict[str, Any]]
    footerDescription: str
    footerLinks: List[Dict[str, Any]]
    header: "ChromeHeader"
    headerLinks: List[Dict[str, Any]]
    height: str
    mobileNav: str
    navMenu: "ThemeBundleExportBundleThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List[Dict[str, Any]]
    sticky: bool
    themeToggle: "ThemeBundleExportBundleThemeChromeThemeToggle"


class ThemeBundleExportBundleThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ThemeBundleExportBundleThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeBundleExportBundleThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ThemeBundleExportBundleThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeBundleExportBundleThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ThemeBundleExportBundleThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemeBundleExportBundleThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ThemeBundleExportBundleThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeBundleExportBundleThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeBundleExportBundleThemeComponents(TypedDict, total=False):
    button: "ThemeBundleExportBundleThemeComponentsButton"
    code: "ThemeBundleExportBundleThemeComponentsCode"
    focus: "ThemeBundleExportBundleThemeComponentsFocus"
    input: "ThemeBundleExportBundleThemeComponentsInput"
    radius: float
    scrollbar: "ThemeBundleExportBundleThemeComponentsScrollbar"
    selection: "ThemeBundleExportBundleThemeComponentsSelection"
    shadow: str
    spacing: "ThemeBundleExportBundleThemeComponentsSpacing"
    syntax: "ThemeBundleExportBundleThemeComponentsSyntax"
    syntaxDark: "ThemeBundleExportBundleThemeComponentsSyntaxDark"


class ThemeBundleExportBundleThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ThemeBundleExportBundleThemeLayout(TypedDict, total=False):
    measure: str


class ThemeBundleExportBundleThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ThemeBundleExportBundleThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ThemeBundleExportBundleThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemeBundleExportBundleThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ThemeBundleExportBundleThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ThemeBundleExportBundleThemeMotionTargets = TypedDict("ThemeBundleExportBundleThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ThemeBundleExportBundleThemeMotion(TypedDict, total=False):
    ambient: "ThemeBundleExportBundleThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ThemeBundleExportBundleThemeMotionHeader"
    hover: "ThemeBundleExportBundleThemeMotionHover"
    keyframes: List[Dict[str, Any]]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ThemeBundleExportBundleThemeMotionReveal"
    speed: float
    targets: "ThemeBundleExportBundleThemeMotionTargets"


class ThemeBundleExportBundleThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeBundleExportBundleThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeBundleExportBundleThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ThemeBundleExportBundleTheme(TypedDict, total=False):
    accentColor: str
    bodyFontFamily: str
    chrome: "ThemeBundleExportBundleThemeChrome"
    colorScheme: str
    components: "ThemeBundleExportBundleThemeComponents"
    contentWidth: str
    cssSnippets: List["ThemeBundleExportBundleThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    elementStyles: List["ElementStyleRule"]
    font: str
    fonts: "ThemeFonts"
    headingFontFamily: str
    layout: "ThemeBundleExportBundleThemeLayout"
    mobile: "ThemeBundleExportBundleThemeMobile"
    monoFontFamily: str
    motion: "ThemeBundleExportBundleThemeMotion"
    onThisPage: str
    palette: "ThemeBundleExportBundleThemePalette"
    paletteDark: "ThemeBundleExportBundleThemePaletteDark"
    primaryColor: str
    settings: Dict[str, Any]
    settingsSchema: List["ThemeBundleExportBundleThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"


class ThemeBundleExportBundle(TypedDict, total=False):
    components: List["ThemeBundleExportBundleComponent"]
    format: str
    formatVersion: Any
    meta: "ThemeBundleExportBundleMeta"
    requiredOrigins: "ThemeBundleExportBundleRequiredOrigins"
    theme: "ThemeBundleExportBundleTheme"


class ThemeComponentExportForumulate(TypedDict, total=False):
    exportedAt: str
    type: str
    version: float


class ThemeComponentExportThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ThemeComponentExportThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ThemeComponentExportThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ThemeComponentExportThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemeComponentExportThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ThemeComponentExportThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ThemeComponentExportThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ThemeComponentExportThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ThemeComponentExportThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ThemeComponentExportThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ThemeComponentExportThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ThemeComponentExportThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ThemeComponentExportThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ThemeComponentExportThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ThemeComponentExportThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ThemeComponentExportThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ThemeComponentExportThemeChromeThemeToggle"


class ThemeComponentExportThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ThemeComponentExportThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ThemeComponentExportThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeComponentExportThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ThemeComponentExportThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeComponentExportThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ThemeComponentExportThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemeComponentExportThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ThemeComponentExportThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeComponentExportThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeComponentExportThemeComponents(TypedDict, total=False):
    button: "ThemeComponentExportThemeComponentsButton"
    code: "ThemeComponentExportThemeComponentsCode"
    focus: "ThemeComponentExportThemeComponentsFocus"
    input: "ThemeComponentExportThemeComponentsInput"
    radius: float
    scrollbar: "ThemeComponentExportThemeComponentsScrollbar"
    selection: "ThemeComponentExportThemeComponentsSelection"
    shadow: str
    spacing: "ThemeComponentExportThemeComponentsSpacing"
    syntax: "ThemeComponentExportThemeComponentsSyntax"
    syntaxDark: "ThemeComponentExportThemeComponentsSyntaxDark"


class ThemeComponentExportThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ThemeComponentExportThemeLayout(TypedDict, total=False):
    measure: str


class ThemeComponentExportThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ThemeComponentExportThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ThemeComponentExportThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemeComponentExportThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ThemeComponentExportThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ThemeComponentExportThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ThemeComponentExportThemeMotionTargets = TypedDict("ThemeComponentExportThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ThemeComponentExportThemeMotion(TypedDict, total=False):
    ambient: "ThemeComponentExportThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ThemeComponentExportThemeMotionHeader"
    hover: "ThemeComponentExportThemeMotionHover"
    keyframes: List["ThemeComponentExportThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ThemeComponentExportThemeMotionReveal"
    speed: float
    targets: "ThemeComponentExportThemeMotionTargets"


class ThemeComponentExportThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ThemeComponentExportThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ThemeComponentExportThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ThemeComponentExportThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeComponentExportThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeComponentExportThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ThemeComponentExportTheme(TypedDict, total=False):
    accentColor: str
    ads: "ThemeComponentExportThemeAds"
    announcement: "ThemeComponentExportThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ThemeComponentExportThemeChrome"
    colorScheme: str
    componentInstalls: List["ThemeComponentExportThemeComponentInstall"]
    components: "ThemeComponentExportThemeComponents"
    contentWidth: str
    cssSnippets: List["ThemeComponentExportThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ThemeComponentExportThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ThemeComponentExportThemeMobile"
    monoFontFamily: str
    motion: "ThemeComponentExportThemeMotion"
    notFound: "ThemeComponentExportThemeNotFound"
    onThisPage: str
    palette: "ThemeComponentExportThemePalette"
    paletteDark: "ThemeComponentExportThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ThemeComponentExportThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ThemeComponentSummaryThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ThemeComponentSummaryThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ThemeComponentSummaryThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ThemeComponentSummaryThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemeComponentSummaryThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ThemeComponentSummaryThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ThemeComponentSummaryThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ThemeComponentSummaryThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ThemeComponentSummaryThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ThemeComponentSummaryThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ThemeComponentSummaryThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ThemeComponentSummaryThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ThemeComponentSummaryThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ThemeComponentSummaryThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ThemeComponentSummaryThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ThemeComponentSummaryThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ThemeComponentSummaryThemeChromeThemeToggle"


class ThemeComponentSummaryThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ThemeComponentSummaryThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ThemeComponentSummaryThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeComponentSummaryThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ThemeComponentSummaryThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeComponentSummaryThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ThemeComponentSummaryThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemeComponentSummaryThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ThemeComponentSummaryThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeComponentSummaryThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeComponentSummaryThemeComponents(TypedDict, total=False):
    button: "ThemeComponentSummaryThemeComponentsButton"
    code: "ThemeComponentSummaryThemeComponentsCode"
    focus: "ThemeComponentSummaryThemeComponentsFocus"
    input: "ThemeComponentSummaryThemeComponentsInput"
    radius: float
    scrollbar: "ThemeComponentSummaryThemeComponentsScrollbar"
    selection: "ThemeComponentSummaryThemeComponentsSelection"
    shadow: str
    spacing: "ThemeComponentSummaryThemeComponentsSpacing"
    syntax: "ThemeComponentSummaryThemeComponentsSyntax"
    syntaxDark: "ThemeComponentSummaryThemeComponentsSyntaxDark"


class ThemeComponentSummaryThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ThemeComponentSummaryThemeLayout(TypedDict, total=False):
    measure: str


class ThemeComponentSummaryThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ThemeComponentSummaryThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ThemeComponentSummaryThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemeComponentSummaryThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ThemeComponentSummaryThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ThemeComponentSummaryThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ThemeComponentSummaryThemeMotionTargets = TypedDict("ThemeComponentSummaryThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ThemeComponentSummaryThemeMotion(TypedDict, total=False):
    ambient: "ThemeComponentSummaryThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ThemeComponentSummaryThemeMotionHeader"
    hover: "ThemeComponentSummaryThemeMotionHover"
    keyframes: List["ThemeComponentSummaryThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ThemeComponentSummaryThemeMotionReveal"
    speed: float
    targets: "ThemeComponentSummaryThemeMotionTargets"


class ThemeComponentSummaryThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ThemeComponentSummaryThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ThemeComponentSummaryThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ThemeComponentSummaryThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeComponentSummaryThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeComponentSummaryThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ThemeComponentSummaryTheme(TypedDict, total=False):
    accentColor: str
    ads: "ThemeComponentSummaryThemeAds"
    announcement: "ThemeComponentSummaryThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ThemeComponentSummaryThemeChrome"
    colorScheme: str
    componentInstalls: List["ThemeComponentSummaryThemeComponentInstall"]
    components: "ThemeComponentSummaryThemeComponents"
    contentWidth: str
    cssSnippets: List["ThemeComponentSummaryThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ThemeComponentSummaryThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ThemeComponentSummaryThemeMobile"
    monoFontFamily: str
    motion: "ThemeComponentSummaryThemeMotion"
    notFound: "ThemeComponentSummaryThemeNotFound"
    onThisPage: str
    palette: "ThemeComponentSummaryThemePalette"
    paletteDark: "ThemeComponentSummaryThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ThemeComponentSummaryThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ThemeLibraryItemThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ThemeLibraryItemThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ThemeLibraryItemThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ThemeLibraryItemThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemeLibraryItemThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ThemeLibraryItemThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ThemeLibraryItemThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ThemeLibraryItemThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ThemeLibraryItemThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ThemeLibraryItemThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ThemeLibraryItemThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ThemeLibraryItemThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ThemeLibraryItemThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ThemeLibraryItemThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ThemeLibraryItemThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ThemeLibraryItemThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ThemeLibraryItemThemeChromeThemeToggle"


class ThemeLibraryItemThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ThemeLibraryItemThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ThemeLibraryItemThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeLibraryItemThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ThemeLibraryItemThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeLibraryItemThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ThemeLibraryItemThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemeLibraryItemThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ThemeLibraryItemThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeLibraryItemThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeLibraryItemThemeComponents(TypedDict, total=False):
    button: "ThemeLibraryItemThemeComponentsButton"
    code: "ThemeLibraryItemThemeComponentsCode"
    focus: "ThemeLibraryItemThemeComponentsFocus"
    input: "ThemeLibraryItemThemeComponentsInput"
    radius: float
    scrollbar: "ThemeLibraryItemThemeComponentsScrollbar"
    selection: "ThemeLibraryItemThemeComponentsSelection"
    shadow: str
    spacing: "ThemeLibraryItemThemeComponentsSpacing"
    syntax: "ThemeLibraryItemThemeComponentsSyntax"
    syntaxDark: "ThemeLibraryItemThemeComponentsSyntaxDark"


class ThemeLibraryItemThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ThemeLibraryItemThemeLayout(TypedDict, total=False):
    measure: str


class ThemeLibraryItemThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ThemeLibraryItemThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ThemeLibraryItemThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemeLibraryItemThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ThemeLibraryItemThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ThemeLibraryItemThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ThemeLibraryItemThemeMotionTargets = TypedDict("ThemeLibraryItemThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ThemeLibraryItemThemeMotion(TypedDict, total=False):
    ambient: "ThemeLibraryItemThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ThemeLibraryItemThemeMotionHeader"
    hover: "ThemeLibraryItemThemeMotionHover"
    keyframes: List["ThemeLibraryItemThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ThemeLibraryItemThemeMotionReveal"
    speed: float
    targets: "ThemeLibraryItemThemeMotionTargets"


class ThemeLibraryItemThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ThemeLibraryItemThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ThemeLibraryItemThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ThemeLibraryItemThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeLibraryItemThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeLibraryItemThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ThemeLibraryItemTheme(TypedDict, total=False):
    accentColor: str
    ads: "ThemeLibraryItemThemeAds"
    announcement: "ThemeLibraryItemThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ThemeLibraryItemThemeChrome"
    colorScheme: str
    componentInstalls: List["ThemeLibraryItemThemeComponentInstall"]
    components: "ThemeLibraryItemThemeComponents"
    contentWidth: str
    cssSnippets: List["ThemeLibraryItemThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ThemeLibraryItemThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ThemeLibraryItemThemeMobile"
    monoFontFamily: str
    motion: "ThemeLibraryItemThemeMotion"
    notFound: "ThemeLibraryItemThemeNotFound"
    onThisPage: str
    palette: "ThemeLibraryItemThemePalette"
    paletteDark: "ThemeLibraryItemThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ThemeLibraryItemThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ThemeLibraryMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemeLibraryMetaPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class ThemeListingAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemeListingPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class ThemeListingRequiredOrigins(TypedDict, total=False):
    fonts: List[str]
    images: List[str]


class ThemeListingDetailAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemeListingDetailPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class ThemeListingDetailRequiredOrigins(TypedDict, total=False):
    fonts: List[str]
    images: List[str]


class ThemeListingDetailThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ThemeListingDetailThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemeListingDetailThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ThemeListingDetailThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ThemeListingDetailThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ThemeListingDetailThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ThemeListingDetailThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ThemeListingDetailThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ThemeListingDetailThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ThemeListingDetailThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ThemeListingDetailThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ThemeListingDetailThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ThemeListingDetailThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ThemeListingDetailThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ThemeListingDetailThemeChromeThemeToggle"


class ThemeListingDetailThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ThemeListingDetailThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeListingDetailThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ThemeListingDetailThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemeListingDetailThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ThemeListingDetailThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemeListingDetailThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ThemeListingDetailThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeListingDetailThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemeListingDetailThemeComponents(TypedDict, total=False):
    button: "ThemeListingDetailThemeComponentsButton"
    code: "ThemeListingDetailThemeComponentsCode"
    focus: "ThemeListingDetailThemeComponentsFocus"
    input: "ThemeListingDetailThemeComponentsInput"
    radius: float
    scrollbar: "ThemeListingDetailThemeComponentsScrollbar"
    selection: "ThemeListingDetailThemeComponentsSelection"
    shadow: str
    spacing: "ThemeListingDetailThemeComponentsSpacing"
    syntax: "ThemeListingDetailThemeComponentsSyntax"
    syntaxDark: "ThemeListingDetailThemeComponentsSyntaxDark"


class ThemeListingDetailThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ThemeListingDetailThemeLayout(TypedDict, total=False):
    measure: str


class ThemeListingDetailThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ThemeListingDetailThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ThemeListingDetailThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemeListingDetailThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ThemeListingDetailThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ThemeListingDetailThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ThemeListingDetailThemeMotionTargets = TypedDict("ThemeListingDetailThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ThemeListingDetailThemeMotion(TypedDict, total=False):
    ambient: "ThemeListingDetailThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ThemeListingDetailThemeMotionHeader"
    hover: "ThemeListingDetailThemeMotionHover"
    keyframes: List["ThemeListingDetailThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ThemeListingDetailThemeMotionReveal"
    speed: float
    targets: "ThemeListingDetailThemeMotionTargets"


class ThemeListingDetailThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeListingDetailThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemeListingDetailThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ThemeListingDetailTheme(TypedDict, total=False):
    accentColor: str
    bodyFontFamily: str
    chrome: "ThemeListingDetailThemeChrome"
    colorScheme: str
    components: "ThemeListingDetailThemeComponents"
    contentWidth: str
    cssSnippets: List["ThemeListingDetailThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    elementStyles: List["ElementStyleRule"]
    font: str
    fonts: "ThemeFonts"
    headingFontFamily: str
    layout: "ThemeListingDetailThemeLayout"
    mobile: "ThemeListingDetailThemeMobile"
    monoFontFamily: str
    motion: "ThemeListingDetailThemeMotion"
    onThisPage: str
    palette: "ThemeListingDetailThemePalette"
    paletteDark: "ThemeListingDetailThemePaletteDark"
    primaryColor: str
    settings: Dict[str, Any]
    settingsSchema: List["ThemeListingDetailThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"


class ThemePresetThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ThemePresetThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ThemePresetThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ThemePresetThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemePresetThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ThemePresetThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ThemePresetThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ThemePresetThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ThemePresetThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ThemePresetThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ThemePresetThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ThemePresetThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ThemePresetThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ThemePresetThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ThemePresetThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ThemePresetThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ThemePresetThemeChromeThemeToggle"


class ThemePresetThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ThemePresetThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ThemePresetThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemePresetThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ThemePresetThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemePresetThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ThemePresetThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemePresetThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ThemePresetThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemePresetThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemePresetThemeComponents(TypedDict, total=False):
    button: "ThemePresetThemeComponentsButton"
    code: "ThemePresetThemeComponentsCode"
    focus: "ThemePresetThemeComponentsFocus"
    input: "ThemePresetThemeComponentsInput"
    radius: float
    scrollbar: "ThemePresetThemeComponentsScrollbar"
    selection: "ThemePresetThemeComponentsSelection"
    shadow: str
    spacing: "ThemePresetThemeComponentsSpacing"
    syntax: "ThemePresetThemeComponentsSyntax"
    syntaxDark: "ThemePresetThemeComponentsSyntaxDark"


class ThemePresetThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ThemePresetThemeLayout(TypedDict, total=False):
    measure: str


class ThemePresetThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ThemePresetThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ThemePresetThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemePresetThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ThemePresetThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ThemePresetThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ThemePresetThemeMotionTargets = TypedDict("ThemePresetThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ThemePresetThemeMotion(TypedDict, total=False):
    ambient: "ThemePresetThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ThemePresetThemeMotionHeader"
    hover: "ThemePresetThemeMotionHover"
    keyframes: List["ThemePresetThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ThemePresetThemeMotionReveal"
    speed: float
    targets: "ThemePresetThemeMotionTargets"


class ThemePresetThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ThemePresetThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ThemePresetThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ThemePresetThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemePresetThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemePresetThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ThemePresetTheme(TypedDict, total=False):
    accentColor: str
    ads: "ThemePresetThemeAds"
    announcement: "ThemePresetThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ThemePresetThemeChrome"
    colorScheme: str
    componentInstalls: List["ThemePresetThemeComponentInstall"]
    components: "ThemePresetThemeComponents"
    contentWidth: str
    cssSnippets: List["ThemePresetThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ThemePresetThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ThemePresetThemeMobile"
    monoFontFamily: str
    motion: "ThemePresetThemeMotion"
    notFound: "ThemePresetThemeNotFound"
    onThisPage: str
    palette: "ThemePresetThemePalette"
    paletteDark: "ThemePresetThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ThemePresetThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class TitleDedupeResultPage(TypedDict, total=False):
    id: str
    slug: str
    title: str


class TopicMapTopParticipant(TypedDict, total=False):
    name: str
    posts: float
    userId: Any


class TopicTimelineMarker(TypedDict, total=False):
    createdAt: str
    postNumber: float


class UnifiedSearchResultFacets(TypedDict, total=False):
    blog: Any
    docs: Any
    topic: Any


class UserActionItemActor(TypedDict, total=False):
    id: str
    name: str


class UserCardUser(TypedDict, total=False):
    avatarUrl: Any
    bio: Any
    id: str
    name: str
    username: str


class UserStateAttributesCosmeticsBadge(TypedDict, total=False):
    icon: str
    name: str
    slug: str


class UserStateAttributesCosmetics(TypedDict, total=False):
    badges: List["UserStateAttributesCosmeticsBadge"]
    flair: str
    nameplate: str
    title: str


class UserStateAttributesIdentity(TypedDict, total=False):
    avatarUrl: Any
    name: str
    username: str


class UserStateAttributesPresence(TypedDict, total=False):
    lastActiveAt: Any
    memberSince: str
    unreadTopics: float


class UserStateAttributesSocial(TypedDict, total=False):
    followers: float
    following: float


class UserStateAttributesStanding(TypedDict, total=False):
    daysVisited: float
    postsRead: float
    reputation: float
    trustLevel: float


class UserStateAttributesWalletInventoryItem(TypedDict, total=False):
    itemKey: str
    name: str
    quantity: float


class UserStateAttributesWallet(TypedDict, total=False):
    balances: Dict[str, Any]
    inventory: List["UserStateAttributesWalletInventoryItem"]


class UserStateAttributes(TypedDict, total=False):
    cosmetics: "UserStateAttributesCosmetics"
    identity: "UserStateAttributesIdentity"
    points: float
    presence: "UserStateAttributesPresence"
    progression: Dict[str, Any]
    social: "UserStateAttributesSocial"
    standing: "UserStateAttributesStanding"
    tier: str
    wallet: "UserStateAttributesWallet"


class WalletSummaryInventoryItem(TypedDict, total=False):
    itemKey: str
    name: str
    quantity: float


class ApiActivityMineResponseSummary(TypedDict, total=False):
    avgMs: float
    errorRate: float
    errors: float
    total: float


class ApiActivityMineResponse(TypedDict, total=False):
    calls: List["ApiCall"]
    page: "PageInfo"
    summary: "ApiActivityMineResponseSummary"


class AuthLogoutResponse(TypedDict, total=False):
    ok: bool


class AuthMeResponseImpersonation(TypedDict, total=False):
    impersonatorId: str
    orgId: str


class AuthMeResponseToken(TypedDict, total=False):
    scopes: List[str]
    spaceIds: Any


class AuthMeResponse(TypedDict, total=False):
    impersonation: "AuthMeResponseImpersonation"
    token: "AuthMeResponseToken"
    user: "PublicUser"


class SessionsListResponse(TypedDict, total=False):
    sessions: List["ActiveSession"]
    page: "PageInfo"


class SessionsRevokeResponse(TypedDict, total=False):
    ok: bool


class SessionsRevokeOthersResponse(TypedDict, total=False):
    ok: bool


class TokensRenameParams(TypedDict, total=False):
    name: str


class TokensRevokeResponse(TypedDict, total=False):
    ok: bool


class TokensRotateParams(TypedDict, total=False):
    graceMinutes: int


class DeviceKeysRevokeResponse(TypedDict, total=False):
    ok: bool


class UsersMeResponse(TypedDict, total=False):
    user: "PublicUser"


class UsersUpdateParams(TypedDict, total=False):
    name: str
    avatarUrl: Optional[str]
    bio: Optional[str]
    location: Optional[str]
    websiteUrl: Optional[str]


class UsersUpdateResponse(TypedDict, total=False):
    user: "PublicUser"
    warnings: List[str]


class UsersSetLocaleParams(TypedDict, total=False):
    locale: Optional[str]


class UsersSetLocaleResponse(TypedDict, total=False):
    user: "PublicUser"
    warnings: List[str]


class UsersChangeUsernameParams(TypedDict, total=False):
    username: str


class UsersChangeUsernameResponse(TypedDict, total=False):
    user: "PublicUser"
    warnings: List[str]


class UsersSetProfileVisibilityParams(TypedDict, total=False):
    hidden: bool


class UsersSetProfileVisibilityResponse(TypedDict, total=False):
    user: "PublicUser"
    warnings: List[str]


class UsersDeleteAccountParams(TypedDict, total=False):
    confirm: str


class UsersDeleteAccountResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class RolesCapabilitiesResponseMatrix(TypedDict, total=False):
    ADMIN: Any
    EDITOR: Any
    GUEST: Any
    MAINTAINER: Any
    MEMBER: Any
    MODERATOR: Any
    OWNER: Any


class RolesCapabilitiesResponse(TypedDict, total=False):
    capabilities: List[str]
    matrix: "RolesCapabilitiesResponseMatrix"
    roles: List[str]


class RolesCustomListResponse(TypedDict, total=False):
    roles: List["CustomRoleView"]
    page: "PageInfo"


class RolesCustomCreateParams(TypedDict, total=False):
    name: str
    capabilities: List[str]


class RolesCustomCreateResponse(TypedDict, total=False):
    role: "CustomRoleView"
    data: "CustomRoleView"
    warnings: List[str]


class RolesCustomUpdateParams(TypedDict, total=False):
    name: str
    capabilities: List[str]


class RolesCustomUpdateResponse(TypedDict, total=False):
    role: "CustomRoleView"
    warnings: List[str]


class RolesCustomRemoveResponse(TypedDict, total=False):
    ok: bool


class GroupsGrantsListResponse(TypedDict, total=False):
    grants: List["GroupGrantRow"]
    page: "PageInfo"


class GroupsGrantsGrantParams(TypedDict, total=False):
    groupId: str
    role: str
    spaceId: Optional[str]
    effect: str
    customRoleId: Optional[str]


class GroupsGrantsGrantResponse(TypedDict, total=False):
    grant: "GroupGrantRow"
    data: "GroupGrantRow"
    warnings: List[str]


class GroupsGrantsRevokeResponse(TypedDict, total=False):
    ok: bool


class TranslationsOverridesListResponse(TypedDict, total=False):
    overrides: List["TranslationOverrideView"]
    page: "PageInfo"


class TranslationsOverridesSetParams(TypedDict, total=False):
    locale: str
    key: str
    value: str


class TranslationsOverridesSetResponse(TypedDict, total=False):
    override: "TranslationOverrideView"
    warnings: List[str]


class TranslationsOverridesRemoveResponse(TypedDict, total=False):
    ok: bool


class PublicTranslationsCatalogResponse(TypedDict, total=False):
    catalog: Dict[str, Any]


class PublicTranslationsMapResponse(TypedDict, total=False):
    overrides: Dict[str, Any]


class SpaceTypesListResponse(TypedDict, total=False):
    spaceTypes: List["SpaceTypeSpec"]
    page: "PageInfo"


class SpaceTypesAllPresetsResponse(TypedDict, total=False):
    presets: Dict[str, Any]


class SpaceTypesOneResponse(TypedDict, total=False):
    spaceType: "SpaceTypeSpec"


class SpaceTypesPresetsResponse(TypedDict, total=False):
    frontDoor: List["PublishedFrontDoorOption"]
    piecePresets: List["PublishedPreset"]
    presets: List["PublishedPreset"]
    shapePresets: List["PublishedShapePreset"]
    type: str


class SpaceTypesSlotsResponse(TypedDict, total=False):
    base: List["EffectiveSlotRole"]
    presets: Dict[str, Any]
    slotKeys: str
    type: str
    unroledPolicy: str


class DocsBlockSchemaResponse(TypedDict, total=False):
    hooks: List["BlockAttrSpec"]
    inline: List["BlockNodeSpec"]
    marks: List["MarkSpec"]
    nodes: List["BlockNodeSpec"]
    root: "BlockNodeSpec"


class SpacesShapePutParamsSpace(TypedDict, total=False):
    index: str
    order: str
    nav: str
    whoCreates: str
    summary: List[str]


class SpacesShapePutParamsSectionsAddItem(TypedDict, total=False):
    key: str
    label: str
    kind: str
    required: bool
    hint: str
    example: str
    schemaProperty: str
    render: str


class SpacesShapePutParamsSections(TypedDict, total=False):
    add: List["SpacesShapePutParamsSectionsAddItem"]
    omit: List[str]
    order: List[str]
    set: Dict[str, Any]


class SpacesShapePutParamsParamsAddItem(TypedDict, total=False):
    key: str
    label: str
    type: str
    options: List[str]
    relationSpaceId: str
    hint: str
    placeholder: str
    internal: bool
    required: bool
    default: Any
    schemaProperty: str


class SpacesShapePutParamsParams(TypedDict, total=False):
    add: List["SpacesShapePutParamsParamsAddItem"]
    omit: List[str]
    order: List[str]
    set: Dict[str, Any]


class SpacesShapePutParams(TypedDict, total=False):
    space: "SpacesShapePutParamsSpace"
    sections: "SpacesShapePutParamsSections"
    params: "SpacesShapePutParamsParams"


class SpacesShapePatchParamsSpace(TypedDict, total=False):
    index: str
    order: str
    nav: str
    whoCreates: str
    summary: List[str]


class SpacesShapePatchParamsSectionsAddItem(TypedDict, total=False):
    key: str
    label: str
    kind: str
    required: bool
    hint: str
    example: str
    schemaProperty: str
    render: str


class SpacesShapePatchParamsSections(TypedDict, total=False):
    add: List["SpacesShapePatchParamsSectionsAddItem"]
    omit: List[str]
    order: List[str]
    set: Dict[str, Any]


class SpacesShapePatchParamsParamsAddItem(TypedDict, total=False):
    key: str
    label: str
    type: str
    options: List[str]
    relationSpaceId: str
    hint: str
    placeholder: str
    internal: bool
    required: bool
    default: Any
    schemaProperty: str


class SpacesShapePatchParamsParams(TypedDict, total=False):
    add: List["SpacesShapePatchParamsParamsAddItem"]
    omit: List[str]
    order: List[str]
    set: Dict[str, Any]


class SpacesShapePatchParams(TypedDict, total=False):
    space: "SpacesShapePatchParamsSpace"
    sections: "SpacesShapePatchParamsSections"
    params: "SpacesShapePatchParamsParams"


class SpacesShapeSetDefaultKindParams(TypedDict, total=False):
    kind: Optional[str]


class SpacesShapeSetKindParamsPatchSpace(TypedDict, total=False):
    index: str
    order: str
    nav: str
    whoCreates: str
    summary: List[str]


class SpacesShapeSetKindParamsPatchSectionsAddItem(TypedDict, total=False):
    key: str
    label: str
    kind: str
    required: bool
    hint: str
    example: str
    schemaProperty: str
    render: str


class SpacesShapeSetKindParamsPatchSections(TypedDict, total=False):
    add: List["SpacesShapeSetKindParamsPatchSectionsAddItem"]
    omit: List[str]
    order: List[str]
    set: Dict[str, Any]


class SpacesShapeSetKindParamsPatchParamsAddItem(TypedDict, total=False):
    key: str
    label: str
    type: str
    options: List[str]
    relationSpaceId: str
    hint: str
    placeholder: str
    internal: bool
    required: bool
    default: Any
    schemaProperty: str


class SpacesShapeSetKindParamsPatchParams(TypedDict, total=False):
    add: List["SpacesShapeSetKindParamsPatchParamsAddItem"]
    omit: List[str]
    order: List[str]
    set: Dict[str, Any]


class SpacesShapeSetKindParamsPatch(TypedDict, total=False):
    space: "SpacesShapeSetKindParamsPatchSpace"
    sections: "SpacesShapeSetKindParamsPatchSections"
    params: "SpacesShapeSetKindParamsPatchParams"


class SpacesShapeSetKindParams(TypedDict, total=False):
    label: str
    description: str
    patch: "SpacesShapeSetKindParamsPatch"


class SpacesHubIntrosGetResponse(TypedDict, total=False):
    doc: Any


class SpacesHubIntrosSetParams(TypedDict, total=False):
    doc: Optional[Any]


class SpacesHubIntrosSetResponse(TypedDict, total=False):
    doc: Any
    warnings: List[str]


class SpacesHubIntrosRenameSeriesParams(TypedDict, total=False):
    name: str


class SpacesHubIntrosRenameSeriesResponse(TypedDict, total=False):
    moved: float
    warnings: List[str]


class OrgsEmailSettingsResponseBranding(TypedDict, total=False):
    footer: str
    hideBranding: bool
    subjectPrefix: str


class OrgsEmailSettingsResponse(TypedDict, total=False):
    branding: "OrgsEmailSettingsResponseBranding"
    emailFrom: Any


class OrgsSetEmailFromParams(TypedDict, total=False):
    emailFrom: Optional[str]


class OrgsSetEmailFromResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class OrgsEmailBrandingResponseBrandingDark(TypedDict, total=False):
    backgroundColor: str
    buttonTextColor: str
    mutedColor: str
    primaryColor: str
    surfaceColor: str
    textColor: str


class OrgsEmailBrandingResponseBrandingFooterLink(TypedDict, total=False):
    label: str
    url: str


class OrgsEmailBrandingResponseBrandingSocialLink(TypedDict, total=False):
    network: str
    url: str


class OrgsEmailBrandingResponseBranding(TypedDict, total=False):
    address: str
    backgroundColor: str
    buttonTextColor: str
    dark: "OrgsEmailBrandingResponseBrandingDark"
    darkMode: bool
    displayName: str
    fontFamily: str
    footer: str
    footerLinks: List["OrgsEmailBrandingResponseBrandingFooterLink"]
    hideBranding: bool
    logoAlt: str
    logoUrl: str
    logoWidth: float
    mutedColor: str
    primaryColor: str
    socialLinks: List["OrgsEmailBrandingResponseBrandingSocialLink"]
    subjectPrefix: str
    surfaceColor: str
    textColor: str
    webFontName: str
    webFontUrl: str


class OrgsEmailBrandingResponse(TypedDict, total=False):
    branding: "OrgsEmailBrandingResponseBranding"


class OrgsSetEmailBrandingParamsDark(TypedDict, total=False):
    primaryColor: str
    buttonTextColor: str
    backgroundColor: str
    surfaceColor: str
    textColor: str
    mutedColor: str


class OrgsSetEmailBrandingParamsFooterLink(TypedDict, total=False):
    label: str
    url: str


class OrgsSetEmailBrandingParamsSocialLink(TypedDict, total=False):
    network: str
    url: str


class OrgsSetEmailBrandingParams(TypedDict, total=False):
    footer: Optional[str]
    subjectPrefix: Optional[str]
    hideBranding: Any
    logoUrl: Optional[str]
    logoAlt: Optional[str]
    logoWidth: Optional[int]
    displayName: Optional[str]
    primaryColor: Optional[str]
    buttonTextColor: Optional[str]
    backgroundColor: Optional[str]
    surfaceColor: Optional[str]
    textColor: Optional[str]
    mutedColor: Optional[str]
    darkMode: Any
    dark: Optional["OrgsSetEmailBrandingParamsDark"]
    fontFamily: Optional[str]
    webFontName: Optional[str]
    webFontUrl: Optional[str]
    address: Optional[str]
    footerLinks: Optional[List["OrgsSetEmailBrandingParamsFooterLink"]]
    socialLinks: Optional[List["OrgsSetEmailBrandingParamsSocialLink"]]


class OrgsSetEmailBrandingResponseBrandingDark(TypedDict, total=False):
    backgroundColor: str
    buttonTextColor: str
    mutedColor: str
    primaryColor: str
    surfaceColor: str
    textColor: str


class OrgsSetEmailBrandingResponseBrandingFooterLink(TypedDict, total=False):
    label: str
    url: str


class OrgsSetEmailBrandingResponseBrandingSocialLink(TypedDict, total=False):
    network: str
    url: str


class OrgsSetEmailBrandingResponseBranding(TypedDict, total=False):
    address: str
    backgroundColor: str
    buttonTextColor: str
    dark: "OrgsSetEmailBrandingResponseBrandingDark"
    darkMode: bool
    displayName: str
    fontFamily: str
    footer: str
    footerLinks: List["OrgsSetEmailBrandingResponseBrandingFooterLink"]
    hideBranding: bool
    logoAlt: str
    logoUrl: str
    logoWidth: float
    mutedColor: str
    primaryColor: str
    socialLinks: List["OrgsSetEmailBrandingResponseBrandingSocialLink"]
    subjectPrefix: str
    surfaceColor: str
    textColor: str
    webFontName: str
    webFontUrl: str


class OrgsSetEmailBrandingResponse(TypedDict, total=False):
    branding: "OrgsSetEmailBrandingResponseBranding"
    warnings: List[str]


class OrgsGetSiemResponse(TypedDict, total=False):
    configured: bool
    url: Any


class OrgsSetSiemParams(TypedDict, total=False):
    url: Optional[str]
    token: Optional[str]


class OrgsSetSiemResponse(TypedDict, total=False):
    configured: bool
    url: Any
    warnings: List[str]


class OrgsUpsertLegalParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class OrgsUpsertLegalParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class OrgsUpsertLegalParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class OrgsUpsertLegalParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class OrgsUpsertLegalParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class OrgsUpsertLegalParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class OrgsUpsertLegalParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class OrgsUpsertLegalParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class OrgsUpsertLegalParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class OrgsUpsertLegalParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class OrgsUpsertLegalParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class OrgsUpsertLegalParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class OrgsUpsertLegalParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "OrgsUpsertLegalParamsCustomizationThemeComponentsFocus"
    code: "OrgsUpsertLegalParamsCustomizationThemeComponentsCode"
    input: "OrgsUpsertLegalParamsCustomizationThemeComponentsInput"
    button: "OrgsUpsertLegalParamsCustomizationThemeComponentsButton"
    spacing: "OrgsUpsertLegalParamsCustomizationThemeComponentsSpacing"
    selection: "OrgsUpsertLegalParamsCustomizationThemeComponentsSelection"
    scrollbar: "OrgsUpsertLegalParamsCustomizationThemeComponentsScrollbar"
    syntax: "OrgsUpsertLegalParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "OrgsUpsertLegalParamsCustomizationThemeComponentsSyntaxDark"


class OrgsUpsertLegalParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class OrgsUpsertLegalParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class OrgsUpsertLegalParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class OrgsUpsertLegalParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class OrgsUpsertLegalParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class OrgsUpsertLegalParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["OrgsUpsertLegalParamsCustomizationThemeMotionKeyframeStep"]


class OrgsUpsertLegalParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "OrgsUpsertLegalParamsCustomizationThemeMotionReveal"
    hover: "OrgsUpsertLegalParamsCustomizationThemeMotionHover"
    header: "OrgsUpsertLegalParamsCustomizationThemeMotionHeader"
    ambient: "OrgsUpsertLegalParamsCustomizationThemeMotionAmbient"
    keyframes: List["OrgsUpsertLegalParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class OrgsUpsertLegalParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "OrgsUpsertLegalParamsCustomizationThemePalette"
    paletteDark: "OrgsUpsertLegalParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "OrgsUpsertLegalParamsCustomizationThemeLayout"
    components: "OrgsUpsertLegalParamsCustomizationThemeComponents"
    motion: "OrgsUpsertLegalParamsCustomizationThemeMotion"


class OrgsUpsertLegalParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["OrgsUpsertLegalParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class OrgsUpsertLegalParams(TypedDict, total=False):
    kind: str
    title: str
    body: str
    required: bool
    onThisPage: Optional[str]
    customization: Optional["OrgsUpsertLegalParamsCustomization"]


class OrgsUpsertLegalResponse(TypedDict, total=False):
    document: "LegalDocView"
    warnings: List[str]


class OrgsLegalEmbedAcceptancesResponseAcceptance(TypedDict, total=False):
    acceptedAt: str
    ip: Any
    source: str
    subject: str
    userAgent: Any
    verification: str
    version: float


class OrgsLegalEmbedAcceptancesResponseAmendment(TypedDict, total=False):
    amendedAt: str
    declaredBy: Any
    declaredByName: str
    note: Any
    version: float


class OrgsLegalEmbedAcceptancesResponse(TypedDict, total=False):
    acceptances: List["OrgsLegalEmbedAcceptancesResponseAcceptance"]
    amendments: List["OrgsLegalEmbedAcceptancesResponseAmendment"]
    currentVersion: float
    subjectVerification: str


class OrgsLegalAcceptanceGateResponse(TypedDict, total=False):
    requireSignedSubject: bool


class OrgsSetLegalAcceptanceGateParams(TypedDict, total=False):
    sharedSecret: Optional[str]


class OrgsSetLegalAcceptanceGateResponse(TypedDict, total=False):
    requireSignedSubject: bool
    warnings: List[str]


class OrgsLegalEditionDiffResponse(TypedDict, total=False):
    diff: Any
    fromVersion: float
    toAmendedAt: Any
    toVersion: float


class OrgsBindLegalPageParams(TypedDict, total=False):
    kind: str
    pageId: str
    required: bool


class OrgsBindLegalPageResponse(TypedDict, total=False):
    document: "LegalDocView"
    warnings: List[str]


class OrgsUnbindLegalResponse(TypedDict, total=False):
    ok: bool


class OrgsSuggestedLegalResponseSuggestedItem(TypedDict, total=False):
    kind: str
    title: str


class OrgsSuggestedLegalResponse(TypedDict, total=False):
    suggested: List["OrgsSuggestedLegalResponseSuggestedItem"]
    page: "PageInfo"


class OrgsReorderLegalParams(TypedDict, total=False):
    kinds: List[str]


class OrgsReorderLegalResponse(TypedDict, total=False):
    documents: List["LegalDocView"]
    warnings: List[str]


class OrgsPlanResponse(TypedDict, total=False):
    metrics: List["QuotaStatus"]
    plan: str


class OrgsSetPlanParams(TypedDict, total=False):
    plan: str


class OrgsSetPlanResponse(TypedDict, total=False):
    metrics: List["QuotaStatus"]
    plan: str
    warnings: List[str]


class OrgsSetOverrideParams(TypedDict, total=False):
    metric: str
    extra: Optional[int]


class OrgsSetOverrideResponse(TypedDict, total=False):
    metrics: List["QuotaStatus"]
    plan: str
    warnings: List[str]


class OrgsImportParamsSpaceCollection(TypedDict, total=False):
    id: str
    name: str
    slug: str


class OrgsImportParamsSpacePage(TypedDict, total=False):
    id: str
    collectionId: Optional[str]
    title: str
    slug: str
    content: Optional[Any]


class OrgsImportParamsSpaceTopicPost(TypedDict, total=False):
    id: str
    authorId: Optional[str]
    createdAt: str
    isOp: bool
    content: Any


class OrgsImportParamsSpaceTopic(TypedDict, total=False):
    id: str
    title: str
    slug: str
    kind: str
    state: str
    tags: List[str]
    posts: List["OrgsImportParamsSpaceTopicPost"]


class OrgsImportParamsSpace(TypedDict, total=False):
    id: str
    name: str
    slug: str
    type: str
    visibility: str
    settings: Dict[str, Any]
    collections: List["OrgsImportParamsSpaceCollection"]
    pages: List["OrgsImportParamsSpacePage"]
    topics: List["OrgsImportParamsSpaceTopic"]


class OrgsImportParams(TypedDict, total=False):
    format: str
    version: int
    exportedAt: str
    organization: Any
    members: Any
    spaces: List["OrgsImportParamsSpace"]


class OrgsImportResponse(TypedDict, total=False):
    summary: "ImportSummary"
    warnings: List[str]


class OrgsCreateParams(TypedDict, total=False):
    name: str
    slug: str


class OrgsCreateResponse(TypedDict, total=False):
    organization: "OrgSummary"
    data: "OrgSummary"
    warnings: List[str]


class OrgsRenameSlugParams(TypedDict, total=False):
    slug: str


class OrgsRenameSlugResponse(TypedDict, total=False):
    previous: Any
    slug: str
    warnings: List[str]


class OrgsGetResponse(TypedDict, total=False):
    organization: "OrgSummary"


class OrgsUpdateParams(TypedDict, total=False):
    name: str
    inboundEmailDomain: Optional[str]
    contentLanguage: Optional[Any]


class OrgsUpdateResponse(TypedDict, total=False):
    organization: "OrgSummary"
    warnings: List[str]


class OrgsRemoveResponse(TypedDict, total=False):
    ok: bool


class SpacesCreateParamsShape(TypedDict, total=False):
    index: str
    order: str
    nav: str
    whoCreates: str


class SpacesCreateParams(TypedDict, total=False):
    name: str
    slug: str
    type: str
    visibility: str
    seed: bool
    preset: str
    shape: "SpacesCreateParamsShape"


class SpacesMyAccessResponse(TypedDict, total=False):
    canEdit: bool
    canModerate: bool


class SpacesOverviewResponse(TypedDict, total=False):
    overview: List["SpaceOverview"]
    page: "PageInfo"


class SpacesUpdateParams(TypedDict, total=False):
    name: str
    visibility: str
    settings: Dict[str, Any]


class SpacesUpdateResponse(TypedDict, total=False):
    space: "SpaceSummary"
    warnings: List[str]


class SpacesRemoveResponse(TypedDict, total=False):
    ok: bool


class SpacesRenameParams(TypedDict, total=False):
    slug: str


class SpacesRenameResponse(TypedDict, total=False):
    previous: Any
    slug: str
    warnings: List[str]


class SpacesSlugHistoryResponse(TypedDict, total=False):
    slugs: List[str]
    page: "PageInfo"


class SpacesForgetSlugResponse(TypedDict, total=False):
    ok: bool


class SpacesPurgeResponse(TypedDict, total=False):
    ok: bool


class SpacesRestoreResponse(TypedDict, total=False):
    space: "SpaceSummary"


class SpacesDuplicateParams(TypedDict, total=False):
    name: str
    slug: str
    publish: bool


class SpacesDuplicateResponse(TypedDict, total=False):
    space: "SpaceSummary"
    data: "SpaceSummary"
    warnings: List[str]


class SpacesMoveParams(TypedDict, total=False):
    targetOrgId: str
    slug: str


class SpacesMoveResponse(TypedDict, total=False):
    space: "SpaceSummary"
    warnings: List[str]


class SpacesSettingsGetThemeResponseThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class SpacesSettingsGetThemeResponseThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class SpacesSettingsGetThemeResponseThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsGetThemeResponseThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class SpacesSettingsGetThemeResponseThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsGetThemeResponseThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class SpacesSettingsGetThemeResponseThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class SpacesSettingsGetThemeResponseThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class SpacesSettingsGetThemeResponseThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class SpacesSettingsGetThemeResponseThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "SpacesSettingsGetThemeResponseThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["SpacesSettingsGetThemeResponseThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["SpacesSettingsGetThemeResponseThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["SpacesSettingsGetThemeResponseThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "SpacesSettingsGetThemeResponseThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["SpacesSettingsGetThemeResponseThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "SpacesSettingsGetThemeResponseThemeChromeThemeToggle"


class SpacesSettingsGetThemeResponseThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsGetThemeResponseThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class SpacesSettingsGetThemeResponseThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsGetThemeResponseThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class SpacesSettingsGetThemeResponseThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsGetThemeResponseThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class SpacesSettingsGetThemeResponseThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SpacesSettingsGetThemeResponseThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class SpacesSettingsGetThemeResponseThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsGetThemeResponseThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsGetThemeResponseThemeComponents(TypedDict, total=False):
    button: "SpacesSettingsGetThemeResponseThemeComponentsButton"
    code: "SpacesSettingsGetThemeResponseThemeComponentsCode"
    focus: "SpacesSettingsGetThemeResponseThemeComponentsFocus"
    input: "SpacesSettingsGetThemeResponseThemeComponentsInput"
    radius: float
    scrollbar: "SpacesSettingsGetThemeResponseThemeComponentsScrollbar"
    selection: "SpacesSettingsGetThemeResponseThemeComponentsSelection"
    shadow: str
    spacing: "SpacesSettingsGetThemeResponseThemeComponentsSpacing"
    syntax: "SpacesSettingsGetThemeResponseThemeComponentsSyntax"
    syntaxDark: "SpacesSettingsGetThemeResponseThemeComponentsSyntaxDark"


class SpacesSettingsGetThemeResponseThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class SpacesSettingsGetThemeResponseThemeLayout(TypedDict, total=False):
    measure: str


class SpacesSettingsGetThemeResponseThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class SpacesSettingsGetThemeResponseThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class SpacesSettingsGetThemeResponseThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SpacesSettingsGetThemeResponseThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class SpacesSettingsGetThemeResponseThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class SpacesSettingsGetThemeResponseThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


SpacesSettingsGetThemeResponseThemeMotionTargets = TypedDict("SpacesSettingsGetThemeResponseThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class SpacesSettingsGetThemeResponseThemeMotion(TypedDict, total=False):
    ambient: "SpacesSettingsGetThemeResponseThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "SpacesSettingsGetThemeResponseThemeMotionHeader"
    hover: "SpacesSettingsGetThemeResponseThemeMotionHover"
    keyframes: List["SpacesSettingsGetThemeResponseThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "SpacesSettingsGetThemeResponseThemeMotionReveal"
    speed: float
    targets: "SpacesSettingsGetThemeResponseThemeMotionTargets"


class SpacesSettingsGetThemeResponseThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsGetThemeResponseThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["SpacesSettingsGetThemeResponseThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class SpacesSettingsGetThemeResponseThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsGetThemeResponseThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsGetThemeResponseThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class SpacesSettingsGetThemeResponseTheme(TypedDict, total=False):
    accentColor: str
    ads: "SpacesSettingsGetThemeResponseThemeAds"
    announcement: "SpacesSettingsGetThemeResponseThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "SpacesSettingsGetThemeResponseThemeChrome"
    colorScheme: str
    componentInstalls: List["SpacesSettingsGetThemeResponseThemeComponentInstall"]
    components: "SpacesSettingsGetThemeResponseThemeComponents"
    contentWidth: str
    cssSnippets: List["SpacesSettingsGetThemeResponseThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "SpacesSettingsGetThemeResponseThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "SpacesSettingsGetThemeResponseThemeMobile"
    monoFontFamily: str
    motion: "SpacesSettingsGetThemeResponseThemeMotion"
    notFound: "SpacesSettingsGetThemeResponseThemeNotFound"
    onThisPage: str
    palette: "SpacesSettingsGetThemeResponseThemePalette"
    paletteDark: "SpacesSettingsGetThemeResponseThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["SpacesSettingsGetThemeResponseThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class SpacesSettingsGetThemeResponse(TypedDict, total=False):
    theme: "SpacesSettingsGetThemeResponseTheme"
    warnings: List["ThemeWarning"]


class SpacesSettingsSetThemeParamsPalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class SpacesSettingsSetThemeParamsPaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class SpacesSettingsSetThemeParamsLayout(TypedDict, total=False):
    measure: str


class SpacesSettingsSetThemeParamsTypographyFluid(TypedDict, total=False):
    enabled: bool
    minViewport: int
    maxViewport: int
    minScale: float
    bodyMinScale: float


class SpacesSettingsSetThemeParamsTypographyLevelsH1(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeParamsTypographyLevelsH2(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeParamsTypographyLevelsH3(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeParamsTypographyLevelsH4(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeParamsTypographyLevelsH5(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeParamsTypographyLevelsH6(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeParamsTypographyLevelsBody(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeParamsTypographyLevelsSmall(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeParamsTypographyLevelsCode(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeParamsTypographyLevels(TypedDict, total=False):
    h1: "SpacesSettingsSetThemeParamsTypographyLevelsH1"
    h2: "SpacesSettingsSetThemeParamsTypographyLevelsH2"
    h3: "SpacesSettingsSetThemeParamsTypographyLevelsH3"
    h4: "SpacesSettingsSetThemeParamsTypographyLevelsH4"
    h5: "SpacesSettingsSetThemeParamsTypographyLevelsH5"
    h6: "SpacesSettingsSetThemeParamsTypographyLevelsH6"
    body: "SpacesSettingsSetThemeParamsTypographyLevelsBody"
    small: "SpacesSettingsSetThemeParamsTypographyLevelsSmall"
    code: "SpacesSettingsSetThemeParamsTypographyLevelsCode"


class SpacesSettingsSetThemeParamsTypographyVariation(TypedDict, total=False):
    heading: str
    body: str
    code: str


class SpacesSettingsSetThemeParamsTypographyFeatures(TypedDict, total=False):
    heading: str
    body: str
    code: str


class SpacesSettingsSetThemeParamsTypography(TypedDict, total=False):
    scale: str
    baseSize: float
    fluid: "SpacesSettingsSetThemeParamsTypographyFluid"
    levels: "SpacesSettingsSetThemeParamsTypographyLevels"
    headingTransform: str
    variation: "SpacesSettingsSetThemeParamsTypographyVariation"
    features: "SpacesSettingsSetThemeParamsTypographyFeatures"
    opticalSizing: str
    headingWrap: str
    bodyWrap: str


class SpacesSettingsSetThemeParamsFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class SpacesSettingsSetThemeParamsFonts(TypedDict, total=False):
    faces: List["SpacesSettingsSetThemeParamsFontsFace"]


class SpacesSettingsSetThemeParamsAds(TypedDict, total=False):
    network: str
    publisherId: str
    slotId: str
    size: str
    enabled: bool
    scriptUrl: str
    slotHtml: str
    configVar: str
    configJson: Dict[str, Any]


class SpacesSettingsSetThemeParamsElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class SpacesSettingsSetThemeParamsSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class SpacesSettingsSetThemeParamsCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class SpacesSettingsSetThemeParamsAnnouncement(TypedDict, total=False):
    text: str
    level: str
    href: Any


class SpacesSettingsSetThemeParamsChromeCta(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeParamsChromeSecondaryCta(TypedDict, total=False):
    label: str
    href: str
    style: str


class SpacesSettingsSetThemeParamsChromeHeader(TypedDict, total=False):
    overlay: bool
    overlayInk: str
    height: int
    border: str
    borderColor: str
    shadow: str
    blur: int
    opacity: float
    logoHeight: int
    navGap: int
    navWeight: int
    navSize: float
    navCase: str
    navTracking: float


class SpacesSettingsSetThemeParamsChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SpacesSettingsSetThemeParamsChromeHeaderLinkPanelColumnLink(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SpacesSettingsSetThemeParamsChromeHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List["SpacesSettingsSetThemeParamsChromeHeaderLinkPanelColumnLink"]


class SpacesSettingsSetThemeParamsChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class SpacesSettingsSetThemeParamsChromeHeaderLinkPanelFooterLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeParamsChromeHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeParamsChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List["SpacesSettingsSetThemeParamsChromeHeaderLinkPanelFooterLink"]
    cta: "SpacesSettingsSetThemeParamsChromeHeaderLinkPanelFooterCta"


class SpacesSettingsSetThemeParamsChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List["SpacesSettingsSetThemeParamsChromeHeaderLinkPanelColumn"]
    featured: "SpacesSettingsSetThemeParamsChromeHeaderLinkPanelFeatured"
    footer: "SpacesSettingsSetThemeParamsChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class SpacesSettingsSetThemeParamsChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["SpacesSettingsSetThemeParamsChromeHeaderLinkChildrenItem"]
    panel: "SpacesSettingsSetThemeParamsChromeHeaderLinkPanel"
    style: str
    highlight: bool


class SpacesSettingsSetThemeParamsChromeNavMenu(TypedDict, total=False):
    trigger: str
    openDelay: int
    closeDelay: int
    animation: str
    radius: float
    shadow: str
    background: str
    ink: str
    border: str
    width: int


class SpacesSettingsSetThemeParamsChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeParamsChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeParamsChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SpacesSettingsSetThemeParamsChromeFooterColumnLink"]


class SpacesSettingsSetThemeParamsChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class SpacesSettingsSetThemeParamsChromeFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class SpacesSettingsSetThemeParamsChromeFooter(TypedDict, total=False):
    logo: Any
    logoMark: Any
    cookieLinkPlacement: str
    html: str
    css: str
    htmlPlacement: str
    newsletter: "SpacesSettingsSetThemeParamsChromeFooterNewsletter"


class SpacesSettingsSetThemeParamsChromeThemeToggle(TypedDict, total=False):
    show: bool
    style: str
    position: str
    radius: float
    activeColor: str


class SpacesSettingsSetThemeParamsChrome(TypedDict, total=False):
    cta: "SpacesSettingsSetThemeParamsChromeCta"
    secondaryCta: "SpacesSettingsSetThemeParamsChromeSecondaryCta"
    header: "SpacesSettingsSetThemeParamsChromeHeader"
    headerLinks: List["SpacesSettingsSetThemeParamsChromeHeaderLink"]
    navMenu: "SpacesSettingsSetThemeParamsChromeNavMenu"
    footerLinks: List["SpacesSettingsSetThemeParamsChromeFooterLink"]
    footerDescription: str
    footerColumns: List["SpacesSettingsSetThemeParamsChromeFooterColumn"]
    socialLinks: List["SpacesSettingsSetThemeParamsChromeSocialLink"]
    copyright: str
    footer: "SpacesSettingsSetThemeParamsChromeFooter"
    mobileNav: str
    sticky: bool
    height: str
    align: str
    ctaStyle: str
    showSignIn: bool
    themeToggle: "SpacesSettingsSetThemeParamsChromeThemeToggle"
    sidebarBrand: str


class SpacesSettingsSetThemeParamsNotFoundLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeParamsNotFound(TypedDict, total=False):
    title: str
    body: str
    pageId: str
    pageSpaceId: str
    hidePage: bool
    links: List["SpacesSettingsSetThemeParamsNotFoundLink"]
    showSearch: bool
    showSections: bool
    hideSearch: bool


class SpacesSettingsSetThemeParamsComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class SpacesSettingsSetThemeParamsComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class SpacesSettingsSetThemeParamsComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class SpacesSettingsSetThemeParamsComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class SpacesSettingsSetThemeParamsComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class SpacesSettingsSetThemeParamsComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SpacesSettingsSetThemeParamsComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class SpacesSettingsSetThemeParamsComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class SpacesSettingsSetThemeParamsComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class SpacesSettingsSetThemeParamsComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "SpacesSettingsSetThemeParamsComponentsFocus"
    code: "SpacesSettingsSetThemeParamsComponentsCode"
    input: "SpacesSettingsSetThemeParamsComponentsInput"
    button: "SpacesSettingsSetThemeParamsComponentsButton"
    spacing: "SpacesSettingsSetThemeParamsComponentsSpacing"
    selection: "SpacesSettingsSetThemeParamsComponentsSelection"
    scrollbar: "SpacesSettingsSetThemeParamsComponentsScrollbar"
    syntax: "SpacesSettingsSetThemeParamsComponentsSyntax"
    syntaxDark: "SpacesSettingsSetThemeParamsComponentsSyntaxDark"


class SpacesSettingsSetThemeParamsMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class SpacesSettingsSetThemeParamsMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class SpacesSettingsSetThemeParamsMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SpacesSettingsSetThemeParamsMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class SpacesSettingsSetThemeParamsMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class SpacesSettingsSetThemeParamsMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["SpacesSettingsSetThemeParamsMotionKeyframeStep"]


class SpacesSettingsSetThemeParamsMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "SpacesSettingsSetThemeParamsMotionReveal"
    hover: "SpacesSettingsSetThemeParamsMotionHover"
    header: "SpacesSettingsSetThemeParamsMotionHeader"
    ambient: "SpacesSettingsSetThemeParamsMotionAmbient"
    keyframes: List["SpacesSettingsSetThemeParamsMotionKeyframe"]
    targets: Dict[str, Any]


class SpacesSettingsSetThemeParamsComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsSetThemeParamsMobile(TypedDict, total=False):
    fontScale: float
    density: str
    logoUrl: Any
    hide: List[str]
    css: str


class SpacesSettingsSetThemeParams(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "SpacesSettingsSetThemeParamsPalette"
    paletteDark: "SpacesSettingsSetThemeParamsPaletteDark"
    font: str
    colorScheme: str
    contentWidth: str
    onThisPage: str
    layout: "SpacesSettingsSetThemeParamsLayout"
    customFontUrl: Any
    customFontFamily: str
    brandName: Any
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    typography: "SpacesSettingsSetThemeParamsTypography"
    fonts: "SpacesSettingsSetThemeParamsFonts"
    logoUrl: Any
    logoMark: Any
    faviconUrl: Any
    customCss: str
    customJs: str
    scriptOrigins: List[str]
    ads: "SpacesSettingsSetThemeParamsAds"
    whiteLabel: bool
    showLanguageSwitcher: bool
    apiOrigins: List[str]
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    imgOrigins: List[str]
    mediaOrigins: List[str]
    frameOrigins: List[str]
    elementStyles: List["SpacesSettingsSetThemeParamsElementStyle"]
    settingsSchema: List["SpacesSettingsSetThemeParamsSettingsSchemaItem"]
    settings: Dict[str, Any]
    stringOverrides: Dict[str, Any]
    cssSnippets: List["SpacesSettingsSetThemeParamsCssSnippet"]
    announcement: "SpacesSettingsSetThemeParamsAnnouncement"
    chrome: "SpacesSettingsSetThemeParamsChrome"
    notFound: "SpacesSettingsSetThemeParamsNotFound"
    components: "SpacesSettingsSetThemeParamsComponents"
    motion: "SpacesSettingsSetThemeParamsMotion"
    componentInstalls: List["SpacesSettingsSetThemeParamsComponentInstall"]
    mobile: "SpacesSettingsSetThemeParamsMobile"


class SpacesSettingsSetThemeResponseThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class SpacesSettingsSetThemeResponseThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class SpacesSettingsSetThemeResponseThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsSetThemeResponseThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class SpacesSettingsSetThemeResponseThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsSetThemeResponseThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class SpacesSettingsSetThemeResponseThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class SpacesSettingsSetThemeResponseThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class SpacesSettingsSetThemeResponseThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class SpacesSettingsSetThemeResponseThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "SpacesSettingsSetThemeResponseThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["SpacesSettingsSetThemeResponseThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["SpacesSettingsSetThemeResponseThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["SpacesSettingsSetThemeResponseThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "SpacesSettingsSetThemeResponseThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["SpacesSettingsSetThemeResponseThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "SpacesSettingsSetThemeResponseThemeChromeThemeToggle"


class SpacesSettingsSetThemeResponseThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsSetThemeResponseThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class SpacesSettingsSetThemeResponseThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsSetThemeResponseThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class SpacesSettingsSetThemeResponseThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsSetThemeResponseThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class SpacesSettingsSetThemeResponseThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SpacesSettingsSetThemeResponseThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class SpacesSettingsSetThemeResponseThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsSetThemeResponseThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsSetThemeResponseThemeComponents(TypedDict, total=False):
    button: "SpacesSettingsSetThemeResponseThemeComponentsButton"
    code: "SpacesSettingsSetThemeResponseThemeComponentsCode"
    focus: "SpacesSettingsSetThemeResponseThemeComponentsFocus"
    input: "SpacesSettingsSetThemeResponseThemeComponentsInput"
    radius: float
    scrollbar: "SpacesSettingsSetThemeResponseThemeComponentsScrollbar"
    selection: "SpacesSettingsSetThemeResponseThemeComponentsSelection"
    shadow: str
    spacing: "SpacesSettingsSetThemeResponseThemeComponentsSpacing"
    syntax: "SpacesSettingsSetThemeResponseThemeComponentsSyntax"
    syntaxDark: "SpacesSettingsSetThemeResponseThemeComponentsSyntaxDark"


class SpacesSettingsSetThemeResponseThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class SpacesSettingsSetThemeResponseThemeLayout(TypedDict, total=False):
    measure: str


class SpacesSettingsSetThemeResponseThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class SpacesSettingsSetThemeResponseThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class SpacesSettingsSetThemeResponseThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SpacesSettingsSetThemeResponseThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class SpacesSettingsSetThemeResponseThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class SpacesSettingsSetThemeResponseThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


SpacesSettingsSetThemeResponseThemeMotionTargets = TypedDict("SpacesSettingsSetThemeResponseThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class SpacesSettingsSetThemeResponseThemeMotion(TypedDict, total=False):
    ambient: "SpacesSettingsSetThemeResponseThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "SpacesSettingsSetThemeResponseThemeMotionHeader"
    hover: "SpacesSettingsSetThemeResponseThemeMotionHover"
    keyframes: List["SpacesSettingsSetThemeResponseThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "SpacesSettingsSetThemeResponseThemeMotionReveal"
    speed: float
    targets: "SpacesSettingsSetThemeResponseThemeMotionTargets"


class SpacesSettingsSetThemeResponseThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsSetThemeResponseThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["SpacesSettingsSetThemeResponseThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class SpacesSettingsSetThemeResponseThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsSetThemeResponseThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsSetThemeResponseThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class SpacesSettingsSetThemeResponseTheme(TypedDict, total=False):
    accentColor: str
    ads: "SpacesSettingsSetThemeResponseThemeAds"
    announcement: "SpacesSettingsSetThemeResponseThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "SpacesSettingsSetThemeResponseThemeChrome"
    colorScheme: str
    componentInstalls: List["SpacesSettingsSetThemeResponseThemeComponentInstall"]
    components: "SpacesSettingsSetThemeResponseThemeComponents"
    contentWidth: str
    cssSnippets: List["SpacesSettingsSetThemeResponseThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "SpacesSettingsSetThemeResponseThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "SpacesSettingsSetThemeResponseThemeMobile"
    monoFontFamily: str
    motion: "SpacesSettingsSetThemeResponseThemeMotion"
    notFound: "SpacesSettingsSetThemeResponseThemeNotFound"
    onThisPage: str
    palette: "SpacesSettingsSetThemeResponseThemePalette"
    paletteDark: "SpacesSettingsSetThemeResponseThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["SpacesSettingsSetThemeResponseThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class SpacesSettingsSetThemeResponse(TypedDict, total=False):
    theme: "SpacesSettingsSetThemeResponseTheme"
    warnings: List["ThemeWarning"]


class SpacesSettingsPatchThemeParamsPalette(TypedDict, total=False):
    primary: Optional[str]
    secondary: Optional[str]
    tertiary: Optional[str]
    quaternary: Optional[str]
    header_background: Optional[str]
    header_primary: Optional[str]
    highlight: Optional[str]
    danger: Optional[str]
    success: Optional[str]
    love: Optional[str]
    background: Optional[str]
    surface: Optional[str]


class SpacesSettingsPatchThemeParamsPaletteDark(TypedDict, total=False):
    primary: Optional[str]
    secondary: Optional[str]
    tertiary: Optional[str]
    quaternary: Optional[str]
    header_background: Optional[str]
    header_primary: Optional[str]
    highlight: Optional[str]
    danger: Optional[str]
    success: Optional[str]
    love: Optional[str]
    background: Optional[str]
    surface: Optional[str]


class SpacesSettingsPatchThemeParamsLayout(TypedDict, total=False):
    measure: Optional[str]


class SpacesSettingsPatchThemeParamsTypographyFluid(TypedDict, total=False):
    enabled: Optional[bool]
    minViewport: Optional[int]
    maxViewport: Optional[int]
    minScale: Optional[float]
    bodyMinScale: Optional[float]


class SpacesSettingsPatchThemeParamsTypographyLevelsH1(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeParamsTypographyLevelsH2(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeParamsTypographyLevelsH3(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeParamsTypographyLevelsH4(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeParamsTypographyLevelsH5(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeParamsTypographyLevelsH6(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeParamsTypographyLevelsBody(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeParamsTypographyLevelsSmall(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeParamsTypographyLevelsCode(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeParamsTypographyLevels(TypedDict, total=False):
    h1: Optional["SpacesSettingsPatchThemeParamsTypographyLevelsH1"]
    h2: Optional["SpacesSettingsPatchThemeParamsTypographyLevelsH2"]
    h3: Optional["SpacesSettingsPatchThemeParamsTypographyLevelsH3"]
    h4: Optional["SpacesSettingsPatchThemeParamsTypographyLevelsH4"]
    h5: Optional["SpacesSettingsPatchThemeParamsTypographyLevelsH5"]
    h6: Optional["SpacesSettingsPatchThemeParamsTypographyLevelsH6"]
    body: Optional["SpacesSettingsPatchThemeParamsTypographyLevelsBody"]
    small: Optional["SpacesSettingsPatchThemeParamsTypographyLevelsSmall"]
    code: Optional["SpacesSettingsPatchThemeParamsTypographyLevelsCode"]


class SpacesSettingsPatchThemeParamsTypographyVariation(TypedDict, total=False):
    heading: Optional[str]
    body: Optional[str]
    code: Optional[str]


class SpacesSettingsPatchThemeParamsTypographyFeatures(TypedDict, total=False):
    heading: Optional[str]
    body: Optional[str]
    code: Optional[str]


class SpacesSettingsPatchThemeParamsTypography(TypedDict, total=False):
    scale: Optional[str]
    baseSize: Optional[float]
    fluid: Optional["SpacesSettingsPatchThemeParamsTypographyFluid"]
    levels: Optional["SpacesSettingsPatchThemeParamsTypographyLevels"]
    headingTransform: Optional[str]
    variation: Optional["SpacesSettingsPatchThemeParamsTypographyVariation"]
    features: Optional["SpacesSettingsPatchThemeParamsTypographyFeatures"]
    opticalSizing: Optional[str]
    headingWrap: Optional[str]
    bodyWrap: Optional[str]


class SpacesSettingsPatchThemeParamsFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class SpacesSettingsPatchThemeParamsFonts(TypedDict, total=False):
    faces: Optional[List["SpacesSettingsPatchThemeParamsFontsFace"]]


class SpacesSettingsPatchThemeParamsAds(TypedDict, total=False):
    network: str
    publisherId: str
    slotId: str
    size: str
    enabled: bool
    scriptUrl: str
    slotHtml: str
    configVar: str
    configJson: Dict[str, Any]


class SpacesSettingsPatchThemeParamsElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class SpacesSettingsPatchThemeParamsSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class SpacesSettingsPatchThemeParamsCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class SpacesSettingsPatchThemeParamsAnnouncement(TypedDict, total=False):
    text: Optional[str]
    level: Optional[str]
    href: Optional[Any]


class SpacesSettingsPatchThemeParamsChromeCta(TypedDict, total=False):
    label: Optional[str]
    href: Optional[str]


class SpacesSettingsPatchThemeParamsChromeSecondaryCta(TypedDict, total=False):
    label: Optional[str]
    href: Optional[str]
    style: Optional[str]


class SpacesSettingsPatchThemeParamsChromeHeader(TypedDict, total=False):
    overlay: Optional[bool]
    overlayInk: Optional[str]
    height: Optional[int]
    border: Optional[str]
    borderColor: Optional[str]
    shadow: Optional[str]
    blur: Optional[int]
    opacity: Optional[float]
    logoHeight: Optional[int]
    navGap: Optional[int]
    navWeight: Optional[int]
    navSize: Optional[float]
    navCase: Optional[str]
    navTracking: Optional[float]


class SpacesSettingsPatchThemeParamsChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelColumnLink(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List["SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelColumnLink"]


class SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelFooterLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List["SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelFooterLink"]
    cta: "SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelFooterCta"


class SpacesSettingsPatchThemeParamsChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List["SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelColumn"]
    featured: "SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelFeatured"
    footer: "SpacesSettingsPatchThemeParamsChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class SpacesSettingsPatchThemeParamsChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["SpacesSettingsPatchThemeParamsChromeHeaderLinkChildrenItem"]
    panel: "SpacesSettingsPatchThemeParamsChromeHeaderLinkPanel"
    style: str
    highlight: bool


class SpacesSettingsPatchThemeParamsChromeNavMenu(TypedDict, total=False):
    trigger: Optional[str]
    openDelay: Optional[int]
    closeDelay: Optional[int]
    animation: Optional[str]
    radius: Optional[float]
    shadow: Optional[str]
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    width: Optional[int]


class SpacesSettingsPatchThemeParamsChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeParamsChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeParamsChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SpacesSettingsPatchThemeParamsChromeFooterColumnLink"]


class SpacesSettingsPatchThemeParamsChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class SpacesSettingsPatchThemeParamsChromeFooterNewsletter(TypedDict, total=False):
    formId: Optional[str]
    heading: Optional[str]


class SpacesSettingsPatchThemeParamsChromeFooter(TypedDict, total=False):
    logo: Optional[Any]
    logoMark: Optional[Any]
    cookieLinkPlacement: Optional[str]
    html: Optional[str]
    css: Optional[str]
    htmlPlacement: Optional[str]
    newsletter: Optional["SpacesSettingsPatchThemeParamsChromeFooterNewsletter"]


class SpacesSettingsPatchThemeParamsChromeThemeToggle(TypedDict, total=False):
    show: Optional[bool]
    style: Optional[str]
    position: Optional[str]
    radius: Optional[float]
    activeColor: Optional[str]


class SpacesSettingsPatchThemeParamsChrome(TypedDict, total=False):
    cta: Optional["SpacesSettingsPatchThemeParamsChromeCta"]
    secondaryCta: Optional["SpacesSettingsPatchThemeParamsChromeSecondaryCta"]
    header: Optional["SpacesSettingsPatchThemeParamsChromeHeader"]
    headerLinks: Optional[List["SpacesSettingsPatchThemeParamsChromeHeaderLink"]]
    navMenu: Optional["SpacesSettingsPatchThemeParamsChromeNavMenu"]
    footerLinks: Optional[List["SpacesSettingsPatchThemeParamsChromeFooterLink"]]
    footerDescription: Optional[str]
    footerColumns: Optional[List["SpacesSettingsPatchThemeParamsChromeFooterColumn"]]
    socialLinks: Optional[List["SpacesSettingsPatchThemeParamsChromeSocialLink"]]
    copyright: Optional[str]
    footer: Optional["SpacesSettingsPatchThemeParamsChromeFooter"]
    mobileNav: Optional[str]
    sticky: Optional[bool]
    height: Optional[str]
    align: Optional[str]
    ctaStyle: Optional[str]
    showSignIn: Optional[bool]
    themeToggle: Optional["SpacesSettingsPatchThemeParamsChromeThemeToggle"]
    sidebarBrand: Optional[str]


class SpacesSettingsPatchThemeParamsNotFoundLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeParamsNotFound(TypedDict, total=False):
    title: Optional[str]
    body: Optional[str]
    pageId: Optional[str]
    pageSpaceId: Optional[str]
    hidePage: Optional[bool]
    links: Optional[List["SpacesSettingsPatchThemeParamsNotFoundLink"]]
    showSearch: Optional[bool]
    showSections: Optional[bool]
    hideSearch: Optional[bool]


class SpacesSettingsPatchThemeParamsComponentsFocus(TypedDict, total=False):
    color: Optional[str]
    width: Optional[float]
    offset: Optional[float]


class SpacesSettingsPatchThemeParamsComponentsCode(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    radius: Optional[float]


class SpacesSettingsPatchThemeParamsComponentsInput(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    radius: Optional[float]


class SpacesSettingsPatchThemeParamsComponentsButton(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    radius: Optional[float]
    shadow: Optional[str]
    weight: Optional[str]


class SpacesSettingsPatchThemeParamsComponentsSpacing(TypedDict, total=False):
    scale: Optional[float]
    block: Optional[float]
    section: Optional[float]
    pad: Optional[float]


class SpacesSettingsPatchThemeParamsComponentsSelection(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]


class SpacesSettingsPatchThemeParamsComponentsScrollbar(TypedDict, total=False):
    width: Optional[str]
    thumb: Optional[str]
    track: Optional[str]


class SpacesSettingsPatchThemeParamsComponentsSyntax(TypedDict, total=False):
    comment: Optional[str]
    keyword: Optional[str]
    string: Optional[str]
    number: Optional[str]
    title: Optional[str]
    built_in: Optional[str]
    tag: Optional[str]
    attr: Optional[str]
    meta: Optional[str]
    emphasis: Optional[str]


class SpacesSettingsPatchThemeParamsComponentsSyntaxDark(TypedDict, total=False):
    comment: Optional[str]
    keyword: Optional[str]
    string: Optional[str]
    number: Optional[str]
    title: Optional[str]
    built_in: Optional[str]
    tag: Optional[str]
    attr: Optional[str]
    meta: Optional[str]
    emphasis: Optional[str]


class SpacesSettingsPatchThemeParamsComponents(TypedDict, total=False):
    radius: Optional[float]
    shadow: Optional[str]
    focus: Optional["SpacesSettingsPatchThemeParamsComponentsFocus"]
    code: Optional["SpacesSettingsPatchThemeParamsComponentsCode"]
    input: Optional["SpacesSettingsPatchThemeParamsComponentsInput"]
    button: Optional["SpacesSettingsPatchThemeParamsComponentsButton"]
    spacing: Optional["SpacesSettingsPatchThemeParamsComponentsSpacing"]
    selection: Optional["SpacesSettingsPatchThemeParamsComponentsSelection"]
    scrollbar: Optional["SpacesSettingsPatchThemeParamsComponentsScrollbar"]
    syntax: Optional["SpacesSettingsPatchThemeParamsComponentsSyntax"]
    syntaxDark: Optional["SpacesSettingsPatchThemeParamsComponentsSyntaxDark"]


class SpacesSettingsPatchThemeParamsMotionReveal(TypedDict, total=False):
    effect: Optional[str]
    stagger: Optional[int]
    distance: Optional[int]
    once: Optional[bool]
    targets: Optional[List[str]]


class SpacesSettingsPatchThemeParamsMotionHover(TypedDict, total=False):
    link: Optional[str]
    button: Optional[str]
    card: Optional[str]
    image: Optional[str]


class SpacesSettingsPatchThemeParamsMotionHeader(TypedDict, total=False):
    behavior: Optional[str]
    blur: Optional[bool]


class SpacesSettingsPatchThemeParamsMotionAmbient(TypedDict, total=False):
    background: Optional[str]
    cursorGlow: Optional[bool]
    scrollProgress: Optional[bool]
    smoothScroll: Optional[bool]
    focusRing: Optional[bool]


class SpacesSettingsPatchThemeParamsMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class SpacesSettingsPatchThemeParamsMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["SpacesSettingsPatchThemeParamsMotionKeyframeStep"]


class SpacesSettingsPatchThemeParamsMotion(TypedDict, total=False):
    preset: Optional[str]
    enabled: Optional[bool]
    respectReducedMotion: Optional[bool]
    speed: Optional[float]
    easing: Optional[str]
    pageTransition: Optional[str]
    reveal: Optional["SpacesSettingsPatchThemeParamsMotionReveal"]
    hover: Optional["SpacesSettingsPatchThemeParamsMotionHover"]
    header: Optional["SpacesSettingsPatchThemeParamsMotionHeader"]
    ambient: Optional["SpacesSettingsPatchThemeParamsMotionAmbient"]
    keyframes: Optional[List["SpacesSettingsPatchThemeParamsMotionKeyframe"]]
    targets: Optional[Dict[str, Any]]


class SpacesSettingsPatchThemeParamsComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsPatchThemeParamsMobile(TypedDict, total=False):
    fontScale: Optional[float]
    density: Optional[str]
    logoUrl: Optional[Any]
    hide: Optional[List[str]]
    css: Optional[str]


class SpacesSettingsPatchThemeParams(TypedDict, total=False):
    primaryColor: Optional[str]
    accentColor: Optional[str]
    palette: Optional["SpacesSettingsPatchThemeParamsPalette"]
    paletteDark: Optional["SpacesSettingsPatchThemeParamsPaletteDark"]
    font: Optional[str]
    colorScheme: Optional[str]
    contentWidth: Optional[str]
    onThisPage: Optional[str]
    layout: Optional["SpacesSettingsPatchThemeParamsLayout"]
    customFontUrl: Optional[Any]
    customFontFamily: Optional[str]
    brandName: Optional[Any]
    headingFontFamily: Optional[str]
    bodyFontFamily: Optional[str]
    monoFontFamily: Optional[str]
    typography: Optional["SpacesSettingsPatchThemeParamsTypography"]
    fonts: Optional["SpacesSettingsPatchThemeParamsFonts"]
    logoUrl: Optional[Any]
    logoMark: Optional[Any]
    faviconUrl: Optional[Any]
    customCss: Optional[str]
    customJs: Optional[str]
    scriptOrigins: Optional[List[str]]
    ads: Optional["SpacesSettingsPatchThemeParamsAds"]
    whiteLabel: Optional[bool]
    showLanguageSwitcher: Optional[bool]
    apiOrigins: Optional[List[str]]
    fontOrigins: Optional[List[str]]
    fontOriginsRemoved: Optional[List[str]]
    imgOrigins: Optional[List[str]]
    mediaOrigins: Optional[List[str]]
    frameOrigins: Optional[List[str]]
    elementStyles: Optional[List["SpacesSettingsPatchThemeParamsElementStyle"]]
    settingsSchema: Optional[List["SpacesSettingsPatchThemeParamsSettingsSchemaItem"]]
    settings: Optional[Dict[str, Any]]
    stringOverrides: Optional[Dict[str, Any]]
    cssSnippets: Optional[List["SpacesSettingsPatchThemeParamsCssSnippet"]]
    announcement: Optional["SpacesSettingsPatchThemeParamsAnnouncement"]
    chrome: Optional["SpacesSettingsPatchThemeParamsChrome"]
    notFound: Optional["SpacesSettingsPatchThemeParamsNotFound"]
    components: Optional["SpacesSettingsPatchThemeParamsComponents"]
    motion: Optional["SpacesSettingsPatchThemeParamsMotion"]
    componentInstalls: Optional[List["SpacesSettingsPatchThemeParamsComponentInstall"]]
    mobile: Optional["SpacesSettingsPatchThemeParamsMobile"]


class SpacesSettingsPatchThemeResponseThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class SpacesSettingsPatchThemeResponseThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class SpacesSettingsPatchThemeResponseThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsPatchThemeResponseThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class SpacesSettingsPatchThemeResponseThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsPatchThemeResponseThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class SpacesSettingsPatchThemeResponseThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class SpacesSettingsPatchThemeResponseThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class SpacesSettingsPatchThemeResponseThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class SpacesSettingsPatchThemeResponseThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "SpacesSettingsPatchThemeResponseThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["SpacesSettingsPatchThemeResponseThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["SpacesSettingsPatchThemeResponseThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["SpacesSettingsPatchThemeResponseThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "SpacesSettingsPatchThemeResponseThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["SpacesSettingsPatchThemeResponseThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "SpacesSettingsPatchThemeResponseThemeChromeThemeToggle"


class SpacesSettingsPatchThemeResponseThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsPatchThemeResponseThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class SpacesSettingsPatchThemeResponseThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsPatchThemeResponseThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class SpacesSettingsPatchThemeResponseThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsPatchThemeResponseThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class SpacesSettingsPatchThemeResponseThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SpacesSettingsPatchThemeResponseThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class SpacesSettingsPatchThemeResponseThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsPatchThemeResponseThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsPatchThemeResponseThemeComponents(TypedDict, total=False):
    button: "SpacesSettingsPatchThemeResponseThemeComponentsButton"
    code: "SpacesSettingsPatchThemeResponseThemeComponentsCode"
    focus: "SpacesSettingsPatchThemeResponseThemeComponentsFocus"
    input: "SpacesSettingsPatchThemeResponseThemeComponentsInput"
    radius: float
    scrollbar: "SpacesSettingsPatchThemeResponseThemeComponentsScrollbar"
    selection: "SpacesSettingsPatchThemeResponseThemeComponentsSelection"
    shadow: str
    spacing: "SpacesSettingsPatchThemeResponseThemeComponentsSpacing"
    syntax: "SpacesSettingsPatchThemeResponseThemeComponentsSyntax"
    syntaxDark: "SpacesSettingsPatchThemeResponseThemeComponentsSyntaxDark"


class SpacesSettingsPatchThemeResponseThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class SpacesSettingsPatchThemeResponseThemeLayout(TypedDict, total=False):
    measure: str


class SpacesSettingsPatchThemeResponseThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class SpacesSettingsPatchThemeResponseThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class SpacesSettingsPatchThemeResponseThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SpacesSettingsPatchThemeResponseThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class SpacesSettingsPatchThemeResponseThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class SpacesSettingsPatchThemeResponseThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


SpacesSettingsPatchThemeResponseThemeMotionTargets = TypedDict("SpacesSettingsPatchThemeResponseThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class SpacesSettingsPatchThemeResponseThemeMotion(TypedDict, total=False):
    ambient: "SpacesSettingsPatchThemeResponseThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "SpacesSettingsPatchThemeResponseThemeMotionHeader"
    hover: "SpacesSettingsPatchThemeResponseThemeMotionHover"
    keyframes: List["SpacesSettingsPatchThemeResponseThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "SpacesSettingsPatchThemeResponseThemeMotionReveal"
    speed: float
    targets: "SpacesSettingsPatchThemeResponseThemeMotionTargets"


class SpacesSettingsPatchThemeResponseThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsPatchThemeResponseThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["SpacesSettingsPatchThemeResponseThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class SpacesSettingsPatchThemeResponseThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsPatchThemeResponseThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsPatchThemeResponseThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class SpacesSettingsPatchThemeResponseTheme(TypedDict, total=False):
    accentColor: str
    ads: "SpacesSettingsPatchThemeResponseThemeAds"
    announcement: "SpacesSettingsPatchThemeResponseThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "SpacesSettingsPatchThemeResponseThemeChrome"
    colorScheme: str
    componentInstalls: List["SpacesSettingsPatchThemeResponseThemeComponentInstall"]
    components: "SpacesSettingsPatchThemeResponseThemeComponents"
    contentWidth: str
    cssSnippets: List["SpacesSettingsPatchThemeResponseThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "SpacesSettingsPatchThemeResponseThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "SpacesSettingsPatchThemeResponseThemeMobile"
    monoFontFamily: str
    motion: "SpacesSettingsPatchThemeResponseThemeMotion"
    notFound: "SpacesSettingsPatchThemeResponseThemeNotFound"
    onThisPage: str
    palette: "SpacesSettingsPatchThemeResponseThemePalette"
    paletteDark: "SpacesSettingsPatchThemeResponseThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["SpacesSettingsPatchThemeResponseThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class SpacesSettingsPatchThemeResponse(TypedDict, total=False):
    theme: "SpacesSettingsPatchThemeResponseTheme"
    warnings: List["ThemeWarning"]


class SpacesSettingsSetThemeDraftParamsPalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class SpacesSettingsSetThemeDraftParamsPaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class SpacesSettingsSetThemeDraftParamsLayout(TypedDict, total=False):
    measure: str


class SpacesSettingsSetThemeDraftParamsTypographyFluid(TypedDict, total=False):
    enabled: bool
    minViewport: int
    maxViewport: int
    minScale: float
    bodyMinScale: float


class SpacesSettingsSetThemeDraftParamsTypographyLevelsH1(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeDraftParamsTypographyLevelsH2(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeDraftParamsTypographyLevelsH3(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeDraftParamsTypographyLevelsH4(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeDraftParamsTypographyLevelsH5(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeDraftParamsTypographyLevelsH6(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeDraftParamsTypographyLevelsBody(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeDraftParamsTypographyLevelsSmall(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeDraftParamsTypographyLevelsCode(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetThemeDraftParamsTypographyLevels(TypedDict, total=False):
    h1: "SpacesSettingsSetThemeDraftParamsTypographyLevelsH1"
    h2: "SpacesSettingsSetThemeDraftParamsTypographyLevelsH2"
    h3: "SpacesSettingsSetThemeDraftParamsTypographyLevelsH3"
    h4: "SpacesSettingsSetThemeDraftParamsTypographyLevelsH4"
    h5: "SpacesSettingsSetThemeDraftParamsTypographyLevelsH5"
    h6: "SpacesSettingsSetThemeDraftParamsTypographyLevelsH6"
    body: "SpacesSettingsSetThemeDraftParamsTypographyLevelsBody"
    small: "SpacesSettingsSetThemeDraftParamsTypographyLevelsSmall"
    code: "SpacesSettingsSetThemeDraftParamsTypographyLevelsCode"


class SpacesSettingsSetThemeDraftParamsTypographyVariation(TypedDict, total=False):
    heading: str
    body: str
    code: str


class SpacesSettingsSetThemeDraftParamsTypographyFeatures(TypedDict, total=False):
    heading: str
    body: str
    code: str


class SpacesSettingsSetThemeDraftParamsTypography(TypedDict, total=False):
    scale: str
    baseSize: float
    fluid: "SpacesSettingsSetThemeDraftParamsTypographyFluid"
    levels: "SpacesSettingsSetThemeDraftParamsTypographyLevels"
    headingTransform: str
    variation: "SpacesSettingsSetThemeDraftParamsTypographyVariation"
    features: "SpacesSettingsSetThemeDraftParamsTypographyFeatures"
    opticalSizing: str
    headingWrap: str
    bodyWrap: str


class SpacesSettingsSetThemeDraftParamsFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class SpacesSettingsSetThemeDraftParamsFonts(TypedDict, total=False):
    faces: List["SpacesSettingsSetThemeDraftParamsFontsFace"]


class SpacesSettingsSetThemeDraftParamsAds(TypedDict, total=False):
    network: str
    publisherId: str
    slotId: str
    size: str
    enabled: bool
    scriptUrl: str
    slotHtml: str
    configVar: str
    configJson: Dict[str, Any]


class SpacesSettingsSetThemeDraftParamsElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class SpacesSettingsSetThemeDraftParamsSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class SpacesSettingsSetThemeDraftParamsCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class SpacesSettingsSetThemeDraftParamsAnnouncement(TypedDict, total=False):
    text: str
    level: str
    href: Any


class SpacesSettingsSetThemeDraftParamsChromeCta(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeDraftParamsChromeSecondaryCta(TypedDict, total=False):
    label: str
    href: str
    style: str


class SpacesSettingsSetThemeDraftParamsChromeHeader(TypedDict, total=False):
    overlay: bool
    overlayInk: str
    height: int
    border: str
    borderColor: str
    shadow: str
    blur: int
    opacity: float
    logoHeight: int
    navGap: int
    navWeight: int
    navSize: float
    navCase: str
    navTracking: float


class SpacesSettingsSetThemeDraftParamsChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelColumnLink(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List["SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelColumnLink"]


class SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelFooterLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List["SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelFooterLink"]
    cta: "SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelFooterCta"


class SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List["SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelColumn"]
    featured: "SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelFeatured"
    footer: "SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class SpacesSettingsSetThemeDraftParamsChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["SpacesSettingsSetThemeDraftParamsChromeHeaderLinkChildrenItem"]
    panel: "SpacesSettingsSetThemeDraftParamsChromeHeaderLinkPanel"
    style: str
    highlight: bool


class SpacesSettingsSetThemeDraftParamsChromeNavMenu(TypedDict, total=False):
    trigger: str
    openDelay: int
    closeDelay: int
    animation: str
    radius: float
    shadow: str
    background: str
    ink: str
    border: str
    width: int


class SpacesSettingsSetThemeDraftParamsChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeDraftParamsChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeDraftParamsChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SpacesSettingsSetThemeDraftParamsChromeFooterColumnLink"]


class SpacesSettingsSetThemeDraftParamsChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class SpacesSettingsSetThemeDraftParamsChromeFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class SpacesSettingsSetThemeDraftParamsChromeFooter(TypedDict, total=False):
    logo: Any
    logoMark: Any
    cookieLinkPlacement: str
    html: str
    css: str
    htmlPlacement: str
    newsletter: "SpacesSettingsSetThemeDraftParamsChromeFooterNewsletter"


class SpacesSettingsSetThemeDraftParamsChromeThemeToggle(TypedDict, total=False):
    show: bool
    style: str
    position: str
    radius: float
    activeColor: str


class SpacesSettingsSetThemeDraftParamsChrome(TypedDict, total=False):
    cta: "SpacesSettingsSetThemeDraftParamsChromeCta"
    secondaryCta: "SpacesSettingsSetThemeDraftParamsChromeSecondaryCta"
    header: "SpacesSettingsSetThemeDraftParamsChromeHeader"
    headerLinks: List["SpacesSettingsSetThemeDraftParamsChromeHeaderLink"]
    navMenu: "SpacesSettingsSetThemeDraftParamsChromeNavMenu"
    footerLinks: List["SpacesSettingsSetThemeDraftParamsChromeFooterLink"]
    footerDescription: str
    footerColumns: List["SpacesSettingsSetThemeDraftParamsChromeFooterColumn"]
    socialLinks: List["SpacesSettingsSetThemeDraftParamsChromeSocialLink"]
    copyright: str
    footer: "SpacesSettingsSetThemeDraftParamsChromeFooter"
    mobileNav: str
    sticky: bool
    height: str
    align: str
    ctaStyle: str
    showSignIn: bool
    themeToggle: "SpacesSettingsSetThemeDraftParamsChromeThemeToggle"
    sidebarBrand: str


class SpacesSettingsSetThemeDraftParamsNotFoundLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetThemeDraftParamsNotFound(TypedDict, total=False):
    title: str
    body: str
    pageId: str
    pageSpaceId: str
    hidePage: bool
    links: List["SpacesSettingsSetThemeDraftParamsNotFoundLink"]
    showSearch: bool
    showSections: bool
    hideSearch: bool


class SpacesSettingsSetThemeDraftParamsComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class SpacesSettingsSetThemeDraftParamsComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class SpacesSettingsSetThemeDraftParamsComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class SpacesSettingsSetThemeDraftParamsComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class SpacesSettingsSetThemeDraftParamsComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class SpacesSettingsSetThemeDraftParamsComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SpacesSettingsSetThemeDraftParamsComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class SpacesSettingsSetThemeDraftParamsComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class SpacesSettingsSetThemeDraftParamsComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class SpacesSettingsSetThemeDraftParamsComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "SpacesSettingsSetThemeDraftParamsComponentsFocus"
    code: "SpacesSettingsSetThemeDraftParamsComponentsCode"
    input: "SpacesSettingsSetThemeDraftParamsComponentsInput"
    button: "SpacesSettingsSetThemeDraftParamsComponentsButton"
    spacing: "SpacesSettingsSetThemeDraftParamsComponentsSpacing"
    selection: "SpacesSettingsSetThemeDraftParamsComponentsSelection"
    scrollbar: "SpacesSettingsSetThemeDraftParamsComponentsScrollbar"
    syntax: "SpacesSettingsSetThemeDraftParamsComponentsSyntax"
    syntaxDark: "SpacesSettingsSetThemeDraftParamsComponentsSyntaxDark"


class SpacesSettingsSetThemeDraftParamsMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class SpacesSettingsSetThemeDraftParamsMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class SpacesSettingsSetThemeDraftParamsMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SpacesSettingsSetThemeDraftParamsMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class SpacesSettingsSetThemeDraftParamsMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class SpacesSettingsSetThemeDraftParamsMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["SpacesSettingsSetThemeDraftParamsMotionKeyframeStep"]


class SpacesSettingsSetThemeDraftParamsMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "SpacesSettingsSetThemeDraftParamsMotionReveal"
    hover: "SpacesSettingsSetThemeDraftParamsMotionHover"
    header: "SpacesSettingsSetThemeDraftParamsMotionHeader"
    ambient: "SpacesSettingsSetThemeDraftParamsMotionAmbient"
    keyframes: List["SpacesSettingsSetThemeDraftParamsMotionKeyframe"]
    targets: Dict[str, Any]


class SpacesSettingsSetThemeDraftParamsComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsSetThemeDraftParamsMobile(TypedDict, total=False):
    fontScale: float
    density: str
    logoUrl: Any
    hide: List[str]
    css: str


class SpacesSettingsSetThemeDraftParams(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "SpacesSettingsSetThemeDraftParamsPalette"
    paletteDark: "SpacesSettingsSetThemeDraftParamsPaletteDark"
    font: str
    colorScheme: str
    contentWidth: str
    onThisPage: str
    layout: "SpacesSettingsSetThemeDraftParamsLayout"
    customFontUrl: Any
    customFontFamily: str
    brandName: Any
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    typography: "SpacesSettingsSetThemeDraftParamsTypography"
    fonts: "SpacesSettingsSetThemeDraftParamsFonts"
    logoUrl: Any
    logoMark: Any
    faviconUrl: Any
    customCss: str
    customJs: str
    scriptOrigins: List[str]
    ads: "SpacesSettingsSetThemeDraftParamsAds"
    whiteLabel: bool
    showLanguageSwitcher: bool
    apiOrigins: List[str]
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    imgOrigins: List[str]
    mediaOrigins: List[str]
    frameOrigins: List[str]
    elementStyles: List["SpacesSettingsSetThemeDraftParamsElementStyle"]
    settingsSchema: List["SpacesSettingsSetThemeDraftParamsSettingsSchemaItem"]
    settings: Dict[str, Any]
    stringOverrides: Dict[str, Any]
    cssSnippets: List["SpacesSettingsSetThemeDraftParamsCssSnippet"]
    announcement: "SpacesSettingsSetThemeDraftParamsAnnouncement"
    chrome: "SpacesSettingsSetThemeDraftParamsChrome"
    notFound: "SpacesSettingsSetThemeDraftParamsNotFound"
    components: "SpacesSettingsSetThemeDraftParamsComponents"
    motion: "SpacesSettingsSetThemeDraftParamsMotion"
    componentInstalls: List["SpacesSettingsSetThemeDraftParamsComponentInstall"]
    mobile: "SpacesSettingsSetThemeDraftParamsMobile"


class SpacesSettingsPatchThemeDraftParamsPalette(TypedDict, total=False):
    primary: Optional[str]
    secondary: Optional[str]
    tertiary: Optional[str]
    quaternary: Optional[str]
    header_background: Optional[str]
    header_primary: Optional[str]
    highlight: Optional[str]
    danger: Optional[str]
    success: Optional[str]
    love: Optional[str]
    background: Optional[str]
    surface: Optional[str]


class SpacesSettingsPatchThemeDraftParamsPaletteDark(TypedDict, total=False):
    primary: Optional[str]
    secondary: Optional[str]
    tertiary: Optional[str]
    quaternary: Optional[str]
    header_background: Optional[str]
    header_primary: Optional[str]
    highlight: Optional[str]
    danger: Optional[str]
    success: Optional[str]
    love: Optional[str]
    background: Optional[str]
    surface: Optional[str]


class SpacesSettingsPatchThemeDraftParamsLayout(TypedDict, total=False):
    measure: Optional[str]


class SpacesSettingsPatchThemeDraftParamsTypographyFluid(TypedDict, total=False):
    enabled: Optional[bool]
    minViewport: Optional[int]
    maxViewport: Optional[int]
    minScale: Optional[float]
    bodyMinScale: Optional[float]


class SpacesSettingsPatchThemeDraftParamsTypographyLevelsH1(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeDraftParamsTypographyLevelsH2(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeDraftParamsTypographyLevelsH3(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeDraftParamsTypographyLevelsH4(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeDraftParamsTypographyLevelsH5(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeDraftParamsTypographyLevelsH6(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeDraftParamsTypographyLevelsBody(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeDraftParamsTypographyLevelsSmall(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeDraftParamsTypographyLevelsCode(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SpacesSettingsPatchThemeDraftParamsTypographyLevels(TypedDict, total=False):
    h1: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevelsH1"]
    h2: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevelsH2"]
    h3: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevelsH3"]
    h4: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevelsH4"]
    h5: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevelsH5"]
    h6: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevelsH6"]
    body: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevelsBody"]
    small: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevelsSmall"]
    code: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevelsCode"]


class SpacesSettingsPatchThemeDraftParamsTypographyVariation(TypedDict, total=False):
    heading: Optional[str]
    body: Optional[str]
    code: Optional[str]


class SpacesSettingsPatchThemeDraftParamsTypographyFeatures(TypedDict, total=False):
    heading: Optional[str]
    body: Optional[str]
    code: Optional[str]


class SpacesSettingsPatchThemeDraftParamsTypography(TypedDict, total=False):
    scale: Optional[str]
    baseSize: Optional[float]
    fluid: Optional["SpacesSettingsPatchThemeDraftParamsTypographyFluid"]
    levels: Optional["SpacesSettingsPatchThemeDraftParamsTypographyLevels"]
    headingTransform: Optional[str]
    variation: Optional["SpacesSettingsPatchThemeDraftParamsTypographyVariation"]
    features: Optional["SpacesSettingsPatchThemeDraftParamsTypographyFeatures"]
    opticalSizing: Optional[str]
    headingWrap: Optional[str]
    bodyWrap: Optional[str]


class SpacesSettingsPatchThemeDraftParamsFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class SpacesSettingsPatchThemeDraftParamsFonts(TypedDict, total=False):
    faces: Optional[List["SpacesSettingsPatchThemeDraftParamsFontsFace"]]


class SpacesSettingsPatchThemeDraftParamsAds(TypedDict, total=False):
    network: str
    publisherId: str
    slotId: str
    size: str
    enabled: bool
    scriptUrl: str
    slotHtml: str
    configVar: str
    configJson: Dict[str, Any]


class SpacesSettingsPatchThemeDraftParamsElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class SpacesSettingsPatchThemeDraftParamsSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class SpacesSettingsPatchThemeDraftParamsCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class SpacesSettingsPatchThemeDraftParamsAnnouncement(TypedDict, total=False):
    text: Optional[str]
    level: Optional[str]
    href: Optional[Any]


class SpacesSettingsPatchThemeDraftParamsChromeCta(TypedDict, total=False):
    label: Optional[str]
    href: Optional[str]


class SpacesSettingsPatchThemeDraftParamsChromeSecondaryCta(TypedDict, total=False):
    label: Optional[str]
    href: Optional[str]
    style: Optional[str]


class SpacesSettingsPatchThemeDraftParamsChromeHeader(TypedDict, total=False):
    overlay: Optional[bool]
    overlayInk: Optional[str]
    height: Optional[int]
    border: Optional[str]
    borderColor: Optional[str]
    shadow: Optional[str]
    blur: Optional[int]
    opacity: Optional[float]
    logoHeight: Optional[int]
    navGap: Optional[int]
    navWeight: Optional[int]
    navSize: Optional[float]
    navCase: Optional[str]
    navTracking: Optional[float]


class SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelColumnLink(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List["SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelColumnLink"]


class SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelFooterLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List["SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelFooterLink"]
    cta: "SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelFooterCta"


class SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List["SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelColumn"]
    featured: "SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelFeatured"
    footer: "SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class SpacesSettingsPatchThemeDraftParamsChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkChildrenItem"]
    panel: "SpacesSettingsPatchThemeDraftParamsChromeHeaderLinkPanel"
    style: str
    highlight: bool


class SpacesSettingsPatchThemeDraftParamsChromeNavMenu(TypedDict, total=False):
    trigger: Optional[str]
    openDelay: Optional[int]
    closeDelay: Optional[int]
    animation: Optional[str]
    radius: Optional[float]
    shadow: Optional[str]
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    width: Optional[int]


class SpacesSettingsPatchThemeDraftParamsChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeDraftParamsChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeDraftParamsChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SpacesSettingsPatchThemeDraftParamsChromeFooterColumnLink"]


class SpacesSettingsPatchThemeDraftParamsChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class SpacesSettingsPatchThemeDraftParamsChromeFooterNewsletter(TypedDict, total=False):
    formId: Optional[str]
    heading: Optional[str]


class SpacesSettingsPatchThemeDraftParamsChromeFooter(TypedDict, total=False):
    logo: Optional[Any]
    logoMark: Optional[Any]
    cookieLinkPlacement: Optional[str]
    html: Optional[str]
    css: Optional[str]
    htmlPlacement: Optional[str]
    newsletter: Optional["SpacesSettingsPatchThemeDraftParamsChromeFooterNewsletter"]


class SpacesSettingsPatchThemeDraftParamsChromeThemeToggle(TypedDict, total=False):
    show: Optional[bool]
    style: Optional[str]
    position: Optional[str]
    radius: Optional[float]
    activeColor: Optional[str]


class SpacesSettingsPatchThemeDraftParamsChrome(TypedDict, total=False):
    cta: Optional["SpacesSettingsPatchThemeDraftParamsChromeCta"]
    secondaryCta: Optional["SpacesSettingsPatchThemeDraftParamsChromeSecondaryCta"]
    header: Optional["SpacesSettingsPatchThemeDraftParamsChromeHeader"]
    headerLinks: Optional[List["SpacesSettingsPatchThemeDraftParamsChromeHeaderLink"]]
    navMenu: Optional["SpacesSettingsPatchThemeDraftParamsChromeNavMenu"]
    footerLinks: Optional[List["SpacesSettingsPatchThemeDraftParamsChromeFooterLink"]]
    footerDescription: Optional[str]
    footerColumns: Optional[List["SpacesSettingsPatchThemeDraftParamsChromeFooterColumn"]]
    socialLinks: Optional[List["SpacesSettingsPatchThemeDraftParamsChromeSocialLink"]]
    copyright: Optional[str]
    footer: Optional["SpacesSettingsPatchThemeDraftParamsChromeFooter"]
    mobileNav: Optional[str]
    sticky: Optional[bool]
    height: Optional[str]
    align: Optional[str]
    ctaStyle: Optional[str]
    showSignIn: Optional[bool]
    themeToggle: Optional["SpacesSettingsPatchThemeDraftParamsChromeThemeToggle"]
    sidebarBrand: Optional[str]


class SpacesSettingsPatchThemeDraftParamsNotFoundLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsPatchThemeDraftParamsNotFound(TypedDict, total=False):
    title: Optional[str]
    body: Optional[str]
    pageId: Optional[str]
    pageSpaceId: Optional[str]
    hidePage: Optional[bool]
    links: Optional[List["SpacesSettingsPatchThemeDraftParamsNotFoundLink"]]
    showSearch: Optional[bool]
    showSections: Optional[bool]
    hideSearch: Optional[bool]


class SpacesSettingsPatchThemeDraftParamsComponentsFocus(TypedDict, total=False):
    color: Optional[str]
    width: Optional[float]
    offset: Optional[float]


class SpacesSettingsPatchThemeDraftParamsComponentsCode(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    radius: Optional[float]


class SpacesSettingsPatchThemeDraftParamsComponentsInput(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    radius: Optional[float]


class SpacesSettingsPatchThemeDraftParamsComponentsButton(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    radius: Optional[float]
    shadow: Optional[str]
    weight: Optional[str]


class SpacesSettingsPatchThemeDraftParamsComponentsSpacing(TypedDict, total=False):
    scale: Optional[float]
    block: Optional[float]
    section: Optional[float]
    pad: Optional[float]


class SpacesSettingsPatchThemeDraftParamsComponentsSelection(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]


class SpacesSettingsPatchThemeDraftParamsComponentsScrollbar(TypedDict, total=False):
    width: Optional[str]
    thumb: Optional[str]
    track: Optional[str]


class SpacesSettingsPatchThemeDraftParamsComponentsSyntax(TypedDict, total=False):
    comment: Optional[str]
    keyword: Optional[str]
    string: Optional[str]
    number: Optional[str]
    title: Optional[str]
    built_in: Optional[str]
    tag: Optional[str]
    attr: Optional[str]
    meta: Optional[str]
    emphasis: Optional[str]


class SpacesSettingsPatchThemeDraftParamsComponentsSyntaxDark(TypedDict, total=False):
    comment: Optional[str]
    keyword: Optional[str]
    string: Optional[str]
    number: Optional[str]
    title: Optional[str]
    built_in: Optional[str]
    tag: Optional[str]
    attr: Optional[str]
    meta: Optional[str]
    emphasis: Optional[str]


class SpacesSettingsPatchThemeDraftParamsComponents(TypedDict, total=False):
    radius: Optional[float]
    shadow: Optional[str]
    focus: Optional["SpacesSettingsPatchThemeDraftParamsComponentsFocus"]
    code: Optional["SpacesSettingsPatchThemeDraftParamsComponentsCode"]
    input: Optional["SpacesSettingsPatchThemeDraftParamsComponentsInput"]
    button: Optional["SpacesSettingsPatchThemeDraftParamsComponentsButton"]
    spacing: Optional["SpacesSettingsPatchThemeDraftParamsComponentsSpacing"]
    selection: Optional["SpacesSettingsPatchThemeDraftParamsComponentsSelection"]
    scrollbar: Optional["SpacesSettingsPatchThemeDraftParamsComponentsScrollbar"]
    syntax: Optional["SpacesSettingsPatchThemeDraftParamsComponentsSyntax"]
    syntaxDark: Optional["SpacesSettingsPatchThemeDraftParamsComponentsSyntaxDark"]


class SpacesSettingsPatchThemeDraftParamsMotionReveal(TypedDict, total=False):
    effect: Optional[str]
    stagger: Optional[int]
    distance: Optional[int]
    once: Optional[bool]
    targets: Optional[List[str]]


class SpacesSettingsPatchThemeDraftParamsMotionHover(TypedDict, total=False):
    link: Optional[str]
    button: Optional[str]
    card: Optional[str]
    image: Optional[str]


class SpacesSettingsPatchThemeDraftParamsMotionHeader(TypedDict, total=False):
    behavior: Optional[str]
    blur: Optional[bool]


class SpacesSettingsPatchThemeDraftParamsMotionAmbient(TypedDict, total=False):
    background: Optional[str]
    cursorGlow: Optional[bool]
    scrollProgress: Optional[bool]
    smoothScroll: Optional[bool]
    focusRing: Optional[bool]


class SpacesSettingsPatchThemeDraftParamsMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class SpacesSettingsPatchThemeDraftParamsMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["SpacesSettingsPatchThemeDraftParamsMotionKeyframeStep"]


class SpacesSettingsPatchThemeDraftParamsMotion(TypedDict, total=False):
    preset: Optional[str]
    enabled: Optional[bool]
    respectReducedMotion: Optional[bool]
    speed: Optional[float]
    easing: Optional[str]
    pageTransition: Optional[str]
    reveal: Optional["SpacesSettingsPatchThemeDraftParamsMotionReveal"]
    hover: Optional["SpacesSettingsPatchThemeDraftParamsMotionHover"]
    header: Optional["SpacesSettingsPatchThemeDraftParamsMotionHeader"]
    ambient: Optional["SpacesSettingsPatchThemeDraftParamsMotionAmbient"]
    keyframes: Optional[List["SpacesSettingsPatchThemeDraftParamsMotionKeyframe"]]
    targets: Optional[Dict[str, Any]]


class SpacesSettingsPatchThemeDraftParamsComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsPatchThemeDraftParamsMobile(TypedDict, total=False):
    fontScale: Optional[float]
    density: Optional[str]
    logoUrl: Optional[Any]
    hide: Optional[List[str]]
    css: Optional[str]


class SpacesSettingsPatchThemeDraftParams(TypedDict, total=False):
    primaryColor: Optional[str]
    accentColor: Optional[str]
    palette: Optional["SpacesSettingsPatchThemeDraftParamsPalette"]
    paletteDark: Optional["SpacesSettingsPatchThemeDraftParamsPaletteDark"]
    font: Optional[str]
    colorScheme: Optional[str]
    contentWidth: Optional[str]
    onThisPage: Optional[str]
    layout: Optional["SpacesSettingsPatchThemeDraftParamsLayout"]
    customFontUrl: Optional[Any]
    customFontFamily: Optional[str]
    brandName: Optional[Any]
    headingFontFamily: Optional[str]
    bodyFontFamily: Optional[str]
    monoFontFamily: Optional[str]
    typography: Optional["SpacesSettingsPatchThemeDraftParamsTypography"]
    fonts: Optional["SpacesSettingsPatchThemeDraftParamsFonts"]
    logoUrl: Optional[Any]
    logoMark: Optional[Any]
    faviconUrl: Optional[Any]
    customCss: Optional[str]
    customJs: Optional[str]
    scriptOrigins: Optional[List[str]]
    ads: Optional["SpacesSettingsPatchThemeDraftParamsAds"]
    whiteLabel: Optional[bool]
    showLanguageSwitcher: Optional[bool]
    apiOrigins: Optional[List[str]]
    fontOrigins: Optional[List[str]]
    fontOriginsRemoved: Optional[List[str]]
    imgOrigins: Optional[List[str]]
    mediaOrigins: Optional[List[str]]
    frameOrigins: Optional[List[str]]
    elementStyles: Optional[List["SpacesSettingsPatchThemeDraftParamsElementStyle"]]
    settingsSchema: Optional[List["SpacesSettingsPatchThemeDraftParamsSettingsSchemaItem"]]
    settings: Optional[Dict[str, Any]]
    stringOverrides: Optional[Dict[str, Any]]
    cssSnippets: Optional[List["SpacesSettingsPatchThemeDraftParamsCssSnippet"]]
    announcement: Optional["SpacesSettingsPatchThemeDraftParamsAnnouncement"]
    chrome: Optional["SpacesSettingsPatchThemeDraftParamsChrome"]
    notFound: Optional["SpacesSettingsPatchThemeDraftParamsNotFound"]
    components: Optional["SpacesSettingsPatchThemeDraftParamsComponents"]
    motion: Optional["SpacesSettingsPatchThemeDraftParamsMotion"]
    componentInstalls: Optional[List["SpacesSettingsPatchThemeDraftParamsComponentInstall"]]
    mobile: Optional["SpacesSettingsPatchThemeDraftParamsMobile"]


class SpacesSettingsPublishThemeDraftParams(TypedDict, total=False):
    force: bool


class SpacesSettingsPublishThemeDraftResponseThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class SpacesSettingsPublishThemeDraftResponseThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class SpacesSettingsPublishThemeDraftResponseThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsPublishThemeDraftResponseThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class SpacesSettingsPublishThemeDraftResponseThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsPublishThemeDraftResponseThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class SpacesSettingsPublishThemeDraftResponseThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class SpacesSettingsPublishThemeDraftResponseThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class SpacesSettingsPublishThemeDraftResponseThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class SpacesSettingsPublishThemeDraftResponseThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "SpacesSettingsPublishThemeDraftResponseThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["SpacesSettingsPublishThemeDraftResponseThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["SpacesSettingsPublishThemeDraftResponseThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["SpacesSettingsPublishThemeDraftResponseThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "SpacesSettingsPublishThemeDraftResponseThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["SpacesSettingsPublishThemeDraftResponseThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "SpacesSettingsPublishThemeDraftResponseThemeChromeThemeToggle"


class SpacesSettingsPublishThemeDraftResponseThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsPublishThemeDraftResponseThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class SpacesSettingsPublishThemeDraftResponseThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsPublishThemeDraftResponseThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class SpacesSettingsPublishThemeDraftResponseThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsPublishThemeDraftResponseThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class SpacesSettingsPublishThemeDraftResponseThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SpacesSettingsPublishThemeDraftResponseThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class SpacesSettingsPublishThemeDraftResponseThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsPublishThemeDraftResponseThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsPublishThemeDraftResponseThemeComponents(TypedDict, total=False):
    button: "SpacesSettingsPublishThemeDraftResponseThemeComponentsButton"
    code: "SpacesSettingsPublishThemeDraftResponseThemeComponentsCode"
    focus: "SpacesSettingsPublishThemeDraftResponseThemeComponentsFocus"
    input: "SpacesSettingsPublishThemeDraftResponseThemeComponentsInput"
    radius: float
    scrollbar: "SpacesSettingsPublishThemeDraftResponseThemeComponentsScrollbar"
    selection: "SpacesSettingsPublishThemeDraftResponseThemeComponentsSelection"
    shadow: str
    spacing: "SpacesSettingsPublishThemeDraftResponseThemeComponentsSpacing"
    syntax: "SpacesSettingsPublishThemeDraftResponseThemeComponentsSyntax"
    syntaxDark: "SpacesSettingsPublishThemeDraftResponseThemeComponentsSyntaxDark"


class SpacesSettingsPublishThemeDraftResponseThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class SpacesSettingsPublishThemeDraftResponseThemeLayout(TypedDict, total=False):
    measure: str


class SpacesSettingsPublishThemeDraftResponseThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class SpacesSettingsPublishThemeDraftResponseThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class SpacesSettingsPublishThemeDraftResponseThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SpacesSettingsPublishThemeDraftResponseThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class SpacesSettingsPublishThemeDraftResponseThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class SpacesSettingsPublishThemeDraftResponseThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


SpacesSettingsPublishThemeDraftResponseThemeMotionTargets = TypedDict("SpacesSettingsPublishThemeDraftResponseThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class SpacesSettingsPublishThemeDraftResponseThemeMotion(TypedDict, total=False):
    ambient: "SpacesSettingsPublishThemeDraftResponseThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "SpacesSettingsPublishThemeDraftResponseThemeMotionHeader"
    hover: "SpacesSettingsPublishThemeDraftResponseThemeMotionHover"
    keyframes: List["SpacesSettingsPublishThemeDraftResponseThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "SpacesSettingsPublishThemeDraftResponseThemeMotionReveal"
    speed: float
    targets: "SpacesSettingsPublishThemeDraftResponseThemeMotionTargets"


class SpacesSettingsPublishThemeDraftResponseThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsPublishThemeDraftResponseThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["SpacesSettingsPublishThemeDraftResponseThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class SpacesSettingsPublishThemeDraftResponseThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsPublishThemeDraftResponseThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsPublishThemeDraftResponseThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class SpacesSettingsPublishThemeDraftResponseTheme(TypedDict, total=False):
    accentColor: str
    ads: "SpacesSettingsPublishThemeDraftResponseThemeAds"
    announcement: "SpacesSettingsPublishThemeDraftResponseThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "SpacesSettingsPublishThemeDraftResponseThemeChrome"
    colorScheme: str
    componentInstalls: List["SpacesSettingsPublishThemeDraftResponseThemeComponentInstall"]
    components: "SpacesSettingsPublishThemeDraftResponseThemeComponents"
    contentWidth: str
    cssSnippets: List["SpacesSettingsPublishThemeDraftResponseThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "SpacesSettingsPublishThemeDraftResponseThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "SpacesSettingsPublishThemeDraftResponseThemeMobile"
    monoFontFamily: str
    motion: "SpacesSettingsPublishThemeDraftResponseThemeMotion"
    notFound: "SpacesSettingsPublishThemeDraftResponseThemeNotFound"
    onThisPage: str
    palette: "SpacesSettingsPublishThemeDraftResponseThemePalette"
    paletteDark: "SpacesSettingsPublishThemeDraftResponseThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["SpacesSettingsPublishThemeDraftResponseThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class SpacesSettingsPublishThemeDraftResponseDataAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class SpacesSettingsPublishThemeDraftResponseDataAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class SpacesSettingsPublishThemeDraftResponseDataChromeCta(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsPublishThemeDraftResponseDataChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class SpacesSettingsPublishThemeDraftResponseDataChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsPublishThemeDraftResponseDataChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class SpacesSettingsPublishThemeDraftResponseDataChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class SpacesSettingsPublishThemeDraftResponseDataChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class SpacesSettingsPublishThemeDraftResponseDataChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class SpacesSettingsPublishThemeDraftResponseDataChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "SpacesSettingsPublishThemeDraftResponseDataChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["SpacesSettingsPublishThemeDraftResponseDataChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["SpacesSettingsPublishThemeDraftResponseDataChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["SpacesSettingsPublishThemeDraftResponseDataChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "SpacesSettingsPublishThemeDraftResponseDataChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["SpacesSettingsPublishThemeDraftResponseDataChromeSocialLink"]
    sticky: bool
    themeToggle: "SpacesSettingsPublishThemeDraftResponseDataChromeThemeToggle"


class SpacesSettingsPublishThemeDraftResponseDataComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsPublishThemeDraftResponseDataComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class SpacesSettingsPublishThemeDraftResponseDataComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsPublishThemeDraftResponseDataComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class SpacesSettingsPublishThemeDraftResponseDataComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class SpacesSettingsPublishThemeDraftResponseDataComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class SpacesSettingsPublishThemeDraftResponseDataComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SpacesSettingsPublishThemeDraftResponseDataComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class SpacesSettingsPublishThemeDraftResponseDataComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsPublishThemeDraftResponseDataComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class SpacesSettingsPublishThemeDraftResponseDataComponents(TypedDict, total=False):
    button: "SpacesSettingsPublishThemeDraftResponseDataComponentsButton"
    code: "SpacesSettingsPublishThemeDraftResponseDataComponentsCode"
    focus: "SpacesSettingsPublishThemeDraftResponseDataComponentsFocus"
    input: "SpacesSettingsPublishThemeDraftResponseDataComponentsInput"
    radius: float
    scrollbar: "SpacesSettingsPublishThemeDraftResponseDataComponentsScrollbar"
    selection: "SpacesSettingsPublishThemeDraftResponseDataComponentsSelection"
    shadow: str
    spacing: "SpacesSettingsPublishThemeDraftResponseDataComponentsSpacing"
    syntax: "SpacesSettingsPublishThemeDraftResponseDataComponentsSyntax"
    syntaxDark: "SpacesSettingsPublishThemeDraftResponseDataComponentsSyntaxDark"


class SpacesSettingsPublishThemeDraftResponseDataCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class SpacesSettingsPublishThemeDraftResponseDataLayout(TypedDict, total=False):
    measure: str


class SpacesSettingsPublishThemeDraftResponseDataMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class SpacesSettingsPublishThemeDraftResponseDataMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class SpacesSettingsPublishThemeDraftResponseDataMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SpacesSettingsPublishThemeDraftResponseDataMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class SpacesSettingsPublishThemeDraftResponseDataMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class SpacesSettingsPublishThemeDraftResponseDataMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


SpacesSettingsPublishThemeDraftResponseDataMotionTargets = TypedDict("SpacesSettingsPublishThemeDraftResponseDataMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class SpacesSettingsPublishThemeDraftResponseDataMotion(TypedDict, total=False):
    ambient: "SpacesSettingsPublishThemeDraftResponseDataMotionAmbient"
    easing: str
    enabled: bool
    header: "SpacesSettingsPublishThemeDraftResponseDataMotionHeader"
    hover: "SpacesSettingsPublishThemeDraftResponseDataMotionHover"
    keyframes: List["SpacesSettingsPublishThemeDraftResponseDataMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "SpacesSettingsPublishThemeDraftResponseDataMotionReveal"
    speed: float
    targets: "SpacesSettingsPublishThemeDraftResponseDataMotionTargets"


class SpacesSettingsPublishThemeDraftResponseDataNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class SpacesSettingsPublishThemeDraftResponseDataNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["SpacesSettingsPublishThemeDraftResponseDataNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class SpacesSettingsPublishThemeDraftResponseDataPalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsPublishThemeDraftResponseDataPaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class SpacesSettingsPublishThemeDraftResponseDataSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class SpacesSettingsPublishThemeDraftResponseData(TypedDict, total=False):
    accentColor: str
    ads: "SpacesSettingsPublishThemeDraftResponseDataAds"
    announcement: "SpacesSettingsPublishThemeDraftResponseDataAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "SpacesSettingsPublishThemeDraftResponseDataChrome"
    colorScheme: str
    componentInstalls: List["SpacesSettingsPublishThemeDraftResponseDataComponentInstall"]
    components: "SpacesSettingsPublishThemeDraftResponseDataComponents"
    contentWidth: str
    cssSnippets: List["SpacesSettingsPublishThemeDraftResponseDataCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "SpacesSettingsPublishThemeDraftResponseDataLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "SpacesSettingsPublishThemeDraftResponseDataMobile"
    monoFontFamily: str
    motion: "SpacesSettingsPublishThemeDraftResponseDataMotion"
    notFound: "SpacesSettingsPublishThemeDraftResponseDataNotFound"
    onThisPage: str
    palette: "SpacesSettingsPublishThemeDraftResponseDataPalette"
    paletteDark: "SpacesSettingsPublishThemeDraftResponseDataPaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["SpacesSettingsPublishThemeDraftResponseDataSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class SpacesSettingsPublishThemeDraftResponse(TypedDict, total=False):
    theme: "SpacesSettingsPublishThemeDraftResponseTheme"
    data: "SpacesSettingsPublishThemeDraftResponseData"
    warnings: List[str]


class SpacesSettingsGetReaderThemesResponse(TypedDict, total=False):
    themes: List["ReaderThemeOption"]
    page: "PageInfo"


class SpacesSettingsSetReaderThemesParamsThemeThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class SpacesSettingsSetReaderThemesParamsThemeThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class SpacesSettingsSetReaderThemesParamsThemeThemeLayout(TypedDict, total=False):
    measure: str


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyFluid(TypedDict, total=False):
    enabled: bool
    minViewport: int
    maxViewport: int
    minScale: float
    bodyMinScale: float


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH1(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH2(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH3(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH4(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH5(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH6(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsBody(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsSmall(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsCode(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevels(TypedDict, total=False):
    h1: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH1"
    h2: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH2"
    h3: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH3"
    h4: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH4"
    h5: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH5"
    h6: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsH6"
    body: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsBody"
    small: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsSmall"
    code: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevelsCode"


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyVariation(TypedDict, total=False):
    heading: str
    body: str
    code: str


class SpacesSettingsSetReaderThemesParamsThemeThemeTypographyFeatures(TypedDict, total=False):
    heading: str
    body: str
    code: str


class SpacesSettingsSetReaderThemesParamsThemeThemeTypography(TypedDict, total=False):
    scale: str
    baseSize: float
    fluid: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyFluid"
    levels: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyLevels"
    headingTransform: str
    variation: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyVariation"
    features: "SpacesSettingsSetReaderThemesParamsThemeThemeTypographyFeatures"
    opticalSizing: str
    headingWrap: str
    bodyWrap: str


class SpacesSettingsSetReaderThemesParamsThemeThemeFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class SpacesSettingsSetReaderThemesParamsThemeThemeFonts(TypedDict, total=False):
    faces: List["SpacesSettingsSetReaderThemesParamsThemeThemeFontsFace"]


class SpacesSettingsSetReaderThemesParamsThemeThemeAds(TypedDict, total=False):
    network: str
    publisherId: str
    slotId: str
    size: str
    enabled: bool
    scriptUrl: str
    slotHtml: str
    configVar: str
    configJson: Dict[str, Any]


class SpacesSettingsSetReaderThemesParamsThemeThemeElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class SpacesSettingsSetReaderThemesParamsThemeThemeSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class SpacesSettingsSetReaderThemesParamsThemeThemeCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class SpacesSettingsSetReaderThemesParamsThemeThemeAnnouncement(TypedDict, total=False):
    text: str
    level: str
    href: Any


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeCta(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeSecondaryCta(TypedDict, total=False):
    label: str
    href: str
    style: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeader(TypedDict, total=False):
    overlay: bool
    overlayInk: str
    height: int
    border: str
    borderColor: str
    shadow: str
    blur: int
    opacity: float
    logoHeight: int
    navGap: int
    navWeight: int
    navSize: float
    navCase: str
    navTracking: float


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List[Dict[str, Any]]
    cta: Dict[str, Any]


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List[Dict[str, Any]]
    featured: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLinkPanelFeatured"
    footer: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLinkChildrenItem"]
    panel: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLinkPanel"
    style: str
    highlight: bool


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeNavMenu(TypedDict, total=False):
    trigger: str
    openDelay: int
    closeDelay: int
    animation: str
    radius: float
    shadow: str
    background: str
    ink: str
    border: str
    width: int


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooterColumnLink"]


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooter(TypedDict, total=False):
    logo: Any
    logoMark: Any
    cookieLinkPlacement: str
    html: str
    css: str
    htmlPlacement: str
    newsletter: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooterNewsletter"


class SpacesSettingsSetReaderThemesParamsThemeThemeChromeThemeToggle(TypedDict, total=False):
    show: bool
    style: str
    position: str
    radius: float
    activeColor: str


class SpacesSettingsSetReaderThemesParamsThemeThemeChrome(TypedDict, total=False):
    cta: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeCta"
    secondaryCta: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeSecondaryCta"
    header: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeader"
    headerLinks: List["SpacesSettingsSetReaderThemesParamsThemeThemeChromeHeaderLink"]
    navMenu: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeNavMenu"
    footerLinks: List["SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooterLink"]
    footerDescription: str
    footerColumns: List["SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooterColumn"]
    socialLinks: List["SpacesSettingsSetReaderThemesParamsThemeThemeChromeSocialLink"]
    copyright: str
    footer: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeFooter"
    mobileNav: str
    sticky: bool
    height: str
    align: str
    ctaStyle: str
    showSignIn: bool
    themeToggle: "SpacesSettingsSetReaderThemesParamsThemeThemeChromeThemeToggle"
    sidebarBrand: str


class SpacesSettingsSetReaderThemesParamsThemeThemeNotFoundLink(TypedDict, total=False):
    label: str
    href: str


class SpacesSettingsSetReaderThemesParamsThemeThemeNotFound(TypedDict, total=False):
    title: str
    body: str
    pageId: str
    pageSpaceId: str
    hidePage: bool
    links: List["SpacesSettingsSetReaderThemesParamsThemeThemeNotFoundLink"]
    showSearch: bool
    showSections: bool
    hideSearch: bool


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class SpacesSettingsSetReaderThemesParamsThemeThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "SpacesSettingsSetReaderThemesParamsThemeThemeComponentsFocus"
    code: "SpacesSettingsSetReaderThemesParamsThemeThemeComponentsCode"
    input: "SpacesSettingsSetReaderThemesParamsThemeThemeComponentsInput"
    button: "SpacesSettingsSetReaderThemesParamsThemeThemeComponentsButton"
    spacing: "SpacesSettingsSetReaderThemesParamsThemeThemeComponentsSpacing"
    selection: "SpacesSettingsSetReaderThemesParamsThemeThemeComponentsSelection"
    scrollbar: "SpacesSettingsSetReaderThemesParamsThemeThemeComponentsScrollbar"
    syntax: "SpacesSettingsSetReaderThemesParamsThemeThemeComponentsSyntax"
    syntaxDark: "SpacesSettingsSetReaderThemesParamsThemeThemeComponentsSyntaxDark"


class SpacesSettingsSetReaderThemesParamsThemeThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class SpacesSettingsSetReaderThemesParamsThemeThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class SpacesSettingsSetReaderThemesParamsThemeThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SpacesSettingsSetReaderThemesParamsThemeThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class SpacesSettingsSetReaderThemesParamsThemeThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class SpacesSettingsSetReaderThemesParamsThemeThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["SpacesSettingsSetReaderThemesParamsThemeThemeMotionKeyframeStep"]


class SpacesSettingsSetReaderThemesParamsThemeThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "SpacesSettingsSetReaderThemesParamsThemeThemeMotionReveal"
    hover: "SpacesSettingsSetReaderThemesParamsThemeThemeMotionHover"
    header: "SpacesSettingsSetReaderThemesParamsThemeThemeMotionHeader"
    ambient: "SpacesSettingsSetReaderThemesParamsThemeThemeMotionAmbient"
    keyframes: List["SpacesSettingsSetReaderThemesParamsThemeThemeMotionKeyframe"]
    targets: Dict[str, Any]


class SpacesSettingsSetReaderThemesParamsThemeThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SpacesSettingsSetReaderThemesParamsThemeThemeMobile(TypedDict, total=False):
    fontScale: float
    density: str
    logoUrl: Any
    hide: List[str]
    css: str


class SpacesSettingsSetReaderThemesParamsThemeTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "SpacesSettingsSetReaderThemesParamsThemeThemePalette"
    paletteDark: "SpacesSettingsSetReaderThemesParamsThemeThemePaletteDark"
    font: str
    colorScheme: str
    contentWidth: str
    onThisPage: str
    layout: "SpacesSettingsSetReaderThemesParamsThemeThemeLayout"
    customFontUrl: Any
    customFontFamily: str
    brandName: Any
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    typography: "SpacesSettingsSetReaderThemesParamsThemeThemeTypography"
    fonts: "SpacesSettingsSetReaderThemesParamsThemeThemeFonts"
    logoUrl: Any
    logoMark: Any
    faviconUrl: Any
    customCss: str
    customJs: str
    scriptOrigins: List[str]
    ads: "SpacesSettingsSetReaderThemesParamsThemeThemeAds"
    whiteLabel: bool
    showLanguageSwitcher: bool
    apiOrigins: List[str]
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    imgOrigins: List[str]
    mediaOrigins: List[str]
    frameOrigins: List[str]
    elementStyles: List["SpacesSettingsSetReaderThemesParamsThemeThemeElementStyle"]
    settingsSchema: List["SpacesSettingsSetReaderThemesParamsThemeThemeSettingsSchemaItem"]
    settings: Dict[str, Any]
    stringOverrides: Dict[str, Any]
    cssSnippets: List["SpacesSettingsSetReaderThemesParamsThemeThemeCssSnippet"]
    announcement: "SpacesSettingsSetReaderThemesParamsThemeThemeAnnouncement"
    chrome: "SpacesSettingsSetReaderThemesParamsThemeThemeChrome"
    notFound: "SpacesSettingsSetReaderThemesParamsThemeThemeNotFound"
    components: "SpacesSettingsSetReaderThemesParamsThemeThemeComponents"
    motion: "SpacesSettingsSetReaderThemesParamsThemeThemeMotion"
    componentInstalls: List["SpacesSettingsSetReaderThemesParamsThemeThemeComponentInstall"]
    mobile: "SpacesSettingsSetReaderThemesParamsThemeThemeMobile"


class SpacesSettingsSetReaderThemesParamsTheme(TypedDict, total=False):
    name: str
    theme: "SpacesSettingsSetReaderThemesParamsThemeTheme"


class SpacesSettingsSetReaderThemesParams(TypedDict, total=False):
    themes: List["SpacesSettingsSetReaderThemesParamsTheme"]


class SpacesSettingsSetReaderThemesResponse(TypedDict, total=False):
    themes: List["ReaderThemeOption"]
    warnings: List[str]


class SpacesSettingsSetPresetParams(TypedDict, total=False):
    preset: str
    piecePreset: str
    frontDoor: Dict[str, Any]


class SpacesSettingsSetPresetResponse(TypedDict, total=False):
    frontDoor: Dict[str, Any]
    piecePreset: str
    preset: str
    warnings: List[str]


class SpacesSettingsGetRedirectsResponse(TypedDict, total=False):
    redirects: List["RedirectRule"]
    page: "PageInfo"


class SpacesSettingsSetRedirectsParamsRedirectMatch(TypedDict, total=False):
    query: Any


SpacesSettingsSetRedirectsParamsRedirect = TypedDict("SpacesSettingsSetRedirectsParamsRedirect", {"from": str, "to": Any, "type": str, "status": float, "match": "SpacesSettingsSetRedirectsParamsRedirectMatch", "passQuery": bool}, total=False)


class SpacesSettingsSetRedirectsParams(TypedDict, total=False):
    redirects: List["SpacesSettingsSetRedirectsParamsRedirect"]


class SpacesSettingsSetRedirectsResponse(TypedDict, total=False):
    redirects: List["RedirectRule"]
    warnings: List[str]


class SpacesSettingsSetAnalyticsParams(TypedDict, total=False):
    ga4: str
    gtm: str
    segment: str
    intercom: str
    customHead: str


class SpacesSettingsGetDiscoveryResponse(TypedDict, total=False):
    aiIngestion: bool
    organization: Any
    space: Any


class SpacesSettingsSetDiscoveryParams(TypedDict, total=False):
    aiIngestion: bool


class SpacesSettingsSetDiscoveryResponse(TypedDict, total=False):
    aiIngestion: bool
    warnings: List[str]


class SpacesSettingsGetSeoResponseSocialCard(TypedDict, total=False):
    accent: str
    accentBar: bool
    background: str
    backgroundTo: str
    eyebrowColor: str
    font: str
    footer: str
    logoUrl: str
    titleColor: str


class SpacesSettingsGetSeoResponseVerification(TypedDict, total=False):
    bing: str
    google: str


class SpacesSettingsGetSeoResponse(TypedDict, total=False):
    contentLanguage: str
    description: str
    noindex: bool
    socialCard: "SpacesSettingsGetSeoResponseSocialCard"
    socialImageUrl: str
    verification: "SpacesSettingsGetSeoResponseVerification"


class SpacesSettingsSetSeoParamsSocialCard(TypedDict, total=False):
    accent: str
    background: str
    backgroundTo: str
    titleColor: str
    eyebrowColor: str
    font: str
    logoUrl: Any
    footer: str
    accentBar: bool


class SpacesSettingsSetSeoParamsVerification(TypedDict, total=False):
    google: Any
    bing: Any


class SpacesSettingsSetSeoParams(TypedDict, total=False):
    description: Any
    socialImageUrl: Any
    socialCard: "SpacesSettingsSetSeoParamsSocialCard"
    verification: "SpacesSettingsSetSeoParamsVerification"
    noindex: bool
    contentLanguage: Any


class SpacesSettingsSetSeoResponseSocialCard(TypedDict, total=False):
    accent: str
    accentBar: bool
    background: str
    backgroundTo: str
    eyebrowColor: str
    font: str
    footer: str
    logoUrl: str
    titleColor: str


class SpacesSettingsSetSeoResponseVerification(TypedDict, total=False):
    bing: str
    google: str


class SpacesSettingsSetSeoResponse(TypedDict, total=False):
    contentLanguage: str
    description: str
    noindex: bool
    socialCard: "SpacesSettingsSetSeoResponseSocialCard"
    socialImageUrl: str
    verification: "SpacesSettingsSetSeoResponseVerification"
    warnings: List[str]


class SpacesSettingsGetGlossaryResponseGlossaryItem(TypedDict, total=False):
    definition: str
    term: str


class SpacesSettingsGetGlossaryResponse(TypedDict, total=False):
    glossary: List["SpacesSettingsGetGlossaryResponseGlossaryItem"]
    page: "PageInfo"


class SpacesSettingsSetGlossaryParamsGlossaryItem(TypedDict, total=False):
    term: str
    definition: str


class SpacesSettingsSetGlossaryParams(TypedDict, total=False):
    glossary: List["SpacesSettingsSetGlossaryParamsGlossaryItem"]


class SpacesSettingsSetGlossaryResponseGlossaryItem(TypedDict, total=False):
    definition: str
    term: str


class SpacesSettingsSetGlossaryResponse(TypedDict, total=False):
    glossary: List["SpacesSettingsSetGlossaryResponseGlossaryItem"]
    warnings: List[str]


class SpacesSettingsGetRoadmapSettingsResponse(TypedDict, total=False):
    anonymousVotes: bool
    hiddenStatuses: List[str]
    inheritedStatusLabels: Dict[str, Any]
    moderateSubmissions: bool
    statusLabels: Dict[str, Any]
    statusOrder: List[str]
    voteBudget: float
    voteWeights: List[float]


class SpacesSettingsSetRoadmapSettingsParams(TypedDict, total=False):
    anonymousVotes: bool
    statusLabels: Dict[str, Any]
    statusOrder: List[str]
    hiddenStatuses: List[str]
    voteBudget: int
    voteWeights: List[int]
    moderateSubmissions: bool


class SpacesSettingsSetRoadmapSettingsResponse(TypedDict, total=False):
    anonymousVotes: bool
    hiddenStatuses: List[str]
    inheritedStatusLabels: Dict[str, Any]
    moderateSubmissions: bool
    statusLabels: Dict[str, Any]
    statusOrder: List[str]
    voteBudget: float
    voteWeights: List[float]
    warnings: List[str]


class SpacesSettingsRenameRoadmapLaneParams(TypedDict, total=False):
    label: str


class SpacesSettingsRenameRoadmapLaneResponse(TypedDict, total=False):
    anonymousVotes: bool
    hiddenStatuses: List[str]
    inheritedStatusLabels: Dict[str, Any]
    moderateSubmissions: bool
    statusLabels: Dict[str, Any]
    statusOrder: List[str]
    voteBudget: float
    voteWeights: List[float]
    warnings: List[str]


class SpacesSettingsGetHomePageResponse(TypedDict, total=False):
    homePageId: Any


class SpacesSettingsSetHomePageParams(TypedDict, total=False):
    homePageId: Optional[str]


class SpacesSettingsSetHomePageResponse(TypedDict, total=False):
    homePageId: Any
    warnings: List[str]


class SpacesSettingsGetHomeDocResponse(TypedDict, total=False):
    doc: Any


class SpacesSettingsSetHomeDocParams(TypedDict, total=False):
    doc: Optional[Any]


class SpacesSettingsSetHomeDocResponse(TypedDict, total=False):
    doc: Any
    warnings: List[str]


class SpacesSettingsGetFaqSettingsResponse(TypedDict, total=False):
    contactSpaceId: Any


class SpacesSettingsSetFaqSettingsParams(TypedDict, total=False):
    contactSpaceId: Optional[str]


class SpacesSettingsSetFaqSettingsResponse(TypedDict, total=False):
    contactSpaceId: Any
    warnings: List[str]


class SpacesSettingsGetCommentSettingsResponse(TypedDict, total=False):
    enabled: bool
    moderated: bool


class SpacesSettingsSetCommentSettingsParams(TypedDict, total=False):
    enabled: bool
    moderated: bool


class SpacesSettingsSetCommentSettingsResponse(TypedDict, total=False):
    enabled: bool
    moderated: bool
    warnings: List[str]


class SpacesSettingsGetAiSettingsResponse(TypedDict, total=False):
    enabled: bool


class SpacesSettingsSetAiSettingsParams(TypedDict, total=False):
    enabled: bool


class SpacesSettingsSetAiSettingsResponse(TypedDict, total=False):
    enabled: bool
    warnings: List[str]


class SpacesSettingsGetVisitorAuthResponse(TypedDict, total=False):
    approveNewMembers: bool
    hostedSignup: bool
    mode: str
    provisionIdentity: bool


class SpacesSettingsSetVisitorAuthParamsOidc(TypedDict, total=False):
    issuer: str
    clientId: str
    clientSecret: str
    scope: str


class SpacesSettingsSetVisitorAuthParams(TypedDict, total=False):
    mode: str
    password: str
    jwtSecret: str
    oidc: "SpacesSettingsSetVisitorAuthParamsOidc"
    provisionIdentity: bool
    approveNewMembers: bool
    hostedSignup: bool


class SpacesSettingsSetVisitorAuthResponse(TypedDict, total=False):
    mode: str
    warnings: List[str]


class SpacesThemeOriginsListResponse(TypedDict, total=False):
    allowed: List[str]
    hosts: List["HostOriginPolicy"]
    origins: List["DiscoveredOrigin"]
    removed: List[str]


class SpacesThemeOriginsRestoreResponse(TypedDict, total=False):
    allowed: List[str]
    removed: List[str]


class SpacesThemeOriginsRemoveResponse(TypedDict, total=False):
    allowed: List[str]
    removed: List[str]


class MembersListResponse(TypedDict, total=False):
    members: List["MemberRow"]
    page: "PageInfo"


class MembersInviteParams(TypedDict, total=False):
    email: str
    role: str
    spaceId: Optional[str]
    effect: str
    groupId: Optional[str]


class MembersInviteResponse(TypedDict, total=False):
    invite: "InviteRow"
    data: "InviteRow"
    warnings: List[str]


class MembersInvitesResponse(TypedDict, total=False):
    invites: List["InviteRow"]
    page: "PageInfo"


class MembersRevokeInviteResponse(TypedDict, total=False):
    ok: bool


class MembersBulkInviteParams(TypedDict, total=False):
    emails: List[str]
    csv: str
    role: str
    spaceId: Optional[str]
    effect: str
    groupId: Optional[str]


class MembersListInviteLinksResponse(TypedDict, total=False):
    links: List["InviteLinkRow"]
    page: "PageInfo"


class MembersCreateInviteLinkParams(TypedDict, total=False):
    role: str
    spaceId: Optional[str]
    effect: str
    groupId: Optional[str]
    email: Optional[str]
    maxUses: Optional[int]
    expiresInDays: Optional[int]


class MembersCreateInviteLinkResponse(TypedDict, total=False):
    link: "CreatedInviteLink"
    data: "CreatedInviteLink"
    warnings: List[str]


class MembersRevokeInviteLinkResponse(TypedDict, total=False):
    ok: bool


class MembersUpdateParams(TypedDict, total=False):
    role: str
    spaceId: Optional[str]
    effect: str
    customRoleId: Optional[str]


class MembersUpdateResponse(TypedDict, total=False):
    member: "MemberRow"
    warnings: List[str]


class MembersRemoveResponse(TypedDict, total=False):
    ok: bool


class MembersRevokeSessionsResponse(TypedDict, total=False):
    ok: bool


class MembersReassignContentParams(TypedDict, total=False):
    targetUserId: str


class MembersReassignContentResponseReassigned(TypedDict, total=False):
    posts: float
    topics: float


class MembersReassignContentResponse(TypedDict, total=False):
    reassigned: "MembersReassignContentResponseReassigned"
    warnings: List[str]


class InvitesPendingResponse(TypedDict, total=False):
    invites: List["PendingInvite"]
    page: "PageInfo"


class InvitesAcceptPendingResponse(TypedDict, total=False):
    organizationId: str


class InvitesAcceptParams(TypedDict, total=False):
    token: str


class InvitesAcceptResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class InvitesAcceptLinkParams(TypedDict, total=False):
    token: str


class InvitesAcceptLinkResponse(TypedDict, total=False):
    organizationId: str
    status: str
    warnings: List[str]


class AuditActionsResponse(TypedDict, total=False):
    actions: List[str]
    page: "PageInfo"


class CustomFieldsListDefsResponse(TypedDict, total=False):
    fields: List["FieldDef"]
    page: "PageInfo"


class CustomFieldsCreateDefParams(TypedDict, total=False):
    label: str
    type: str
    options: List[str]
    sortOrder: int
    visibility: str
    showOnCard: bool
    editableByUser: bool
    requiredAtSignup: bool


class CustomFieldsCreateDefResponse(TypedDict, total=False):
    field: "FieldDef"
    data: "FieldDef"
    warnings: List[str]


class CustomFieldsDeleteDefResponse(TypedDict, total=False):
    ok: bool


class CustomFieldsGetValuesResponse(TypedDict, total=False):
    values: List["FieldValue"]
    page: "PageInfo"


class CustomFieldsSetValueParams(TypedDict, total=False):
    key: str
    value: str


class CustomFieldsSetValueResponse(TypedDict, total=False):
    values: List["FieldValue"]
    warnings: List[str]


class CustomFieldsSetOwnValuesParamsValue(TypedDict, total=False):
    key: str
    value: str


class CustomFieldsSetOwnValuesParams(TypedDict, total=False):
    values: List["CustomFieldsSetOwnValuesParamsValue"]


class CustomFieldsSetOwnValuesResponse(TypedDict, total=False):
    values: List["FieldValue"]
    warnings: List[str]


class ModerationScreeningListResponse(TypedDict, total=False):
    screened: List["ScreenedRow"]
    page: "PageInfo"


class ModerationScreeningAddParams(TypedDict, total=False):
    kind: str
    pattern: str
    note: str
    action: str


class ModerationScreeningAddResponse(TypedDict, total=False):
    screened: "ScreenedRow"
    data: "ScreenedRow"
    warnings: List[str]


class ModerationScreeningRemoveResponse(TypedDict, total=False):
    ok: bool


class ServiceAccountsListResponse(TypedDict, total=False):
    accounts: List["ServiceAccountSummary"]
    page: "PageInfo"


class ServiceAccountsCreateParams(TypedDict, total=False):
    name: str
    role: str


class ServiceAccountsCreateResponse(TypedDict, total=False):
    account: "ServiceAccountSummary"
    data: "ServiceAccountSummary"
    warnings: List[str]


class ServiceAccountsRenameParams(TypedDict, total=False):
    name: str


class ServiceAccountsRenameResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ServiceAccountsRevokeResponse(TypedDict, total=False):
    ok: bool


class ServiceAccountsTokensResponse(TypedDict, total=False):
    tokens: List["PatSummary"]
    page: "PageInfo"


class ServiceAccountsMintParamsConstraints(TypedDict, total=False):
    spaceIds: List[str]
    categoryIds: List[str]
    orgIds: List[str]


class ServiceAccountsMintParams(TypedDict, total=False):
    name: str
    scopes: List[str]
    expiresInDays: int
    spaceIds: List[str]
    capabilities: List[str]
    scopeGrants: List[str]
    constraints: "ServiceAccountsMintParamsConstraints"


class ServiceAccountsMintResponse(TypedDict, total=False):
    pat: "PatSummary"
    token: str
    data: "PatSummary"
    warnings: List[str]


class ServiceAccountsRevokeTokenResponse(TypedDict, total=False):
    ok: bool


class ThemesComponentsGalleryResponse(TypedDict, total=False):
    builtin: List["ThemePreset"]
    saved: List["ThemeComponentSummary"]


class ThemesComponentsSaveParams(TypedDict, total=False):
    name: str
    spaceId: str
    parentThemeId: str
    enabled: bool


class ThemesComponentsSaveResponse(TypedDict, total=False):
    component: "ThemeComponentSummary"
    data: "ThemeComponentSummary"
    warnings: List[str]


class ThemesComponentsPatchParams(TypedDict, total=False):
    enabled: bool
    parentThemeId: Optional[str]


class ThemesComponentsPatchResponse(TypedDict, total=False):
    component: "ThemeComponentSummary"
    warnings: List[str]


class ThemesComponentsRemoveResponse(TypedDict, total=False):
    ok: bool


class ThemesComponentsCompositeResponseThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ThemesComponentsCompositeResponseThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ThemesComponentsCompositeResponseThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ThemesComponentsCompositeResponseThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemesComponentsCompositeResponseThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ThemesComponentsCompositeResponseThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ThemesComponentsCompositeResponseThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ThemesComponentsCompositeResponseThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ThemesComponentsCompositeResponseThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ThemesComponentsCompositeResponseThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ThemesComponentsCompositeResponseThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ThemesComponentsCompositeResponseThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ThemesComponentsCompositeResponseThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ThemesComponentsCompositeResponseThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ThemesComponentsCompositeResponseThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ThemesComponentsCompositeResponseThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ThemesComponentsCompositeResponseThemeChromeThemeToggle"


class ThemesComponentsCompositeResponseThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ThemesComponentsCompositeResponseThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ThemesComponentsCompositeResponseThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemesComponentsCompositeResponseThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ThemesComponentsCompositeResponseThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemesComponentsCompositeResponseThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ThemesComponentsCompositeResponseThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemesComponentsCompositeResponseThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ThemesComponentsCompositeResponseThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemesComponentsCompositeResponseThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemesComponentsCompositeResponseThemeComponents(TypedDict, total=False):
    button: "ThemesComponentsCompositeResponseThemeComponentsButton"
    code: "ThemesComponentsCompositeResponseThemeComponentsCode"
    focus: "ThemesComponentsCompositeResponseThemeComponentsFocus"
    input: "ThemesComponentsCompositeResponseThemeComponentsInput"
    radius: float
    scrollbar: "ThemesComponentsCompositeResponseThemeComponentsScrollbar"
    selection: "ThemesComponentsCompositeResponseThemeComponentsSelection"
    shadow: str
    spacing: "ThemesComponentsCompositeResponseThemeComponentsSpacing"
    syntax: "ThemesComponentsCompositeResponseThemeComponentsSyntax"
    syntaxDark: "ThemesComponentsCompositeResponseThemeComponentsSyntaxDark"


class ThemesComponentsCompositeResponseThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ThemesComponentsCompositeResponseThemeLayout(TypedDict, total=False):
    measure: str


class ThemesComponentsCompositeResponseThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ThemesComponentsCompositeResponseThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ThemesComponentsCompositeResponseThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemesComponentsCompositeResponseThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ThemesComponentsCompositeResponseThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ThemesComponentsCompositeResponseThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ThemesComponentsCompositeResponseThemeMotionTargets = TypedDict("ThemesComponentsCompositeResponseThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ThemesComponentsCompositeResponseThemeMotion(TypedDict, total=False):
    ambient: "ThemesComponentsCompositeResponseThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ThemesComponentsCompositeResponseThemeMotionHeader"
    hover: "ThemesComponentsCompositeResponseThemeMotionHover"
    keyframes: List["ThemesComponentsCompositeResponseThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ThemesComponentsCompositeResponseThemeMotionReveal"
    speed: float
    targets: "ThemesComponentsCompositeResponseThemeMotionTargets"


class ThemesComponentsCompositeResponseThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ThemesComponentsCompositeResponseThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ThemesComponentsCompositeResponseThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ThemesComponentsCompositeResponseThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemesComponentsCompositeResponseThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemesComponentsCompositeResponseThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ThemesComponentsCompositeResponseTheme(TypedDict, total=False):
    accentColor: str
    ads: "ThemesComponentsCompositeResponseThemeAds"
    announcement: "ThemesComponentsCompositeResponseThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ThemesComponentsCompositeResponseThemeChrome"
    colorScheme: str
    componentInstalls: List["ThemesComponentsCompositeResponseThemeComponentInstall"]
    components: "ThemesComponentsCompositeResponseThemeComponents"
    contentWidth: str
    cssSnippets: List["ThemesComponentsCompositeResponseThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ThemesComponentsCompositeResponseThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ThemesComponentsCompositeResponseThemeMobile"
    monoFontFamily: str
    motion: "ThemesComponentsCompositeResponseThemeMotion"
    notFound: "ThemesComponentsCompositeResponseThemeNotFound"
    onThisPage: str
    palette: "ThemesComponentsCompositeResponseThemePalette"
    paletteDark: "ThemesComponentsCompositeResponseThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ThemesComponentsCompositeResponseThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ThemesComponentsCompositeResponse(TypedDict, total=False):
    theme: "ThemesComponentsCompositeResponseTheme"


class ThemesComponentsImportParams(TypedDict, total=False):
    url: str
    name: str


class ThemesComponentsImportResponse(TypedDict, total=False):
    component: "ThemeComponentSummary"
    data: "ThemeComponentSummary"
    warnings: List[str]


class ThemesComponentsApplyParams(TypedDict, total=False):
    presetId: str
    componentId: str


class ThemesComponentsApplyResponseThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ThemesComponentsApplyResponseThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ThemesComponentsApplyResponseThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ThemesComponentsApplyResponseThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemesComponentsApplyResponseThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ThemesComponentsApplyResponseThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ThemesComponentsApplyResponseThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ThemesComponentsApplyResponseThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ThemesComponentsApplyResponseThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ThemesComponentsApplyResponseThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ThemesComponentsApplyResponseThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ThemesComponentsApplyResponseThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ThemesComponentsApplyResponseThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ThemesComponentsApplyResponseThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ThemesComponentsApplyResponseThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ThemesComponentsApplyResponseThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ThemesComponentsApplyResponseThemeChromeThemeToggle"


class ThemesComponentsApplyResponseThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ThemesComponentsApplyResponseThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ThemesComponentsApplyResponseThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemesComponentsApplyResponseThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ThemesComponentsApplyResponseThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemesComponentsApplyResponseThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ThemesComponentsApplyResponseThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemesComponentsApplyResponseThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ThemesComponentsApplyResponseThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemesComponentsApplyResponseThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemesComponentsApplyResponseThemeComponents(TypedDict, total=False):
    button: "ThemesComponentsApplyResponseThemeComponentsButton"
    code: "ThemesComponentsApplyResponseThemeComponentsCode"
    focus: "ThemesComponentsApplyResponseThemeComponentsFocus"
    input: "ThemesComponentsApplyResponseThemeComponentsInput"
    radius: float
    scrollbar: "ThemesComponentsApplyResponseThemeComponentsScrollbar"
    selection: "ThemesComponentsApplyResponseThemeComponentsSelection"
    shadow: str
    spacing: "ThemesComponentsApplyResponseThemeComponentsSpacing"
    syntax: "ThemesComponentsApplyResponseThemeComponentsSyntax"
    syntaxDark: "ThemesComponentsApplyResponseThemeComponentsSyntaxDark"


class ThemesComponentsApplyResponseThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ThemesComponentsApplyResponseThemeLayout(TypedDict, total=False):
    measure: str


class ThemesComponentsApplyResponseThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ThemesComponentsApplyResponseThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ThemesComponentsApplyResponseThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemesComponentsApplyResponseThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ThemesComponentsApplyResponseThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ThemesComponentsApplyResponseThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ThemesComponentsApplyResponseThemeMotionTargets = TypedDict("ThemesComponentsApplyResponseThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ThemesComponentsApplyResponseThemeMotion(TypedDict, total=False):
    ambient: "ThemesComponentsApplyResponseThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ThemesComponentsApplyResponseThemeMotionHeader"
    hover: "ThemesComponentsApplyResponseThemeMotionHover"
    keyframes: List["ThemesComponentsApplyResponseThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ThemesComponentsApplyResponseThemeMotionReveal"
    speed: float
    targets: "ThemesComponentsApplyResponseThemeMotionTargets"


class ThemesComponentsApplyResponseThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ThemesComponentsApplyResponseThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ThemesComponentsApplyResponseThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ThemesComponentsApplyResponseThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemesComponentsApplyResponseThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemesComponentsApplyResponseThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ThemesComponentsApplyResponseTheme(TypedDict, total=False):
    accentColor: str
    ads: "ThemesComponentsApplyResponseThemeAds"
    announcement: "ThemesComponentsApplyResponseThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ThemesComponentsApplyResponseThemeChrome"
    colorScheme: str
    componentInstalls: List["ThemesComponentsApplyResponseThemeComponentInstall"]
    components: "ThemesComponentsApplyResponseThemeComponents"
    contentWidth: str
    cssSnippets: List["ThemesComponentsApplyResponseThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ThemesComponentsApplyResponseThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ThemesComponentsApplyResponseThemeMobile"
    monoFontFamily: str
    motion: "ThemesComponentsApplyResponseThemeMotion"
    notFound: "ThemesComponentsApplyResponseThemeNotFound"
    onThisPage: str
    palette: "ThemesComponentsApplyResponseThemePalette"
    paletteDark: "ThemesComponentsApplyResponseThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ThemesComponentsApplyResponseThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ThemesComponentsApplyResponse(TypedDict, total=False):
    theme: "ThemesComponentsApplyResponseTheme"
    warnings: List[str]


class CoursesCompleteParams(TypedDict, total=False):
    completed: bool


class CoursesCompleteResponse(TypedDict, total=False):
    completed: bool
    warnings: List[str]


class CoursesQuizzesSaveLessonQuizParamsQuestion(TypedDict, total=False):
    id: str
    prompt: str
    choices: List[str]
    correctIndexes: List[int]
    explanation: str


class CoursesQuizzesSaveLessonQuizParams(TypedDict, total=False):
    title: str
    passingScore: int
    questions: List["CoursesQuizzesSaveLessonQuizParamsQuestion"]


class CoursesQuizzesSaveLessonQuizResponse(TypedDict, total=False):
    id: str
    warnings: List[str]


class CoursesQuizzesSaveModuleQuizParamsQuestion(TypedDict, total=False):
    id: str
    prompt: str
    choices: List[str]
    correctIndexes: List[int]
    explanation: str


class CoursesQuizzesSaveModuleQuizParams(TypedDict, total=False):
    title: str
    passingScore: int
    questions: List["CoursesQuizzesSaveModuleQuizParamsQuestion"]


class CoursesQuizzesSaveModuleQuizResponse(TypedDict, total=False):
    id: str
    warnings: List[str]


class CoursesQuizzesDeleteQuizResponse(TypedDict, total=False):
    deleted: bool


class CoursesQuizzesSetQuizPolicyParams(TypedDict, total=False):
    reveal: str
    maxAttempts: int
    cooldownSeconds: int


class CoursesQuizzesSubmitParamsAnswer(TypedDict, total=False):
    questionId: str
    selected: List[int]


class CoursesQuizzesSubmitParams(TypedDict, total=False):
    answers: List["CoursesQuizzesSubmitParamsAnswer"]


class DocsCollectionsListResponse(TypedDict, total=False):
    collections: List["CollectionSummary"]
    page: "PageInfo"


class DocsCollectionsCreateParams(TypedDict, total=False):
    name: str
    slug: str


class DocsCollectionsCreateResponse(TypedDict, total=False):
    collection: "CollectionSummary"
    data: "CollectionSummary"
    warnings: List[str]


class DocsCollectionsGetResponse(TypedDict, total=False):
    collection: "CollectionSummary"


class DocsCollectionsUpdateParams(TypedDict, total=False):
    name: str
    slug: str


class DocsCollectionsUpdateResponse(TypedDict, total=False):
    collection: "CollectionSummary"
    warnings: List[str]


class DocsCollectionsRemoveResponse(TypedDict, total=False):
    ok: bool
    pages: float


class DocsCollectionsReorderParams(TypedDict, total=False):
    ids: List[str]


class DocsCollectionsReorderResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class DocsCollectionsPagesResponse(TypedDict, total=False):
    pages: List["PageNode"]
    page: "PageInfo"


class DocsPagesCreateParams(TypedDict, total=False):
    preset: Optional[str]
    title: str
    slug: str
    parentId: Optional[str]
    content: "BlockDoc"
    sections: Dict[str, Any]
    body: str
    params: Dict[str, Any]
    versionKey: str
    locale: str
    onSlugTaken: str


class DocsPagesCreateResponsePage(TypedDict, total=False):
    id: str
    slug: str
    title: str


class DocsPagesCreateResponseSlugChanged(TypedDict, total=False):
    asked: str
    used: str


class DocsPagesCreateResponseData(TypedDict, total=False):
    id: str
    slug: str
    title: str


class DocsPagesCreateResponse(TypedDict, total=False):
    page: "DocsPagesCreateResponsePage"
    slugChanged: "DocsPagesCreateResponseSlugChanged"
    warnings: List[str]
    data: "DocsPagesCreateResponseData"


class DocsPagesGetResponse(TypedDict, total=False):
    page: "PageDetail"


class DocsPagesUpdateParams(TypedDict, total=False):
    slug: str
    title: str
    onSlugTaken: str


class DocsPagesUpdateResponseSlugChanged(TypedDict, total=False):
    asked: str
    used: str


class DocsPagesUpdateResponse(TypedDict, total=False):
    ok: bool
    slug: str
    slugChanged: "DocsPagesUpdateResponseSlugChanged"
    warnings: List[str]


class DocsPagesRemoveResponse(TypedDict, total=False):
    ok: bool


class DocsPagesGetMetadataResponse(TypedDict, total=False):
    metadata: Dict[str, Any]


class DocsPagesSetMetadataParamsAudience(TypedDict, total=False):
    claim: str
    equals: str
    condition: str


class DocsPagesSetMetadataParamsThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class DocsPagesSetMetadataParamsThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class DocsPagesSetMetadataParamsThemeLayout(TypedDict, total=False):
    measure: str


class DocsPagesSetMetadataParamsThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class DocsPagesSetMetadataParamsThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class DocsPagesSetMetadataParamsThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class DocsPagesSetMetadataParamsThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class DocsPagesSetMetadataParamsThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class DocsPagesSetMetadataParamsThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class DocsPagesSetMetadataParamsThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class DocsPagesSetMetadataParamsThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class DocsPagesSetMetadataParamsThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class DocsPagesSetMetadataParamsThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "DocsPagesSetMetadataParamsThemeComponentsFocus"
    code: "DocsPagesSetMetadataParamsThemeComponentsCode"
    input: "DocsPagesSetMetadataParamsThemeComponentsInput"
    button: "DocsPagesSetMetadataParamsThemeComponentsButton"
    spacing: "DocsPagesSetMetadataParamsThemeComponentsSpacing"
    selection: "DocsPagesSetMetadataParamsThemeComponentsSelection"
    scrollbar: "DocsPagesSetMetadataParamsThemeComponentsScrollbar"
    syntax: "DocsPagesSetMetadataParamsThemeComponentsSyntax"
    syntaxDark: "DocsPagesSetMetadataParamsThemeComponentsSyntaxDark"


class DocsPagesSetMetadataParamsThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class DocsPagesSetMetadataParamsThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class DocsPagesSetMetadataParamsThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class DocsPagesSetMetadataParamsThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class DocsPagesSetMetadataParamsThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class DocsPagesSetMetadataParamsThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["DocsPagesSetMetadataParamsThemeMotionKeyframeStep"]


class DocsPagesSetMetadataParamsThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "DocsPagesSetMetadataParamsThemeMotionReveal"
    hover: "DocsPagesSetMetadataParamsThemeMotionHover"
    header: "DocsPagesSetMetadataParamsThemeMotionHeader"
    ambient: "DocsPagesSetMetadataParamsThemeMotionAmbient"
    keyframes: List["DocsPagesSetMetadataParamsThemeMotionKeyframe"]
    targets: Dict[str, Any]


class DocsPagesSetMetadataParamsTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "DocsPagesSetMetadataParamsThemePalette"
    paletteDark: "DocsPagesSetMetadataParamsThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "DocsPagesSetMetadataParamsThemeLayout"
    components: "DocsPagesSetMetadataParamsThemeComponents"
    motion: "DocsPagesSetMetadataParamsThemeMotion"


class DocsPagesSetMetadataParams(TypedDict, total=False):
    coverUrl: Any
    icon: str
    hideFromNav: bool
    layout: str
    onThisPage: Optional[str]
    seoTitle: str
    seoDescription: str
    noindex: bool
    contentLanguage: Optional[Any]
    canonicalUrl: Any
    externalUrl: Any
    tags: List[str]
    audience: Optional["DocsPagesSetMetadataParamsAudience"]
    fields: Dict[str, Any]
    customCss: Optional[str]
    theme: Optional["DocsPagesSetMetadataParamsTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class DocsPagesSetMetadataResponse(TypedDict, total=False):
    metadata: Dict[str, Any]
    warnings: List[str]


class DocsPagesReorderParams(TypedDict, total=False):
    parentId: Optional[str]
    afterId: Optional[str]
    collectionId: str


class DocsPagesReorderResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class DocsPagesListResponse(TypedDict, total=False):
    page: "PageInfo"
    pages: List["PageListRow"]


class DocsPagesInventoryResponse(TypedDict, total=False):
    page: "PageInfo"
    pages: List["PageInventoryRow"]


class DocsPagesBulkDeleteParams(TypedDict, total=False):
    ids: List[str]
    collectionId: str


class DocsPagesBulkDeleteResponse(TypedDict, total=False):
    deleted: float
    warnings: List[str]


class DocsPagesBulkMoveParams(TypedDict, total=False):
    ids: List[str]
    collectionId: str
    parentId: Optional[str]


class DocsPagesBulkMoveResponse(TypedDict, total=False):
    moved: float
    warnings: List[str]


class DocsPagesDuplicateParams(TypedDict, total=False):
    title: str
    slug: str
    collectionId: str
    parentId: Optional[str]


class DocsPagesDuplicateResponsePage(TypedDict, total=False):
    id: str
    slug: str
    status: str
    title: str


class DocsPagesDuplicateResponse(TypedDict, total=False):
    page: "DocsPagesDuplicateResponsePage"
    warnings: List[str]


class DocsPagesTrashResponse(TypedDict, total=False):
    page: "PageInfo"
    pages: List["PageTrashRow"]


class DocsPagesEmptyTrashResponse(TypedDict, total=False):
    purged: float


class DocsPagesRestoreResponse(TypedDict, total=False):
    detached: bool
    ok: bool
    reattachedChildren: float
    renamedFrom: Any
    slug: str


class DocsPagesUnpublishResponse(TypedDict, total=False):
    pageId: str
    status: str


class DocsPagesPurgeResponse(TypedDict, total=False):
    ok: bool


class DocsPagesRevisionsSaveParams(TypedDict, total=False):
    title: str
    content: "BlockDoc"
    body: str
    changeRequestId: Optional[str]


class DocsPagesRevisionsSaveResponse(TypedDict, total=False):
    revision: "RevisionSummary"
    warnings: List[str]


class DocsPagesRevisionsPutSectionParams(TypedDict, total=False):
    markdown: str


class DocsPagesRevisionsPutSectionResponse(TypedDict, total=False):
    conformance: "Conformance"
    warnings: List[str]


class DocsPagesRevisionsSetShapeParams(TypedDict, total=False):
    preset: Optional[str]


class DocsPagesRevisionsSetShapeResponse(TypedDict, total=False):
    preset: Any
    warnings: List[str]


class DocsPagesRevisionsHistoryResponse(TypedDict, total=False):
    revisions: List["RevisionSummary"]
    page: "PageInfo"


class DocsPagesRevisionsCheckpointsResponse(TypedDict, total=False):
    checkpoints: List["SnapshotSummary2"]
    definition: str


class DocsPagesRevisionsCheckpointResponse(TypedDict, total=False):
    content: Any
    title: str


class DocsPagesRevisionsRestoreCheckpointResponse(TypedDict, total=False):
    revision: "RevisionSummary"


class DocsPagesPublishParams(TypedDict, total=False):
    editorial: bool
    editorialNote: str


class DocsPagesPublishResponse(TypedDict, total=False):
    revision: "RevisionSummary"
    warnings: List[str]


class DocsPagesRevisionsGetScheduleResponse(TypedDict, total=False):
    schedule: Optional["ScheduleSummary2"]


class DocsPagesSchedulePublishParams(TypedDict, total=False):
    publishAt: str


class DocsPagesSchedulePublishResponse(TypedDict, total=False):
    schedule: "ScheduleSummary2"
    warnings: List[str]


class DocsPagesRevisionsCancelScheduleResponse(TypedDict, total=False):
    ok: bool


class DocsPagesRollbackParams(TypedDict, total=False):
    revisionId: str
    mode: str


class DocsPagesRollbackResponse(TypedDict, total=False):
    revision: "RevisionSummary"
    warnings: List[str]


class SpacesPublishAllResponse(TypedDict, total=False):
    published: float
    data: float


class DocsChangeRequestsAgentReviewResponse(TypedDict, total=False):
    comments: float
    findings: List["Finding"]


class DocsChangeRequestsAgentRunParams(TypedDict, total=False):
    instruction: str


class DocsChangeRequestsListResponse(TypedDict, total=False):
    changeRequests: List["ChangeRequestSummary"]
    page: "PageInfo"


class DocsChangeRequestsCreateParams(TypedDict, total=False):
    title: str


class DocsChangeRequestsCreateResponse(TypedDict, total=False):
    changeRequest: "ChangeRequestSummary"
    data: "ChangeRequestSummary"
    warnings: List[str]


class DocsChangeRequestsMergeRulesResponse(TypedDict, total=False):
    rules: "MergeRules"


class DocsChangeRequestsSetMergeRulesParams(TypedDict, total=False):
    requiredApprovals: int
    requireAllReviewers: bool
    blockOnChangesRequested: bool


class DocsChangeRequestsSetMergeRulesResponse(TypedDict, total=False):
    rules: "MergeRules"
    warnings: List[str]


class DocsChangeRequestsMergeBlockersResponse(TypedDict, total=False):
    blockers: List[str]
    page: "PageInfo"


class DocsChangeRequestsConflictsResponse(TypedDict, total=False):
    conflicts: List["ConflictDetail"]
    page: "PageInfo"


class DocsChangeRequestsEligibilityResponse(TypedDict, total=False):
    canPropose: bool
    requiredLevel: float
    trustLevel: float
    via: Any


class DocsChangeRequestsPagesResponsePage(TypedDict, total=False):
    pageId: str
    revisionId: str
    slug: str
    spaceId: str
    title: str


class DocsChangeRequestsPagesResponse(TypedDict, total=False):
    pages: List["DocsChangeRequestsPagesResponsePage"]
    page: "PageInfo"


class DocsChangeRequestsRequestReviewResponse(TypedDict, total=False):
    changeRequest: "ChangeRequestSummary"


class DocsChangeRequestsApproveResponse(TypedDict, total=False):
    changeRequest: "ChangeRequestSummary"


class DocsChangeRequestsMergeParams(TypedDict, total=False):
    force: bool


class DocsChangeRequestsMergeResponse(TypedDict, total=False):
    mergedPages: float
    warnings: List[str]


class DocsChangeRequestsRebaseResponse(TypedDict, total=False):
    rebased: float


class DocsChangeRequestsListReviewersResponseReviewer(TypedDict, total=False):
    status: str
    userId: str


class DocsChangeRequestsListReviewersResponse(TypedDict, total=False):
    reviewers: List["DocsChangeRequestsListReviewersResponseReviewer"]
    page: "PageInfo"


class DocsChangeRequestsAddReviewersParams(TypedDict, total=False):
    userIds: List[str]


class DocsChangeRequestsAddReviewersResponseReviewer(TypedDict, total=False):
    status: str
    userId: str


class DocsChangeRequestsAddReviewersResponse(TypedDict, total=False):
    reviewers: List["DocsChangeRequestsAddReviewersResponseReviewer"]
    warnings: List[str]


class DocsChangeRequestsRemoveReviewerResponse(TypedDict, total=False):
    ok: bool


class DocsChangeRequestsReviewParams(TypedDict, total=False):
    verdict: str


class DocsChangeRequestsReviewResponse(TypedDict, total=False):
    changeRequest: "ChangeRequestSummary"
    warnings: List[str]


class DocsChangeRequestsCloseResponse(TypedDict, total=False):
    changeRequest: "ChangeRequestSummary"


class DocsChangeRequestsCommentsResponse(TypedDict, total=False):
    comments: List["ChangeRequestCommentRow"]
    page: "PageInfo"


class DocsChangeRequestsCommentParamsAnchor(TypedDict, total=False):
    blockIndex: int
    quote: str


class DocsChangeRequestsCommentParams(TypedDict, total=False):
    body: str
    pageId: Optional[str]
    parentCommentId: Optional[str]
    anchor: Optional["DocsChangeRequestsCommentParamsAnchor"]


class DocsChangeRequestsCommentResponse(TypedDict, total=False):
    comment: "ChangeRequestCommentCreated"
    data: "ChangeRequestCommentCreated"
    warnings: List[str]


class DocsReusablesListReusableResponse(TypedDict, total=False):
    reusables: List["ReusableSummary"]
    page: "PageInfo"


class DocsReusablesCreateReusableParams(TypedDict, total=False):
    name: str
    content: Any


class DocsReusablesCreateReusableResponse(TypedDict, total=False):
    reusable: "ReusableSummary"
    data: "ReusableSummary"
    warnings: List[str]


class DocsReusablesUpdateReusableParams(TypedDict, total=False):
    name: str
    content: Any


class DocsReusablesUpdateReusableResponse(TypedDict, total=False):
    reusable: "ReusableSummary"
    warnings: List[str]


class DocsReusablesDeleteReusableResponse(TypedDict, total=False):
    ok: bool


class DocsReusablesListVariablesResponse(TypedDict, total=False):
    variables: List["VariableRow"]
    page: "PageInfo"


class DocsReusablesSetVariableParams(TypedDict, total=False):
    key: str
    value: str
    type: str


class DocsReusablesSetVariableResponse(TypedDict, total=False):
    variable: "VariableRow"
    warnings: List[str]


class DocsReusablesDeleteVariableResponse(TypedDict, total=False):
    ok: bool


class DocsSearchResponse(TypedDict, total=False):
    hits: List["SearchHit"]
    minQueryLength: float


class DocsAnalyticsTagsResponseTag(TypedDict, total=False):
    count: float
    tag: str


class DocsAnalyticsTagsResponse(TypedDict, total=False):
    tags: List["DocsAnalyticsTagsResponseTag"]
    page: "PageInfo"


class DocsAnalyticsTagPagesResponsePage(TypedDict, total=False):
    id: str
    slug: str
    title: str


class DocsAnalyticsTagPagesResponse(TypedDict, total=False):
    pages: List["DocsAnalyticsTagPagesResponsePage"]
    page: "PageInfo"


class DocsAnalyticsCheckLinksResponse(TypedDict, total=False):
    broken: List["BrokenLink"]


class DocsAnalyticsEmptySectionsResponseSection(TypedDict, total=False):
    heading: str
    level: float
    pageId: str
    pageSlug: str


class DocsAnalyticsEmptySectionsResponse(TypedDict, total=False):
    sections: List["DocsAnalyticsEmptySectionsResponseSection"]
    page: "PageInfo"


class DocsAnalyticsOrphansResponseOrphan(TypedDict, total=False):
    pageId: str
    slug: str
    title: str


class DocsAnalyticsOrphansResponse(TypedDict, total=False):
    definition: str
    orphans: List["DocsAnalyticsOrphansResponseOrphan"]


class DocsAnalyticsBacklinksResponse(TypedDict, total=False):
    backlinks: List["Backlink"]
    page: "PageInfo"


class DocsAnalyticsStaleResponseStaleItem(TypedDict, total=False):
    ageDays: float
    pageId: str
    slug: str
    title: str
    updatedAt: str


class DocsAnalyticsStaleResponse(TypedDict, total=False):
    stale: List["DocsAnalyticsStaleResponseStaleItem"]
    page: "PageInfo"


class DocsVersionsListResponse(TypedDict, total=False):
    versions: List["DocVersion"]
    page: "PageInfo"


class DocsVersionsCreateParams(TypedDict, total=False):
    key: str
    label: str
    fromVersion: str


class DocsVersionsCreateResponse(TypedDict, total=False):
    versions: List["DocVersion"]
    warnings: List[str]


class DocsVersionsRemoveResponse(TypedDict, total=False):
    versions: List["DocVersion"]


class DocsTranslationsListResponse(TypedDict, total=False):
    locales: List["DocLocale"]
    page: "PageInfo"


class DocsTranslationsCreateParams(TypedDict, total=False):
    code: str
    label: str


class DocsTranslationsCreateResponse(TypedDict, total=False):
    locales: List["DocLocale"]
    warnings: List[str]


class DocsTranslationsRemoveResponse(TypedDict, total=False):
    locales: List["DocLocale"]


class DocsOpenapiListSpecsResponse(TypedDict, total=False):
    specs: List["StoredSpecSummary"]
    page: "PageInfo"


class DocsOpenapiRegisterSpecParams(TypedDict, total=False):
    sourceUrl: str
    url: str
    name: str
    collectionId: str
    mode: str
    slugPrefix: str
    includeTags: List[str]
    excludeTags: List[str]
    onExisting: str


class DocsOpenapiRegisterSpecResponse(TypedDict, total=False):
    spec: "StoredSpecSummary"
    data: "StoredSpecSummary"
    warnings: List[str]


class DocsOpenapiResyncSpecParams(TypedDict, total=False):
    collectionId: str
    title: str
    mode: str
    slugPrefix: str
    includeTags: List[str]
    excludeTags: List[str]
    onExisting: str
    background: bool


class DocsOpenapiResyncStatusResponse(TypedDict, total=False):
    jobId: str
    result: Optional["ResyncOpenApiResult"]
    state: str


class DocsOpenapiSpecReferenceResponseGroup(TypedDict, total=False):
    operations: List["OpenApiOperation"]
    tag: str


class DocsOpenapiSpecReferenceResponse(TypedDict, total=False):
    groups: List["DocsOpenapiSpecReferenceResponseGroup"]
    lastSyncedAt: Any
    title: str


class DocsOpenapiRemoveSpecResponse(TypedDict, total=False):
    ok: bool


class DocsOpenapiSdkLanguagesResponseLanguage(TypedDict, total=False):
    id: str
    label: str


class DocsOpenapiSdkLanguagesResponse(TypedDict, total=False):
    languages: List["DocsOpenapiSdkLanguagesResponseLanguage"]
    page: "PageInfo"


class DocsOpenapiSpecSdkResponse(TypedDict, total=False):
    file: "SdkFile"


class DocsOpenapiSpecLintResponse(TypedDict, total=False):
    report: "LintReport"


class DocsOpenapiLintUrlParams(TypedDict, total=False):
    sourceUrl: str


class DocsOpenapiLintUrlResponse(TypedDict, total=False):
    report: "LintReport"
    warnings: List[str]


class DocsOpenapiOperationsParams(TypedDict, total=False):
    url: str


class DocsOpenapiOperationsResponseOperation(TypedDict, total=False):
    method: str
    path: str
    summary: str


class DocsOpenapiOperationsResponse(TypedDict, total=False):
    operations: List["DocsOpenapiOperationsResponseOperation"]
    warnings: List[str]


class DocsOpenapiResolveParams(TypedDict, total=False):
    url: str
    method: str
    path: str


class DocsOpenapiResolveResponse(TypedDict, total=False):
    operation: "OpenApiOperation"
    warnings: List[str]


class DocsOpenapiGenerateParamsEnhance(TypedDict, total=False):
    prose: bool
    diagrams: bool


class DocsOpenapiGenerateParams(TypedDict, total=False):
    url: str
    sourceUrl: str
    spec: Any
    collectionId: str
    enhance: "DocsOpenapiGenerateParamsEnhance"


class DocsOpenapiGenerateResponsePage(TypedDict, total=False):
    id: str
    slug: str
    title: str


class DocsOpenapiGenerateResponse(TypedDict, total=False):
    generated: float
    jobId: str
    pages: List["DocsOpenapiGenerateResponsePage"]
    updated: float
    warnings: List[str]


class DocsOpenapiGenerateStatusResponse(TypedDict, total=False):
    jobId: str
    result: Optional["GenerateResult"]
    state: str


class DocsOpenapiImportParams(TypedDict, total=False):
    url: str
    sourceUrl: str
    spec: Any
    collectionId: str
    title: str
    mode: str
    slugPrefix: str
    replaceCollection: bool
    dryRun: bool
    includeTags: List[str]
    excludeTags: List[str]
    onExisting: str
    specId: str


class DocsOpenapiImportFileParams(TypedDict, total=False):
    collectionId: str
    title: str
    mode: str
    slugPrefix: str
    replaceCollection: bool
    dryRun: bool
    includeTags: str
    excludeTags: str
    onExisting: str


class PublicOpenapiForwardParams(TypedDict, total=False):
    targetUrl: str
    method: str
    headers: Dict[str, Any]
    body: str


class PublicOpenapiForwardResponse(TypedDict, total=False):
    response: "ProxyResponse"
    data: "ProxyResponse"
    warnings: List[str]


class PublicOpenapiLanguagesResponseLanguage(TypedDict, total=False):
    id: str
    label: str


class PublicOpenapiLanguagesResponse(TypedDict, total=False):
    languages: List["PublicOpenapiLanguagesResponseLanguage"]
    page: "PageInfo"


class PublicOpenapiDownloadResponse(TypedDict, total=False):
    file: "SdkFile"


class SdksListRegistriesResponse(TypedDict, total=False):
    registries: List["RegistryTokenStatus"]
    page: "PageInfo"


class SdksSetRegistryParams(TypedDict, total=False):
    token: str
    settings: Dict[str, Any]


class SdksSetRegistryResponse(TypedDict, total=False):
    registry: "RegistryTokenStatus"
    warnings: List[str]


class SdksDeleteRegistryResponse(TypedDict, total=False):
    ok: bool


class SdksTestRegistryResponse(TypedDict, total=False):
    error: str
    ok: bool


class SdksRegisterPackageParams(TypedDict, total=False):
    packageName: str
    config: Dict[str, Any]


class SdksRegisterPackageResponsePackage(TypedDict, total=False):
    id: str
    language: str
    packageName: str


class SdksRegisterPackageResponse(TypedDict, total=False):
    package: "SdksRegisterPackageResponsePackage"
    warnings: List[str]


class SdksListPackagesResponse(TypedDict, total=False):
    packages: List[Any]
    page: "PageInfo"


class SdksPublishParams(TypedDict, total=False):
    target: str


class SdksPublishResponsePublish(TypedDict, total=False):
    id: str
    status: str


class SdksPublishResponse(TypedDict, total=False):
    publish: "SdksPublishResponsePublish"
    warnings: List[str]


class SdksListPublishesResponse(TypedDict, total=False):
    publishes: List[Any]
    page: "PageInfo"


class ModerationContentRulesListResponse(TypedDict, total=False):
    rules: List["ContentRule"]
    page: "PageInfo"


class ModerationContentRulesCreateParams(TypedDict, total=False):
    pattern: str
    isRegex: bool
    message: str
    severity: str


class ModerationContentRulesCreateResponse(TypedDict, total=False):
    rule: "ContentRule"
    data: "ContentRule"
    warnings: List[str]


class ModerationContentRulesRemoveResponse(TypedDict, total=False):
    ok: bool


class DocsPagesCollabTokenResponse(TypedDict, total=False):
    room: str
    token: str
    url: str


class DocsPagesCollabStateResponse(TypedDict, total=False):
    state: Any


class DocsCommentsListResponse(TypedDict, total=False):
    comments: List["CommentSummary"]
    page: "PageInfo"


class DocsCommentsModerateParams(TypedDict, total=False):
    status: str


class DocsCommentsModerateResponse(TypedDict, total=False):
    comment: "CommentSummary"
    warnings: List[str]


class DocsCommentsRemoveResponse(TypedDict, total=False):
    ok: bool


class DocsCommentsResolveParams(TypedDict, total=False):
    resolved: bool


class DocsCommentsResolveResponse(TypedDict, total=False):
    comment: "CommentSummary"
    warnings: List[str]


class DocsCommentsApplySuggestionResponse(TypedDict, total=False):
    comment: "CommentSummary"


class DocsImportsDedupeTitlesParams(TypedDict, total=False):
    dryRun: bool


class DocsImportsImportFilesParamsFile(TypedDict, total=False):
    name: str
    content: str


class DocsImportsImportFilesParams(TypedDict, total=False):
    files: List["DocsImportsImportFilesParamsFile"]
    collection: str
    collectionId: str
    replaceCollection: bool
    onExisting: str
    prune: str
    dryRun: bool


class DocsImportsImportZipParams(TypedDict, total=False):
    file: str


class DocsImportsImportUrlParams(TypedDict, total=False):
    url: str
    branch: str
    collection: str
    onExisting: str
    prune: str
    dryRun: bool


class DocsImportsImportDocxParams(TypedDict, total=False):
    file: str


class IntegrationsDeeplStatusResponse(TypedDict, total=False):
    configured: bool


class IntegrationsDeeplSetKeyParams(TypedDict, total=False):
    apiKey: str


class IntegrationsDeeplSetKeyResponse(TypedDict, total=False):
    configured: bool
    warnings: List[str]


class IntegrationsDeeplClearResponse(TypedDict, total=False):
    ok: bool


class SpacesShareLinksListResponse(TypedDict, total=False):
    links: List["ShareLinkSummary"]
    page: "PageInfo"


class SpacesShareLinksCreateParams(TypedDict, total=False):
    label: str


class SpacesShareLinksCreateResponse(TypedDict, total=False):
    id: str
    token: str
    warnings: List[str]


class SpacesShareLinksPreviewResponse(TypedDict, total=False):
    id: str
    token: str


class SpacesShareLinksRevokeResponse(TypedDict, total=False):
    ok: bool


class LibraryListResponse(TypedDict, total=False):
    reusables: List["ReusableSummary"]
    page: "PageInfo"


class LibraryCreateParams(TypedDict, total=False):
    name: str
    content: Any


class LibraryCreateResponse(TypedDict, total=False):
    reusable: "ReusableSummary"
    data: "ReusableSummary"
    warnings: List[str]


class LibraryRemoveResponse(TypedDict, total=False):
    ok: bool


class LibraryListVariablesResponse(TypedDict, total=False):
    variables: List["VariableRow"]
    page: "PageInfo"


class LibrarySetVariableParams(TypedDict, total=False):
    key: str
    value: str
    type: str


class LibrarySetVariableResponse(TypedDict, total=False):
    variable: "VariableRow"
    warnings: List[str]


class LibraryDeleteVariableResponse(TypedDict, total=False):
    ok: bool


class SpacesSnapshotsListResponse(TypedDict, total=False):
    snapshots: List["SnapshotSummary"]
    page: "PageInfo"


class SpacesSnapshotsCreateParams(TypedDict, total=False):
    label: str


class SpacesSnapshotsCreateResponse(TypedDict, total=False):
    snapshot: "SnapshotSummary"
    data: "SnapshotSummary"
    warnings: List[str]


class SpacesSnapshotsRestoreParams(TypedDict, total=False):
    newPages: str


class SpacesSnapshotsRestoreResponse(TypedDict, total=False):
    addedSince: float
    restored: float
    skipped: float
    unpublished: float
    warnings: List[str]


class SpacesSnapshotsRemoveResponse(TypedDict, total=False):
    ok: bool


class TemplatesListResponseTemplate(TypedDict, total=False):
    description: str
    key: str
    name: str


class TemplatesListResponse(TypedDict, total=False):
    templates: List["TemplatesListResponseTemplate"]
    page: "PageInfo"


class DocsTemplatesListResponse(TypedDict, total=False):
    templates: List["TemplateSummary"]
    page: "PageInfo"


class DocsTemplatesSaveParams(TypedDict, total=False):
    name: str
    content: Any
    orgWide: bool


class DocsTemplatesSaveResponse(TypedDict, total=False):
    template: "TemplateSummary"
    data: "TemplateSummary"
    warnings: List[str]


class DocsTemplatesRemoveResponse(TypedDict, total=False):
    ok: bool


class DocsTemplatesNewPageParams(TypedDict, total=False):
    collectionId: str
    title: str
    slug: str


class DocsTemplatesNewPageResponsePage(TypedDict, total=False):
    id: str


class DocsTemplatesNewPageResponseData(TypedDict, total=False):
    id: str


class DocsTemplatesNewPageResponse(TypedDict, total=False):
    page: "DocsTemplatesNewPageResponsePage"
    data: "DocsTemplatesNewPageResponseData"
    warnings: List[str]


class WebhooksEventsResponseCatalogItem(TypedDict, total=False):
    event: str
    item: Any
    means: str
    subscribe: bool


class WebhooksEventsResponse(TypedDict, total=False):
    catalog: List["WebhooksEventsResponseCatalogItem"]
    events: List[str]


class WebhooksListResponse(TypedDict, total=False):
    page: "PageInfo"
    webhooks: List["WebhookSummary"]


class WebhooksCreateParams(TypedDict, total=False):
    url: str
    events: List[str]
    spaceId: Optional[str]
    format: str
    categoryIds: Optional[List[str]]
    tagIds: Optional[List[str]]
    groupIds: Optional[List[str]]
    bodyEncoding: str
    signatureVersion: str


class WebhooksCreateResponse(TypedDict, total=False):
    secret: str
    webhook: "WebhookSummary"
    data: "WebhookSummary"
    warnings: List[str]


class WebhooksUpdateParams(TypedDict, total=False):
    url: str
    events: List[str]
    active: bool
    spaceId: Optional[str]
    categoryIds: Optional[List[str]]
    tagIds: Optional[List[str]]
    groupIds: Optional[List[str]]
    bodyEncoding: str
    signatureVersion: str


class WebhooksUpdateResponse(TypedDict, total=False):
    webhook: "WebhookSummary"
    warnings: List[str]


class WebhooksRemoveResponse(TypedDict, total=False):
    ok: bool


class WebhooksDeliveriesResponseDelivery(TypedDict, total=False):
    attempts: Any
    completedAt: Any
    createdAt: Any
    error: Any
    event: Any
    id: Any
    organizationId: Any
    payload: Any
    status: Any
    statusCode: Any
    webhookId: Any


class WebhooksDeliveriesResponse(TypedDict, total=False):
    deliveries: List["WebhooksDeliveriesResponseDelivery"]
    page: "PageInfo"


class WebhooksRotateParams(TypedDict, total=False):
    overlapHours: int


class WebhooksRotateResponse(TypedDict, total=False):
    previousValidUntil: str
    secret: str
    warnings: List[str]


class NotificationsGetDndResponse(TypedDict, total=False):
    dnd: "DndSummary"


class NotificationsSetDndParams(TypedDict, total=False):
    endsAt: Optional[str]
    dailyStart: Optional[int]
    dailyEnd: Optional[int]
    timezone: str


class NotificationsSetDndResponse(TypedDict, total=False):
    dnd: "DndSummary"
    warnings: List[str]


class NotificationsSnoozeDndParams(TypedDict, total=False):
    minutes: int


class NotificationsSnoozeDndResponse(TypedDict, total=False):
    dnd: "DndSummary"
    warnings: List[str]


class NotificationsGetScheduleResponse(TypedDict, total=False):
    schedule: "ScheduleSummary"


class NotificationsSetScheduleParams(TypedDict, total=False):
    enabled: bool
    timezone: str
    days: Dict[str, Any]


class NotificationsSetScheduleResponse(TypedDict, total=False):
    schedule: "ScheduleSummary"
    warnings: List[str]


class NotificationsSetTypePreferencesParamsPreference(TypedDict, total=False):
    type: str
    inApp: bool
    email: bool


class NotificationsSetTypePreferencesParams(TypedDict, total=False):
    preferences: List["NotificationsSetTypePreferencesParamsPreference"]


class NotificationsGetPreferencesResponse(TypedDict, total=False):
    preferences: "PrefsSummary"


class NotificationsSetPreferencesParams(TypedDict, total=False):
    deliverEmail: str
    mutedTypes: List[str]
    deliverPush: str
    pushMutedTypes: List[str]
    quietStart: Optional[int]
    quietEnd: Optional[int]
    timezone: str
    digestHour: int
    communitySummary: bool
    mailingListMode: str
    messagesFrom: str


class NotificationsSetPreferencesResponse(TypedDict, total=False):
    preferences: "PrefsSummary"
    warnings: List[str]


class NotificationsListResponse(TypedDict, total=False):
    notifications: List["NotificationSummary"]
    page: "PageInfo"
    unread: float


class NotificationsReadResponse(TypedDict, total=False):
    ok: bool


class NotificationsReadAllResponse(TypedDict, total=False):
    ok: bool


class NotificationsPushPublicKeyResponse(TypedDict, total=False):
    enabled: bool
    publicKey: Any


class NotificationsPushStatusResponse(TypedDict, total=False):
    enabled: bool
    subscriptions: float


class NotificationsPushSubscribeParamsKeys(TypedDict, total=False):
    p256dh: str
    auth: str


class NotificationsPushSubscribeParams(TypedDict, total=False):
    endpoint: str
    keys: "NotificationsPushSubscribeParamsKeys"


class NotificationsPushSubscribeResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class NotificationsPushUnsubscribeParams(TypedDict, total=False):
    endpoint: str


class NotificationsPushUnsubscribeResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class MailUnsubscribeOneClickResponse(TypedDict, total=False):
    ok: bool


class MailListResponse(TypedDict, total=False):
    suppressions: List["SuppressionRow"]
    page: "PageInfo"


class MailSuppressParams(TypedDict, total=False):
    email: str


class MailSuppressResponse(TypedDict, total=False):
    ok: bool
    suppression: Optional["SuppressionRow"]
    warnings: List[str]


class MailUnsuppressResponse(TypedDict, total=False):
    ok: bool


class MailLogResponse(TypedDict, total=False):
    log: List["MailLogRow"]
    page: "PageInfo"


class MailCheckResponse(TypedDict, total=False):
    suppressed: bool


class MailProviderConnectParams(TypedDict, total=False):
    provider: str
    apiKey: str
    domain: str
    region: str


class MailProviderConnectResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class MailProviderDisconnectResponse(TypedDict, total=False):
    ok: bool


class MailProviderTestParams(TypedDict, total=False):
    to: str


MailProviderTestResponse = TypedDict("MailProviderTestResponse", {"from": str, "ok": bool, "warnings": List[str]}, total=False)


class OrgsSettingsListResponse(TypedDict, total=False):
    settings: List["SettingView"]
    page: "PageInfo"


class OrgsSettingsSetParams(TypedDict, total=False):
    value: Any


class OrgsSettingsSetResponse(TypedDict, total=False):
    setting: "SettingView"
    warnings: List[str]


class OrgsSettingsResetResponse(TypedDict, total=False):
    setting: "SettingView"


class SpacesAssetsListResponse(TypedDict, total=False):
    assets: List["UploadedAsset"]
    page: "PageInfo"


class SpacesAssetsUploadParams(TypedDict, total=False):
    file: str


class SpacesAssetsUploadResponse(TypedDict, total=False):
    asset: "UploadedAsset"
    data: "UploadedAsset"
    warnings: List[str]


class SpacesAssetsCatalogResponse(TypedDict, total=False):
    assets: List["CatalogedAsset"]
    page: "PageInfo"
    totalBytes: float


class SpacesAssetsRemoveResponse(TypedDict, total=False):
    ok: bool


class SpacesDomainsAddParams(TypedDict, total=False):
    hostname: str
    basePath: str


class SpacesDomainsAllocateSubdomainParams(TypedDict, total=False):
    subdomain: str


class SpacesDomainsSetAcmeChallengeParams(TypedDict, total=False):
    hostname: str
    token: str
    keyAuthorization: str


class SpacesDomainsSetAcmeChallengeResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class SpacesDomainsVerifyParams(TypedDict, total=False):
    activate: bool


class SpacesDomainsPreviewParams(TypedDict, total=False):
    hostname: str
    basePath: str


class SpacesDomainsRemoveResponse(TypedDict, total=False):
    ok: bool


class SpacesDomainsSetIpAllowListParams(TypedDict, total=False):
    ipAllowList: List[str]


class SpacesDomainsSetIpAllowListResponse(TypedDict, total=False):
    ipAllowList: List[str]
    warnings: List[str]


class SpacesDomainsSetRedirectParams(TypedDict, total=False):
    redirectTo: Optional[str]


class SpacesDomainsSetRedirectResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class PublicDomainsPrimaryResponse(TypedDict, total=False):
    primary: Any


class PublicDomainsResolveResponse(TypedDict, total=False):
    mounts: List[str]
    site: Any
    space: Any


class SpacesAddressesListResponse(TypedDict, total=False):
    addresses: List["SpaceAddress"]
    sitemapUrl: str


class IntegrationsCloudflareSetParams(TypedDict, total=False):
    token: str
    enabled: bool
    zoneMode: str


class IntegrationsCloudflareClearResponse(TypedDict, total=False):
    ok: bool


class IntegrationsCloudflareTestResponse(TypedDict, total=False):
    checkedHost: str
    error: str
    ok: bool
    status: str


class ForumAutomationsListResponse(TypedDict, total=False):
    automations: List["AutomationSummary"]
    page: "PageInfo"


class ForumAutomationsCreateParamsCondition(TypedDict, total=False):
    field: str
    op: str
    value: Any


class ForumAutomationsCreateParams(TypedDict, total=False):
    spaceId: Optional[str]
    name: str
    enabled: bool
    trigger: str
    conditions: List["ForumAutomationsCreateParamsCondition"]
    action: str
    config: Dict[str, Any]


class ForumAutomationsUpdateParamsCondition(TypedDict, total=False):
    field: str
    op: str
    value: Any


class ForumAutomationsUpdateParams(TypedDict, total=False):
    spaceId: Optional[str]
    name: str
    enabled: bool
    trigger: str
    conditions: List["ForumAutomationsUpdateParamsCondition"]
    action: str
    config: Dict[str, Any]


class ForumAutomationsRemoveResponse(TypedDict, total=False):
    ok: bool


class ForumAutomationsRunsResponse(TypedDict, total=False):
    page: "PageInfo"
    runs: List["AutomationRunSummary"]


class ForumAutomationsInvokeParams(TypedDict, total=False):
    payload: Dict[str, Any]


class BlogNewsletterSubscribersResponse(TypedDict, total=False):
    page: "PageInfo"
    subscribers: List["SubscriberSummary"]


class BlogNewsletterBroadcastsResponse(TypedDict, total=False):
    broadcasts: List["BroadcastSummary"]
    page: "PageInfo"


class BlogNewsletterSendBroadcastParamsSegment(TypedDict, total=False):
    subscribedAfter: str
    subscribedBefore: str
    tags: List[str]


class BlogNewsletterSendBroadcastParams(TypedDict, total=False):
    subject: str
    body: str
    segment: "BlogNewsletterSendBroadcastParamsSegment"


class BlogNewsletterSendBroadcastResponse(TypedDict, total=False):
    broadcast: "BroadcastSummary"
    data: "BroadcastSummary"
    warnings: List[str]


class BlogNewsletterSetSubscriberTagsParams(TypedDict, total=False):
    tags: List[str]


class BlogNewsletterSetSubscriberTagsResponse(TypedDict, total=False):
    subscriber: "SubscriberSummary"
    warnings: List[str]


class BlogNewsletterSubscriberTagsResponse(TypedDict, total=False):
    tags: List[str]
    page: "PageInfo"


class BlogModerationFlagsResponse(TypedDict, total=False):
    flags: List["FlagRow"]
    page: "PageInfo"


class BlogModerationReviewFlagParams(TypedDict, total=False):
    action: str


class BlogModerationReviewFlagResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class BlogModerationResolveFlagParams(TypedDict, total=False):
    action: str


class BlogModerationResolveFlagResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class BlogArticlesListResponse(TypedDict, total=False):
    articles: List["ArticleSummary"]
    page: "PageInfo"


class BlogArticlesCreateParamsByline(TypedDict, total=False):
    name: str
    url: Any
    avatarUrl: Any


class BlogArticlesCreateParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class BlogArticlesCreateParamsSeo(TypedDict, total=False):
    seoTitle: str
    seoDescription: str
    noindex: bool
    canonicalUrl: str
    socialImageUrl: Any


class BlogArticlesCreateParamsFurtherReadingItem(TypedDict, total=False):
    label: str
    href: str


class BlogArticlesCreateParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class BlogArticlesCreateParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class BlogArticlesCreateParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class BlogArticlesCreateParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class BlogArticlesCreateParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class BlogArticlesCreateParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class BlogArticlesCreateParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class BlogArticlesCreateParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class BlogArticlesCreateParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class BlogArticlesCreateParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class BlogArticlesCreateParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class BlogArticlesCreateParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class BlogArticlesCreateParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "BlogArticlesCreateParamsCustomizationThemeComponentsFocus"
    code: "BlogArticlesCreateParamsCustomizationThemeComponentsCode"
    input: "BlogArticlesCreateParamsCustomizationThemeComponentsInput"
    button: "BlogArticlesCreateParamsCustomizationThemeComponentsButton"
    spacing: "BlogArticlesCreateParamsCustomizationThemeComponentsSpacing"
    selection: "BlogArticlesCreateParamsCustomizationThemeComponentsSelection"
    scrollbar: "BlogArticlesCreateParamsCustomizationThemeComponentsScrollbar"
    syntax: "BlogArticlesCreateParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "BlogArticlesCreateParamsCustomizationThemeComponentsSyntaxDark"


class BlogArticlesCreateParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class BlogArticlesCreateParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class BlogArticlesCreateParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class BlogArticlesCreateParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class BlogArticlesCreateParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class BlogArticlesCreateParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["BlogArticlesCreateParamsCustomizationThemeMotionKeyframeStep"]


class BlogArticlesCreateParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "BlogArticlesCreateParamsCustomizationThemeMotionReveal"
    hover: "BlogArticlesCreateParamsCustomizationThemeMotionHover"
    header: "BlogArticlesCreateParamsCustomizationThemeMotionHeader"
    ambient: "BlogArticlesCreateParamsCustomizationThemeMotionAmbient"
    keyframes: List["BlogArticlesCreateParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class BlogArticlesCreateParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "BlogArticlesCreateParamsCustomizationThemePalette"
    paletteDark: "BlogArticlesCreateParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "BlogArticlesCreateParamsCustomizationThemeLayout"
    components: "BlogArticlesCreateParamsCustomizationThemeComponents"
    motion: "BlogArticlesCreateParamsCustomizationThemeMotion"


class BlogArticlesCreateParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["BlogArticlesCreateParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class BlogArticlesCreateParams(TypedDict, total=False):
    title: str
    slug: str
    publishedAt: str
    byline: Optional["BlogArticlesCreateParamsByline"]
    author: Optional[str]
    content: "BlogArticlesCreateParamsContent"
    sections: Dict[str, Any]
    excerpt: str
    coverUrl: Any
    series: Optional[str]
    socialImageUrl: Any
    tags: List[str]
    seo: "BlogArticlesCreateParamsSeo"
    furtherReading: List["BlogArticlesCreateParamsFurtherReadingItem"]
    commentsEnabled: bool
    onThisPage: Optional[str]
    customization: Optional["BlogArticlesCreateParamsCustomization"]
    markdown: str


class BlogArticlesCreateResponse(TypedDict, total=False):
    article: "ArticleDetail"
    warnings: List[str]
    data: "ArticleDetail"


class BlogTagsResponseTag(TypedDict, total=False):
    count: float
    tag: str


class BlogTagsResponse(TypedDict, total=False):
    tags: List["BlogTagsResponseTag"]
    page: "PageInfo"


class BlogSearchResponseHit(TypedDict, total=False):
    slug: str
    snippet: str
    title: str
    topicId: str


class BlogSearchResponse(TypedDict, total=False):
    hits: List["BlogSearchResponseHit"]
    minQueryLength: float


class BlogBookmarksResponse(TypedDict, total=False):
    articles: List["ArticleSummary"]
    page: "PageInfo"


class BlogGetSettingsResponse(TypedDict, total=False):
    settings: "CommunitySettings"


class BlogUpdateSettingsParams(TypedDict, total=False):
    whoCanPost: Optional[str]
    moderateComments: Optional[bool]
    moderateAnonymous: Optional[bool]
    allowAnonymous: Optional[bool]
    anonymousCaptcha: Optional[str]
    defaultSort: Optional[str]
    reactionsEnabled: Optional[bool]
    defaultByline: Optional[str]


class BlogUpdateSettingsResponse(TypedDict, total=False):
    settings: "CommunitySettings"
    warnings: List[str]


class BlogArticlesGetResponse(TypedDict, total=False):
    article: "ArticleDetail"


class BlogArticlesUpdateParamsByline(TypedDict, total=False):
    name: str
    url: Any
    avatarUrl: Any


class BlogArticlesUpdateParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class BlogArticlesUpdateParamsSeo(TypedDict, total=False):
    seoTitle: str
    seoDescription: str
    noindex: bool
    canonicalUrl: str
    socialImageUrl: Any


class BlogArticlesUpdateParamsFurtherReadingItem(TypedDict, total=False):
    label: str
    href: str


class BlogArticlesUpdateParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class BlogArticlesUpdateParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class BlogArticlesUpdateParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class BlogArticlesUpdateParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class BlogArticlesUpdateParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class BlogArticlesUpdateParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class BlogArticlesUpdateParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class BlogArticlesUpdateParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class BlogArticlesUpdateParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class BlogArticlesUpdateParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class BlogArticlesUpdateParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class BlogArticlesUpdateParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class BlogArticlesUpdateParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "BlogArticlesUpdateParamsCustomizationThemeComponentsFocus"
    code: "BlogArticlesUpdateParamsCustomizationThemeComponentsCode"
    input: "BlogArticlesUpdateParamsCustomizationThemeComponentsInput"
    button: "BlogArticlesUpdateParamsCustomizationThemeComponentsButton"
    spacing: "BlogArticlesUpdateParamsCustomizationThemeComponentsSpacing"
    selection: "BlogArticlesUpdateParamsCustomizationThemeComponentsSelection"
    scrollbar: "BlogArticlesUpdateParamsCustomizationThemeComponentsScrollbar"
    syntax: "BlogArticlesUpdateParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "BlogArticlesUpdateParamsCustomizationThemeComponentsSyntaxDark"


class BlogArticlesUpdateParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class BlogArticlesUpdateParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class BlogArticlesUpdateParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class BlogArticlesUpdateParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class BlogArticlesUpdateParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class BlogArticlesUpdateParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["BlogArticlesUpdateParamsCustomizationThemeMotionKeyframeStep"]


class BlogArticlesUpdateParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "BlogArticlesUpdateParamsCustomizationThemeMotionReveal"
    hover: "BlogArticlesUpdateParamsCustomizationThemeMotionHover"
    header: "BlogArticlesUpdateParamsCustomizationThemeMotionHeader"
    ambient: "BlogArticlesUpdateParamsCustomizationThemeMotionAmbient"
    keyframes: List["BlogArticlesUpdateParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class BlogArticlesUpdateParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "BlogArticlesUpdateParamsCustomizationThemePalette"
    paletteDark: "BlogArticlesUpdateParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "BlogArticlesUpdateParamsCustomizationThemeLayout"
    components: "BlogArticlesUpdateParamsCustomizationThemeComponents"
    motion: "BlogArticlesUpdateParamsCustomizationThemeMotion"


class BlogArticlesUpdateParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["BlogArticlesUpdateParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class BlogArticlesUpdateParams(TypedDict, total=False):
    title: str
    slug: str
    publishedAt: str
    byline: Optional["BlogArticlesUpdateParamsByline"]
    author: Optional[str]
    content: "BlogArticlesUpdateParamsContent"
    sections: Dict[str, Any]
    excerpt: str
    coverUrl: Any
    series: Optional[str]
    socialImageUrl: Any
    tags: List[str]
    seo: "BlogArticlesUpdateParamsSeo"
    furtherReading: List["BlogArticlesUpdateParamsFurtherReadingItem"]
    commentsEnabled: bool
    onThisPage: Optional[str]
    customization: Optional["BlogArticlesUpdateParamsCustomization"]
    editReason: str
    markdown: str


class BlogArticlesUpdateResponse(TypedDict, total=False):
    article: "ArticleDetail"
    warnings: List[str]


class BlogArticlesRemoveResponse(TypedDict, total=False):
    ok: bool


class BlogArticlesSlugHistoryResponse(TypedDict, total=False):
    history: List["SlugHistoryEntry"]
    page: "PageInfo"


class BlogArticlesScheduleParams(TypedDict, total=False):
    publishAt: str


class BlogArticlesScheduleResponse(TypedDict, total=False):
    article: "ArticleDetail"
    warnings: List[str]


class BlogArticlesUnscheduleResponse(TypedDict, total=False):
    article: "ArticleDetail"


class BlogArticlesSetAuthorsParams(TypedDict, total=False):
    userIds: List[str]


class BlogArticlesSetAuthorsResponse(TypedDict, total=False):
    article: "ArticleDetail"
    warnings: List[str]


class BlogArticlesSetCommentsParams(TypedDict, total=False):
    enabled: bool


class BlogArticlesSetCommentsResponse(TypedDict, total=False):
    article: "ArticleDetail"
    warnings: List[str]


class BlogArticlesPublishParams(TypedDict, total=False):
    notify: bool


class BlogArticlesPublishResponse(TypedDict, total=False):
    article: "ArticleDetail"
    mailed: float
    warnings: List[str]


class BlogArticlesSetStateParams(TypedDict, total=False):
    state: str


class BlogArticlesSetStateResponse(TypedDict, total=False):
    article: "ArticleDetail"
    warnings: List[str]


class BlogArticlesPinParams(TypedDict, total=False):
    pinned: bool


class BlogArticlesPinResponse(TypedDict, total=False):
    article: "ArticleDetail"
    warnings: List[str]


class BlogArticlesAnswerParams(TypedDict, total=False):
    postId: Optional[str]


class BlogArticlesAnswerResponse(TypedDict, total=False):
    article: "ArticleDetail"
    warnings: List[str]


class BlogArticlesReplyParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class BlogArticlesReplyParams(TypedDict, total=False):
    content: "BlogArticlesReplyParamsContent"
    parentPostId: Optional[str]
    markdown: str


class BlogArticlesReplyResponse(TypedDict, total=False):
    post: "PostSummary"
    data: "PostSummary"
    warnings: List[str]


class BlogArticlesBookmarkResponse(TypedDict, total=False):
    bookmarked: bool


class BlogArticlesVoteResponse(TypedDict, total=False):
    voteCount: float
    voted: bool


class BlogArticlesReactParams(TypedDict, total=False):
    emoji: str


class BlogArticlesReactResponse(TypedDict, total=False):
    reacted: bool
    reactions: Dict[str, Any]
    voteCount: float
    warnings: List[str]


class BlogArticlesEditPostParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class BlogArticlesEditPostParams(TypedDict, total=False):
    content: "BlogArticlesEditPostParamsContent"
    editReason: str
    markdown: str


class BlogArticlesEditPostResponse(TypedDict, total=False):
    post: "PostSummary"
    warnings: List[str]


class BlogArticlesDeletePostResponse(TypedDict, total=False):
    ok: bool


class BlogArticlesRevisionsResponse(TypedDict, total=False):
    revisions: List["PostRevisionMeta"]
    page: "PageInfo"


class BlogArticlesRevisionDiffResponse(TypedDict, total=False):
    revision: "PostRevisionDetail"


class BlogArticlesFlagParams(TypedDict, total=False):
    reason: str
    flagType: str


class BlogArticlesFlagResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class BlogArticlesSetPostStatusParams(TypedDict, total=False):
    status: str


class BlogArticlesSetPostStatusResponse(TypedDict, total=False):
    post: "PostSummary"
    warnings: List[str]


class BlogArticlesRecoverArticleResponse(TypedDict, total=False):
    article: "ArticleDetail"


class BlogArticlesRecoverPostResponse(TypedDict, total=False):
    post: "PostSummary"


class NewsletterConfirmParams(TypedDict, total=False):
    token: str


class NewsletterConfirmResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class NewsletterUnsubscribeParams(TypedDict, total=False):
    token: str


class NewsletterUnsubscribeResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class NewsletterOneClickUnsubscribeResponse(TypedDict, total=False):
    ok: bool


class CommunityExtrasListSavedResponse(TypedDict, total=False):
    searches: List["SavedSearchRow"]
    page: "PageInfo"


class CommunityExtrasSaveParams(TypedDict, total=False):
    name: str
    query: str
    notify: bool


class CommunityExtrasSaveResponse(TypedDict, total=False):
    search: "SavedSearchRow"
    data: "SavedSearchRow"
    warnings: List[str]


class CommunityExtrasSetSavedNotifyParams(TypedDict, total=False):
    notify: bool


class CommunityExtrasSetSavedNotifyResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class CommunityExtrasRemoveSavedResponse(TypedDict, total=False):
    ok: bool


class CommunityExtrasCakedayResponse(TypedDict, total=False):
    cakedays: List["CakedayRow"]
    page: "PageInfo"


class CommunityExtrasListNotesResponse(TypedDict, total=False):
    notes: List["UserNoteRow"]
    page: "PageInfo"


class CommunityExtrasAddNoteParams(TypedDict, total=False):
    body: str


class CommunityExtrasAddNoteResponse(TypedDict, total=False):
    note: "UserNoteRow"
    data: "UserNoteRow"
    warnings: List[str]


class CommunityExtrasRemoveNoteResponse(TypedDict, total=False):
    ok: bool


class CommunityExtrasAckStatusResponse(TypedDict, total=False):
    acknowledged: bool
    count: float
    requiresAck: bool


class CommunityExtrasAcknowledgeResponse(TypedDict, total=False):
    acknowledged: bool
    count: float
    requiresAck: bool


class CommunityExtrasSetPolicyParams(TypedDict, total=False):
    requiresAck: bool


class CommunityExtrasSetPolicyResponse(TypedDict, total=False):
    acknowledged: bool
    count: float
    requiresAck: bool
    warnings: List[str]


class CommunityExtrasAssignParams(TypedDict, total=False):
    assigneeId: Optional[str]
    assignedGroupId: Optional[str]


class CommunityExtrasAssignResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class CommunityExtrasSetEventParams(TypedDict, total=False):
    eventAt: Optional[str]


class CommunityExtrasSetEventResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class CommunityExtrasEventsResponseEvent(TypedDict, total=False):
    eventAt: str
    slug: str
    title: str
    topicId: str


class CommunityExtrasEventsResponse(TypedDict, total=False):
    events: List["CommunityExtrasEventsResponseEvent"]
    page: "PageInfo"


class CommunityExtrasRsvpStateResponse(TypedDict, total=False):
    eventAt: Any
    going: float
    interested: float
    mine: str


class CommunityExtrasRsvpParams(TypedDict, total=False):
    status: str


class CommunityExtrasRsvpResponse(TypedDict, total=False):
    going: float
    interested: float
    mine: str
    warnings: List[str]


class CommunityExtrasPreviewResponse(TypedDict, total=False):
    preview: Any


class CommunityExtrasYearlyReviewResponseReview(TypedDict, total=False):
    likesReceived: float
    posts: float
    solutions: float
    topicsStarted: float
    year: float


class CommunityExtrasYearlyReviewResponse(TypedDict, total=False):
    review: "CommunityExtrasYearlyReviewResponseReview"


class PublicBlogSubscribeParams(TypedDict, total=False):
    email: str
    captchaToken: str


class PublicBlogSubscribeResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class PublicBlogIndexResponse(TypedDict, total=False):
    articles: List["ArticleSummary"]
    blog: str
    frontDoor: Dict[str, Any]
    homeDoc: Any
    page: "PageInfo"
    preset: str


class PublicBlogTagsResponseTag(TypedDict, total=False):
    count: float
    tag: str


class PublicBlogTagsResponse(TypedDict, total=False):
    tags: List["PublicBlogTagsResponseTag"]
    page: "PageInfo"


class PublicBlogSearchResponseHit(TypedDict, total=False):
    slug: str
    snippet: str
    title: str
    topicId: str


class PublicBlogSearchResponse(TypedDict, total=False):
    hits: List["PublicBlogSearchResponseHit"]
    page: "PageInfo"


class PublicBlogPermalinkResponse(TypedDict, total=False):
    resolution: Optional["PermalinkResolution"]


class PublicBlogArchiveResponseMonth(TypedDict, total=False):
    count: float
    month: str


class PublicBlogArchiveResponse(TypedDict, total=False):
    months: List["PublicBlogArchiveResponseMonth"]
    page: "PageInfo"


class PublicBlogSeriesResponseSery(TypedDict, total=False):
    count: float
    name: str


class PublicBlogSeriesResponse(TypedDict, total=False):
    series: List["PublicBlogSeriesResponseSery"]
    page: "PageInfo"


class PublicBlogArticleResponseReactions(TypedDict, total=False):
    enabled: bool
    palette: List[str]


class PublicBlogArticleResponseSuggestedItem(TypedDict, total=False):
    excerpt: Any
    id: str
    slug: str
    title: str


class PublicBlogArticleResponse(TypedDict, total=False):
    article: "ArticleDetail"
    piecePreset: Any
    reactions: "PublicBlogArticleResponseReactions"
    suggested: List["PublicBlogArticleResponseSuggestedItem"]


class PublicBlogReactParams(TypedDict, total=False):
    emoji: str


class PublicBlogReactResponse(TypedDict, total=False):
    reacted: bool
    reactions: Dict[str, Any]
    warnings: List[str]


class PublicBlogCommentParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class PublicBlogCommentParams(TypedDict, total=False):
    authorName: str
    content: "PublicBlogCommentParamsContent"
    parentPostId: Optional[str]
    captchaToken: str


class PublicBlogCommentResponse(TypedDict, total=False):
    post: "PostSummary"
    data: "PostSummary"
    warnings: List[str]


class CommunityReactionsResponse(TypedDict, total=False):
    emojis: List[str]
    page: "PageInfo"


class CommunitySetReactionsParams(TypedDict, total=False):
    emojis: List[str]


class CommunitySetReactionsResponse(TypedDict, total=False):
    emojis: List[str]
    warnings: List[str]


class CommunityListCustomReactionsResponse(TypedDict, total=False):
    reactions: List["CustomReaction"]
    page: "PageInfo"


class CommunityUploadCustomReactionParams(TypedDict, total=False):
    file: str


class CommunityUploadCustomReactionResponse(TypedDict, total=False):
    reaction: "CustomReaction"
    data: "CustomReaction"
    warnings: List[str]


class CommunityDeleteCustomReactionResponse(TypedDict, total=False):
    ok: bool


class CommunityTagFeedResponse(TypedDict, total=False):
    items: List["ArticleSummary"]
    page: "PageInfo"
    tag: str


class CommunitySearchResponse(TypedDict, total=False):
    hits: List["CommunityHit"]
    minQueryLength: float


class CommunityBookmarksResponse(TypedDict, total=False):
    articles: List["ArticleSummary"]
    page: "PageInfo"


class ForumTopicsCreateParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ForumTopicsCreateParamsPoll(TypedDict, total=False):
    question: str
    options: List[str]
    allowMultiple: bool
    type: str
    ranked: bool
    public: bool
    minValue: int
    maxValue: int
    step: int
    allowedGroupId: Optional[str]
    closesAt: Optional[str]
    resultsVisibility: str
    minChoices: Optional[int]
    maxChoices: Optional[int]
    chartType: str


class ForumTopicsCreateParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ForumTopicsCreateParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ForumTopicsCreateParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class ForumTopicsCreateParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class ForumTopicsCreateParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ForumTopicsCreateParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ForumTopicsCreateParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class ForumTopicsCreateParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class ForumTopicsCreateParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ForumTopicsCreateParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class ForumTopicsCreateParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ForumTopicsCreateParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ForumTopicsCreateParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "ForumTopicsCreateParamsCustomizationThemeComponentsFocus"
    code: "ForumTopicsCreateParamsCustomizationThemeComponentsCode"
    input: "ForumTopicsCreateParamsCustomizationThemeComponentsInput"
    button: "ForumTopicsCreateParamsCustomizationThemeComponentsButton"
    spacing: "ForumTopicsCreateParamsCustomizationThemeComponentsSpacing"
    selection: "ForumTopicsCreateParamsCustomizationThemeComponentsSelection"
    scrollbar: "ForumTopicsCreateParamsCustomizationThemeComponentsScrollbar"
    syntax: "ForumTopicsCreateParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "ForumTopicsCreateParamsCustomizationThemeComponentsSyntaxDark"


class ForumTopicsCreateParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class ForumTopicsCreateParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class ForumTopicsCreateParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ForumTopicsCreateParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class ForumTopicsCreateParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class ForumTopicsCreateParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["ForumTopicsCreateParamsCustomizationThemeMotionKeyframeStep"]


class ForumTopicsCreateParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "ForumTopicsCreateParamsCustomizationThemeMotionReveal"
    hover: "ForumTopicsCreateParamsCustomizationThemeMotionHover"
    header: "ForumTopicsCreateParamsCustomizationThemeMotionHeader"
    ambient: "ForumTopicsCreateParamsCustomizationThemeMotionAmbient"
    keyframes: List["ForumTopicsCreateParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class ForumTopicsCreateParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "ForumTopicsCreateParamsCustomizationThemePalette"
    paletteDark: "ForumTopicsCreateParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "ForumTopicsCreateParamsCustomizationThemeLayout"
    components: "ForumTopicsCreateParamsCustomizationThemeComponents"
    motion: "ForumTopicsCreateParamsCustomizationThemeMotion"


class ForumTopicsCreateParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["ForumTopicsCreateParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class ForumTopicsCreateParams(TypedDict, total=False):
    title: str
    content: "ForumTopicsCreateParamsContent"
    kind: str
    tags: List[str]
    categoryId: Optional[str]
    featuredLink: Optional[str]
    poll: "ForumTopicsCreateParamsPoll"
    anonymous: bool
    customization: Optional["ForumTopicsCreateParamsCustomization"]
    markdown: str


class ForumTopicsCreateResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]
    data: "ArticleDetail"


class ForumSpaceLevelResponse(TypedDict, total=False):
    level: str


class ForumSetSpaceLevelParams(TypedDict, total=False):
    level: str


class ForumSetSpaceLevelResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ForumMarkReadParams(TypedDict, total=False):
    postNumber: int


class ForumMarkReadResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ForumReadTimeParams(TypedDict, total=False):
    seconds: int


class ForumReadTimeResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ForumSetTopicLevelParams(TypedDict, total=False):
    level: Optional[str]


class ForumSetTopicLevelResponse(TypedDict, total=False):
    state: "TopicReadState"
    warnings: List[str]


class ForumTagSubscriptionsResponseSubscription(TypedDict, total=False):
    level: str
    tag: str


class ForumTagSubscriptionsResponse(TypedDict, total=False):
    subscriptions: List["ForumTagSubscriptionsResponseSubscription"]
    page: "PageInfo"


class ForumSetTagSubscriptionParams(TypedDict, total=False):
    tag: str
    level: Optional[str]


class ForumSetTagSubscriptionResponseSubscription(TypedDict, total=False):
    level: str
    tag: str


class ForumSetTagSubscriptionResponse(TypedDict, total=False):
    subscriptions: List["ForumSetTagSubscriptionResponseSubscription"]
    warnings: List[str]


class ForumCategorySubscriptionsResponseSubscription(TypedDict, total=False):
    categoryId: str
    level: str


class ForumCategorySubscriptionsResponse(TypedDict, total=False):
    subscriptions: List["ForumCategorySubscriptionsResponseSubscription"]
    page: "PageInfo"


class ForumSetCategorySubscriptionParams(TypedDict, total=False):
    categoryId: str
    level: Optional[str]


class ForumSetCategorySubscriptionResponseSubscription(TypedDict, total=False):
    categoryId: str
    level: str


class ForumSetCategorySubscriptionResponse(TypedDict, total=False):
    subscriptions: List["ForumSetCategorySubscriptionResponseSubscription"]
    warnings: List[str]


class ForumTagsResponseTag(TypedDict, total=False):
    count: float
    tag: str


class ForumTagsResponse(TypedDict, total=False):
    tags: List["ForumTagsResponseTag"]
    page: "PageInfo"


class ForumGetSettingsResponseEffective(TypedDict, total=False):
    anonymousRepliesAllowed: bool
    whoCreates: str


class ForumGetSettingsResponse(TypedDict, total=False):
    effective: "ForumGetSettingsResponseEffective"
    settings: "CommunitySettings"


class ForumUpdateSettingsParams(TypedDict, total=False):
    whoCanPost: Optional[str]
    moderateComments: Optional[bool]
    moderateAnonymous: Optional[bool]
    allowAnonymous: Optional[bool]
    anonymousCaptcha: Optional[str]
    defaultSort: Optional[str]
    reactionsEnabled: Optional[bool]


class ForumUpdateSettingsResponse(TypedDict, total=False):
    settings: "CommunitySettings"
    warnings: List[str]


class ForumFlagsResponse(TypedDict, total=False):
    flags: List["FlagRow"]
    page: "PageInfo"


class ForumResolveFlagParams(TypedDict, total=False):
    action: str


class ForumResolveFlagResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ForumBulkModerateParams(TypedDict, total=False):
    topicIds: List[str]
    action: str
    categoryId: Optional[str]
    tags: List[str]
    level: Optional[str]


class ForumBulkModerateResponse(TypedDict, total=False):
    affected: float
    warnings: List[str]


class ForumReviewFlagParams(TypedDict, total=False):
    action: str


class ForumReviewFlagResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ForumTaxonomyListCategoriesResponse(TypedDict, total=False):
    categories: List["CategorySummary"]
    page: "PageInfo"


class ForumTaxonomyCreateCategoryParamsRequiredTagGroup(TypedDict, total=False):
    tagGroupId: str
    minCount: int


class ForumTaxonomyCreateCategoryParams(TypedDict, total=False):
    name: str
    description: str
    color: Optional[str]
    parentId: Optional[str]
    sortOrder: int
    defaultNotificationLevel: str
    topicTemplate: Optional[Dict[str, Any]]
    minimumRequiredTags: int
    defaultTags: List[str]
    allowedTags: List[str]
    defaultSort: Optional[str]
    logoUrl: Optional[str]
    backgroundUrl: Optional[str]
    numFeaturedTopics: Optional[int]
    showSubcategoryList: bool
    autoCloseHours: Optional[int]
    defaultSlowModeSeconds: Optional[int]
    requiredTagGroups: List["ForumTaxonomyCreateCategoryParamsRequiredTagGroup"]
    navigateToFirstPost: Any
    defaultListFilter: Optional[str]


class ForumTaxonomyCreateCategoryResponse(TypedDict, total=False):
    category: "CategorySummary"
    data: "CategorySummary"
    warnings: List[str]


class ForumTaxonomyReorderCategoriesParams(TypedDict, total=False):
    ids: List[str]


class ForumTaxonomyReorderCategoriesResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ForumTaxonomyUpdateCategoryParamsRequiredTagGroup(TypedDict, total=False):
    tagGroupId: str
    minCount: int


class ForumTaxonomyUpdateCategoryParams(TypedDict, total=False):
    name: str
    description: str
    color: Optional[str]
    parentId: Optional[str]
    sortOrder: int
    defaultNotificationLevel: str
    topicTemplate: Optional[Dict[str, Any]]
    minimumRequiredTags: int
    defaultTags: List[str]
    allowedTags: List[str]
    defaultSort: Optional[str]
    logoUrl: Optional[str]
    backgroundUrl: Optional[str]
    numFeaturedTopics: Optional[int]
    showSubcategoryList: bool
    autoCloseHours: Optional[int]
    defaultSlowModeSeconds: Optional[int]
    requiredTagGroups: List["ForumTaxonomyUpdateCategoryParamsRequiredTagGroup"]
    navigateToFirstPost: Any
    defaultListFilter: Optional[str]


class ForumTaxonomyUpdateCategoryResponse(TypedDict, total=False):
    category: "CategorySummary"
    warnings: List[str]


class ForumTaxonomyRemoveCategoryResponse(TypedDict, total=False):
    ok: bool
    topics: int
    movedTo: Any


class ForumTaxonomyEmailInResponse(TypedDict, total=False):
    address: Any


class ForumTaxonomyListSharedDraftsResponse(TypedDict, total=False):
    drafts: List["SharedDraftSummary"]
    page: "PageInfo"


class ForumTaxonomyCreateSharedDraftParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ForumTaxonomyCreateSharedDraftParams(TypedDict, total=False):
    title: str
    content: "ForumTaxonomyCreateSharedDraftParamsContent"
    categoryId: Optional[str]
    tags: List[str]
    kind: str
    markdown: str


class ForumTaxonomyCreateSharedDraftResponse(TypedDict, total=False):
    draft: "SharedDraftSummary"
    data: "SharedDraftSummary"
    warnings: List[str]


class ForumTaxonomyUpdateSharedDraftParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ForumTaxonomyUpdateSharedDraftParams(TypedDict, total=False):
    title: str
    content: "ForumTaxonomyUpdateSharedDraftParamsContent"
    categoryId: Optional[str]
    tags: List[str]
    kind: str
    markdown: str


class ForumTaxonomyUpdateSharedDraftResponse(TypedDict, total=False):
    draft: "SharedDraftSummary"
    warnings: List[str]


class ForumTaxonomyRemoveSharedDraftResponse(TypedDict, total=False):
    ok: bool


class ForumTaxonomyPublishSharedDraftResponse(TypedDict, total=False):
    topic: "ArticleDetail"


class ForumTaxonomyListPermalinksResponse(TypedDict, total=False):
    permalinks: List["PermalinkRow"]
    page: "PageInfo"


class ForumTaxonomyCreatePermalinkParams(TypedDict, total=False):
    fromPath: str
    targetType: str
    targetTopicId: Optional[str]
    targetCategoryId: Optional[str]
    targetUserId: Optional[str]
    targetTag: Optional[str]
    externalUrl: Optional[str]


class ForumTaxonomyCreatePermalinkResponse(TypedDict, total=False):
    permalink: "PermalinkRow"
    data: "PermalinkRow"
    warnings: List[str]


class ForumTaxonomyImportPermalinksParamsPermalink(TypedDict, total=False):
    fromPath: str
    targetType: str
    targetTopicId: Optional[str]
    targetCategoryId: Optional[str]
    targetUserId: Optional[str]
    targetTag: Optional[str]
    externalUrl: Optional[str]


class ForumTaxonomyImportPermalinksParams(TypedDict, total=False):
    permalinks: List["ForumTaxonomyImportPermalinksParamsPermalink"]


class ForumTaxonomyImportPermalinksResponse(TypedDict, total=False):
    imported: float
    warnings: List[str]


class ForumTaxonomyRemovePermalinkResponse(TypedDict, total=False):
    ok: bool


class ForumTaxonomyListCategoryPermsResponse(TypedDict, total=False):
    permissions: List["CategoryPermissionRow"]
    page: "PageInfo"


class ForumTaxonomySetCategoryPermsParamsGrant(TypedDict, total=False):
    groupId: str
    canSee: bool
    canReply: bool
    canCreate: bool


class ForumTaxonomySetCategoryPermsParams(TypedDict, total=False):
    grants: List["ForumTaxonomySetCategoryPermsParamsGrant"]


class ForumTaxonomySetCategoryPermsResponse(TypedDict, total=False):
    permissions: List["CategoryPermissionRow"]
    warnings: List[str]


class ForumTaxonomyListCategoryModsResponse(TypedDict, total=False):
    moderators: List["CategoryModeratorRow"]
    page: "PageInfo"


class ForumTaxonomyAddCategoryModParams(TypedDict, total=False):
    userId: str


class ForumTaxonomyAddCategoryModResponse(TypedDict, total=False):
    moderators: List["CategoryModeratorRow"]
    warnings: List[str]


class ForumTaxonomyRemoveCategoryModResponse(TypedDict, total=False):
    ok: bool


class ForumTaxonomyListTagGroupsResponse(TypedDict, total=False):
    tagGroups: List["TagGroupSummary"]
    page: "PageInfo"


class ForumTaxonomyCreateTagGroupParams(TypedDict, total=False):
    name: str
    mode: str
    tags: List[str]
    categoryIds: List[str]


class ForumTaxonomyCreateTagGroupResponse(TypedDict, total=False):
    tagGroup: "TagGroupSummary"
    data: "TagGroupSummary"
    warnings: List[str]


class ForumTaxonomyUpdateTagGroupParams(TypedDict, total=False):
    name: str
    mode: str
    tags: List[str]
    categoryIds: List[str]


class ForumTaxonomyUpdateTagGroupResponse(TypedDict, total=False):
    tagGroup: "TagGroupSummary"
    warnings: List[str]


class ForumTaxonomyRemoveTagGroupResponse(TypedDict, total=False):
    ok: bool


class ForumTaxonomyListTagInfoResponse(TypedDict, total=False):
    tagInfo: List["TagInfoRow"]
    page: "PageInfo"


class ForumTaxonomySetTagInfoParams(TypedDict, total=False):
    tag: str
    description: Optional[str]
    canonical: Optional[str]
    staffOnly: bool
    minTrustLevel: Optional[int]
    color: Optional[str]
    textColor: Optional[str]


class ForumTaxonomySetTagInfoResponse(TypedDict, total=False):
    tagInfo: "TagInfoRow"
    data: "TagInfoRow"
    warnings: List[str]


class ForumTaxonomyRemoveTagInfoResponse(TypedDict, total=False):
    ok: bool


class ForumTaxonomySetTopicCategoryParams(TypedDict, total=False):
    categoryId: Optional[str]


class ForumTaxonomySetTopicCategoryResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumTopicsBannerResponse(TypedDict, total=False):
    banner: Any


class ForumTopicsGetResponse(TypedDict, total=False):
    poll: Optional["PollSummary"]
    polls: List["PollSummary"]
    readState: "TopicReadState"
    topic: "ArticleDetail"


class ForumTopicsUpdateParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ForumTopicsUpdateParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ForumTopicsUpdateParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class ForumTopicsUpdateParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class ForumTopicsUpdateParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ForumTopicsUpdateParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ForumTopicsUpdateParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class ForumTopicsUpdateParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class ForumTopicsUpdateParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ForumTopicsUpdateParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class ForumTopicsUpdateParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ForumTopicsUpdateParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ForumTopicsUpdateParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "ForumTopicsUpdateParamsCustomizationThemeComponentsFocus"
    code: "ForumTopicsUpdateParamsCustomizationThemeComponentsCode"
    input: "ForumTopicsUpdateParamsCustomizationThemeComponentsInput"
    button: "ForumTopicsUpdateParamsCustomizationThemeComponentsButton"
    spacing: "ForumTopicsUpdateParamsCustomizationThemeComponentsSpacing"
    selection: "ForumTopicsUpdateParamsCustomizationThemeComponentsSelection"
    scrollbar: "ForumTopicsUpdateParamsCustomizationThemeComponentsScrollbar"
    syntax: "ForumTopicsUpdateParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "ForumTopicsUpdateParamsCustomizationThemeComponentsSyntaxDark"


class ForumTopicsUpdateParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class ForumTopicsUpdateParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class ForumTopicsUpdateParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ForumTopicsUpdateParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class ForumTopicsUpdateParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class ForumTopicsUpdateParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["ForumTopicsUpdateParamsCustomizationThemeMotionKeyframeStep"]


class ForumTopicsUpdateParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "ForumTopicsUpdateParamsCustomizationThemeMotionReveal"
    hover: "ForumTopicsUpdateParamsCustomizationThemeMotionHover"
    header: "ForumTopicsUpdateParamsCustomizationThemeMotionHeader"
    ambient: "ForumTopicsUpdateParamsCustomizationThemeMotionAmbient"
    keyframes: List["ForumTopicsUpdateParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class ForumTopicsUpdateParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "ForumTopicsUpdateParamsCustomizationThemePalette"
    paletteDark: "ForumTopicsUpdateParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "ForumTopicsUpdateParamsCustomizationThemeLayout"
    components: "ForumTopicsUpdateParamsCustomizationThemeComponents"
    motion: "ForumTopicsUpdateParamsCustomizationThemeMotion"


class ForumTopicsUpdateParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["ForumTopicsUpdateParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class ForumTopicsUpdateParams(TypedDict, total=False):
    title: str
    tags: List[str]
    featuredLink: Optional[str]
    slug: str
    customization: Optional["ForumTopicsUpdateParamsCustomization"]


class ForumTopicsUpdateResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumTopicsRelatedResponse(TypedDict, total=False):
    map: Optional["TopicMap"]
    related: List["RelatedTopic"]


class ForumTopicsTimelineResponse(TypedDict, total=False):
    timeline: Optional["TopicTimeline"]


class ForumTopicsReplyAsLinkedTopicParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ForumTopicsReplyAsLinkedTopicParams(TypedDict, total=False):
    title: str
    content: "ForumTopicsReplyAsLinkedTopicParamsContent"
    categoryId: Optional[str]
    markdown: str


class ForumTopicsReplyAsLinkedTopicResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    data: "ArticleDetail"
    warnings: List[str]


class ForumTopicsAddPollParams(TypedDict, total=False):
    question: str
    options: List[str]
    allowMultiple: bool
    type: str
    ranked: bool
    public: bool
    minValue: int
    maxValue: int
    step: int
    allowedGroupId: Optional[str]
    closesAt: Optional[str]
    resultsVisibility: str
    minChoices: Optional[int]
    maxChoices: Optional[int]
    chartType: str


class ForumTopicsAddPollResponse(TypedDict, total=False):
    poll: "PollSummary"
    data: "PollSummary"
    warnings: List[str]


class ForumTopicsVotePollParams(TypedDict, total=False):
    optionIds: List[str]


class ForumTopicsVotePollResponse(TypedDict, total=False):
    poll: "PollSummary"
    warnings: List[str]


class ForumTopicsClosePollResponse(TypedDict, total=False):
    poll: "PollSummary"


class ForumTopicsReopenPollResponse(TypedDict, total=False):
    poll: "PollSummary"


class ForumTopicsRemovePollResponse(TypedDict, total=False):
    ok: bool


class ForumTopicsReplyParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ForumTopicsReplyParams(TypedDict, total=False):
    content: "ForumTopicsReplyParamsContent"
    parentPostId: Optional[str]
    whisper: bool
    anonymous: bool
    markdown: str


class ForumTopicsReplyResponse(TypedDict, total=False):
    post: "PostSummary"
    data: "PostSummary"
    warnings: List[str]


class ForumTopicsSetWikiParams(TypedDict, total=False):
    wiki: bool


class ForumTopicsSetWikiResponse(TypedDict, total=False):
    post: "PostSummary"
    warnings: List[str]


class ForumToolsSummarizeResponse(TypedDict, total=False):
    summary: str


class ForumToolsUnansweredExpertsResponseItem(TypedDict, total=False):
    experts: List["ExpertSuggestion"]
    title: str
    topicId: str


class ForumToolsUnansweredExpertsResponse(TypedDict, total=False):
    items: List["ForumToolsUnansweredExpertsResponseItem"]
    page: "PageInfo"


class ForumToolsExpertsResponse(TypedDict, total=False):
    experts: List["ExpertSuggestion"]
    page: "PageInfo"


class ForumToolsNotifyExpertsResponse(TypedDict, total=False):
    notified: List[str]


class ForumToolsGetTimerResponse(TypedDict, total=False):
    timer: Optional["TimerSummary"]


class ForumToolsSetTimerParams(TypedDict, total=False):
    action: str
    runAt: str
    basedOnLastPost: bool
    durationMinutes: int
    targetCategoryId: str


class ForumToolsSetTimerResponse(TypedDict, total=False):
    timer: "TimerSummary"
    warnings: List[str]


class ForumToolsClearTimerResponse(TypedDict, total=False):
    ok: bool


class ForumToolsRecoverResponse(TypedDict, total=False):
    topic: "ArticleDetail"


class ForumToolsBumpResponse(TypedDict, total=False):
    topic: "ArticleDetail"


class ForumToolsSplitParams(TypedDict, total=False):
    postIds: List[str]
    title: str


class ForumToolsSplitResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    data: "ArticleDetail"
    warnings: List[str]


class ForumToolsMergeParams(TypedDict, total=False):
    targetTopicId: str


class ForumToolsMergeResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumToolsPromoteToDocsParams(TypedDict, total=False):
    targetSpaceId: str
    collectionId: str
    title: str


class ForumToolsPromoteToDocsResponse(TypedDict, total=False):
    promotion: "PromotionResult"
    data: "PromotionResult"
    warnings: List[str]


class ForumToolsMovePostsParams(TypedDict, total=False):
    postIds: List[str]
    targetTopicId: str


class ForumToolsMovePostsResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumToolsChangeOwnerParams(TypedDict, total=False):
    postIds: List[str]
    newOwnerId: str


class ForumToolsChangeOwnerResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumToolsEditPostParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ForumToolsEditPostParams(TypedDict, total=False):
    content: "ForumToolsEditPostParamsContent"
    editReason: str
    markdown: str


class ForumToolsEditPostResponse(TypedDict, total=False):
    post: "PostSummary"
    warnings: List[str]


class ForumToolsDeletePostResponse(TypedDict, total=False):
    ok: bool


class ForumToolsRevisionsResponse(TypedDict, total=False):
    revisions: List["PostRevisionMeta"]
    page: "PageInfo"


class ForumToolsRevisionDiffResponse(TypedDict, total=False):
    revision: "PostRevisionDetail"


class ForumToolsVoteResponse(TypedDict, total=False):
    voteCount: float
    voted: bool


class ForumToolsReactParams(TypedDict, total=False):
    emoji: str
    anonymous: bool


class ForumToolsReactResponse(TypedDict, total=False):
    reacted: bool
    reactions: Dict[str, Any]
    voteCount: float
    warnings: List[str]


class ForumToolsBookmarkResponse(TypedDict, total=False):
    bookmarked: bool


class ForumToolsBookmarkReminderParams(TypedDict, total=False):
    remindAt: Optional[str]
    preset: str
    note: Optional[str]
    name: Optional[str]
    autoDelete: bool


class ForumToolsBookmarkReminderResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ForumToolsFlagParams(TypedDict, total=False):
    reason: str
    flagType: str


class ForumToolsFlagResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ForumToolsFlagTopicParams(TypedDict, total=False):
    reason: str
    flagType: str


class ForumToolsFlagTopicResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ForumToolsAnswerParams(TypedDict, total=False):
    postId: Optional[str]


class ForumToolsAnswerResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumToolsOfferBountyParams(TypedDict, total=False):
    amount: int
    days: int


class ForumToolsOfferBountyResponse(TypedDict, total=False):
    bounty: "BountyView"
    data: "BountyView"
    warnings: List[str]


class ForumToolsBountyHistoryResponse(TypedDict, total=False):
    bounties: List["BountyView"]
    page: "PageInfo"


class ForumToolsSetStateParams(TypedDict, total=False):
    state: str


class ForumToolsSetStateResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumToolsSetKindParams(TypedDict, total=False):
    kind: str


class ForumToolsSetKindResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumToolsPinParams(TypedDict, total=False):
    pinned: bool


class ForumToolsPinResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


ForumToolsPinAdvancedParams = TypedDict("ForumToolsPinAdvancedParams", {"pinned": bool, "until": Optional[str], "global": bool, "banner": bool}, total=False)


class ForumToolsPinAdvancedResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumToolsSlowModeParams(TypedDict, total=False):
    seconds: int


class ForumToolsSlowModeResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumToolsDismissPinResponse(TypedDict, total=False):
    ok: bool


class ForumToolsSetListedParams(TypedDict, total=False):
    listed: bool


class ForumToolsSetListedResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]


class ForumToolsSetPostStatusParams(TypedDict, total=False):
    status: str


class ForumToolsSetPostStatusResponse(TypedDict, total=False):
    post: "PostSummary"
    warnings: List[str]


class PublicForumTopicsHeartbeatParams(TypedDict, total=False):
    viewerId: str
    typing: bool
    name: str


class PublicForumTopicsHeartbeatResponse(TypedDict, total=False):
    viewers: float
    warnings: List[str]


class PublicForumTopicsReplyParams(TypedDict, total=False):
    authorName: str
    content: Dict[str, Any]
    parentPostId: Optional[str]
    whisper: bool


class PublicForumTopicsReplyResponse(TypedDict, total=False):
    post: "PostSummary"
    data: "PostSummary"
    warnings: List[str]


class PublicForumTopicsReplyAsLinkedTopicParams(TypedDict, total=False):
    title: str
    content: Dict[str, Any]
    categoryId: Optional[str]


class PublicForumTopicsReplyAsLinkedTopicResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    data: "ArticleDetail"
    warnings: List[str]


class PublicForumTopicsReactParams(TypedDict, total=False):
    emoji: str


class PublicForumTopicsReactResponse(TypedDict, total=False):
    reacted: bool
    reactions: Dict[str, Any]
    voteCount: float
    warnings: List[str]


class PublicForumTopicsReactorsResponseReactionUser(TypedDict, total=False):
    name: str
    userId: str


class PublicForumTopicsReactorsResponseReaction(TypedDict, total=False):
    emoji: str
    users: List["PublicForumTopicsReactorsResponseReactionUser"]


class PublicForumTopicsReactorsResponse(TypedDict, total=False):
    reactions: List["PublicForumTopicsReactorsResponseReaction"]
    page: "PageInfo"


class PublicForumTopicsFlagParams(TypedDict, total=False):
    flagType: str
    reason: str


class PublicForumTopicsFlagResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class PublicForumTopicsFlagTopicParams(TypedDict, total=False):
    flagType: str
    reason: str


class PublicForumTopicsFlagTopicResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class PublicForumTopicsBookmarkResponse(TypedDict, total=False):
    bookmarked: bool
    data: bool


class PublicForumTopicsBookmarkPostResponse(TypedDict, total=False):
    bookmarked: bool
    data: bool


class PublicForumTopicsBookmarkReminderParams(TypedDict, total=False):
    remindAt: Optional[str]
    preset: str
    note: Optional[str]
    name: Optional[str]
    autoDelete: bool


class PublicForumTopicsBookmarkReminderResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class PublicForumTopicsAnswerParams(TypedDict, total=False):
    postId: Optional[str]


class PublicForumTopicsAnswerResponse(TypedDict, total=False):
    answerPostId: Any
    data: Any
    warnings: List[str]


class PublicForumTopicsOfferBountyParams(TypedDict, total=False):
    amount: int
    days: int


class PublicForumTopicsOfferBountyResponse(TypedDict, total=False):
    bounty: "BountyView"
    data: "BountyView"
    warnings: List[str]


class PublicForumTopicsEditParams(TypedDict, total=False):
    content: Dict[str, Any]


class PublicForumTopicsEditResponse(TypedDict, total=False):
    post: "PostSummary"
    data: "PostSummary"
    warnings: List[str]


class PublicForumTopicsPostRevisionsResponse(TypedDict, total=False):
    revisions: List["PostRevisionMeta"]
    page: "PageInfo"


class PublicForumTopicsPostRevisionDiffResponse(TypedDict, total=False):
    revision: "PostRevisionDetail"


class PublicForumTopicsNotifyParams(TypedDict, total=False):
    level: str


class PublicForumTopicsNotifyResponse(TypedDict, total=False):
    level: str
    data: str
    warnings: List[str]


class PublicForumTopicsRelatedTopicsResponseTopic(TypedDict, total=False):
    excerpt: str
    id: str
    replyCount: float
    score: Any
    slug: str
    title: str


class PublicForumTopicsRelatedTopicsResponse(TypedDict, total=False):
    basis: str
    topics: List["PublicForumTopicsRelatedTopicsResponseTopic"]


class PublicForumPeopleDirectoryResponse(TypedDict, total=False):
    members: List[Any]
    page: "PageInfo"


class PublicForumPeopleBadgesResponseBadge(TypedDict, total=False):
    custom: bool
    description: str
    group: str
    icon: str
    name: str
    slug: str


class PublicForumPeopleBadgesResponse(TypedDict, total=False):
    badges: List["PublicForumPeopleBadgesResponseBadge"]
    page: "PageInfo"


class PublicForumPeopleLeaderboardResponseLeader(TypedDict, total=False):
    label: str
    level: float
    likesReceived: float
    name: str
    points: float
    postsCreated: float
    solutions: float
    userId: str


class PublicForumPeopleLeaderboardResponse(TypedDict, total=False):
    leaders: List["PublicForumPeopleLeaderboardResponseLeader"]
    period: str


class PublicForumPeopleProfileResponseBadge(TypedDict, total=False):
    description: str
    grantedAt: str
    icon: str
    name: str
    slug: str


class PublicForumPeopleProfileResponseCustomField(TypedDict, total=False):
    key: str
    label: str
    type: str
    value: str


class PublicForumPeopleProfileResponseFeaturedBadge(TypedDict, total=False):
    description: str
    grantedAt: str
    icon: str
    name: str
    slug: str


class PublicForumPeopleProfileResponseProfile(TypedDict, total=False):
    avatarUrl: Any
    bio: Any
    flair: Any
    followers: float
    following: float
    label: str
    lastSeen: Any
    level: float
    likesReceived: float
    location: Any
    memberSince: Any
    name: str
    online: bool
    postsCreated: float
    solutions: float
    title: Any
    userId: str
    username: str
    viewerFollows: bool
    viewerRelation: Any
    websiteUrl: Any


class PublicForumPeopleProfileResponseRecentReply(TypedDict, total=False):
    createdAt: str
    snippet: str
    topicSlug: str
    topicTitle: str


class PublicForumPeopleProfileResponse(TypedDict, total=False):
    badges: List["PublicForumPeopleProfileResponseBadge"]
    customFields: List["PublicForumPeopleProfileResponseCustomField"]
    featuredBadges: List["PublicForumPeopleProfileResponseFeaturedBadge"]
    profile: "PublicForumPeopleProfileResponseProfile"
    recentReplies: List["PublicForumPeopleProfileResponseRecentReply"]
    topics: List["ArticleSummary"]
    viewerIsOwner: bool


class PublicForumPeopleUserActionsFeedResponse(TypedDict, total=False):
    items: List["UserActionItem"]
    page: "PageInfo"


class PublicForumPeopleUserCardResponseCustomField(TypedDict, total=False):
    key: str
    label: str
    type: str
    value: str


class PublicForumPeopleUserCardResponse(TypedDict, total=False):
    avatarUrl: Any
    bio: Any
    cardBackgroundUrl: Any
    customFields: List["PublicForumPeopleUserCardResponseCustomField"]
    flair: Any
    label: str
    lastSeen: Any
    level: float
    likesReceived: float
    memberSince: Any
    name: str
    online: bool
    postsCreated: float
    solutions: float
    title: Any
    userId: str
    username: str
    viewerFollows: bool
    viewerRelation: Any


class PublicForumPeopleOnlineRosterResponseOnlineItem(TypedDict, total=False):
    avatarUrl: Any
    id: str
    name: str


class PublicForumPeopleOnlineRosterResponse(TypedDict, total=False):
    online: List["PublicForumPeopleOnlineRosterResponseOnlineItem"]
    page: "PageInfo"


class PublicForumTaxonomyCategoriesListResponse(TypedDict, total=False):
    categories: List["CategorySummary"]
    page: "PageInfo"


class PublicForumTaxonomyCategoryFormTemplateResponse(TypedDict, total=False):
    formTemplate: Any


class PublicForumTaxonomyCategoriesOverviewResponseCategory(TypedDict, total=False):
    allowedTags: List[str]
    autoCloseHours: Any
    backgroundUrl: Any
    color: Any
    defaultListFilter: Any
    defaultNotificationLevel: str
    defaultSlowModeSeconds: Any
    defaultSort: Any
    defaultTags: List[str]
    description: str
    id: str
    latest: Any
    logoUrl: Any
    minimumRequiredTags: float
    name: str
    navigateToFirstPost: Any
    new: float
    numFeaturedTopics: Any
    parentId: Any
    requiredTagGroups: List["RequiredTagGroup"]
    showSubcategoryList: bool
    slug: str
    sortOrder: float
    topicCount: float
    topicTemplate: Any
    unread: float


class PublicForumTaxonomyCategoriesOverviewResponse(TypedDict, total=False):
    categories: List["PublicForumTaxonomyCategoriesOverviewResponseCategory"]
    page: "PageInfo"


class PublicForumTaxonomyTagsResponseTag(TypedDict, total=False):
    count: float
    tag: str


class PublicForumTaxonomyTagsResponse(TypedDict, total=False):
    tags: List["PublicForumTaxonomyTagsResponseTag"]
    page: "PageInfo"


class PublicForumTaxonomyTagAboutResponseRelatedItem(TypedDict, total=False):
    count: float
    tag: str


class PublicForumTaxonomyTagAboutResponse(TypedDict, total=False):
    color: Any
    description: Any
    related: List["PublicForumTaxonomyTagAboutResponseRelatedItem"]
    synonyms: List[str]
    tag: str
    textColor: Any
    topics: List["ArticleSummary"]


class PublicForumTaxonomyTagIntersectionResponse(TypedDict, total=False):
    tags: List[str]
    topics: List["ArticleSummary"]


class PublicForumDiscoveryPermalinkResponse(TypedDict, total=False):
    resolution: Optional["PermalinkResolution"]


class PublicForumDiscoveryBookmarksResponseTopic(TypedDict, total=False):
    excerpt: str
    replyCount: float
    slug: str
    title: str


class PublicForumDiscoveryBookmarksResponse(TypedDict, total=False):
    topics: List["PublicForumDiscoveryBookmarksResponseTopic"]
    page: "PageInfo"


class PublicForumDiscoveryMentionSuggestResponseSuggestion(TypedDict, total=False):
    avatarUrl: Any
    handle: str
    name: str


class PublicForumDiscoveryMentionSuggestResponse(TypedDict, total=False):
    suggestions: List["PublicForumDiscoveryMentionSuggestResponseSuggestion"]
    page: "PageInfo"


class PublicForumDiscoveryResolveRefsResponse(TypedDict, total=False):
    refs: Dict[str, Any]


class PublicForumDiscoverySearchResponseHit(TypedDict, total=False):
    slug: str
    snippet: str
    title: str
    topicId: str


class PublicForumDiscoverySearchResponse(TypedDict, total=False):
    hits: List["PublicForumDiscoverySearchResponseHit"]
    minQueryLength: float


class PublicForumReadAllResponse(TypedDict, total=False):
    marked: float


class PublicForumDismissNewResponse(TypedDict, total=False):
    dismissed: float


class PublicForumDismissUnreadResponse(TypedDict, total=False):
    dismissed: float


class PublicForumEmbedResolveParams(TypedDict, total=False):
    articleUrl: str
    title: str


class PublicForumEmbedResolveResponse(TypedDict, total=False):
    slug: str
    topicId: str
    warnings: List[str]


class PublicForumUploadParams(TypedDict, total=False):
    file: str


class PublicForumUploadResponse(TypedDict, total=False):
    asset: "UploadedAsset"
    data: "UploadedAsset"
    warnings: List[str]


class PublicForumCreateAnonParams(TypedDict, total=False):
    authorName: str
    title: str
    content: Dict[str, Any]
    kind: str
    tags: List[str]
    categoryId: Optional[str]


class PublicForumCreateAnonResponse(TypedDict, total=False):
    topic: "ArticleDetail"
    warnings: List[str]
    data: "ArticleDetail"


class PublicForumIndexResponse(TypedDict, total=False):
    forum: str
    frontDoor: Dict[str, Any]
    homeDoc: Any
    page: "PageInfo"
    preset: str
    signedIn: bool
    sort: str
    topics: List["ArticleSummary"]


class PublicForumThreadsTopicResponseReaderSettingsContentLocalization(TypedDict, total=False):
    defaultLocale: str
    enabled: bool


class PublicForumThreadsTopicResponseReaderSettings(TypedDict, total=False):
    contentLocalization: "PublicForumThreadsTopicResponseReaderSettingsContentLocalization"
    threadedReplies: bool


class PublicForumThreadsTopicResponseSuggestedItem(TypedDict, total=False):
    id: str
    replyCount: float
    slug: str
    title: str


class PublicForumThreadsTopicResponse(TypedDict, total=False):
    bookmarkAutoDelete: bool
    bookmarked: bool
    bookmarkedPostIds: List[str]
    bookmarkName: Any
    bookmarkNote: Any
    bookmarkRemindAt: Any
    bookmarkReminderPreset: Any
    bounty: Optional["BountyView"]
    canAccept: bool
    canFlag: bool
    canModerate: bool
    canOfferBounty: bool
    myReactions: Dict[str, Any]
    notifyLevel: Any
    poll: Optional["PollSummary"]
    polls: List["PollSummary"]
    reactionEmojis: List[str]
    readerSettings: "PublicForumThreadsTopicResponseReaderSettings"
    readState: Any
    suggested: List["PublicForumThreadsTopicResponseSuggestedItem"]
    topic: "ArticleDetail"
    viewerId: Any
    viewerLevel: Any


class ForumTranslationsTranslateTopicParams(TypedDict, total=False):
    locale: str


class ForumTranslationsTranslateTopicResponse(TypedDict, total=False):
    translation: "TranslatedContent"
    warnings: List[str]


class ForumTranslationsTranslatePostParams(TypedDict, total=False):
    locale: str


class ForumTranslationsTranslatePostResponse(TypedDict, total=False):
    translation: "TranslatedContent"
    warnings: List[str]


class RoadmapBoardResponseLane(TypedDict, total=False):
    items: List["ArticleSummary"]
    status: str


class RoadmapBoardResponse(TypedDict, total=False):
    lanes: List["RoadmapBoardResponseLane"]
    page: "PageInfo"


class RoadmapSubmitParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class RoadmapSubmitParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class RoadmapSubmitParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class RoadmapSubmitParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class RoadmapSubmitParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class RoadmapSubmitParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class RoadmapSubmitParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class RoadmapSubmitParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class RoadmapSubmitParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class RoadmapSubmitParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class RoadmapSubmitParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class RoadmapSubmitParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class RoadmapSubmitParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class RoadmapSubmitParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "RoadmapSubmitParamsCustomizationThemeComponentsFocus"
    code: "RoadmapSubmitParamsCustomizationThemeComponentsCode"
    input: "RoadmapSubmitParamsCustomizationThemeComponentsInput"
    button: "RoadmapSubmitParamsCustomizationThemeComponentsButton"
    spacing: "RoadmapSubmitParamsCustomizationThemeComponentsSpacing"
    selection: "RoadmapSubmitParamsCustomizationThemeComponentsSelection"
    scrollbar: "RoadmapSubmitParamsCustomizationThemeComponentsScrollbar"
    syntax: "RoadmapSubmitParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "RoadmapSubmitParamsCustomizationThemeComponentsSyntaxDark"


class RoadmapSubmitParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class RoadmapSubmitParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class RoadmapSubmitParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class RoadmapSubmitParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class RoadmapSubmitParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class RoadmapSubmitParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["RoadmapSubmitParamsCustomizationThemeMotionKeyframeStep"]


class RoadmapSubmitParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "RoadmapSubmitParamsCustomizationThemeMotionReveal"
    hover: "RoadmapSubmitParamsCustomizationThemeMotionHover"
    header: "RoadmapSubmitParamsCustomizationThemeMotionHeader"
    ambient: "RoadmapSubmitParamsCustomizationThemeMotionAmbient"
    keyframes: List["RoadmapSubmitParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class RoadmapSubmitParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "RoadmapSubmitParamsCustomizationThemePalette"
    paletteDark: "RoadmapSubmitParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "RoadmapSubmitParamsCustomizationThemeLayout"
    components: "RoadmapSubmitParamsCustomizationThemeComponents"
    motion: "RoadmapSubmitParamsCustomizationThemeMotion"


class RoadmapSubmitParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["RoadmapSubmitParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class RoadmapSubmitParams(TypedDict, total=False):
    title: str
    content: "RoadmapSubmitParamsContent"
    tags: List[str]
    customization: Optional["RoadmapSubmitParamsCustomization"]
    markdown: str


class RoadmapSubmitResponse(TypedDict, total=False):
    item: "ArticleDetail"
    warnings: List[str]
    data: "ArticleDetail"


class RoadmapGetResponse(TypedDict, total=False):
    item: "ArticleDetail"


class RoadmapUpdateParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class RoadmapUpdateParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class RoadmapUpdateParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class RoadmapUpdateParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class RoadmapUpdateParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class RoadmapUpdateParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class RoadmapUpdateParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class RoadmapUpdateParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class RoadmapUpdateParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class RoadmapUpdateParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class RoadmapUpdateParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class RoadmapUpdateParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class RoadmapUpdateParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "RoadmapUpdateParamsCustomizationThemeComponentsFocus"
    code: "RoadmapUpdateParamsCustomizationThemeComponentsCode"
    input: "RoadmapUpdateParamsCustomizationThemeComponentsInput"
    button: "RoadmapUpdateParamsCustomizationThemeComponentsButton"
    spacing: "RoadmapUpdateParamsCustomizationThemeComponentsSpacing"
    selection: "RoadmapUpdateParamsCustomizationThemeComponentsSelection"
    scrollbar: "RoadmapUpdateParamsCustomizationThemeComponentsScrollbar"
    syntax: "RoadmapUpdateParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "RoadmapUpdateParamsCustomizationThemeComponentsSyntaxDark"


class RoadmapUpdateParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class RoadmapUpdateParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class RoadmapUpdateParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class RoadmapUpdateParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class RoadmapUpdateParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class RoadmapUpdateParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["RoadmapUpdateParamsCustomizationThemeMotionKeyframeStep"]


class RoadmapUpdateParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "RoadmapUpdateParamsCustomizationThemeMotionReveal"
    hover: "RoadmapUpdateParamsCustomizationThemeMotionHover"
    header: "RoadmapUpdateParamsCustomizationThemeMotionHeader"
    ambient: "RoadmapUpdateParamsCustomizationThemeMotionAmbient"
    keyframes: List["RoadmapUpdateParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class RoadmapUpdateParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "RoadmapUpdateParamsCustomizationThemePalette"
    paletteDark: "RoadmapUpdateParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "RoadmapUpdateParamsCustomizationThemeLayout"
    components: "RoadmapUpdateParamsCustomizationThemeComponents"
    motion: "RoadmapUpdateParamsCustomizationThemeMotion"


class RoadmapUpdateParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["RoadmapUpdateParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class RoadmapUpdateParams(TypedDict, total=False):
    title: str
    tags: List[str]
    customization: Optional["RoadmapUpdateParamsCustomization"]


class RoadmapUpdateResponse(TypedDict, total=False):
    item: "ArticleDetail"
    warnings: List[str]


class RoadmapVoteResponse(TypedDict, total=False):
    voteCount: float
    voted: bool


class RoadmapCommentParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class RoadmapCommentParams(TypedDict, total=False):
    content: "RoadmapCommentParamsContent"
    markdown: str


class RoadmapCommentResponse(TypedDict, total=False):
    post: "PostSummary"
    data: "PostSummary"
    warnings: List[str]


class RoadmapMergeParams(TypedDict, total=False):
    canonicalId: str


class RoadmapMergeResponse(TypedDict, total=False):
    item: "ArticleDetail"
    warnings: List[str]


class RoadmapSetStatusParams(TypedDict, total=False):
    status: str


class RoadmapSetStatusResponse(TypedDict, total=False):
    item: "ArticleDetail"
    warnings: List[str]


class PublicRoadmapSubmitParams(TypedDict, total=False):
    title: str
    content: Dict[str, Any]
    authorName: str
    captchaToken: str
    markdown: str


class PublicRoadmapSubmitResponse(TypedDict, total=False):
    item: "ArticleDetail"
    data: "ArticleDetail"
    warnings: List[str]


class PublicRoadmapBoardResponseLane(TypedDict, total=False):
    items: List["ArticleSummary"]
    status: str


class PublicRoadmapBoardResponse(TypedDict, total=False):
    anonymousVotes: bool
    frontDoor: Dict[str, Any]
    homeDoc: Any
    lanes: List["PublicRoadmapBoardResponseLane"]
    page: "PageInfo"
    preset: str
    roadmap: str
    statusLabels: Dict[str, Any]


class PublicRoadmapSearchResponseHit(TypedDict, total=False):
    slug: str
    snippet: str
    title: str
    topicId: str


class PublicRoadmapSearchResponse(TypedDict, total=False):
    hits: List["PublicRoadmapSearchResponseHit"]
    page: "PageInfo"


class PublicRoadmapItemResponse(TypedDict, total=False):
    item: "ArticleDetail"
    statusLabels: Dict[str, Any]


class PublicRoadmapCommentParams(TypedDict, total=False):
    authorName: str
    content: Dict[str, Any]
    parentPostId: Optional[str]
    captchaToken: str
    markdown: str


class PublicRoadmapCommentResponse(TypedDict, total=False):
    post: "PostSummary"
    warnings: List[str]


class PublicRoadmapWatchParams(TypedDict, total=False):
    email: str
    captchaToken: str


class PublicRoadmapWatchResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class PublicRoadmapVoteResponse(TypedDict, total=False):
    voteCount: float
    voted: bool


class CommunityReputationProfileResponse(TypedDict, total=False):
    profile: "MemberProfile"


class CommunityReputationCatalogResponseLevel(TypedDict, total=False):
    key: str
    label: str
    level: float


class CommunityReputationCatalogResponse(TypedDict, total=False):
    badges: List[Any]
    levels: List["CommunityReputationCatalogResponseLevel"]


class CommunityReputationCreateBadgeParams(TypedDict, total=False):
    slug: str
    name: str
    description: str
    icon: str
    tier: str
    grouping: Optional[str]
    counter: Optional[str]
    threshold: Optional[int]
    allowTitle: bool


class CommunityReputationCreateBadgeResponse(TypedDict, total=False):
    badge: Any
    data: Any
    warnings: List[str]


class CommunityReputationUpdateBadgeParams(TypedDict, total=False):
    slug: str
    name: str
    description: str
    icon: str
    tier: str
    grouping: Optional[str]
    counter: Optional[str]
    threshold: Optional[int]
    allowTitle: bool
    enabled: bool


class CommunityReputationUpdateBadgeResponse(TypedDict, total=False):
    badge: Any
    warnings: List[str]


class CommunityReputationDeleteBadgeResponse(TypedDict, total=False):
    ok: bool


class CommunityReputationGrantBadgeParams(TypedDict, total=False):
    slug: str


class CommunityReputationGrantBadgeResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class CommunityReputationRevokeBadgeResponse(TypedDict, total=False):
    ok: bool


class CommunityReputationRecomputeResponse(TypedDict, total=False):
    changed: List["RecomputedTrust"]
    members: float


class CommunityReputationMeResponse(TypedDict, total=False):
    badges: List["BadgeSummary"]
    external: List["ExternalStanding"]
    trust: "TrustSummary"


class CommunityReputationSetExternalParams(TypedDict, total=False):
    source: str
    label: str
    value: Optional[int]
    tier: Optional[str]
    profileUrl: Optional[str]
    icon: Optional[str]
    iconUrl: Optional[str]


class CommunityReputationSetExternalResponse(TypedDict, total=False):
    standing: "ExternalStanding"
    warnings: List[str]


class CommunityReputationRemoveExternalResponse(TypedDict, total=False):
    ok: bool


class CommunityReputationGetFeaturedResponse(TypedDict, total=False):
    earned: List["BadgeSummary"]
    featured: List["BadgeSummary"]


class CommunityReputationSetFeaturedParams(TypedDict, total=False):
    slugs: List[str]


class CommunityReputationSetFeaturedResponse(TypedDict, total=False):
    featured: List["BadgeSummary"]
    warnings: List[str]


class CommunityReputationSetFeaturedTopicParams(TypedDict, total=False):
    topicId: Optional[str]


class CommunityReputationSetFeaturedTopicResponse(TypedDict, total=False):
    featuredTopic: Optional["FeaturedTopic"]
    warnings: List[str]


class CommunityReputationSetBackgroundsParams(TypedDict, total=False):
    profileBackgroundUrl: Optional[str]
    cardBackgroundUrl: Optional[str]


class CommunityReputationSetBackgroundsResponse(TypedDict, total=False):
    cardBackgroundUrl: Any
    profileBackgroundUrl: Any
    warnings: List[str]


class CommunityReputationLeaderboardResponseLeader(TypedDict, total=False):
    label: str
    level: float
    likesGiven: float
    likesReceived: float
    name: str
    postsCreated: float
    solutions: float
    staff: bool
    topicsCreated: float
    userId: str


class CommunityReputationLeaderboardResponse(TypedDict, total=False):
    leaders: List["CommunityReputationLeaderboardResponseLeader"]
    page: "PageInfo"


class CommunityReputationPointsLeaderboardResponse(TypedDict, total=False):
    leaders: List["PointsLeader"]


class CommunityReputationDirectoryResponse(TypedDict, total=False):
    members: List[Any]
    page: "PageInfo"
    period: str


class CommunityReputationForUserResponse(TypedDict, total=False):
    badges: List["BadgeSummary"]
    external: List["ExternalStanding"]
    trust: "TrustSummary"


class CommunityReputationSetLevelParams(TypedDict, total=False):
    level: int


class CommunityReputationSetLevelResponse(TypedDict, total=False):
    trust: "TrustSummary"
    warnings: List[str]


class CommunityReputationUnfurlLinkResponse(TypedDict, total=False):
    preview: "Unfurled"


class PublicOneboxOneboxResponse(TypedDict, total=False):
    onebox: "Onebox"


class PublicOneboxInlineResponse(TypedDict, total=False):
    inline: Any


class PublicOneboxOneboxPostParamsContent(TypedDict, total=False):
    content: List[Any]


class PublicOneboxOneboxPostParams(TypedDict, total=False):
    content: "PublicOneboxOneboxPostParamsContent"


class PublicOneboxOneboxPostResponse(TypedDict, total=False):
    oneboxes: List["Onebox"]
    warnings: List[str]


class GroupsListResponse(TypedDict, total=False):
    groups: List["GroupSummary"]
    page: "PageInfo"


class GroupsCreateParams(TypedDict, total=False):
    name: str
    description: str
    visibility: str
    joinPolicy: str
    flair: Optional[str]
    title: Optional[str]
    flairIcon: Optional[str]
    flairColor: Optional[str]
    flairBgColor: Optional[str]
    bio: Optional[str]
    grantTrustLevel: Optional[int]
    autoJoinDomains: Optional[str]
    membersVisibility: str
    mentionableLevel: str
    messageableLevel: str
    defaultNotificationLevel: str
    watchedCategoryIds: List[str]
    watchedTagIds: List[str]
    categoryNotificationDefaults: Dict[str, Any]
    tagNotificationDefaults: Dict[str, Any]


class GroupsCreateResponse(TypedDict, total=False):
    group: "GroupDetail"
    data: "GroupDetail"
    warnings: List[str]


class GroupsGetResponse(TypedDict, total=False):
    group: "GroupDetail"


class GroupsUpdateParams(TypedDict, total=False):
    name: str
    description: str
    visibility: str
    joinPolicy: str
    flair: Optional[str]
    title: Optional[str]
    flairIcon: Optional[str]
    flairColor: Optional[str]
    flairBgColor: Optional[str]
    bio: Optional[str]
    grantTrustLevel: Optional[int]
    autoJoinDomains: Optional[str]
    membersVisibility: str
    mentionableLevel: str
    messageableLevel: str
    defaultNotificationLevel: str
    watchedCategoryIds: List[str]
    watchedTagIds: List[str]
    categoryNotificationDefaults: Dict[str, Any]
    tagNotificationDefaults: Dict[str, Any]
    inboxEmail: Optional[str]
    inboxEnabled: bool


class GroupsUpdateResponse(TypedDict, total=False):
    group: "GroupDetail"
    warnings: List[str]


class GroupsRemoveResponse(TypedDict, total=False):
    ok: bool


class GroupsAddMemberParams(TypedDict, total=False):
    userId: str
    isManager: bool


class GroupsAddMemberResponse(TypedDict, total=False):
    group: "GroupDetail"
    warnings: List[str]


class GroupsRemoveMemberResponse(TypedDict, total=False):
    group: "GroupDetail"


class GroupsJoinResponse(TypedDict, total=False):
    joined: bool
    pending: bool


class GroupsLeaveResponse(TypedDict, total=False):
    ok: bool


class GroupsRequestsResponse(TypedDict, total=False):
    requests: List["JoinRequestRow"]
    page: "PageInfo"


class GroupsReviewParams(TypedDict, total=False):
    action: str


class GroupsReviewResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class GroupsIdentitySetParams(TypedDict, total=False):
    title: Optional[str]
    primaryGroupId: Optional[str]


class GroupsMailboxGetResponse(TypedDict, total=False):
    mailbox: "GroupMailboxStatus"


class GroupsMailboxSetParamsConfigSettings(TypedDict, total=False):
    imapHost: str
    imapPort: int
    imapUser: str
    imapTls: bool
    imapFolder: str
    smtpHost: str
    smtpPort: int
    smtpUser: str
    smtpTls: bool


class GroupsMailboxSetParamsConfigSecret(TypedDict, total=False):
    imapPassword: str
    smtpPassword: str


class GroupsMailboxSetParamsConfig(TypedDict, total=False):
    provider: str
    settings: "GroupsMailboxSetParamsConfigSettings"
    secret: "GroupsMailboxSetParamsConfigSecret"


class GroupsMailboxSetParams(TypedDict, total=False):
    fromEmail: str
    enabled: bool
    config: "GroupsMailboxSetParamsConfig"


class GroupsMailboxSetResponse(TypedDict, total=False):
    mailbox: "GroupMailboxStatus"
    warnings: List[str]


class GroupsMailboxClearResponse(TypedDict, total=False):
    ok: bool


class DraftsListResponse(TypedDict, total=False):
    drafts: List["DraftSummary"]
    page: "PageInfo"


class DraftsGetResponse(TypedDict, total=False):
    draft: Any


class DraftsSaveParams(TypedDict, total=False):
    content: str


class DraftsSaveResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class DraftsRemoveResponse(TypedDict, total=False):
    ok: bool


class ModerationReviewablesResponse(TypedDict, total=False):
    reviewables: List["Reviewable"]
    page: "PageInfo"


class ModerationReviewFlagParams(TypedDict, total=False):
    action: str
    reason: str


class ModerationReviewFlagResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ModerationReviewFlagsBulkParams(TypedDict, total=False):
    flagIds: List[str]
    action: str


class ModerationReviewFlagsBulkResponse(TypedDict, total=False):
    handled: float
    ok: bool
    warnings: List[str]


class ModerationReviewPostParams(TypedDict, total=False):
    action: str
    reason: str


class ModerationReviewPostResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ModerationClaimFlagResponse(TypedDict, total=False):
    ok: bool


class ModerationUnclaimFlagResponse(TypedDict, total=False):
    ok: bool


class ModerationSetPriorityParams(TypedDict, total=False):
    priority: str


class ModerationSetPriorityResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ModerationDeleteAndBlockParams(TypedDict, total=False):
    kind: str
    reason: str


class ModerationDeleteAndBlockResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ModerationHardDeletePostResponse(TypedDict, total=False):
    ok: bool


class ModerationHardDeleteTopicResponse(TypedDict, total=False):
    ok: bool


class ModerationFlagHistoryResponse(TypedDict, total=False):
    history: List["FlagHistoryEntry"]
    page: "PageInfo"


class ModerationListWordsResponse(TypedDict, total=False):
    words: List["WatchedWordSummary"]
    page: "PageInfo"


class ModerationAddWordParams(TypedDict, total=False):
    word: str
    action: str
    replacement: str
    caseSensitive: bool
    isRegex: bool


class ModerationAddWordResponse(TypedDict, total=False):
    word: "WatchedWordSummary"
    data: "WatchedWordSummary"
    warnings: List[str]


class ModerationRemoveWordResponse(TypedDict, total=False):
    ok: bool


class ModerationListSuspensionsResponse(TypedDict, total=False):
    suspensions: List["SuspensionSummary"]
    page: "PageInfo"


class ModerationSuspendParams(TypedDict, total=False):
    kind: str
    reason: str
    expiresAt: Optional[str]


class ModerationSuspendResponse(TypedDict, total=False):
    suspension: "SuspensionSummary"
    data: "SuspensionSummary"
    warnings: List[str]


class ModerationLiftResponse(TypedDict, total=False):
    ok: bool


class ModerationAnonymizeResponseAnonymized(TypedDict, total=False):
    posts: float
    topics: float


class ModerationAnonymizeResponse(TypedDict, total=False):
    anonymized: "ModerationAnonymizeResponseAnonymized"


class ModerationSelfAnonymizeResponseAnonymized(TypedDict, total=False):
    posts: float
    topics: float


class ModerationSelfAnonymizeResponse(TypedDict, total=False):
    anonymized: "ModerationSelfAnonymizeResponseAnonymized"


class ModerationListWatchedUsersResponse(TypedDict, total=False):
    watchedUsers: List["WatchedUserRow"]
    page: "PageInfo"


class ModerationWatchUserParams(TypedDict, total=False):
    reason: str


class ModerationWatchUserResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ModerationUnwatchUserResponse(TypedDict, total=False):
    ok: bool


class ModerationLogResponse(TypedDict, total=False):
    actions: List["StaffActionSummary"]
    page: "PageInfo"


class CommunityCannedRepliesListResponse(TypedDict, total=False):
    cannedReplies: List["CannedReplyRow"]
    page: "PageInfo"


class CommunityCannedRepliesCreateParams(TypedDict, total=False):
    title: str
    body: Dict[str, Any]
    spaceId: Optional[str]


class CommunityCannedRepliesCreateResponse(TypedDict, total=False):
    cannedReply: "CannedReplyRow"
    data: "CannedReplyRow"
    warnings: List[str]


class CommunityCannedRepliesUpdateParams(TypedDict, total=False):
    title: str
    body: Dict[str, Any]


class CommunityCannedRepliesUpdateResponse(TypedDict, total=False):
    cannedReply: "CannedReplyRow"
    warnings: List[str]


class CommunityCannedRepliesRemoveResponse(TypedDict, total=False):
    ok: bool


class CommunityCannedRepliesUseResponse(TypedDict, total=False):
    cannedReply: "CannedReplyRow"


class CommunityRelationshipsSetStatusParams(TypedDict, total=False):
    emoji: Optional[str]
    message: Optional[str]
    until: Optional[str]


class CommunityRelationshipsSetStatusResponse(TypedDict, total=False):
    status: "UserStatus"
    warnings: List[str]


class CommunityRelationshipsClearStatusResponse(TypedDict, total=False):
    ok: bool


class CommunityRelationshipsListResponse(TypedDict, total=False):
    relationships: List["RelationshipRow"]
    page: "PageInfo"


class CommunityRelationshipsMuteParams(TypedDict, total=False):
    mode: str
    expiresAt: Optional[str]


class CommunityRelationshipsMuteResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class CommunityRelationshipsUnmuteResponse(TypedDict, total=False):
    ok: bool


class CommunityRelationshipsFollowResponse(TypedDict, total=False):
    following: bool


class CommunityRelationshipsUnfollowResponse(TypedDict, total=False):
    following: bool


class CommunityRelationshipsCardResponse(TypedDict, total=False):
    card: "UserCard"


class ChangelogListResponse(TypedDict, total=False):
    page: "PageInfo"
    releases: List["ArticleDetail"]


class ChangelogCreateParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ChangelogCreateParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ChangelogCreateParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ChangelogCreateParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class ChangelogCreateParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class ChangelogCreateParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ChangelogCreateParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ChangelogCreateParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class ChangelogCreateParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class ChangelogCreateParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ChangelogCreateParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class ChangelogCreateParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ChangelogCreateParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ChangelogCreateParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "ChangelogCreateParamsCustomizationThemeComponentsFocus"
    code: "ChangelogCreateParamsCustomizationThemeComponentsCode"
    input: "ChangelogCreateParamsCustomizationThemeComponentsInput"
    button: "ChangelogCreateParamsCustomizationThemeComponentsButton"
    spacing: "ChangelogCreateParamsCustomizationThemeComponentsSpacing"
    selection: "ChangelogCreateParamsCustomizationThemeComponentsSelection"
    scrollbar: "ChangelogCreateParamsCustomizationThemeComponentsScrollbar"
    syntax: "ChangelogCreateParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "ChangelogCreateParamsCustomizationThemeComponentsSyntaxDark"


class ChangelogCreateParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class ChangelogCreateParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class ChangelogCreateParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ChangelogCreateParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class ChangelogCreateParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class ChangelogCreateParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["ChangelogCreateParamsCustomizationThemeMotionKeyframeStep"]


class ChangelogCreateParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "ChangelogCreateParamsCustomizationThemeMotionReveal"
    hover: "ChangelogCreateParamsCustomizationThemeMotionHover"
    header: "ChangelogCreateParamsCustomizationThemeMotionHeader"
    ambient: "ChangelogCreateParamsCustomizationThemeMotionAmbient"
    keyframes: List["ChangelogCreateParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class ChangelogCreateParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "ChangelogCreateParamsCustomizationThemePalette"
    paletteDark: "ChangelogCreateParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "ChangelogCreateParamsCustomizationThemeLayout"
    components: "ChangelogCreateParamsCustomizationThemeComponents"
    motion: "ChangelogCreateParamsCustomizationThemeMotion"


class ChangelogCreateParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["ChangelogCreateParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class ChangelogCreateParams(TypedDict, total=False):
    title: str
    content: "ChangelogCreateParamsContent"
    version: Optional[str]
    publishedAt: str
    shippedTopicIds: List[str]
    tags: List[str]
    fields: Dict[str, Any]
    onThisPage: Optional[str]
    customization: Optional["ChangelogCreateParamsCustomization"]
    markdown: str


class ChangelogCreateResponse(TypedDict, total=False):
    release: "ArticleDetail"
    data: "ArticleDetail"
    warnings: List[str]


class ChangelogPublishResponse(TypedDict, total=False):
    release: "ArticleDetail"


class ChangelogGetResponse(TypedDict, total=False):
    release: "ArticleDetail"


class ChangelogUpdateParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ChangelogUpdateParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ChangelogUpdateParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ChangelogUpdateParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class ChangelogUpdateParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class ChangelogUpdateParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ChangelogUpdateParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ChangelogUpdateParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class ChangelogUpdateParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class ChangelogUpdateParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ChangelogUpdateParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class ChangelogUpdateParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ChangelogUpdateParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ChangelogUpdateParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "ChangelogUpdateParamsCustomizationThemeComponentsFocus"
    code: "ChangelogUpdateParamsCustomizationThemeComponentsCode"
    input: "ChangelogUpdateParamsCustomizationThemeComponentsInput"
    button: "ChangelogUpdateParamsCustomizationThemeComponentsButton"
    spacing: "ChangelogUpdateParamsCustomizationThemeComponentsSpacing"
    selection: "ChangelogUpdateParamsCustomizationThemeComponentsSelection"
    scrollbar: "ChangelogUpdateParamsCustomizationThemeComponentsScrollbar"
    syntax: "ChangelogUpdateParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "ChangelogUpdateParamsCustomizationThemeComponentsSyntaxDark"


class ChangelogUpdateParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class ChangelogUpdateParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class ChangelogUpdateParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ChangelogUpdateParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class ChangelogUpdateParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class ChangelogUpdateParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["ChangelogUpdateParamsCustomizationThemeMotionKeyframeStep"]


class ChangelogUpdateParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "ChangelogUpdateParamsCustomizationThemeMotionReveal"
    hover: "ChangelogUpdateParamsCustomizationThemeMotionHover"
    header: "ChangelogUpdateParamsCustomizationThemeMotionHeader"
    ambient: "ChangelogUpdateParamsCustomizationThemeMotionAmbient"
    keyframes: List["ChangelogUpdateParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class ChangelogUpdateParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "ChangelogUpdateParamsCustomizationThemePalette"
    paletteDark: "ChangelogUpdateParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "ChangelogUpdateParamsCustomizationThemeLayout"
    components: "ChangelogUpdateParamsCustomizationThemeComponents"
    motion: "ChangelogUpdateParamsCustomizationThemeMotion"


class ChangelogUpdateParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["ChangelogUpdateParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class ChangelogUpdateParams(TypedDict, total=False):
    title: str
    content: "ChangelogUpdateParamsContent"
    version: Optional[str]
    publishedAt: str
    shippedTopicIds: List[str]
    tags: List[str]
    fields: Dict[str, Any]
    onThisPage: Optional[str]
    customization: Optional["ChangelogUpdateParamsCustomization"]
    editReason: str
    markdown: str


class ChangelogUpdateResponse(TypedDict, total=False):
    release: "ArticleDetail"
    warnings: List[str]


class ChangelogRemoveResponse(TypedDict, total=False):
    ok: bool


class ChangelogScheduleParams(TypedDict, total=False):
    publishAt: str


class ChangelogScheduleResponse(TypedDict, total=False):
    release: "ArticleDetail"
    warnings: List[str]


class ChangelogUnscheduleResponse(TypedDict, total=False):
    release: "ArticleDetail"


class PublicChangelogCommentParams(TypedDict, total=False):
    authorName: str
    content: Dict[str, Any]
    parentPostId: Optional[str]
    captchaToken: str
    markdown: str


class PublicChangelogCommentResponse(TypedDict, total=False):
    post: "PostSummary"
    warnings: List[str]


class PublicChangelogReleaseResponse(TypedDict, total=False):
    release: "ArticleDetail"


class PublicChangelogReactParams(TypedDict, total=False):
    emoji: str


class PublicChangelogReactResponse(TypedDict, total=False):
    reacted: bool
    reactions: Dict[str, Any]
    warnings: List[str]


class PublicChangelogSubscribeParams(TypedDict, total=False):
    email: str
    captchaToken: str


class PublicChangelogSubscribeResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class EventsListResponse(TypedDict, total=False):
    events: List["EventSummary"]
    page: "PageInfo"


class EventsCreateParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class EventsCreateParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class EventsCreateParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class EventsCreateParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class EventsCreateParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class EventsCreateParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class EventsCreateParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class EventsCreateParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class EventsCreateParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class EventsCreateParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class EventsCreateParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class EventsCreateParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class EventsCreateParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "EventsCreateParamsCustomizationThemeComponentsFocus"
    code: "EventsCreateParamsCustomizationThemeComponentsCode"
    input: "EventsCreateParamsCustomizationThemeComponentsInput"
    button: "EventsCreateParamsCustomizationThemeComponentsButton"
    spacing: "EventsCreateParamsCustomizationThemeComponentsSpacing"
    selection: "EventsCreateParamsCustomizationThemeComponentsSelection"
    scrollbar: "EventsCreateParamsCustomizationThemeComponentsScrollbar"
    syntax: "EventsCreateParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "EventsCreateParamsCustomizationThemeComponentsSyntaxDark"


class EventsCreateParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class EventsCreateParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class EventsCreateParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class EventsCreateParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class EventsCreateParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class EventsCreateParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["EventsCreateParamsCustomizationThemeMotionKeyframeStep"]


class EventsCreateParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "EventsCreateParamsCustomizationThemeMotionReveal"
    hover: "EventsCreateParamsCustomizationThemeMotionHover"
    header: "EventsCreateParamsCustomizationThemeMotionHeader"
    ambient: "EventsCreateParamsCustomizationThemeMotionAmbient"
    keyframes: List["EventsCreateParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class EventsCreateParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "EventsCreateParamsCustomizationThemePalette"
    paletteDark: "EventsCreateParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "EventsCreateParamsCustomizationThemeLayout"
    components: "EventsCreateParamsCustomizationThemeComponents"
    motion: "EventsCreateParamsCustomizationThemeMotion"


class EventsCreateParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["EventsCreateParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class EventsCreateParams(TypedDict, total=False):
    title: str
    description: str
    location: Optional[str]
    url: Optional[str]
    startsAt: str
    endsAt: Optional[str]
    timezone: str
    capacity: Optional[int]
    coverUrl: Optional[str]
    state: str
    topicId: Optional[str]
    customization: Optional["EventsCreateParamsCustomization"]


class EventsCreateResponse(TypedDict, total=False):
    event: "EventSummary"
    data: "EventSummary"
    warnings: List[str]


class EventsListAllEventsResponse(TypedDict, total=False):
    events: List["EventSummary"]
    page: "PageInfo"


class EventsUpdateParamsCustomizationThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class EventsUpdateParamsCustomizationThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class EventsUpdateParamsCustomizationThemeLayout(TypedDict, total=False):
    measure: str


class EventsUpdateParamsCustomizationThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class EventsUpdateParamsCustomizationThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class EventsUpdateParamsCustomizationThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class EventsUpdateParamsCustomizationThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class EventsUpdateParamsCustomizationThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class EventsUpdateParamsCustomizationThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class EventsUpdateParamsCustomizationThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class EventsUpdateParamsCustomizationThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class EventsUpdateParamsCustomizationThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class EventsUpdateParamsCustomizationThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "EventsUpdateParamsCustomizationThemeComponentsFocus"
    code: "EventsUpdateParamsCustomizationThemeComponentsCode"
    input: "EventsUpdateParamsCustomizationThemeComponentsInput"
    button: "EventsUpdateParamsCustomizationThemeComponentsButton"
    spacing: "EventsUpdateParamsCustomizationThemeComponentsSpacing"
    selection: "EventsUpdateParamsCustomizationThemeComponentsSelection"
    scrollbar: "EventsUpdateParamsCustomizationThemeComponentsScrollbar"
    syntax: "EventsUpdateParamsCustomizationThemeComponentsSyntax"
    syntaxDark: "EventsUpdateParamsCustomizationThemeComponentsSyntaxDark"


class EventsUpdateParamsCustomizationThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class EventsUpdateParamsCustomizationThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class EventsUpdateParamsCustomizationThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class EventsUpdateParamsCustomizationThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class EventsUpdateParamsCustomizationThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class EventsUpdateParamsCustomizationThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["EventsUpdateParamsCustomizationThemeMotionKeyframeStep"]


class EventsUpdateParamsCustomizationThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "EventsUpdateParamsCustomizationThemeMotionReveal"
    hover: "EventsUpdateParamsCustomizationThemeMotionHover"
    header: "EventsUpdateParamsCustomizationThemeMotionHeader"
    ambient: "EventsUpdateParamsCustomizationThemeMotionAmbient"
    keyframes: List["EventsUpdateParamsCustomizationThemeMotionKeyframe"]
    targets: Dict[str, Any]


class EventsUpdateParamsCustomizationTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "EventsUpdateParamsCustomizationThemePalette"
    paletteDark: "EventsUpdateParamsCustomizationThemePaletteDark"
    font: str
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    colorScheme: str
    contentWidth: str
    layout: "EventsUpdateParamsCustomizationThemeLayout"
    components: "EventsUpdateParamsCustomizationThemeComponents"
    motion: "EventsUpdateParamsCustomizationThemeMotion"


class EventsUpdateParamsCustomization(TypedDict, total=False):
    customCss: Optional[str]
    theme: Optional["EventsUpdateParamsCustomizationTheme"]
    shareImageUrl: Optional[Any]
    ogTitle: Optional[str]
    ogDescription: Optional[str]
    twitterCard: Optional[str]
    jsonLd: Optional[str]


class EventsUpdateParams(TypedDict, total=False):
    title: str
    description: str
    location: Optional[str]
    url: Optional[str]
    startsAt: str
    endsAt: Optional[str]
    timezone: str
    capacity: Optional[int]
    coverUrl: Optional[str]
    state: str
    topicId: Optional[str]
    customization: Optional["EventsUpdateParamsCustomization"]


class EventsMyRsvpResponse(TypedDict, total=False):
    status: Any


class EventsRsvpParams(TypedDict, total=False):
    status: str


class PublicEventsListResponse(TypedDict, total=False):
    events: List["EventSummary"]
    page: "PageInfo"


class EmbedFeedsListResponseFeed(TypedDict, total=False):
    author: Any
    categoryId: Any
    createdAt: Any
    cursor: Any
    enabled: Any
    feedUrl: Any
    id: Any
    lastError: Any
    lastPolledAt: Any
    organizationId: Any
    pollIntervalMinutes: Any
    spaceId: Any
    updatedAt: Any


class EmbedFeedsListResponse(TypedDict, total=False):
    feeds: List["EmbedFeedsListResponseFeed"]
    page: "PageInfo"


class EmbedFeedsAddParams(TypedDict, total=False):
    spaceId: str
    feedUrl: str
    categoryId: Optional[str]
    author: Optional[str]
    enabled: bool
    pollIntervalMinutes: int


class EmbedFeedsAddResponseFeed(TypedDict, total=False):
    author: Any
    categoryId: Any
    createdAt: Any
    cursor: Any
    enabled: Any
    feedUrl: Any
    id: Any
    lastError: Any
    lastPolledAt: Any
    organizationId: Any
    pollIntervalMinutes: Any
    spaceId: Any
    updatedAt: Any


class EmbedFeedsAddResponseData(TypedDict, total=False):
    author: Any
    categoryId: Any
    createdAt: Any
    cursor: Any
    enabled: Any
    feedUrl: Any
    id: Any
    lastError: Any
    lastPolledAt: Any
    organizationId: Any
    pollIntervalMinutes: Any
    spaceId: Any
    updatedAt: Any


class EmbedFeedsAddResponse(TypedDict, total=False):
    feed: "EmbedFeedsAddResponseFeed"
    data: "EmbedFeedsAddResponseData"
    warnings: List[str]


class EmbedFeedsUpdateParams(TypedDict, total=False):
    spaceId: str
    categoryId: Optional[str]
    author: Optional[str]
    enabled: bool
    pollIntervalMinutes: int


class EmbedFeedsUpdateResponseFeed(TypedDict, total=False):
    author: Any
    categoryId: Any
    createdAt: Any
    cursor: Any
    enabled: Any
    feedUrl: Any
    id: Any
    lastError: Any
    lastPolledAt: Any
    organizationId: Any
    pollIntervalMinutes: Any
    spaceId: Any
    updatedAt: Any


class EmbedFeedsUpdateResponse(TypedDict, total=False):
    feed: "EmbedFeedsUpdateResponseFeed"
    warnings: List[str]


class EmbedFeedsRemoveResponse(TypedDict, total=False):
    ok: bool


class EmbedFeedsPollNowResponse(TypedDict, total=False):
    imported: float


class ModerationFlagTypesListResponseFlagType(TypedDict, total=False):
    appliesTo: Any
    createdAt: Any
    description: Any
    enabled: Any
    id: Any
    name: Any
    organizationId: Any
    updatedAt: Any


class ModerationFlagTypesListResponse(TypedDict, total=False):
    catalogue: List["FlagTypeCatalogueEntry"]
    flagTypes: List["ModerationFlagTypesListResponseFlagType"]


class ModerationFlagTypesAddParams(TypedDict, total=False):
    name: str
    description: str
    enabled: bool
    appliesTo: str


class ModerationFlagTypesAddResponseFlagType(TypedDict, total=False):
    appliesTo: Any
    createdAt: Any
    description: Any
    enabled: Any
    id: Any
    name: Any
    organizationId: Any
    updatedAt: Any


class ModerationFlagTypesAddResponseData(TypedDict, total=False):
    appliesTo: Any
    createdAt: Any
    description: Any
    enabled: Any
    id: Any
    name: Any
    organizationId: Any
    updatedAt: Any


class ModerationFlagTypesAddResponse(TypedDict, total=False):
    flagType: "ModerationFlagTypesAddResponseFlagType"
    data: "ModerationFlagTypesAddResponseData"
    warnings: List[str]


class ModerationFlagTypesCatalogueResponse(TypedDict, total=False):
    catalogue: List["FlagTypeCatalogueEntry"]
    page: "PageInfo"


class ModerationFlagTypesUpdateParams(TypedDict, total=False):
    description: str
    enabled: bool
    appliesTo: str


class ModerationFlagTypesUpdateResponseFlagType(TypedDict, total=False):
    appliesTo: Any
    createdAt: Any
    description: Any
    enabled: Any
    id: Any
    name: Any
    organizationId: Any
    updatedAt: Any


class ModerationFlagTypesUpdateResponse(TypedDict, total=False):
    flagType: "ModerationFlagTypesUpdateResponseFlagType"
    warnings: List[str]


class ModerationFlagTypesRemoveResponse(TypedDict, total=False):
    ok: bool


class FormsTemplatesListResponseFormTemplate(TypedDict, total=False):
    createdAt: Any
    id: Any
    name: Any
    organizationId: Any
    spaceId: Any
    template: Any
    updatedAt: Any


class FormsTemplatesListResponse(TypedDict, total=False):
    formTemplates: List["FormsTemplatesListResponseFormTemplate"]
    page: "PageInfo"


class FormsTemplatesCreateParamsTemplateItem(TypedDict, total=False):
    id: str
    type: str
    label: str
    description: str
    placeholder: str
    required: bool
    choices: List[str]


class FormsTemplatesCreateParams(TypedDict, total=False):
    name: str
    template: List["FormsTemplatesCreateParamsTemplateItem"]


class FormsTemplatesCreateResponseFormTemplate(TypedDict, total=False):
    createdAt: Any
    id: Any
    name: Any
    organizationId: Any
    spaceId: Any
    template: Any
    updatedAt: Any


class FormsTemplatesCreateResponseData(TypedDict, total=False):
    createdAt: Any
    id: Any
    name: Any
    organizationId: Any
    spaceId: Any
    template: Any
    updatedAt: Any


class FormsTemplatesCreateResponse(TypedDict, total=False):
    formTemplate: "FormsTemplatesCreateResponseFormTemplate"
    data: "FormsTemplatesCreateResponseData"
    warnings: List[str]


class FormsTemplatesGetResponseFormTemplate(TypedDict, total=False):
    createdAt: Any
    id: Any
    name: Any
    organizationId: Any
    spaceId: Any
    template: Any
    updatedAt: Any


class FormsTemplatesGetResponse(TypedDict, total=False):
    formTemplate: "FormsTemplatesGetResponseFormTemplate"


class FormsTemplatesUpdateParamsTemplateItem(TypedDict, total=False):
    id: str
    type: str
    label: str
    description: str
    placeholder: str
    required: bool
    choices: List[str]


class FormsTemplatesUpdateParams(TypedDict, total=False):
    name: str
    template: List["FormsTemplatesUpdateParamsTemplateItem"]


class FormsTemplatesUpdateResponseFormTemplate(TypedDict, total=False):
    createdAt: Any
    id: Any
    name: Any
    organizationId: Any
    spaceId: Any
    template: Any
    updatedAt: Any


class FormsTemplatesUpdateResponse(TypedDict, total=False):
    formTemplate: "FormsTemplatesUpdateResponseFormTemplate"
    warnings: List[str]


class FormsTemplatesRemoveResponse(TypedDict, total=False):
    ok: bool


class FormsTemplatesAttachParams(TypedDict, total=False):
    categoryId: str
    formTemplateId: Optional[str]


class FormsTemplatesAttachResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class DocsAiReviewParams(TypedDict, total=False):
    recentChanges: str


class DocsAiReviewResponse(TypedDict, total=False):
    report: "FreshnessReport"
    warnings: List[str]


class DocsAiRewriteParams(TypedDict, total=False):
    content: Any
    instruction: str


class DocsAiRewriteResponse(TypedDict, total=False):
    content: "BlockDoc"
    warnings: List[str]


class DocsAiTranslateParams(TypedDict, total=False):
    content: Any
    language: str


class DocsAiTranslateResponse(TypedDict, total=False):
    content: "BlockDoc"
    warnings: List[str]


class DocsAiAskParams(TypedDict, total=False):
    question: str


class DocsAiAskResponse(TypedDict, total=False):
    result: "AnswerResult"
    warnings: List[str]


class DocsAiAskStreamParams(TypedDict, total=False):
    question: str


class DocsAiAskFeedbackParams(TypedDict, total=False):
    helpful: bool
    comment: str


class DocsAiAskFeedbackResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class DocsAiAgentParams(TypedDict, total=False):
    collectionId: str
    instruction: str


class DocsAiAgentResponsePage(TypedDict, total=False):
    id: str
    title: str


class DocsAiAgentResponseData(TypedDict, total=False):
    id: str
    title: str


class DocsAiAgentResponse(TypedDict, total=False):
    page: "DocsAiAgentResponsePage"
    data: "DocsAiAgentResponseData"
    warnings: List[str]


class AiListSourcesResponse(TypedDict, total=False):
    sources: List["AiSourceSummary"]
    page: "PageInfo"


class AiAddSourceParams(TypedDict, total=False):
    spaceId: Optional[str]
    kind: str
    title: str
    url: str
    content: str


class AiAddSourceResponse(TypedDict, total=False):
    id: str
    data: str
    warnings: List[str]


class AiRemoveSourceResponse(TypedDict, total=False):
    ok: bool


class AiAskParams(TypedDict, total=False):
    question: str


class AiAskResponse(TypedDict, total=False):
    result: "OrgAnswer"
    warnings: List[str]


class AiProviderConnectParams(TypedDict, total=False):
    provider: str
    apiKey: str
    model: str


class AiProviderDisconnectResponse(TypedDict, total=False):
    ok: bool


class AiProviderTestResponse(TypedDict, total=False):
    model: str
    ok: bool


class SearchRetrieveParams(TypedDict, total=False):
    q: str
    roles: List[str]
    boost: Dict[str, Any]
    limit: int
    maxStalenessDays: int
    spaceIds: List[str]


class SearchRetrieveResponsePolicy(TypedDict, total=False):
    version: str


class SearchRetrieveResponse(TypedDict, total=False):
    chunks: List["RetrievedChunk"]
    policy: "SearchRetrieveResponsePolicy"
    warnings: List[str]


class SearchRecentResponse(TypedDict, total=False):
    queries: List[str]


class SearchSemanticSearchResponse(TypedDict, total=False):
    hits: List["SemanticHit"]


class SearchReindexResponseLexical(TypedDict, total=False):
    changed: float
    pages: float


class SearchReindexResponse(TypedDict, total=False):
    indexed: float
    lexical: "SearchReindexResponseLexical"
    linkSources: float
    topics: float


class SearchTagsResponseTag(TypedDict, total=False):
    count: float
    tag: str


class SearchTagsResponse(TypedDict, total=False):
    tags: List["SearchTagsResponseTag"]
    page: "PageInfo"


class SearchGapsResponse(TypedDict, total=False):
    gaps: List["KnowledgeGap"]


class SearchEmbeddingProviderStatusResponseIndexed(TypedDict, total=False):
    pages: float
    topics: float


class SearchEmbeddingProviderStatusResponse(TypedDict, total=False):
    dimensions: Any
    indexed: "SearchEmbeddingProviderStatusResponseIndexed"
    keyHint: Any
    maxDimensions: float
    model: Any
    provider: Any
    providers: List["ProviderSpec"]
    usingFallback: bool


class SearchEmbeddingProviderConnectParams(TypedDict, total=False):
    provider: str
    apiKey: str
    model: str
    dimensions: int


class SearchEmbeddingProviderConnectResponse(TypedDict, total=False):
    dimensions: Any
    keyHint: Any
    maxDimensions: float
    model: Any
    provider: Any
    providers: List["ProviderSpec"]
    reindexed: float
    usingFallback: bool
    warnings: List[str]


class SearchEmbeddingProviderDisconnectResponse(TypedDict, total=False):
    ok: bool
    reindexed: float


class SearchEmbeddingProviderTestResponse(TypedDict, total=False):
    dimensions: float
    model: str
    ok: bool


class SearchEmbeddingProviderReindexResponse(TypedDict, total=False):
    indexed: float
    topics: float


class EmbeddableHostsListResponseHost(TypedDict, total=False):
    allowedPaths: Any
    categoryId: Any
    className: Any
    createdAt: Any
    host: Any
    id: Any
    organizationId: Any
    postAuthor: Any
    updatedAt: Any


class EmbeddableHostsListResponse(TypedDict, total=False):
    hosts: List["EmbeddableHostsListResponseHost"]
    page: "PageInfo"


class EmbeddableHostsAddParams(TypedDict, total=False):
    host: str
    categoryId: Optional[str]
    postAuthor: Optional[str]
    allowedPaths: Optional[List[str]]
    className: Optional[str]


class EmbeddableHostsAddResponseHost(TypedDict, total=False):
    allowedPaths: Any
    categoryId: Any
    className: Any
    createdAt: Any
    host: Any
    id: Any
    organizationId: Any
    postAuthor: Any
    updatedAt: Any


class EmbeddableHostsAddResponseData(TypedDict, total=False):
    allowedPaths: Any
    categoryId: Any
    className: Any
    createdAt: Any
    host: Any
    id: Any
    organizationId: Any
    postAuthor: Any
    updatedAt: Any


class EmbeddableHostsAddResponse(TypedDict, total=False):
    host: "EmbeddableHostsAddResponseHost"
    data: "EmbeddableHostsAddResponseData"
    warnings: List[str]


class EmbeddableHostsRemoveResponse(TypedDict, total=False):
    ok: bool


class CustomEmojiListResponse(TypedDict, total=False):
    emoji: List["CustomEmoji"]
    page: "PageInfo"


class CustomEmojiUploadParams(TypedDict, total=False):
    file: str


class CustomEmojiUploadResponse(TypedDict, total=False):
    emoji: "CustomEmoji"
    data: "CustomEmoji"
    warnings: List[str]


class CustomEmojiRemoveResponse(TypedDict, total=False):
    ok: bool


class PublicCustomEmojiListResponseEmojiItem(TypedDict, total=False):
    imageUrl: str
    name: str
    shortcode: str


class PublicCustomEmojiListResponse(TypedDict, total=False):
    emoji: List["PublicCustomEmojiListResponseEmojiItem"]
    page: "PageInfo"


class ChatChannelsResponse(TypedDict, total=False):
    channels: List["ChannelSummary"]
    page: "PageInfo"


class ChatCreateChannelParams(TypedDict, total=False):
    name: str
    spaceId: Optional[str]
    visibility: str


class ChatCreateChannelResponse(TypedDict, total=False):
    channel: "ChannelSummary"
    data: "ChannelSummary"
    warnings: List[str]


class ChatArchiveParams(TypedDict, total=False):
    archived: bool


class ChatArchiveResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ChatCloseParams(TypedDict, total=False):
    closed: bool


class ChatCloseResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ChatArchiveToTopicParams(TypedDict, total=False):
    spaceId: str
    title: str


class ChatArchiveToTopicResponse(TypedDict, total=False):
    slug: str
    topicId: str
    warnings: List[str]


class ChatSetNotificationParams(TypedDict, total=False):
    level: str
    muted: bool


class ChatSetNotificationResponse(TypedDict, total=False):
    level: str
    muted: bool
    warnings: List[str]


class ChatJoinResponse(TypedDict, total=False):
    ok: bool


class ChatAddMemberParams(TypedDict, total=False):
    userId: str


class ChatAddMemberResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ChatListMessagesResponse(TypedDict, total=False):
    messages: List["ChatMessageSummary"]
    page: "PageInfo"


class ChatSendParamsAttachment(TypedDict, total=False):
    url: str
    name: str
    contentType: str


class ChatSendParams(TypedDict, total=False):
    body: str
    parentId: Optional[str]
    attachments: List["ChatSendParamsAttachment"]


class ChatSendResponse(TypedDict, total=False):
    message: "ChatMessageSummary"
    data: "ChatMessageSummary"
    warnings: List[str]


class ChatUpdateSettingsParams(TypedDict, total=False):
    slowModeSeconds: int
    autoJoin: bool
    retentionDays: Optional[int]
    allowedGroupId: Optional[str]


class ChatUpdateSettingsResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ChatListIncomingWebhooksResponse(TypedDict, total=False):
    webhooks: List["IncomingWebhookSummary"]
    page: "PageInfo"


class ChatCreateIncomingWebhookParams(TypedDict, total=False):
    name: str


class ChatRevokeIncomingWebhookResponse(TypedDict, total=False):
    ok: bool


class ChatReceiptsResponse(TypedDict, total=False):
    receipts: List["ReadReceipt"]
    page: "PageInfo"


class ChatPinsResponse(TypedDict, total=False):
    messages: List["ChatMessageSummary"]
    page: "PageInfo"


class ChatPinParams(TypedDict, total=False):
    pinned: bool


class ChatPinResponse(TypedDict, total=False):
    message: "ChatMessageSummary"
    warnings: List[str]


class ChatReadResponse(TypedDict, total=False):
    ok: bool


class ChatGetDraftResponse(TypedDict, total=False):
    draft: Any


class ChatPutDraftParams(TypedDict, total=False):
    body: str
    parentId: Optional[str]


class ChatPutDraftResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ChatDeleteDraftResponse(TypedDict, total=False):
    ok: bool


class ChatHeartbeatParams(TypedDict, total=False):
    viewerId: str
    typing: bool


class ChatHeartbeatResponse(TypedDict, total=False):
    present: float
    warnings: List[str]


class ChatOnlineResponseOnlineItem(TypedDict, total=False):
    avatarUrl: Any
    id: str
    name: str


class ChatOnlineResponse(TypedDict, total=False):
    online: List["ChatOnlineResponseOnlineItem"]
    page: "PageInfo"


class ChatMessagesThreadResponse(TypedDict, total=False):
    messages: List["ChatMessageSummary"]
    page: "PageInfo"


class ChatMessagesEditParams(TypedDict, total=False):
    body: str


class ChatMessagesEditResponse(TypedDict, total=False):
    message: "ChatMessageSummary"
    warnings: List[str]


class ChatMessagesRemoveResponse(TypedDict, total=False):
    ok: bool


class ChatMessagesReactParams(TypedDict, total=False):
    emoji: str


class ChatMessagesReactResponse(TypedDict, total=False):
    message: "ChatMessageSummary"
    warnings: List[str]


class ChatMessagesDmParams(TypedDict, total=False):
    userId: str


class ChatMessagesDmResponse(TypedDict, total=False):
    channel: "ChannelSummary"
    warnings: List[str]


class ChatMessagesGroupDmParams(TypedDict, total=False):
    userIds: List[str]


class ChatMessagesGroupDmResponse(TypedDict, total=False):
    channel: "ChannelSummary"
    warnings: List[str]


class ChatMessagesMessageLinkResponse(TypedDict, total=False):
    link: "MessageLink"


class ChatMessagesQuoteToTopicParams(TypedDict, total=False):
    spaceId: str
    title: str


class ChatMessagesQuoteToTopicResponse(TypedDict, total=False):
    slug: str
    topicId: str
    warnings: List[str]


class ChatMessagesFlagParams(TypedDict, total=False):
    reason: str
    flagType: str


class ChatMessagesFlagResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ChatMessagesBookmarkResponse(TypedDict, total=False):
    bookmarked: bool


class ChatMessagesRemoveBookmarkResponse(TypedDict, total=False):
    ok: bool


class ChatMessagesBookmarkReminderParams(TypedDict, total=False):
    preset: str
    remindAt: Optional[str]
    note: Optional[str]
    name: Optional[str]
    autoDelete: bool


class ChatMessagesBookmarkReminderResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ChatMessagesListBookmarksResponse(TypedDict, total=False):
    bookmarks: List["ChatBookmarkSummary"]
    page: "PageInfo"


class ChatMessagesMoveParams(TypedDict, total=False):
    messageIds: List[str]
    targetChannelId: str
    threadParentId: Optional[str]


class ChatMessagesMoveResponse(TypedDict, total=False):
    moved: float
    warnings: List[str]


class GroupsMessagesMessageParams(TypedDict, total=False):
    body: str


class GroupsMessagesMessageResponse(TypedDict, total=False):
    channel: "ChannelSummary"
    message: "ChatMessageSummary"
    warnings: List[str]


class GroupsMessagesInboxResponse(TypedDict, total=False):
    threads: List["ChannelSummary"]
    page: "PageInfo"


class ChatIncomingWebhooksPostParams(TypedDict, total=False):
    text: str
    body: str


class ChatIncomingWebhooksPostResponse(TypedDict, total=False):
    messageId: str
    ok: bool
    warnings: List[str]


class MessagesListResponse(TypedDict, total=False):
    conversations: List["ConversationSummary"]
    page: "PageInfo"


class MessagesStartParams(TypedDict, total=False):
    to: List[str]
    subject: Optional[str]
    content: str


class MessagesStartResponse(TypedDict, total=False):
    conversationId: str
    data: str
    warnings: List[str]


class MessagesRecipientsResponse(TypedDict, total=False):
    members: List["Candidate"]
    page: "PageInfo"


class MessagesUnreadCountResponse(TypedDict, total=False):
    count: float


class MessagesGetResponse(TypedDict, total=False):
    conversation: "ConversationDetail"


class MessagesReplyParams(TypedDict, total=False):
    content: str


class MessagesReplyResponse(TypedDict, total=False):
    messageId: str
    data: str
    warnings: List[str]


class MessagesArchiveParams(TypedDict, total=False):
    archived: bool


class MessagesArchiveResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class MessagesAddParticipantParams(TypedDict, total=False):
    userId: str


class MessagesAddParticipantResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class MessagesRemoveParticipantResponse(TypedDict, total=False):
    ok: bool


class ItemsCreateParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ItemsCreateParams(TypedDict, total=False):
    title: str
    slug: str
    preset: Optional[str]
    sections: Dict[str, Any]
    body: str
    content: "ItemsCreateParamsContent"
    params: Dict[str, Any]


class ItemsCreateResponse(TypedDict, total=False):
    item: "ItemRef"
    warnings: List[str]
    data: "ItemRef"


class ItemsPatchParams(TypedDict, total=False):
    title: str
    slug: str
    params: Dict[str, Any]


class ItemsPatchResponse(TypedDict, total=False):
    item: "ItemRef"
    warnings: List[str]


class ItemsRemoveResponse(TypedDict, total=False):
    ok: bool


class ItemsGetContentResponse(TypedDict, total=False):
    content: "BlockDoc"
    kind: str
    title: str


class ItemsPutContentParamsContent(TypedDict, total=False):
    type: str
    content: List[Any]


class ItemsPutContentParams(TypedDict, total=False):
    content: "ItemsPutContentParamsContent"
    body: str


class ItemsPutContentResponse(TypedDict, total=False):
    conformance: "Conformance"
    warnings: List[str]


class ItemsChunksResponsePolicy(TypedDict, total=False):
    maxTokens: float
    version: str


class ItemsChunksResponse(TypedDict, total=False):
    chunks: List["Chunk"]
    policy: "ItemsChunksResponsePolicy"


class ItemsVerifyResponse(TypedDict, total=False):
    freshness: "Freshness"


class ItemsPublishResponse(TypedDict, total=False):
    conformance: "Conformance"
    note: str
    published: bool


class ItemsFieldsResponse(TypedDict, total=False):
    fields: Dict[str, Any]


class ItemsSetFieldsParams(TypedDict, total=False):
    fields: Dict[str, Any]


class ItemsSetFieldsResponse(TypedDict, total=False):
    fields: Dict[str, Any]
    warnings: List[str]


class ItemsPutSectionParams(TypedDict, total=False):
    markdown: str


class ItemsPutSectionResponse(TypedDict, total=False):
    conformance: "Conformance"
    warnings: List[str]


class QuestionsListResponse(TypedDict, total=False):
    page: "PageInfo"
    questions: List["IngestedQuestion"]


class QuestionsIngestParamsQuestion(TypedDict, total=False):
    text: str
    askedAt: str
    outcome: str
    citedChunks: List[str]


class QuestionsIngestParams(TypedDict, total=False):
    source: str
    questions: List["QuestionsIngestParamsQuestion"]


class QuestionsClustersResponse(TypedDict, total=False):
    clusters: List["QuestionCluster"]
    page: "PageInfo"


class QuestionsRemoveResponse(TypedDict, total=False):
    deleted: float


class QuestionsDraftParams(TypedDict, total=False):
    max: int
    days: int
    preset: Optional[str]


class QuestionsDraftResponse(TypedDict, total=False):
    drafts: List["ProposedDraft"]
    warnings: List[str]


class QuestionsSuggestParams(TypedDict, total=False):
    source: str
    slot: str
    markdown: str
    note: str


class QuestionsListAssertionsResponse(TypedDict, total=False):
    assertions: List["AssertionView"]
    page: "PageInfo"


class QuestionsAddAssertionParams(TypedDict, total=False):
    slot: str
    kind: str
    target: str
    expects: str


class QuestionsAddAssertionResponse(TypedDict, total=False):
    assertion: "AssertionView"
    data: "AssertionView"
    warnings: List[str]


class QuestionsRunAssertionsResponse(TypedDict, total=False):
    assertions: List["AssertionView"]


class QuestionsRemoveAssertionResponse(TypedDict, total=False):
    ok: bool


class QuestionsUncoveredResponse(TypedDict, total=False):
    threads: List["UncoveredThread"]


class PublicRelationsResolveResponse(TypedDict, total=False):
    items: List["ResolvedRelation"]
    page: "PageInfo"


class StatusListChannelsResponse(TypedDict, total=False):
    channels: List["StatusChannel"]
    page: "PageInfo"


class StatusAddChannelParams(TypedDict, total=False):
    kind: str
    url: str
    label: str


class StatusAddChannelResponse(TypedDict, total=False):
    channel: "StatusChannel"
    data: "StatusChannel"
    warnings: List[str]


class StatusRemoveChannelResponse(TypedDict, total=False):
    ok: bool


class StatusMonitorsStatusResponse(TypedDict, total=False):
    monitors: List["MonitorSummary"]
    page: "PageInfo"


class StatusAddMonitorParams(TypedDict, total=False):
    name: str
    url: str
    method: str
    kind: str
    intervalSeconds: int
    visible: bool
    alertsEnabled: bool
    failureThreshold: int
    successThreshold: int
    keyword: Optional[str]
    certExpiryDays: Optional[int]
    expectStatus: Optional[int]
    maxLatencyMs: Optional[int]
    requestHeaders: Optional[Dict[str, Any]]
    requestBody: Optional[str]
    bodyPath: Optional[str]
    bodyExpect: Optional[str]
    group: Optional[str]
    declaredState: Optional[str]


class StatusAddMonitorResponse(TypedDict, total=False):
    monitor: "MonitorSummary"
    data: "MonitorSummary"
    warnings: List[str]


class StatusUpdateMonitorParams(TypedDict, total=False):
    name: str
    url: str
    method: str
    kind: str
    intervalSeconds: int
    visible: bool
    alertsEnabled: bool
    failureThreshold: int
    successThreshold: int
    keyword: Optional[str]
    certExpiryDays: Optional[int]
    expectStatus: Optional[int]
    maxLatencyMs: Optional[int]
    requestHeaders: Optional[Dict[str, Any]]
    requestBody: Optional[str]
    bodyPath: Optional[str]
    bodyExpect: Optional[str]
    group: Optional[str]
    declaredState: Optional[str]


class StatusUpdateMonitorResponse(TypedDict, total=False):
    monitor: "MonitorSummary"
    warnings: List[str]


class StatusRemoveMonitorResponse(TypedDict, total=False):
    ok: bool


class StatusGetSettingsResponse(TypedDict, total=False):
    autoIncident: bool
    notifySubscribers: bool
    subscribers: float


class StatusSetSettingsParams(TypedDict, total=False):
    autoIncident: bool
    notifySubscribers: bool


class StatusSetSettingsResponse(TypedDict, total=False):
    autoIncident: bool
    notifySubscribers: bool
    subscribers: float
    warnings: List[str]


class StatusCreateIncidentParamsFields(TypedDict, total=False):
    components: str
    postmortemUrl: str


class StatusCreateIncidentParams(TypedDict, total=False):
    title: str
    state: str
    severity: str
    body: Dict[str, Any]
    fields: "StatusCreateIncidentParamsFields"
    scheduledFor: Optional[str]
    scheduledUntil: Optional[str]


class StatusCreateIncidentResponse(TypedDict, total=False):
    incident: "IncidentSummary"
    data: "IncidentSummary"
    warnings: List[str]


class StatusUpdateIncidentParamsFields(TypedDict, total=False):
    components: str
    postmortemUrl: str


class StatusUpdateIncidentParams(TypedDict, total=False):
    title: str
    state: str
    severity: str
    body: Dict[str, Any]
    fields: "StatusUpdateIncidentParamsFields"
    scheduledFor: Optional[str]
    scheduledUntil: Optional[str]


class StatusUpdateIncidentResponse(TypedDict, total=False):
    incident: "IncidentSummary"
    warnings: List[str]


class StatusAddIncidentUpdateParams(TypedDict, total=False):
    body: str
    state: str


class StatusAddIncidentUpdateResponse(TypedDict, total=False):
    incident: "IncidentSummary"
    warnings: List[str]


class PublicStatusSubscribeParams(TypedDict, total=False):
    email: str


class PublicStatusSubscribeResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class StatusMonitorsPingGetResponse(TypedDict, total=False):
    ok: bool


class StatusMonitorsPingPostResponse(TypedDict, total=False):
    ok: bool


class StatusMonitorsReportParams(TypedDict, total=False):
    reason: str


class StatusMonitorsReportResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class UsersProgressionSignalParams(TypedDict, total=False):
    track: str
    amount: int
    reason: str
    idempotencyKey: str


class UsersWalletCreditParams(TypedDict, total=False):
    currency: str
    amount: int
    reason: str
    idempotencyKey: str


class UsersWalletDebitParams(TypedDict, total=False):
    currency: str
    amount: int
    reason: str
    idempotencyKey: str


class UsersWalletGrantItemParams(TypedDict, total=False):
    itemKey: str
    quantity: int
    name: str
    reason: str
    idempotencyKey: str


class UsersWalletConsumeItemParams(TypedDict, total=False):
    itemKey: str
    quantity: int
    name: str
    reason: str
    idempotencyKey: str


class PublicContactExistsResponse(TypedDict, total=False):
    departments: List[str]
    formFields: List["ContactField"]
    homeDoc: Any
    info: Dict[str, Any]
    ok: bool
    pageId: Any


class PublicContactSubmitParamsAttachment(TypedDict, total=False):
    assetId: str
    filename: str
    size: int


class PublicContactSubmitParams(TypedDict, total=False):
    name: str
    email: str
    subject: str
    body: str
    department: str
    attachments: List["PublicContactSubmitParamsAttachment"]
    website: str
    captchaToken: str
    fields: Dict[str, Any]


class PublicContactSubmitResponse(TypedDict, total=False):
    ok: bool
    submission: "SubmissionRow"
    data: "SubmissionRow"
    warnings: List[str]


class PublicContactAttachParams(TypedDict, total=False):
    file: str


class PublicContactAttachResponse(TypedDict, total=False):
    asset: "UploadedAsset"
    data: "UploadedAsset"
    warnings: List[str]


class ContactDepartmentsResponse(TypedDict, total=False):
    departments: List["Department"]
    page: "PageInfo"


class ContactSetDepartmentsParamsDepartment(TypedDict, total=False):
    name: str
    email: str


class ContactSetDepartmentsParams(TypedDict, total=False):
    departments: List["ContactSetDepartmentsParamsDepartment"]


class ContactSetDepartmentsResponse(TypedDict, total=False):
    departments: List["Department"]
    warnings: List[str]


class ContactFormFieldsResponse(TypedDict, total=False):
    fields: List["ContactField"]
    page: "PageInfo"


class ContactSetFormFieldsParamsField(TypedDict, total=False):
    key: str
    label: str
    type: str
    required: bool
    options: List[str]


class ContactSetFormFieldsParams(TypedDict, total=False):
    fields: List["ContactSetFormFieldsParamsField"]


class ContactSetFormFieldsResponse(TypedDict, total=False):
    fields: List["ContactField"]
    warnings: List[str]


class ContactListResponse(TypedDict, total=False):
    page: "PageInfo"
    submissions: List["SubmissionRow"]


class ContactSetHandledParams(TypedDict, total=False):
    handled: bool


class ContactSetHandledResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ContactAssignParams(TypedDict, total=False):
    assigneeId: Optional[str]


class ContactAssignResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class ContactRepliesResponse(TypedDict, total=False):
    page: "PageInfo"
    replies: List["InboxReply"]


class ContactReplyParams(TypedDict, total=False):
    body: str


class ContactReplyResponse(TypedDict, total=False):
    ok: bool
    reply: "InboxReply"
    warnings: List[str]


class PublicFormsDefinitionResponse(TypedDict, total=False):
    form: "PublicFormDefinition"


class PublicFormsSubmitResponse(TypedDict, total=False):
    ok: bool
    submission: Any
    successMessage: str
    redirectUrl: Any
    data: Any


class FormsListResponse(TypedDict, total=False):
    forms: List["FormSummary"]
    page: "PageInfo"


class FormsCreateParamsField(TypedDict, total=False):
    name: str
    type: str
    label: str
    placeholder: str
    required: bool
    options: List[str]
    help: str
    pattern: str
    min: float
    max: float
    value: str


class FormsCreateParams(TypedDict, total=False):
    name: str
    fields: List["FormsCreateParamsField"]
    submitLabel: str
    successMessage: str
    redirectUrl: Optional[Any]
    layout: str
    consentText: Optional[str]
    notifyEmails: List[str]
    status: str


class FormsCreateResponse(TypedDict, total=False):
    form: "FormDefinition"
    data: "FormDefinition"
    warnings: List[str]


class FormsGetResponse(TypedDict, total=False):
    form: "FormDefinition"


class FormsUpdateParamsField(TypedDict, total=False):
    name: str
    type: str
    label: str
    placeholder: str
    required: bool
    options: List[str]
    help: str
    pattern: str
    min: float
    max: float
    value: str


class FormsUpdateParams(TypedDict, total=False):
    name: str
    fields: List["FormsUpdateParamsField"]
    submitLabel: str
    successMessage: str
    redirectUrl: Optional[Any]
    layout: str
    consentText: Optional[str]
    notifyEmails: List[str]
    status: str


class FormsUpdateResponse(TypedDict, total=False):
    form: "FormDefinition"
    warnings: List[str]


class FormsListSubmissionsResponse(TypedDict, total=False):
    page: "PageInfo"
    submissions: List["FormSubmissionRow"]


class FormsSetSpamParams(TypedDict, total=False):
    spam: bool


class FormsSetSpamResponse(TypedDict, total=False):
    submission: "FormSubmissionRow"
    warnings: List[str]


class FormsSubmissionsByEmailResponse(TypedDict, total=False):
    submissions: List["FormSubmissionRow"]
    page: "PageInfo"


class FormsSubmissionsEraseByEmailResponse(TypedDict, total=False):
    deleted: float


class MailTemplatesListResponse(TypedDict, total=False):
    templates: List["EmailTemplateSummary"]
    page: "PageInfo"


class MailTemplatesGetResponse(TypedDict, total=False):
    template: "EmailTemplateDetail"


class MailTemplatesSaveParamsBlock(TypedDict, total=False):
    type: str
    text: str
    level: float
    align: str
    muted: bool
    label: str
    url: str
    showUrl: bool
    src: str
    alt: str
    href: str
    width: int
    size: str


class MailTemplatesSaveParams(TypedDict, total=False):
    subject: str
    preheader: str
    blocks: List["MailTemplatesSaveParamsBlock"]
    spaceId: Optional[str]
    locale: Optional[str]


class MailTemplatesSaveResponse(TypedDict, total=False):
    created: bool
    override: "EmailTemplateOverride"
    warnings: List[str]


class MailTemplatesResetResponse(TypedDict, total=False):
    removed: float


class MailTemplatesPreviewParamsContentBlock(TypedDict, total=False):
    type: str
    text: str
    level: float
    align: str
    muted: bool
    label: str
    url: str
    showUrl: bool
    src: str
    alt: str
    href: str
    width: int
    size: str


class MailTemplatesPreviewParamsContent(TypedDict, total=False):
    subject: str
    preheader: str
    blocks: List["MailTemplatesPreviewParamsContentBlock"]


class MailTemplatesPreviewParams(TypedDict, total=False):
    spaceId: Optional[str]
    locale: Optional[str]
    content: "MailTemplatesPreviewParamsContent"
    vars: Dict[str, Any]
    scheme: str


class MailTemplatesTestParamsContentBlock(TypedDict, total=False):
    type: str
    text: str
    level: float
    align: str
    muted: bool
    label: str
    url: str
    showUrl: bool
    src: str
    alt: str
    href: str
    width: int
    size: str


class MailTemplatesTestParamsContent(TypedDict, total=False):
    subject: str
    preheader: str
    blocks: List["MailTemplatesTestParamsContentBlock"]


class MailTemplatesTestParams(TypedDict, total=False):
    spaceId: Optional[str]
    locale: Optional[str]
    content: "MailTemplatesTestParamsContent"


class MailTemplatesTestResponse(TypedDict, total=False):
    ok: bool
    remaining: float
    to: str
    warnings: List[str]


class PublicCareersAttachParams(TypedDict, total=False):
    file: str


class PublicCareersAttachResponse(TypedDict, total=False):
    asset: "UploadedAsset"
    data: "UploadedAsset"
    warnings: List[str]


class PublicCareersApplyParamsAttachment(TypedDict, total=False):
    assetId: str
    filename: str
    size: int


class PublicCareersApplyParams(TypedDict, total=False):
    pageId: str
    name: str
    email: str
    coverLetter: str
    links: str
    attachments: List["PublicCareersApplyParamsAttachment"]
    website: str
    captchaToken: str


class PublicCareersApplyResponse(TypedDict, total=False):
    application: "ApplicationRow"
    ok: bool
    data: "ApplicationRow"
    warnings: List[str]


class CareersListResponse(TypedDict, total=False):
    applications: List["ApplicationRow"]
    page: "PageInfo"


class CareersSetStatusParams(TypedDict, total=False):
    status: str


class CareersSetStatusResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class CareersRepliesResponse(TypedDict, total=False):
    page: "PageInfo"
    replies: List["InboxReply"]


class CareersReplyParams(TypedDict, total=False):
    body: str


class CareersReplyResponse(TypedDict, total=False):
    ok: bool
    reply: "InboxReply"
    warnings: List[str]


class CareersAssignParams(TypedDict, total=False):
    assigneeId: Optional[str]


class CareersAssignResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class SpaceTemplatesListResponse(TypedDict, total=False):
    templates: List["TemplateView"]
    page: "PageInfo"


class SpaceTemplatesPublishParams(TypedDict, total=False):
    published: bool


class SpaceTemplatesPublishResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class SpaceTemplatesRemoveResponse(TypedDict, total=False):
    ok: bool


class SpaceTemplatesSaveParams(TypedDict, total=False):
    name: str
    description: str


class SpaceTemplatesSaveResponse(TypedDict, total=False):
    id: str
    warnings: List[str]


class SpaceTemplatesApplyParams(TypedDict, total=False):
    templateId: str
    template: str


class SsoAtlasListSsoResponse(TypedDict, total=False):
    connections: List["SsoConnectionView"]
    page: "PageInfo"


class SsoAtlasCreateSsoParamsOidc(TypedDict, total=False):
    issuer: str
    clientId: str
    clientSecret: str


class SsoAtlasCreateSsoParamsSaml(TypedDict, total=False):
    idpEntityId: str
    idpSsoUrl: str
    idpCertificate: str
    attributeMapping: Dict[str, Any]


class SsoAtlasCreateSsoParams(TypedDict, total=False):
    type: str
    name: str
    domain: str
    oidc: "SsoAtlasCreateSsoParamsOidc"
    saml: "SsoAtlasCreateSsoParamsSaml"


class SsoAtlasCreateSsoResponse(TypedDict, total=False):
    connection: "SsoConnectionView"
    data: "SsoConnectionView"
    warnings: List[str]


class SsoAtlasUpdateSsoParamsOidc(TypedDict, total=False):
    issuer: str
    clientId: str
    clientSecret: str


class SsoAtlasUpdateSsoParamsSaml(TypedDict, total=False):
    idpEntityId: str
    idpSsoUrl: str
    idpCertificate: str
    attributeMapping: Dict[str, Any]


class SsoAtlasUpdateSsoParams(TypedDict, total=False):
    name: str
    domain: str
    active: bool
    oidc: "SsoAtlasUpdateSsoParamsOidc"
    saml: "SsoAtlasUpdateSsoParamsSaml"


class SsoAtlasUpdateSsoResponse(TypedDict, total=False):
    connection: "SsoConnectionView"
    warnings: List[str]


class SsoAtlasDeleteSsoResponse(TypedDict, total=False):
    deleted: bool


class SsoAtlasSetEnforcedParams(TypedDict, total=False):
    enforced: bool


class SsoAtlasSetEnforcedResponse(TypedDict, total=False):
    enforced: bool
    warnings: List[str]


class SsoAtlasGetScimResponse(TypedDict, total=False):
    active: Optional["ScimTokenView"]


class SsoAtlasMintScimResponse(TypedDict, total=False):
    token: "ScimTokenMinted"
    data: "ScimTokenMinted"


class SsoAtlasRotateScimResponse(TypedDict, total=False):
    token: "ScimTokenMinted"
    data: "ScimTokenMinted"


class SsoAtlasDisableScimResponse(TypedDict, total=False):
    revoked: float


class SsoAtlasListOauthClientsResponse(TypedDict, total=False):
    clients: List["OauthClientView"]
    page: "PageInfo"


class SsoAtlasCreateOauthClientParams(TypedDict, total=False):
    name: str
    redirectUris: List[str]
    scopes: List[str]
    type: str


class SsoAtlasCreateOauthClientResponse(TypedDict, total=False):
    client: "OauthClientCreated"
    data: "OauthClientCreated"
    warnings: List[str]


class SsoAtlasRotateOauthClientSecretResponse(TypedDict, total=False):
    id: str
    secret: str


class SsoAtlasDeleteOauthClientResponse(TypedDict, total=False):
    deleted: bool


class CommunityBadgeQueryGrantsListResponseRule(TypedDict, total=False):
    badgeSlug: Any
    createdAt: Any
    enabled: Any
    id: Any
    lastRunAt: Any
    organizationId: Any
    sql: Any
    updatedAt: Any


class CommunityBadgeQueryGrantsListResponse(TypedDict, total=False):
    rules: List["CommunityBadgeQueryGrantsListResponseRule"]
    page: "PageInfo"


class CommunityBadgeQueryGrantsCreateParams(TypedDict, total=False):
    badgeSlug: str
    sql: str
    enabled: bool


class CommunityBadgeQueryGrantsCreateResponseRule(TypedDict, total=False):
    badgeSlug: Any
    createdAt: Any
    enabled: Any
    id: Any
    lastRunAt: Any
    organizationId: Any
    sql: Any
    updatedAt: Any


class CommunityBadgeQueryGrantsCreateResponseData(TypedDict, total=False):
    badgeSlug: Any
    createdAt: Any
    enabled: Any
    id: Any
    lastRunAt: Any
    organizationId: Any
    sql: Any
    updatedAt: Any


class CommunityBadgeQueryGrantsCreateResponse(TypedDict, total=False):
    rule: "CommunityBadgeQueryGrantsCreateResponseRule"
    data: "CommunityBadgeQueryGrantsCreateResponseData"
    warnings: List[str]


class CommunityBadgeQueryGrantsUpdateParams(TypedDict, total=False):
    badgeSlug: str
    sql: str
    enabled: bool


class CommunityBadgeQueryGrantsUpdateResponseRule(TypedDict, total=False):
    badgeSlug: Any
    createdAt: Any
    enabled: Any
    id: Any
    lastRunAt: Any
    organizationId: Any
    sql: Any
    updatedAt: Any


class CommunityBadgeQueryGrantsUpdateResponse(TypedDict, total=False):
    rule: "CommunityBadgeQueryGrantsUpdateResponseRule"
    warnings: List[str]


class CommunityBadgeQueryGrantsRemoveResponse(TypedDict, total=False):
    ok: bool


class CommunityBadgeQueryGrantsRunOneResponse(TypedDict, total=False):
    result: "RuleRunResult"


class CommunityBadgeQueryGrantsRunAllResponse(TypedDict, total=False):
    granted: float
    results: List["RuleRunResult"]
    ruleCount: float


class OrgsCaptchaGetResponse(TypedDict, total=False):
    configured: bool
    provider: Any
    siteKey: Any


class OrgsCaptchaSetParams(TypedDict, total=False):
    provider: str
    siteKey: str
    secret: str


class OrgsCaptchaSetResponse(TypedDict, total=False):
    configured: bool
    provider: str
    siteKey: str
    warnings: List[str]


class IntegrationsGithubStatusResponse(TypedDict, total=False):
    connection: Optional["ConnectionSummary"]


class IntegrationsGithubConnectParams(TypedDict, total=False):
    provider: str
    repo: str
    branch: str
    path: str
    token: str
    autoExport: bool
    commitTemplate: Optional[str]


class IntegrationsGithubConnectResponse(TypedDict, total=False):
    connection: "ConnectionSummary"
    warnings: List[str]


class IntegrationsGithubEgressIpsResponse(TypedDict, total=False):
    ips: List[str]
    page: "PageInfo"


class IntegrationsGithubImportResponse(TypedDict, total=False):
    imported: float


class IntegrationsGithubExportResponse(TypedDict, total=False):
    exported: float


class IntegrationsGithubPullRequestResponse(TypedDict, total=False):
    branch: str
    number: float
    pushed: float
    url: str


class IntegrationsGithubAgentStatusResponse(TypedDict, total=False):
    github: "GithubAgentStatus"


class IntegrationsGithubAgentConnectParams(TypedDict, total=False):
    repoFullName: str
    webhookSecret: str
    accessToken: str


class IntegrationsGithubAgentConnectResponse(TypedDict, total=False):
    github: "GithubAgentStatus"
    warnings: List[str]


class IntegrationsGithubAgentDisconnectResponse(TypedDict, total=False):
    ok: bool


class PublicOrgsScriptOriginsResponse(TypedDict, total=False):
    origins: List[str]
    page: "PageInfo"


class PublicOrgsGetResponseOrganization(TypedDict, total=False):
    name: str
    slug: str


class PublicOrgsGetResponse(TypedDict, total=False):
    organization: "PublicOrgsGetResponseOrganization"


class PublicSpacesListResponseSpace(TypedDict, total=False):
    aiIngestion: bool
    orgId: str
    orgSlug: Any
    ownDomain: bool
    path: Any
    spaceId: str
    spaceSlug: Any
    type: str
    updatedAt: str


class PublicSpacesListResponse(TypedDict, total=False):
    spaces: List["PublicSpacesListResponseSpace"]
    page: "PageInfo"


class PublicGateResponse(TypedDict, total=False):
    mode: str
    spaceName: str


class PublicHubIntroResponse(TypedDict, total=False):
    doc: Any


class PublicSearchResponse(TypedDict, total=False):
    hits: List["SearchHit"]
    minQueryLength: float


class PublicApiOriginsResponse(TypedDict, total=False):
    origins: List[str]
    page: "PageInfo"


class PublicScriptOriginsResponse(TypedDict, total=False):
    origins: List[str]
    page: "PageInfo"


class PublicStyleOriginsResponse(TypedDict, total=False):
    frameOrigins: List[str]
    imgOrigins: List[str]
    mediaOrigins: List[str]
    origins: List[str]


class PublicSiteOfResponse(TypedDict, total=False):
    site: Any


class PublicUpdatesResponse(TypedDict, total=False):
    page: "PageInfo"
    updates: List["SpaceUpdateRow"]


class PublicTagsResponseTag(TypedDict, total=False):
    count: float
    tag: str


class PublicTagsResponse(TypedDict, total=False):
    tags: List["PublicTagsResponseTag"]
    page: "PageInfo"


class PublicTagPagesResponsePage(TypedDict, total=False):
    id: str
    slug: str
    title: str


class PublicTagPagesResponse(TypedDict, total=False):
    pages: List["PublicTagPagesResponsePage"]
    page: "PageInfo"


class PublicPageVersionResponse(TypedDict, total=False):
    version: str


class PublicIdentityUnlockParams(TypedDict, total=False):
    password: str


class PublicIdentityUnlockResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class PublicIdentityUnlockJwtParams(TypedDict, total=False):
    jwt: str


class PublicIdentityUnlockJwtResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class PublicIdentitySignupFieldsResponseField(TypedDict, total=False):
    key: str
    label: str
    options: List[str]
    required: bool
    type: str


class PublicIdentitySignupFieldsResponse(TypedDict, total=False):
    fields: List["PublicIdentitySignupFieldsResponseField"]
    page: "PageInfo"


class PublicIdentityRegisterParams(TypedDict, total=False):
    email: str
    name: str
    password: str
    fields: Dict[str, Any]
    company: str
    formRenderedAt: int


class PublicIdentityRegisterResponse(TypedDict, total=False):
    status: str
    warnings: List[str]


class PublicIdentitySignInParams(TypedDict, total=False):
    email: str
    password: str


class PublicIdentitySignInResponse(TypedDict, total=False):
    status: str
    warnings: List[str]


class PublicInteractionsAskParams(TypedDict, total=False):
    question: str


class PublicInteractionsAskResponseResultCitation(TypedDict, total=False):
    anchor: str
    itemId: str
    slot: str
    title: str
    url: Any


class PublicInteractionsAskResponseResult(TypedDict, total=False):
    answer: str
    answered: bool
    citations: List["PublicInteractionsAskResponseResultCitation"]
    citedRefs: List[str]
    citedTitles: List[str]
    queryId: Any


class PublicInteractionsAskResponse(TypedDict, total=False):
    result: "PublicInteractionsAskResponseResult"
    warnings: List[str]


class PublicInteractionsAskStreamParams(TypedDict, total=False):
    question: str


class PublicInteractionsAskFeedbackParams(TypedDict, total=False):
    helpful: bool
    comment: str


class PublicInteractionsAskFeedbackResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class PublicInteractionsListCommentsResponse(TypedDict, total=False):
    comments: List["CommentSummary"]
    page: "PageInfo"


class PublicInteractionsPostCommentParamsAnchor(TypedDict, total=False):
    quote: str
    blockIndex: int


class PublicInteractionsPostCommentParams(TypedDict, total=False):
    authorName: str
    body: str
    parentId: Optional[str]
    anchor: Optional["PublicInteractionsPostCommentParamsAnchor"]
    suggestion: Optional[str]


class PublicInteractionsPostCommentResponse(TypedDict, total=False):
    comment: "CommentSummary"
    data: "CommentSummary"
    warnings: List[str]


class PublicInteractionsReactToCommentParams(TypedDict, total=False):
    emoji: str


class PublicInteractionsReactToCommentResponse(TypedDict, total=False):
    comment: "CommentSummary"
    warnings: List[str]


class PublicInteractionsExtRenderParams(TypedDict, total=False):
    extension: str
    block: str
    props: Dict[str, Any]
    context: Dict[str, Any]


class PublicInteractionsExtRenderResponseUiChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class PublicInteractionsExtRenderResponseUiOption(TypedDict, total=False):
    label: str
    value: str


class PublicInteractionsExtRenderResponseUi(TypedDict, total=False):
    children: List["PublicInteractionsExtRenderResponseUiChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["PublicInteractionsExtRenderResponseUiOption"]
    action: str
    href: str


class PublicInteractionsExtRenderResponse(TypedDict, total=False):
    ui: Optional["PublicInteractionsExtRenderResponseUi"]
    warnings: List[str]


class PublicInteractionsExtActionParams(TypedDict, total=False):
    extension: str
    block: str
    action: str
    props: Dict[str, Any]
    inputs: Dict[str, Any]
    context: Dict[str, Any]


class PublicInteractionsExtActionResponseUiChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class PublicInteractionsExtActionResponseUiOption(TypedDict, total=False):
    label: str
    value: str


class PublicInteractionsExtActionResponseUi(TypedDict, total=False):
    children: List["PublicInteractionsExtActionResponseUiChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["PublicInteractionsExtActionResponseUiOption"]
    action: str
    href: str


class PublicInteractionsExtActionResponse(TypedDict, total=False):
    ui: Optional["PublicInteractionsExtActionResponseUi"]
    warnings: List[str]


class PublicInteractionsFeedbackParams(TypedDict, total=False):
    rating: str
    comment: str


class PublicVisitorAuthRedeemJwtPostParams(TypedDict, total=False):
    jwt: str
    returnTo: str


class PublicVisitorAuthRedeemJwtPostResponseNeedsField(TypedDict, total=False):
    key: str
    label: str


class PublicVisitorAuthRedeemJwtPostResponse(TypedDict, total=False):
    needsFields: List["PublicVisitorAuthRedeemJwtPostResponseNeedsField"]
    ok: bool
    pending: bool
    returnTo: str
    warnings: List[str]


class PublicLegalListResponse(TypedDict, total=False):
    documents: List["PublicLegalDoc"]
    frontDoor: bool


class PublicLegalAcceptParams(TypedDict, total=False):
    subject: str
    subjectToken: str


class PublicLegalAcceptResponse(TypedDict, total=False):
    accepted: bool
    verification: str
    version: float
    warnings: List[str]


class PublicLegalVersionsResponseVersionAmendment(TypedDict, total=False):
    amendedAt: str
    note: Any


class PublicLegalVersionsResponseVersion(TypedDict, total=False):
    amendments: List["PublicLegalVersionsResponseVersionAmendment"]
    publishedAt: str
    version: float


class PublicLegalVersionsResponse(TypedDict, total=False):
    currentVersion: float
    versions: List["PublicLegalVersionsResponseVersion"]


class PublicLegalGetResponse(TypedDict, total=False):
    document: "PublicLegalDoc"


class PublicLegalGateStatusResponse(TypedDict, total=False):
    acceptor: Any
    documents: List["PendingLegalDoc"]
    gate: "ResolvedLegalGate"


class PublicLegalGateAcceptResponse(TypedDict, total=False):
    accepted: bool
    kind: str
    verification: str
    version: float


class ExtensionsListResponse(TypedDict, total=False):
    installed: List["InstalledExtensionSummary"]
    page: "PageInfo"


class ExtensionsAvailableResponse(TypedDict, total=False):
    available: List["AvailableExtension"]
    page: "PageInfo"


class ExtensionsInstallParams(TypedDict, total=False):
    manifestUrl: str
    manifest: Dict[str, Any]
    config: Dict[str, Any]


class ExtensionsUpdateParams(TypedDict, total=False):
    config: Dict[str, Any]
    events: List[str]
    enabled: bool


class ExtensionsUpdateResponse(TypedDict, total=False):
    integration: "InstalledExtensionSummary"
    warnings: List[str]


class ExtensionsUninstallResponse(TypedDict, total=False):
    ok: bool


class ExtensionsTestResponse(TypedDict, total=False):
    ok: bool


class ExtensionsDeliveriesResponse(TypedDict, total=False):
    deliveries: List["ExtensionDelivery"]
    page: "PageInfo"


class ExtensionsRotateResponse(TypedDict, total=False):
    accessToken: str


class ExtensionsUpgradeResponse(TypedDict, total=False):
    integration: "InstalledExtensionSummary"


class ExtensionsApiMeResponse(TypedDict, total=False):
    installId: str
    organizationId: str
    scopes: List[str]


class ExtensionsApiPageResponse(TypedDict, total=False):
    page: "ExtPage"


class ExtensionsApiSpacePagesResponse(TypedDict, total=False):
    pages: List["ExtPageSummary"]
    page: "PageInfo"


class ExtensionsApiSaveDraftParams(TypedDict, total=False):
    title: str
    content: Dict[str, Any]


class ExtensionsApiSaveDraftResponse(TypedDict, total=False):
    revisionId: str
    data: str
    warnings: List[str]


class ExtensionsApiCommentsResponse(TypedDict, total=False):
    comments: List["ExtComment"]
    page: "PageInfo"


class ExtensionsApiPostCommentParams(TypedDict, total=False):
    body: str
    authorName: str


class ExtensionsApiPostCommentResponse(TypedDict, total=False):
    comment: "ExtCommentRef"
    data: "ExtCommentRef"
    warnings: List[str]


class ExtensionsApiMembersResponse(TypedDict, total=False):
    members: List["ExtMember"]
    page: "PageInfo"


class ExtensionsApiAnalyticsResponse(TypedDict, total=False):
    analytics: "AnalyticsSummary"


class ExtensionsRenderRenderBlockParams(TypedDict, total=False):
    extension: str
    block: str
    props: Dict[str, Any]
    context: Dict[str, Any]


class ExtensionsRenderRenderBlockResponseUiChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class ExtensionsRenderRenderBlockResponseUiOption(TypedDict, total=False):
    label: str
    value: str


class ExtensionsRenderRenderBlockResponseUi(TypedDict, total=False):
    children: List["ExtensionsRenderRenderBlockResponseUiChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["ExtensionsRenderRenderBlockResponseUiOption"]
    action: str
    href: str


class ExtensionsRenderRenderBlockResponseDataChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class ExtensionsRenderRenderBlockResponseDataOption(TypedDict, total=False):
    label: str
    value: str


class ExtensionsRenderRenderBlockResponseData(TypedDict, total=False):
    children: List["ExtensionsRenderRenderBlockResponseDataChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["ExtensionsRenderRenderBlockResponseDataOption"]
    action: str
    href: str


class ExtensionsRenderRenderBlockResponse(TypedDict, total=False):
    ui: Optional["ExtensionsRenderRenderBlockResponseUi"]
    data: Optional["ExtensionsRenderRenderBlockResponseData"]
    warnings: List[str]


class ExtensionsRenderActionParams(TypedDict, total=False):
    extension: str
    block: str
    action: str
    props: Dict[str, Any]
    inputs: Dict[str, Any]
    context: Dict[str, Any]


class ExtensionsRenderActionResponseUiChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class ExtensionsRenderActionResponseUiOption(TypedDict, total=False):
    label: str
    value: str


class ExtensionsRenderActionResponseUi(TypedDict, total=False):
    children: List["ExtensionsRenderActionResponseUiChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["ExtensionsRenderActionResponseUiOption"]
    action: str
    href: str


class ExtensionsRenderActionResponseDataChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class ExtensionsRenderActionResponseDataOption(TypedDict, total=False):
    label: str
    value: str


class ExtensionsRenderActionResponseData(TypedDict, total=False):
    children: List["ExtensionsRenderActionResponseDataChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["ExtensionsRenderActionResponseDataOption"]
    action: str
    href: str


class ExtensionsRenderActionResponse(TypedDict, total=False):
    ui: Optional["ExtensionsRenderActionResponseUi"]
    data: Optional["ExtensionsRenderActionResponseData"]
    warnings: List[str]


class ExtensionsRenderRenderSurfaceParams(TypedDict, total=False):
    extension: str
    surface: str
    context: Dict[str, Any]


class ExtensionsRenderRenderSurfaceResponseUiChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class ExtensionsRenderRenderSurfaceResponseUiOption(TypedDict, total=False):
    label: str
    value: str


class ExtensionsRenderRenderSurfaceResponseUi(TypedDict, total=False):
    children: List["ExtensionsRenderRenderSurfaceResponseUiChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["ExtensionsRenderRenderSurfaceResponseUiOption"]
    action: str
    href: str


class ExtensionsRenderRenderSurfaceResponseDataChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class ExtensionsRenderRenderSurfaceResponseDataOption(TypedDict, total=False):
    label: str
    value: str


class ExtensionsRenderRenderSurfaceResponseData(TypedDict, total=False):
    children: List["ExtensionsRenderRenderSurfaceResponseDataChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["ExtensionsRenderRenderSurfaceResponseDataOption"]
    action: str
    href: str


class ExtensionsRenderRenderSurfaceResponse(TypedDict, total=False):
    ui: Optional["ExtensionsRenderRenderSurfaceResponseUi"]
    data: Optional["ExtensionsRenderRenderSurfaceResponseData"]
    warnings: List[str]


class ExtensionsRenderSurfaceActionParams(TypedDict, total=False):
    extension: str
    surface: str
    action: str
    inputs: Dict[str, Any]
    context: Dict[str, Any]


class ExtensionsRenderSurfaceActionResponseUiChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class ExtensionsRenderSurfaceActionResponseUiOption(TypedDict, total=False):
    label: str
    value: str


class ExtensionsRenderSurfaceActionResponseUi(TypedDict, total=False):
    children: List["ExtensionsRenderSurfaceActionResponseUiChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["ExtensionsRenderSurfaceActionResponseUiOption"]
    action: str
    href: str


class ExtensionsRenderSurfaceActionResponseDataChildrenItem(TypedDict, total=False):
    children: List[Dict[str, Any]]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List[Dict[str, Any]]
    action: str
    href: str


class ExtensionsRenderSurfaceActionResponseDataOption(TypedDict, total=False):
    label: str
    value: str


class ExtensionsRenderSurfaceActionResponseData(TypedDict, total=False):
    children: List["ExtensionsRenderSurfaceActionResponseDataChildrenItem"]
    type: str
    muted: bool
    text: str
    label: str
    value: str
    name: str
    placeholder: str
    options: List["ExtensionsRenderSurfaceActionResponseDataOption"]
    action: str
    href: str


class ExtensionsRenderSurfaceActionResponse(TypedDict, total=False):
    ui: Optional["ExtensionsRenderSurfaceActionResponseUi"]
    data: Optional["ExtensionsRenderSurfaceActionResponseData"]
    warnings: List[str]


class ExtensionsRegistryPublishResponse(TypedDict, total=False):
    published: bool


class ExtensionsRegistryUnpublishResponse(TypedDict, total=False):
    published: bool


class ExtensionsRegistryInstallParams(TypedDict, total=False):
    slug: str
    config: Dict[str, Any]


class ExtensionsRegistryRateParams(TypedDict, total=False):
    slug: str
    rating: int
    review: str


class ExtensionsRegistryRateResponse(TypedDict, total=False):
    ratingAvg: float
    ratingCount: float
    warnings: List[str]


class ExtensionsRegistrySubmitResponse(TypedDict, total=False):
    reviewStatus: str


class ExtensionsRegistryPricingParams(TypedDict, total=False):
    pricing: str
    priceCents: int
    currency: str


class ExtensionsRegistryPricingResponse(TypedDict, total=False):
    priceCents: float
    pricing: str
    warnings: List[str]


class ExtensionsRegistryPurchaseParams(TypedDict, total=False):
    slug: str


class ExtensionsRegistryPurchaseResponse(TypedDict, total=False):
    checkoutUrl: str
    entitled: bool
    warnings: List[str]


class PublicExtensionRegistryListResponse(TypedDict, total=False):
    extensions: List["RegistryListing"]
    page: "PageInfo"


class PublicExtensionRegistryGetResponse(TypedDict, total=False):
    extension: "RegistryListing"


class SsoGetResponse(TypedDict, total=False):
    sso: "SsoConfigView"


class SsoSetParams(TypedDict, total=False):
    provider: str
    issuer: str
    clientId: str
    clientSecret: str
    allowedDomain: Optional[str]
    defaultRole: str
    enabled: bool
    requireSso: bool


class SsoSetResponse(TypedDict, total=False):
    sso: "SsoConfigView"
    warnings: List[str]


class SsoProvidersResponseProvider(TypedDict, total=False):
    key: str
    kind: str
    label: str


class SsoProvidersResponse(TypedDict, total=False):
    providers: List["SsoProvidersResponseProvider"]
    page: "PageInfo"


class SsoSamlGetResponse(TypedDict, total=False):
    saml: "SamlConfigView"


class SsoSamlSetParams(TypedDict, total=False):
    idpEntryPoint: str
    idpCert: str
    allowedDomain: Optional[str]
    defaultRole: str
    enabled: bool


class SsoSamlSetResponse(TypedDict, total=False):
    saml: "SamlConfigView"
    warnings: List[str]


class SsoLtiGetResponse(TypedDict, total=False):
    lti: "LtiConfigView"


class SsoLtiSetParams(TypedDict, total=False):
    issuer: str
    clientId: str
    authLoginUrl: str
    jwksUrl: str
    deploymentId: Optional[str]
    allowedDomain: Optional[str]
    defaultRole: str
    enabled: bool


class SsoLtiSetResponse(TypedDict, total=False):
    lti: "LtiConfigView"
    warnings: List[str]


class SsoScimStatusResponse(TypedDict, total=False):
    configured: bool
    endpoint: str


class SsoScimCreateResponse(TypedDict, total=False):
    token: str


class SsoScimRevokeResponse(TypedDict, total=False):
    revoked: bool


class ScimUsersListResponse(TypedDict, total=False):
    Resources: List["ScimUser"]
    schemas: List[str]
    totalResults: float


class ScimUsersCreateParamsName(TypedDict, total=False):
    formatted: str


class ScimUsersCreateParams(TypedDict, total=False):
    userName: str
    name: "ScimUsersCreateParamsName"
    active: bool


class ScimUsersPatchParamsOperation(TypedDict, total=False):
    op: str
    path: str
    value: Any


class ScimUsersPatchParams(TypedDict, total=False):
    Operations: List["ScimUsersPatchParamsOperation"]
    active: bool


class ScimGroupsListResponse(TypedDict, total=False):
    Resources: List["ScimGroup"]
    schemas: List[str]
    totalResults: float


class ScimGroupsCreateParamsMember(TypedDict, total=False):
    value: str


class ScimGroupsCreateParams(TypedDict, total=False):
    displayName: str
    members: List["ScimGroupsCreateParamsMember"]


class ScimGroupsReplaceParamsMember(TypedDict, total=False):
    value: str


class ScimGroupsReplaceParams(TypedDict, total=False):
    displayName: str
    members: List["ScimGroupsReplaceParamsMember"]


class ScimGroupsPatchParamsOperation(TypedDict, total=False):
    op: str
    path: str
    value: Any


class ScimGroupsPatchParams(TypedDict, total=False):
    Operations: List["ScimGroupsPatchParamsOperation"]
    active: bool


class SsoDiscourseConnectGetConfigResponse(TypedDict, total=False):
    config: "DiscourseConnectView"


class SsoDiscourseConnectSetConfigParams(TypedDict, total=False):
    mode: str
    secret: str
    providerUrl: Optional[str]
    allowedDomain: Optional[str]
    defaultRole: str
    enabled: bool


class SsoDiscourseConnectSetConfigResponse(TypedDict, total=False):
    config: "DiscourseConnectView"
    warnings: List[str]


class ReaderSignupsListResponse(TypedDict, total=False):
    signups: List["ReaderSignupRow"]
    page: "PageInfo"


class ReaderSignupsApproveResponse(TypedDict, total=False):
    ok: bool


class ReaderSignupsRejectResponse(TypedDict, total=False):
    ok: bool


class ReaderAuthSetOrgParamsProvider(TypedDict, total=False):
    method: str
    label: str
    order: int
    config: Dict[str, Any]
    provisionIdentity: bool


class ReaderAuthSetOrgParamsOutboundSync(TypedDict, total=False):
    scimBaseUrl: str
    scimBearerToken: str
    deprovisionAction: str
    targetId: str
    status: str
    lastError: Any


class ReaderAuthSetOrgParams(TypedDict, total=False):
    sourceOfTruth: str
    providers: List["ReaderAuthSetOrgParamsProvider"]
    approveNewMembers: bool
    hostedSignup: bool
    signInUrl: str
    outboundSync: "ReaderAuthSetOrgParamsOutboundSync"


class ReaderAuthSetSpaceParamsProvider(TypedDict, total=False):
    method: str
    label: str
    order: int
    config: Dict[str, Any]
    provisionIdentity: bool


class ReaderAuthSetSpaceParamsOutboundSync(TypedDict, total=False):
    scimBaseUrl: str
    scimBearerToken: str
    deprovisionAction: str
    targetId: str
    status: str
    lastError: Any


class ReaderAuthSetSpaceParams(TypedDict, total=False):
    sourceOfTruth: str
    providers: List["ReaderAuthSetSpaceParamsProvider"]
    approveNewMembers: bool
    hostedSignup: bool
    signInUrl: str
    outboundSync: "ReaderAuthSetSpaceParamsOutboundSync"


class ReaderAuthDeleteSpaceResponse(TypedDict, total=False):
    hasOverride: bool
    inherits: bool


class PublicReaderAuthResolvedResponseOutboundSync(TypedDict, total=False):
    deprovisionAction: str
    lastError: str
    scimBaseUrl: str
    scimBearerToken: str
    status: str
    targetId: str


class PublicReaderAuthResolvedResponseProvider(TypedDict, total=False):
    config: Dict[str, Any]
    label: str
    method: str
    order: float
    provisionIdentity: bool


class PublicReaderAuthResolvedResponse(TypedDict, total=False):
    approveNewMembers: bool
    hostedSignup: bool
    outboundSync: "PublicReaderAuthResolvedResponseOutboundSync"
    providers: List["PublicReaderAuthResolvedResponseProvider"]
    signInUrl: str
    sourceOfTruth: str


class ReaderDomainGetResponse(TypedDict, total=False):
    domain: Optional["ReaderDomain"]


class ReaderDomainConfigureParams(TypedDict, total=False):
    host: str


class ReaderDomainConfigureResponse(TypedDict, total=False):
    domain: "ReaderDomain"
    warnings: List[str]


class ReaderDomainRemoveResponse(TypedDict, total=False):
    removed: bool


class ReaderDomainVerifyResponse(TypedDict, total=False):
    domain: "ReaderDomain"
    data: "ReaderDomain"


class ReaderPolicySetLegalGateParams(TypedDict, total=False):
    scope: str
    anonymous: str


class ReaderPolicyDeleteLegalGateResponse(TypedDict, total=False):
    hasOverride: bool
    inherits: bool


class ReaderPolicySetReaderIdentityParams(TypedDict, total=False):
    scope: str


class ReaderPolicyDeleteReaderIdentityResponse(TypedDict, total=False):
    hasOverride: bool
    inherits: bool


class PublicReaderPolicyResolvedResponse(TypedDict, total=False):
    legalGate: "ResolvedLegalGate"
    readerIdentity: "ResolvedReaderIdentity"


class ConnectorsListResponse(TypedDict, total=False):
    connectors: List["ConnectorSummary"]
    page: "PageInfo"


class ConnectorsInstallParamsAppearance(TypedDict, total=False):
    primaryColor: str
    colorScheme: str
    position: str
    greeting: str


class ConnectorsInstallParams(TypedDict, total=False):
    providerId: str
    config: Dict[str, Any]
    embedEnabled: bool
    knowledgeEnabled: bool
    knowledgeScopes: List[str]
    appearance: "ConnectorsInstallParamsAppearance"


class ConnectorsInstallResponse(TypedDict, total=False):
    connector: "ConnectorSummary"
    data: "ConnectorSummary"
    warnings: List[str]


class ConnectorsUpdateParamsAppearance(TypedDict, total=False):
    primaryColor: str
    colorScheme: str
    position: str
    greeting: str


class ConnectorsUpdateParams(TypedDict, total=False):
    embedEnabled: bool
    knowledgeEnabled: bool
    knowledgeScopes: List[str]
    appearance: "ConnectorsUpdateParamsAppearance"
    config: Dict[str, Any]


class ConnectorsUpdateResponse(TypedDict, total=False):
    connector: "ConnectorSummary"
    warnings: List[str]


class ConnectorsRemoveResponse(TypedDict, total=False):
    deleted: bool


class ConnectorsRevokeTokenResponse(TypedDict, total=False):
    revoked: bool


class ConnectorsTestParams(TypedDict, total=False):
    onCustomDomain: bool


class ConnectorsActivityResponse(TypedDict, total=False):
    activity: List["ConnectorActivityEntry"]
    page: "PageInfo"


class ConnectorsProvidersListResponse(TypedDict, total=False):
    providers: List["ChatProviderDef"]
    page: "PageInfo"


class ChatProvidersListResponse(TypedDict, total=False):
    providers: List["ChatProviderDef"]
    page: "PageInfo"


class ChatProvidersCreateParamsField(TypedDict, total=False):
    key: str
    label: str
    type: str
    required: bool
    placeholder: str
    help: str


class ChatProvidersCreateParamsEmbed(TypedDict, total=False):
    origin: str
    script: str
    src: str
    connectOrigins: List[str]
    themeSupport: List[str]
    themeInit: Dict[str, Any]
    initScript: str
    colorSchemeMap: Dict[str, Any]
    consent: str
    platformSafe: bool


class ChatProvidersCreateParamsKnowledgeRegister(TypedDict, total=False):
    endpoint: str
    method: str
    keyField: str
    authHeader: str
    body: str
    idPath: str


class ChatProvidersCreateParamsKnowledge(TypedDict, total=False):
    capabilities: List[str]
    setupUrl: str
    setupHint: str
    pull: bool
    register: "ChatProvidersCreateParamsKnowledgeRegister"


class ChatProvidersCreateParams(TypedDict, total=False):
    id: str
    name: str
    description: str
    icon: str
    docsUrl: str
    fields: List["ChatProvidersCreateParamsField"]
    embed: "ChatProvidersCreateParamsEmbed"
    knowledge: "ChatProvidersCreateParamsKnowledge"


class ChatProvidersCreateResponse(TypedDict, total=False):
    id: str
    data: str
    warnings: List[str]


class ChatProvidersUpdateParamsField(TypedDict, total=False):
    key: str
    label: str
    type: str
    required: bool
    placeholder: str
    help: str


class ChatProvidersUpdateParamsEmbed(TypedDict, total=False):
    origin: str
    script: str
    src: str
    connectOrigins: List[str]
    themeSupport: List[str]
    themeInit: Dict[str, Any]
    initScript: str
    colorSchemeMap: Dict[str, Any]
    consent: str
    platformSafe: bool


class ChatProvidersUpdateParamsKnowledgeRegister(TypedDict, total=False):
    endpoint: str
    method: str
    keyField: str
    authHeader: str
    body: str
    idPath: str


class ChatProvidersUpdateParamsKnowledge(TypedDict, total=False):
    capabilities: List[str]
    setupUrl: str
    setupHint: str
    pull: bool
    register: "ChatProvidersUpdateParamsKnowledgeRegister"


class ChatProvidersUpdateParams(TypedDict, total=False):
    id: str
    name: str
    description: str
    icon: str
    docsUrl: str
    fields: List["ChatProvidersUpdateParamsField"]
    embed: "ChatProvidersUpdateParamsEmbed"
    knowledge: "ChatProvidersUpdateParamsKnowledge"


class ChatProvidersUpdateResponse(TypedDict, total=False):
    updated: bool
    warnings: List[str]


class ChatProvidersRemoveResponse(TypedDict, total=False):
    deleted: bool


class ConnectorsKbLlmsResponse(TypedDict, total=False):
    text: str


class ConnectorsKbAskParams(TypedDict, total=False):
    question: str


class ConnectorsKbQuestionsParamsQuestion(TypedDict, total=False):
    text: str
    askedAt: str
    outcome: str
    citedChunks: List[str]


class ConnectorsKbQuestionsParams(TypedDict, total=False):
    questions: List["ConnectorsKbQuestionsParamsQuestion"]


class ConnectorsKbSuggestParams(TypedDict, total=False):
    itemId: str
    slot: str
    markdown: str
    note: str


class IntegrationsCatalogResponse(TypedDict, total=False):
    catalog: List["IntegrationDef"]
    page: "PageInfo"


class IntegrationsListResponse(TypedDict, total=False):
    installed: List["InstalledSummary"]
    page: "PageInfo"


class IntegrationsInstallParams(TypedDict, total=False):
    integrationId: str
    config: Dict[str, Any]
    events: List[str]


class IntegrationsInstallResponse(TypedDict, total=False):
    integration: "InstalledSummary"
    data: "InstalledSummary"
    warnings: List[str]


class IntegrationsUpdateParams(TypedDict, total=False):
    config: Dict[str, Any]
    events: List[str]
    enabled: bool


class IntegrationsUpdateResponse(TypedDict, total=False):
    integration: "InstalledSummary"
    warnings: List[str]


class IntegrationsUninstallResponse(TypedDict, total=False):
    ok: bool


class IntegrationsTestResponse(TypedDict, total=False):
    ok: bool


class UsersAvatarUploadParams(TypedDict, total=False):
    file: str


class UsersAvatarUploadResponse(TypedDict, total=False):
    user: "PublicUser"
    warnings: List[str]


class UsersAvatarClearResponse(TypedDict, total=False):
    user: "PublicUser"


class UsersAvatarGravatarResponse(TypedDict, total=False):
    user: "PublicUser"


class SitesListResponse(TypedDict, total=False):
    sites: List["SiteSummary"]
    page: "PageInfo"


class SitesCreateParamsConfigCta(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigSecondaryCta(TypedDict, total=False):
    label: str
    href: str
    style: str


class SitesCreateParamsConfigHeader(TypedDict, total=False):
    overlay: bool
    overlayInk: str
    height: int
    border: str
    borderColor: str
    shadow: str
    blur: int
    opacity: float
    logoHeight: int
    navGap: int
    navWeight: int
    navSize: float
    navCase: str
    navTracking: float


class SitesCreateParamsConfigHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SitesCreateParamsConfigHeaderLinkPanelColumnLink(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SitesCreateParamsConfigHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List["SitesCreateParamsConfigHeaderLinkPanelColumnLink"]


class SitesCreateParamsConfigHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class SitesCreateParamsConfigHeaderLinkPanelFooterLink(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigHeaderLinkPanelFooter(TypedDict, total=False):
    links: List["SitesCreateParamsConfigHeaderLinkPanelFooterLink"]
    cta: "SitesCreateParamsConfigHeaderLinkPanelFooterCta"


class SitesCreateParamsConfigHeaderLinkPanel(TypedDict, total=False):
    columns: List["SitesCreateParamsConfigHeaderLinkPanelColumn"]
    featured: "SitesCreateParamsConfigHeaderLinkPanelFeatured"
    footer: "SitesCreateParamsConfigHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class SitesCreateParamsConfigHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["SitesCreateParamsConfigHeaderLinkChildrenItem"]
    panel: "SitesCreateParamsConfigHeaderLinkPanel"
    style: str
    highlight: bool


class SitesCreateParamsConfigNavMenu(TypedDict, total=False):
    trigger: str
    openDelay: int
    closeDelay: int
    animation: str
    radius: float
    shadow: str
    background: str
    ink: str
    border: str
    width: int


class SitesCreateParamsConfigFooterLink(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SitesCreateParamsConfigFooterColumnLink"]


class SitesCreateParamsConfigSocialLink(TypedDict, total=False):
    platform: str
    href: str


class SitesCreateParamsConfigFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class SitesCreateParamsConfigFooter(TypedDict, total=False):
    logo: Any
    logoMark: Any
    cookieLinkPlacement: str
    html: str
    css: str
    htmlPlacement: str
    newsletter: "SitesCreateParamsConfigFooterNewsletter"


class SitesCreateParamsConfigThemeToggle(TypedDict, total=False):
    show: bool
    style: str
    position: str
    radius: float
    activeColor: str


class SitesCreateParamsConfigTab(TypedDict, total=False):
    title: str
    slug: str
    spaceIds: List[str]


class SitesCreateParamsConfigThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class SitesCreateParamsConfigThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class SitesCreateParamsConfigThemeLayout(TypedDict, total=False):
    measure: str


class SitesCreateParamsConfigThemeTypographyFluid(TypedDict, total=False):
    enabled: bool
    minViewport: int
    maxViewport: int
    minScale: float
    bodyMinScale: float


class SitesCreateParamsConfigThemeTypographyLevelsH1(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SitesCreateParamsConfigThemeTypographyLevelsH2(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SitesCreateParamsConfigThemeTypographyLevelsH3(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SitesCreateParamsConfigThemeTypographyLevelsH4(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SitesCreateParamsConfigThemeTypographyLevelsH5(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SitesCreateParamsConfigThemeTypographyLevelsH6(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SitesCreateParamsConfigThemeTypographyLevelsBody(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SitesCreateParamsConfigThemeTypographyLevelsSmall(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SitesCreateParamsConfigThemeTypographyLevelsCode(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class SitesCreateParamsConfigThemeTypographyLevels(TypedDict, total=False):
    h1: "SitesCreateParamsConfigThemeTypographyLevelsH1"
    h2: "SitesCreateParamsConfigThemeTypographyLevelsH2"
    h3: "SitesCreateParamsConfigThemeTypographyLevelsH3"
    h4: "SitesCreateParamsConfigThemeTypographyLevelsH4"
    h5: "SitesCreateParamsConfigThemeTypographyLevelsH5"
    h6: "SitesCreateParamsConfigThemeTypographyLevelsH6"
    body: "SitesCreateParamsConfigThemeTypographyLevelsBody"
    small: "SitesCreateParamsConfigThemeTypographyLevelsSmall"
    code: "SitesCreateParamsConfigThemeTypographyLevelsCode"


class SitesCreateParamsConfigThemeTypographyVariation(TypedDict, total=False):
    heading: str
    body: str
    code: str


class SitesCreateParamsConfigThemeTypographyFeatures(TypedDict, total=False):
    heading: str
    body: str
    code: str


class SitesCreateParamsConfigThemeTypography(TypedDict, total=False):
    scale: str
    baseSize: float
    fluid: "SitesCreateParamsConfigThemeTypographyFluid"
    levels: "SitesCreateParamsConfigThemeTypographyLevels"
    headingTransform: str
    variation: "SitesCreateParamsConfigThemeTypographyVariation"
    features: "SitesCreateParamsConfigThemeTypographyFeatures"
    opticalSizing: str
    headingWrap: str
    bodyWrap: str


class SitesCreateParamsConfigThemeFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class SitesCreateParamsConfigThemeFonts(TypedDict, total=False):
    faces: List["SitesCreateParamsConfigThemeFontsFace"]


class SitesCreateParamsConfigThemeAds(TypedDict, total=False):
    network: str
    publisherId: str
    slotId: str
    size: str
    enabled: bool
    scriptUrl: str
    slotHtml: str
    configVar: str
    configJson: Dict[str, Any]


class SitesCreateParamsConfigThemeElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class SitesCreateParamsConfigThemeSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class SitesCreateParamsConfigThemeCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class SitesCreateParamsConfigThemeAnnouncement(TypedDict, total=False):
    text: str
    level: str
    href: Any


class SitesCreateParamsConfigThemeChromeCta(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigThemeChromeSecondaryCta(TypedDict, total=False):
    label: str
    href: str
    style: str


class SitesCreateParamsConfigThemeChromeHeader(TypedDict, total=False):
    overlay: bool
    overlayInk: str
    height: int
    border: str
    borderColor: str
    shadow: str
    blur: int
    opacity: float
    logoHeight: int
    navGap: int
    navWeight: int
    navSize: float
    navCase: str
    navTracking: float


class SitesCreateParamsConfigThemeChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SitesCreateParamsConfigThemeChromeHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class SitesCreateParamsConfigThemeChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class SitesCreateParamsConfigThemeChromeHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigThemeChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List[Dict[str, Any]]
    cta: "SitesCreateParamsConfigThemeChromeHeaderLinkPanelFooterCta"


class SitesCreateParamsConfigThemeChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List["SitesCreateParamsConfigThemeChromeHeaderLinkPanelColumn"]
    featured: "SitesCreateParamsConfigThemeChromeHeaderLinkPanelFeatured"
    footer: "SitesCreateParamsConfigThemeChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class SitesCreateParamsConfigThemeChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["SitesCreateParamsConfigThemeChromeHeaderLinkChildrenItem"]
    panel: "SitesCreateParamsConfigThemeChromeHeaderLinkPanel"
    style: str
    highlight: bool


class SitesCreateParamsConfigThemeChromeNavMenu(TypedDict, total=False):
    trigger: str
    openDelay: int
    closeDelay: int
    animation: str
    radius: float
    shadow: str
    background: str
    ink: str
    border: str
    width: int


class SitesCreateParamsConfigThemeChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigThemeChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SitesCreateParamsConfigThemeChromeFooterColumnLink"]


class SitesCreateParamsConfigThemeChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class SitesCreateParamsConfigThemeChromeFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class SitesCreateParamsConfigThemeChromeFooter(TypedDict, total=False):
    logo: Any
    logoMark: Any
    cookieLinkPlacement: str
    html: str
    css: str
    htmlPlacement: str
    newsletter: "SitesCreateParamsConfigThemeChromeFooterNewsletter"


class SitesCreateParamsConfigThemeChromeThemeToggle(TypedDict, total=False):
    show: bool
    style: str
    position: str
    radius: float
    activeColor: str


class SitesCreateParamsConfigThemeChrome(TypedDict, total=False):
    cta: "SitesCreateParamsConfigThemeChromeCta"
    secondaryCta: "SitesCreateParamsConfigThemeChromeSecondaryCta"
    header: "SitesCreateParamsConfigThemeChromeHeader"
    headerLinks: List["SitesCreateParamsConfigThemeChromeHeaderLink"]
    navMenu: "SitesCreateParamsConfigThemeChromeNavMenu"
    footerLinks: List["SitesCreateParamsConfigThemeChromeFooterLink"]
    footerDescription: str
    footerColumns: List["SitesCreateParamsConfigThemeChromeFooterColumn"]
    socialLinks: List["SitesCreateParamsConfigThemeChromeSocialLink"]
    copyright: str
    footer: "SitesCreateParamsConfigThemeChromeFooter"
    mobileNav: str
    sticky: bool
    height: str
    align: str
    ctaStyle: str
    showSignIn: bool
    themeToggle: "SitesCreateParamsConfigThemeChromeThemeToggle"
    sidebarBrand: str


class SitesCreateParamsConfigThemeNotFoundLink(TypedDict, total=False):
    label: str
    href: str


class SitesCreateParamsConfigThemeNotFound(TypedDict, total=False):
    title: str
    body: str
    pageId: str
    pageSpaceId: str
    hidePage: bool
    links: List["SitesCreateParamsConfigThemeNotFoundLink"]
    showSearch: bool
    showSections: bool
    hideSearch: bool


class SitesCreateParamsConfigThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class SitesCreateParamsConfigThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class SitesCreateParamsConfigThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class SitesCreateParamsConfigThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class SitesCreateParamsConfigThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class SitesCreateParamsConfigThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class SitesCreateParamsConfigThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class SitesCreateParamsConfigThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class SitesCreateParamsConfigThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class SitesCreateParamsConfigThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "SitesCreateParamsConfigThemeComponentsFocus"
    code: "SitesCreateParamsConfigThemeComponentsCode"
    input: "SitesCreateParamsConfigThemeComponentsInput"
    button: "SitesCreateParamsConfigThemeComponentsButton"
    spacing: "SitesCreateParamsConfigThemeComponentsSpacing"
    selection: "SitesCreateParamsConfigThemeComponentsSelection"
    scrollbar: "SitesCreateParamsConfigThemeComponentsScrollbar"
    syntax: "SitesCreateParamsConfigThemeComponentsSyntax"
    syntaxDark: "SitesCreateParamsConfigThemeComponentsSyntaxDark"


class SitesCreateParamsConfigThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class SitesCreateParamsConfigThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class SitesCreateParamsConfigThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class SitesCreateParamsConfigThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class SitesCreateParamsConfigThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class SitesCreateParamsConfigThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["SitesCreateParamsConfigThemeMotionKeyframeStep"]


class SitesCreateParamsConfigThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "SitesCreateParamsConfigThemeMotionReveal"
    hover: "SitesCreateParamsConfigThemeMotionHover"
    header: "SitesCreateParamsConfigThemeMotionHeader"
    ambient: "SitesCreateParamsConfigThemeMotionAmbient"
    keyframes: List["SitesCreateParamsConfigThemeMotionKeyframe"]
    targets: Dict[str, Any]


class SitesCreateParamsConfigThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SitesCreateParamsConfigThemeMobile(TypedDict, total=False):
    fontScale: float
    density: str
    logoUrl: Any
    hide: List[str]
    css: str


class SitesCreateParamsConfigTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "SitesCreateParamsConfigThemePalette"
    paletteDark: "SitesCreateParamsConfigThemePaletteDark"
    font: str
    colorScheme: str
    contentWidth: str
    onThisPage: str
    layout: "SitesCreateParamsConfigThemeLayout"
    customFontUrl: Any
    customFontFamily: str
    brandName: Any
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    typography: "SitesCreateParamsConfigThemeTypography"
    fonts: "SitesCreateParamsConfigThemeFonts"
    logoUrl: Any
    logoMark: Any
    faviconUrl: Any
    customCss: str
    customJs: str
    scriptOrigins: List[str]
    ads: "SitesCreateParamsConfigThemeAds"
    whiteLabel: bool
    showLanguageSwitcher: bool
    apiOrigins: List[str]
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    imgOrigins: List[str]
    mediaOrigins: List[str]
    frameOrigins: List[str]
    elementStyles: List["SitesCreateParamsConfigThemeElementStyle"]
    settingsSchema: List["SitesCreateParamsConfigThemeSettingsSchemaItem"]
    settings: Dict[str, Any]
    stringOverrides: Dict[str, Any]
    cssSnippets: List["SitesCreateParamsConfigThemeCssSnippet"]
    announcement: "SitesCreateParamsConfigThemeAnnouncement"
    chrome: "SitesCreateParamsConfigThemeChrome"
    notFound: "SitesCreateParamsConfigThemeNotFound"
    components: "SitesCreateParamsConfigThemeComponents"
    motion: "SitesCreateParamsConfigThemeMotion"
    componentInstalls: List["SitesCreateParamsConfigThemeComponentInstall"]
    mobile: "SitesCreateParamsConfigThemeMobile"


class SitesCreateParamsConfig(TypedDict, total=False):
    cta: "SitesCreateParamsConfigCta"
    secondaryCta: "SitesCreateParamsConfigSecondaryCta"
    header: "SitesCreateParamsConfigHeader"
    headerLinks: List["SitesCreateParamsConfigHeaderLink"]
    navMenu: "SitesCreateParamsConfigNavMenu"
    footerLinks: List["SitesCreateParamsConfigFooterLink"]
    footerDescription: str
    footerColumns: List["SitesCreateParamsConfigFooterColumn"]
    socialLinks: List["SitesCreateParamsConfigSocialLink"]
    copyright: str
    footer: "SitesCreateParamsConfigFooter"
    mobileNav: str
    sticky: bool
    height: str
    align: str
    ctaStyle: str
    showSignIn: bool
    themeToggle: "SitesCreateParamsConfigThemeToggle"
    sidebarBrand: str
    tagline: str
    tabs: List["SitesCreateParamsConfigTab"]
    headerSpaceIds: List[str]
    theme: "SitesCreateParamsConfigTheme"


class SitesCreateParams(TypedDict, total=False):
    slug: str
    name: str
    spaceIds: List[str]
    config: "SitesCreateParamsConfig"


class SitesCreateResponse(TypedDict, total=False):
    site: "SiteSummary"
    data: "SiteSummary"
    warnings: List[str]


class SitesGetResponse(TypedDict, total=False):
    site: "SiteSummary"


class SitesUpdateParamsConfigCta(TypedDict, total=False):
    label: Optional[str]
    href: Optional[str]


class SitesUpdateParamsConfigSecondaryCta(TypedDict, total=False):
    label: Optional[str]
    href: Optional[str]
    style: Optional[str]


class SitesUpdateParamsConfigHeader(TypedDict, total=False):
    overlay: Optional[bool]
    overlayInk: Optional[str]
    height: Optional[int]
    border: Optional[str]
    borderColor: Optional[str]
    shadow: Optional[str]
    blur: Optional[int]
    opacity: Optional[float]
    logoHeight: Optional[int]
    navGap: Optional[int]
    navWeight: Optional[int]
    navSize: Optional[float]
    navCase: Optional[str]
    navTracking: Optional[float]


class SitesUpdateParamsConfigHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SitesUpdateParamsConfigHeaderLinkPanelColumnLink(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SitesUpdateParamsConfigHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List["SitesUpdateParamsConfigHeaderLinkPanelColumnLink"]


class SitesUpdateParamsConfigHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class SitesUpdateParamsConfigHeaderLinkPanelFooterLink(TypedDict, total=False):
    label: str
    href: str


class SitesUpdateParamsConfigHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class SitesUpdateParamsConfigHeaderLinkPanelFooter(TypedDict, total=False):
    links: List["SitesUpdateParamsConfigHeaderLinkPanelFooterLink"]
    cta: "SitesUpdateParamsConfigHeaderLinkPanelFooterCta"


class SitesUpdateParamsConfigHeaderLinkPanel(TypedDict, total=False):
    columns: List["SitesUpdateParamsConfigHeaderLinkPanelColumn"]
    featured: "SitesUpdateParamsConfigHeaderLinkPanelFeatured"
    footer: "SitesUpdateParamsConfigHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class SitesUpdateParamsConfigHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["SitesUpdateParamsConfigHeaderLinkChildrenItem"]
    panel: "SitesUpdateParamsConfigHeaderLinkPanel"
    style: str
    highlight: bool


class SitesUpdateParamsConfigNavMenu(TypedDict, total=False):
    trigger: Optional[str]
    openDelay: Optional[int]
    closeDelay: Optional[int]
    animation: Optional[str]
    radius: Optional[float]
    shadow: Optional[str]
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    width: Optional[int]


class SitesUpdateParamsConfigFooterLink(TypedDict, total=False):
    label: str
    href: str


class SitesUpdateParamsConfigFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class SitesUpdateParamsConfigFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SitesUpdateParamsConfigFooterColumnLink"]


class SitesUpdateParamsConfigSocialLink(TypedDict, total=False):
    platform: str
    href: str


class SitesUpdateParamsConfigFooterNewsletter(TypedDict, total=False):
    formId: Optional[str]
    heading: Optional[str]


class SitesUpdateParamsConfigFooter(TypedDict, total=False):
    logo: Optional[Any]
    logoMark: Optional[Any]
    cookieLinkPlacement: Optional[str]
    html: Optional[str]
    css: Optional[str]
    htmlPlacement: Optional[str]
    newsletter: Optional["SitesUpdateParamsConfigFooterNewsletter"]


class SitesUpdateParamsConfigThemeToggle(TypedDict, total=False):
    show: Optional[bool]
    style: Optional[str]
    position: Optional[str]
    radius: Optional[float]
    activeColor: Optional[str]


class SitesUpdateParamsConfigTab(TypedDict, total=False):
    title: str
    slug: str
    spaceIds: List[str]


class SitesUpdateParamsConfigThemePalette(TypedDict, total=False):
    primary: Optional[str]
    secondary: Optional[str]
    tertiary: Optional[str]
    quaternary: Optional[str]
    header_background: Optional[str]
    header_primary: Optional[str]
    highlight: Optional[str]
    danger: Optional[str]
    success: Optional[str]
    love: Optional[str]
    background: Optional[str]
    surface: Optional[str]


class SitesUpdateParamsConfigThemePaletteDark(TypedDict, total=False):
    primary: Optional[str]
    secondary: Optional[str]
    tertiary: Optional[str]
    quaternary: Optional[str]
    header_background: Optional[str]
    header_primary: Optional[str]
    highlight: Optional[str]
    danger: Optional[str]
    success: Optional[str]
    love: Optional[str]
    background: Optional[str]
    surface: Optional[str]


class SitesUpdateParamsConfigThemeLayout(TypedDict, total=False):
    measure: Optional[str]


class SitesUpdateParamsConfigThemeTypographyFluid(TypedDict, total=False):
    enabled: Optional[bool]
    minViewport: Optional[int]
    maxViewport: Optional[int]
    minScale: Optional[float]
    bodyMinScale: Optional[float]


class SitesUpdateParamsConfigThemeTypographyLevelsH1(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SitesUpdateParamsConfigThemeTypographyLevelsH2(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SitesUpdateParamsConfigThemeTypographyLevelsH3(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SitesUpdateParamsConfigThemeTypographyLevelsH4(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SitesUpdateParamsConfigThemeTypographyLevelsH5(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SitesUpdateParamsConfigThemeTypographyLevelsH6(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SitesUpdateParamsConfigThemeTypographyLevelsBody(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SitesUpdateParamsConfigThemeTypographyLevelsSmall(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SitesUpdateParamsConfigThemeTypographyLevelsCode(TypedDict, total=False):
    size: Optional[float]
    lineHeight: Optional[float]
    tracking: Optional[float]
    weight: Optional[int]


class SitesUpdateParamsConfigThemeTypographyLevels(TypedDict, total=False):
    h1: Optional["SitesUpdateParamsConfigThemeTypographyLevelsH1"]
    h2: Optional["SitesUpdateParamsConfigThemeTypographyLevelsH2"]
    h3: Optional["SitesUpdateParamsConfigThemeTypographyLevelsH3"]
    h4: Optional["SitesUpdateParamsConfigThemeTypographyLevelsH4"]
    h5: Optional["SitesUpdateParamsConfigThemeTypographyLevelsH5"]
    h6: Optional["SitesUpdateParamsConfigThemeTypographyLevelsH6"]
    body: Optional["SitesUpdateParamsConfigThemeTypographyLevelsBody"]
    small: Optional["SitesUpdateParamsConfigThemeTypographyLevelsSmall"]
    code: Optional["SitesUpdateParamsConfigThemeTypographyLevelsCode"]


class SitesUpdateParamsConfigThemeTypographyVariation(TypedDict, total=False):
    heading: Optional[str]
    body: Optional[str]
    code: Optional[str]


class SitesUpdateParamsConfigThemeTypographyFeatures(TypedDict, total=False):
    heading: Optional[str]
    body: Optional[str]
    code: Optional[str]


class SitesUpdateParamsConfigThemeTypography(TypedDict, total=False):
    scale: Optional[str]
    baseSize: Optional[float]
    fluid: Optional["SitesUpdateParamsConfigThemeTypographyFluid"]
    levels: Optional["SitesUpdateParamsConfigThemeTypographyLevels"]
    headingTransform: Optional[str]
    variation: Optional["SitesUpdateParamsConfigThemeTypographyVariation"]
    features: Optional["SitesUpdateParamsConfigThemeTypographyFeatures"]
    opticalSizing: Optional[str]
    headingWrap: Optional[str]
    bodyWrap: Optional[str]


class SitesUpdateParamsConfigThemeFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class SitesUpdateParamsConfigThemeFonts(TypedDict, total=False):
    faces: Optional[List["SitesUpdateParamsConfigThemeFontsFace"]]


class SitesUpdateParamsConfigThemeAds(TypedDict, total=False):
    network: str
    publisherId: str
    slotId: str
    size: str
    enabled: bool
    scriptUrl: str
    slotHtml: str
    configVar: str
    configJson: Dict[str, Any]


class SitesUpdateParamsConfigThemeElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class SitesUpdateParamsConfigThemeSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class SitesUpdateParamsConfigThemeCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class SitesUpdateParamsConfigThemeAnnouncement(TypedDict, total=False):
    text: Optional[str]
    level: Optional[str]
    href: Optional[Any]


class SitesUpdateParamsConfigThemeChromeCta(TypedDict, total=False):
    label: Optional[str]
    href: Optional[str]


class SitesUpdateParamsConfigThemeChromeSecondaryCta(TypedDict, total=False):
    label: Optional[str]
    href: Optional[str]
    style: Optional[str]


class SitesUpdateParamsConfigThemeChromeHeader(TypedDict, total=False):
    overlay: Optional[bool]
    overlayInk: Optional[str]
    height: Optional[int]
    border: Optional[str]
    borderColor: Optional[str]
    shadow: Optional[str]
    blur: Optional[int]
    opacity: Optional[float]
    logoHeight: Optional[int]
    navGap: Optional[int]
    navWeight: Optional[int]
    navSize: Optional[float]
    navCase: Optional[str]
    navTracking: Optional[float]


class SitesUpdateParamsConfigThemeChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class SitesUpdateParamsConfigThemeChromeHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class SitesUpdateParamsConfigThemeChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class SitesUpdateParamsConfigThemeChromeHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class SitesUpdateParamsConfigThemeChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List[Dict[str, Any]]
    cta: "SitesUpdateParamsConfigThemeChromeHeaderLinkPanelFooterCta"


class SitesUpdateParamsConfigThemeChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List["SitesUpdateParamsConfigThemeChromeHeaderLinkPanelColumn"]
    featured: "SitesUpdateParamsConfigThemeChromeHeaderLinkPanelFeatured"
    footer: "SitesUpdateParamsConfigThemeChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class SitesUpdateParamsConfigThemeChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["SitesUpdateParamsConfigThemeChromeHeaderLinkChildrenItem"]
    panel: "SitesUpdateParamsConfigThemeChromeHeaderLinkPanel"
    style: str
    highlight: bool


class SitesUpdateParamsConfigThemeChromeNavMenu(TypedDict, total=False):
    trigger: Optional[str]
    openDelay: Optional[int]
    closeDelay: Optional[int]
    animation: Optional[str]
    radius: Optional[float]
    shadow: Optional[str]
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    width: Optional[int]


class SitesUpdateParamsConfigThemeChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class SitesUpdateParamsConfigThemeChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class SitesUpdateParamsConfigThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["SitesUpdateParamsConfigThemeChromeFooterColumnLink"]


class SitesUpdateParamsConfigThemeChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class SitesUpdateParamsConfigThemeChromeFooterNewsletter(TypedDict, total=False):
    formId: Optional[str]
    heading: Optional[str]


class SitesUpdateParamsConfigThemeChromeFooter(TypedDict, total=False):
    logo: Optional[Any]
    logoMark: Optional[Any]
    cookieLinkPlacement: Optional[str]
    html: Optional[str]
    css: Optional[str]
    htmlPlacement: Optional[str]
    newsletter: Optional["SitesUpdateParamsConfigThemeChromeFooterNewsletter"]


class SitesUpdateParamsConfigThemeChromeThemeToggle(TypedDict, total=False):
    show: Optional[bool]
    style: Optional[str]
    position: Optional[str]
    radius: Optional[float]
    activeColor: Optional[str]


class SitesUpdateParamsConfigThemeChrome(TypedDict, total=False):
    cta: Optional["SitesUpdateParamsConfigThemeChromeCta"]
    secondaryCta: Optional["SitesUpdateParamsConfigThemeChromeSecondaryCta"]
    header: Optional["SitesUpdateParamsConfigThemeChromeHeader"]
    headerLinks: Optional[List["SitesUpdateParamsConfigThemeChromeHeaderLink"]]
    navMenu: Optional["SitesUpdateParamsConfigThemeChromeNavMenu"]
    footerLinks: Optional[List["SitesUpdateParamsConfigThemeChromeFooterLink"]]
    footerDescription: Optional[str]
    footerColumns: Optional[List["SitesUpdateParamsConfigThemeChromeFooterColumn"]]
    socialLinks: Optional[List["SitesUpdateParamsConfigThemeChromeSocialLink"]]
    copyright: Optional[str]
    footer: Optional["SitesUpdateParamsConfigThemeChromeFooter"]
    mobileNav: Optional[str]
    sticky: Optional[bool]
    height: Optional[str]
    align: Optional[str]
    ctaStyle: Optional[str]
    showSignIn: Optional[bool]
    themeToggle: Optional["SitesUpdateParamsConfigThemeChromeThemeToggle"]
    sidebarBrand: Optional[str]


class SitesUpdateParamsConfigThemeNotFoundLink(TypedDict, total=False):
    label: str
    href: str


class SitesUpdateParamsConfigThemeNotFound(TypedDict, total=False):
    title: Optional[str]
    body: Optional[str]
    pageId: Optional[str]
    pageSpaceId: Optional[str]
    hidePage: Optional[bool]
    links: Optional[List["SitesUpdateParamsConfigThemeNotFoundLink"]]
    showSearch: Optional[bool]
    showSections: Optional[bool]
    hideSearch: Optional[bool]


class SitesUpdateParamsConfigThemeComponentsFocus(TypedDict, total=False):
    color: Optional[str]
    width: Optional[float]
    offset: Optional[float]


class SitesUpdateParamsConfigThemeComponentsCode(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    radius: Optional[float]


class SitesUpdateParamsConfigThemeComponentsInput(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    radius: Optional[float]


class SitesUpdateParamsConfigThemeComponentsButton(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]
    border: Optional[str]
    radius: Optional[float]
    shadow: Optional[str]
    weight: Optional[str]


class SitesUpdateParamsConfigThemeComponentsSpacing(TypedDict, total=False):
    scale: Optional[float]
    block: Optional[float]
    section: Optional[float]
    pad: Optional[float]


class SitesUpdateParamsConfigThemeComponentsSelection(TypedDict, total=False):
    background: Optional[str]
    ink: Optional[str]


class SitesUpdateParamsConfigThemeComponentsScrollbar(TypedDict, total=False):
    width: Optional[str]
    thumb: Optional[str]
    track: Optional[str]


class SitesUpdateParamsConfigThemeComponentsSyntax(TypedDict, total=False):
    comment: Optional[str]
    keyword: Optional[str]
    string: Optional[str]
    number: Optional[str]
    title: Optional[str]
    built_in: Optional[str]
    tag: Optional[str]
    attr: Optional[str]
    meta: Optional[str]
    emphasis: Optional[str]


class SitesUpdateParamsConfigThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: Optional[str]
    keyword: Optional[str]
    string: Optional[str]
    number: Optional[str]
    title: Optional[str]
    built_in: Optional[str]
    tag: Optional[str]
    attr: Optional[str]
    meta: Optional[str]
    emphasis: Optional[str]


class SitesUpdateParamsConfigThemeComponents(TypedDict, total=False):
    radius: Optional[float]
    shadow: Optional[str]
    focus: Optional["SitesUpdateParamsConfigThemeComponentsFocus"]
    code: Optional["SitesUpdateParamsConfigThemeComponentsCode"]
    input: Optional["SitesUpdateParamsConfigThemeComponentsInput"]
    button: Optional["SitesUpdateParamsConfigThemeComponentsButton"]
    spacing: Optional["SitesUpdateParamsConfigThemeComponentsSpacing"]
    selection: Optional["SitesUpdateParamsConfigThemeComponentsSelection"]
    scrollbar: Optional["SitesUpdateParamsConfigThemeComponentsScrollbar"]
    syntax: Optional["SitesUpdateParamsConfigThemeComponentsSyntax"]
    syntaxDark: Optional["SitesUpdateParamsConfigThemeComponentsSyntaxDark"]


class SitesUpdateParamsConfigThemeMotionReveal(TypedDict, total=False):
    effect: Optional[str]
    stagger: Optional[int]
    distance: Optional[int]
    once: Optional[bool]
    targets: Optional[List[str]]


class SitesUpdateParamsConfigThemeMotionHover(TypedDict, total=False):
    link: Optional[str]
    button: Optional[str]
    card: Optional[str]
    image: Optional[str]


class SitesUpdateParamsConfigThemeMotionHeader(TypedDict, total=False):
    behavior: Optional[str]
    blur: Optional[bool]


class SitesUpdateParamsConfigThemeMotionAmbient(TypedDict, total=False):
    background: Optional[str]
    cursorGlow: Optional[bool]
    scrollProgress: Optional[bool]
    smoothScroll: Optional[bool]
    focusRing: Optional[bool]


class SitesUpdateParamsConfigThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class SitesUpdateParamsConfigThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["SitesUpdateParamsConfigThemeMotionKeyframeStep"]


class SitesUpdateParamsConfigThemeMotion(TypedDict, total=False):
    preset: Optional[str]
    enabled: Optional[bool]
    respectReducedMotion: Optional[bool]
    speed: Optional[float]
    easing: Optional[str]
    pageTransition: Optional[str]
    reveal: Optional["SitesUpdateParamsConfigThemeMotionReveal"]
    hover: Optional["SitesUpdateParamsConfigThemeMotionHover"]
    header: Optional["SitesUpdateParamsConfigThemeMotionHeader"]
    ambient: Optional["SitesUpdateParamsConfigThemeMotionAmbient"]
    keyframes: Optional[List["SitesUpdateParamsConfigThemeMotionKeyframe"]]
    targets: Optional[Dict[str, Any]]


class SitesUpdateParamsConfigThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class SitesUpdateParamsConfigThemeMobile(TypedDict, total=False):
    fontScale: Optional[float]
    density: Optional[str]
    logoUrl: Optional[Any]
    hide: Optional[List[str]]
    css: Optional[str]


class SitesUpdateParamsConfigTheme(TypedDict, total=False):
    primaryColor: Optional[str]
    accentColor: Optional[str]
    palette: Optional["SitesUpdateParamsConfigThemePalette"]
    paletteDark: Optional["SitesUpdateParamsConfigThemePaletteDark"]
    font: Optional[str]
    colorScheme: Optional[str]
    contentWidth: Optional[str]
    onThisPage: Optional[str]
    layout: Optional["SitesUpdateParamsConfigThemeLayout"]
    customFontUrl: Optional[Any]
    customFontFamily: Optional[str]
    brandName: Optional[Any]
    headingFontFamily: Optional[str]
    bodyFontFamily: Optional[str]
    monoFontFamily: Optional[str]
    typography: Optional["SitesUpdateParamsConfigThemeTypography"]
    fonts: Optional["SitesUpdateParamsConfigThemeFonts"]
    logoUrl: Optional[Any]
    logoMark: Optional[Any]
    faviconUrl: Optional[Any]
    customCss: Optional[str]
    customJs: Optional[str]
    scriptOrigins: Optional[List[str]]
    ads: Optional["SitesUpdateParamsConfigThemeAds"]
    whiteLabel: Optional[bool]
    showLanguageSwitcher: Optional[bool]
    apiOrigins: Optional[List[str]]
    fontOrigins: Optional[List[str]]
    fontOriginsRemoved: Optional[List[str]]
    imgOrigins: Optional[List[str]]
    mediaOrigins: Optional[List[str]]
    frameOrigins: Optional[List[str]]
    elementStyles: Optional[List["SitesUpdateParamsConfigThemeElementStyle"]]
    settingsSchema: Optional[List["SitesUpdateParamsConfigThemeSettingsSchemaItem"]]
    settings: Optional[Dict[str, Any]]
    stringOverrides: Optional[Dict[str, Any]]
    cssSnippets: Optional[List["SitesUpdateParamsConfigThemeCssSnippet"]]
    announcement: Optional["SitesUpdateParamsConfigThemeAnnouncement"]
    chrome: Optional["SitesUpdateParamsConfigThemeChrome"]
    notFound: Optional["SitesUpdateParamsConfigThemeNotFound"]
    components: Optional["SitesUpdateParamsConfigThemeComponents"]
    motion: Optional["SitesUpdateParamsConfigThemeMotion"]
    componentInstalls: Optional[List["SitesUpdateParamsConfigThemeComponentInstall"]]
    mobile: Optional["SitesUpdateParamsConfigThemeMobile"]


class SitesUpdateParamsConfig(TypedDict, total=False):
    cta: Optional["SitesUpdateParamsConfigCta"]
    secondaryCta: Optional["SitesUpdateParamsConfigSecondaryCta"]
    header: Optional["SitesUpdateParamsConfigHeader"]
    headerLinks: Optional[List["SitesUpdateParamsConfigHeaderLink"]]
    navMenu: Optional["SitesUpdateParamsConfigNavMenu"]
    footerLinks: Optional[List["SitesUpdateParamsConfigFooterLink"]]
    footerDescription: Optional[str]
    footerColumns: Optional[List["SitesUpdateParamsConfigFooterColumn"]]
    socialLinks: Optional[List["SitesUpdateParamsConfigSocialLink"]]
    copyright: Optional[str]
    footer: Optional["SitesUpdateParamsConfigFooter"]
    mobileNav: Optional[str]
    sticky: Optional[bool]
    height: Optional[str]
    align: Optional[str]
    ctaStyle: Optional[str]
    showSignIn: Optional[bool]
    themeToggle: Optional["SitesUpdateParamsConfigThemeToggle"]
    sidebarBrand: Optional[str]
    tagline: Optional[str]
    tabs: Optional[List["SitesUpdateParamsConfigTab"]]
    headerSpaceIds: Optional[List[str]]
    theme: Optional["SitesUpdateParamsConfigTheme"]


class SitesUpdateParams(TypedDict, total=False):
    name: str
    spaceIds: List[str]
    config: "SitesUpdateParamsConfig"


class SitesUpdateResponse(TypedDict, total=False):
    site: "SiteSummary"
    warnings: List[str]


class SitesRemoveResponse(TypedDict, total=False):
    ok: bool


class SitesSetStagingParams(TypedDict, total=False):
    staging: bool


class SitesSetStagingResponse(TypedDict, total=False):
    staging: bool
    stagingToken: Any
    warnings: List[str]


class SitesListDomainsResponse(TypedDict, total=False):
    domains: List["DomainSummary"]
    page: "PageInfo"


class SitesAddDomainParams(TypedDict, total=False):
    hostname: str
    basePath: str


class SitesAddDomainResponse(TypedDict, total=False):
    domain: "DomainSummary"
    data: "DomainSummary"
    warnings: List[str]


class SitesAllocateSubdomainParams(TypedDict, total=False):
    subdomain: str


class SitesAllocateSubdomainResponse(TypedDict, total=False):
    domain: "DomainSummary"
    data: "DomainSummary"
    warnings: List[str]


class SitesVerifyDomainParams(TypedDict, total=False):
    activate: bool


class SitesVerifyDomainResponse(TypedDict, total=False):
    domain: "DomainSummary"
    warnings: List[str]


class SitesActivateDomainResponse(TypedDict, total=False):
    domain: "DomainSummary"


class SitesRemoveDomainResponse(TypedDict, total=False):
    ok: bool


class PublicSitesSearchResponse(TypedDict, total=False):
    hits: List["OrgSearchHit"]
    minQueryLength: float


class PublicSitesAskParams(TypedDict, total=False):
    question: str


class PublicSitesAskResponseResultCitation(TypedDict, total=False):
    anchor: str
    itemId: str
    slot: str
    title: str
    url: Any


class PublicSitesAskResponseResult(TypedDict, total=False):
    answer: str
    answered: bool
    citations: List["PublicSitesAskResponseResultCitation"]
    citedRefs: List[str]
    citedTitles: List[str]
    queryId: Any


class PublicSitesAskResponse(TypedDict, total=False):
    result: "PublicSitesAskResponseResult"
    warnings: List[str]


class ThemesBundlesImportSpaceParamsMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesBundlesImportSpaceParamsMetaPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesBundlesImportSpaceParamsMeta(TypedDict, total=False):
    name: str
    slug: str
    description: str
    author: "ThemesBundlesImportSpaceParamsMetaAuthor"
    version: str
    license: str
    homepage: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesBundlesImportSpaceParamsMetaPreviewImage"]


class ThemesBundlesImportSpaceParamsRequiredOrigins(TypedDict, total=False):
    fonts: List[str]
    images: List[str]


class ThemesBundlesImportSpaceParamsThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ThemesBundlesImportSpaceParamsThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ThemesBundlesImportSpaceParamsThemeLayout(TypedDict, total=False):
    measure: str


class ThemesBundlesImportSpaceParamsThemeTypographyFluid(TypedDict, total=False):
    enabled: bool
    minViewport: int
    maxViewport: int
    minScale: float
    bodyMinScale: float


class ThemesBundlesImportSpaceParamsThemeTypographyLevelsH1(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSpaceParamsThemeTypographyLevelsH2(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSpaceParamsThemeTypographyLevelsH3(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSpaceParamsThemeTypographyLevelsH4(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSpaceParamsThemeTypographyLevelsH5(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSpaceParamsThemeTypographyLevelsH6(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSpaceParamsThemeTypographyLevelsBody(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSpaceParamsThemeTypographyLevelsSmall(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSpaceParamsThemeTypographyLevelsCode(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSpaceParamsThemeTypographyLevels(TypedDict, total=False):
    h1: "ThemesBundlesImportSpaceParamsThemeTypographyLevelsH1"
    h2: "ThemesBundlesImportSpaceParamsThemeTypographyLevelsH2"
    h3: "ThemesBundlesImportSpaceParamsThemeTypographyLevelsH3"
    h4: "ThemesBundlesImportSpaceParamsThemeTypographyLevelsH4"
    h5: "ThemesBundlesImportSpaceParamsThemeTypographyLevelsH5"
    h6: "ThemesBundlesImportSpaceParamsThemeTypographyLevelsH6"
    body: "ThemesBundlesImportSpaceParamsThemeTypographyLevelsBody"
    small: "ThemesBundlesImportSpaceParamsThemeTypographyLevelsSmall"
    code: "ThemesBundlesImportSpaceParamsThemeTypographyLevelsCode"


class ThemesBundlesImportSpaceParamsThemeTypographyVariation(TypedDict, total=False):
    heading: str
    body: str
    code: str


class ThemesBundlesImportSpaceParamsThemeTypographyFeatures(TypedDict, total=False):
    heading: str
    body: str
    code: str


class ThemesBundlesImportSpaceParamsThemeTypography(TypedDict, total=False):
    scale: str
    baseSize: float
    fluid: "ThemesBundlesImportSpaceParamsThemeTypographyFluid"
    levels: "ThemesBundlesImportSpaceParamsThemeTypographyLevels"
    headingTransform: str
    variation: "ThemesBundlesImportSpaceParamsThemeTypographyVariation"
    features: "ThemesBundlesImportSpaceParamsThemeTypographyFeatures"
    opticalSizing: str
    headingWrap: str
    bodyWrap: str


class ThemesBundlesImportSpaceParamsThemeFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class ThemesBundlesImportSpaceParamsThemeFonts(TypedDict, total=False):
    faces: List["ThemesBundlesImportSpaceParamsThemeFontsFace"]


class ThemesBundlesImportSpaceParamsThemeElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class ThemesBundlesImportSpaceParamsThemeSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class ThemesBundlesImportSpaceParamsThemeCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class ThemesBundlesImportSpaceParamsThemeChromeCta(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSpaceParamsThemeChromeSecondaryCta(TypedDict, total=False):
    label: str
    href: str
    style: str


class ThemesBundlesImportSpaceParamsThemeChromeHeader(TypedDict, total=False):
    overlay: bool
    overlayInk: str
    height: int
    border: str
    borderColor: str
    shadow: str
    blur: int
    opacity: float
    logoHeight: int
    navGap: int
    navWeight: int
    navSize: float
    navCase: str
    navTracking: float


class ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelFooterLink(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List["ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelFooterLink"]
    cta: "ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelFooterCta"


class ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List["ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelColumn"]
    featured: "ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelFeatured"
    footer: "ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class ThemesBundlesImportSpaceParamsThemeChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkChildrenItem"]
    panel: "ThemesBundlesImportSpaceParamsThemeChromeHeaderLinkPanel"
    style: str
    highlight: bool


class ThemesBundlesImportSpaceParamsThemeChromeNavMenu(TypedDict, total=False):
    trigger: str
    openDelay: int
    closeDelay: int
    animation: str
    radius: float
    shadow: str
    background: str
    ink: str
    border: str
    width: int


class ThemesBundlesImportSpaceParamsThemeChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSpaceParamsThemeChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSpaceParamsThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["ThemesBundlesImportSpaceParamsThemeChromeFooterColumnLink"]


class ThemesBundlesImportSpaceParamsThemeChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class ThemesBundlesImportSpaceParamsThemeChromeFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class ThemesBundlesImportSpaceParamsThemeChromeFooter(TypedDict, total=False):
    logo: Any
    logoMark: Any
    cookieLinkPlacement: str
    html: str
    css: str
    htmlPlacement: str
    newsletter: "ThemesBundlesImportSpaceParamsThemeChromeFooterNewsletter"


class ThemesBundlesImportSpaceParamsThemeChromeThemeToggle(TypedDict, total=False):
    show: bool
    style: str
    position: str
    radius: float
    activeColor: str


class ThemesBundlesImportSpaceParamsThemeChrome(TypedDict, total=False):
    cta: "ThemesBundlesImportSpaceParamsThemeChromeCta"
    secondaryCta: "ThemesBundlesImportSpaceParamsThemeChromeSecondaryCta"
    header: "ThemesBundlesImportSpaceParamsThemeChromeHeader"
    headerLinks: List["ThemesBundlesImportSpaceParamsThemeChromeHeaderLink"]
    navMenu: "ThemesBundlesImportSpaceParamsThemeChromeNavMenu"
    footerLinks: List["ThemesBundlesImportSpaceParamsThemeChromeFooterLink"]
    footerDescription: str
    footerColumns: List["ThemesBundlesImportSpaceParamsThemeChromeFooterColumn"]
    socialLinks: List["ThemesBundlesImportSpaceParamsThemeChromeSocialLink"]
    copyright: str
    footer: "ThemesBundlesImportSpaceParamsThemeChromeFooter"
    mobileNav: str
    sticky: bool
    height: str
    align: str
    ctaStyle: str
    showSignIn: bool
    themeToggle: "ThemesBundlesImportSpaceParamsThemeChromeThemeToggle"
    sidebarBrand: str


class ThemesBundlesImportSpaceParamsThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class ThemesBundlesImportSpaceParamsThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ThemesBundlesImportSpaceParamsThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ThemesBundlesImportSpaceParamsThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class ThemesBundlesImportSpaceParamsThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class ThemesBundlesImportSpaceParamsThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemesBundlesImportSpaceParamsThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class ThemesBundlesImportSpaceParamsThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ThemesBundlesImportSpaceParamsThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ThemesBundlesImportSpaceParamsThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "ThemesBundlesImportSpaceParamsThemeComponentsFocus"
    code: "ThemesBundlesImportSpaceParamsThemeComponentsCode"
    input: "ThemesBundlesImportSpaceParamsThemeComponentsInput"
    button: "ThemesBundlesImportSpaceParamsThemeComponentsButton"
    spacing: "ThemesBundlesImportSpaceParamsThemeComponentsSpacing"
    selection: "ThemesBundlesImportSpaceParamsThemeComponentsSelection"
    scrollbar: "ThemesBundlesImportSpaceParamsThemeComponentsScrollbar"
    syntax: "ThemesBundlesImportSpaceParamsThemeComponentsSyntax"
    syntaxDark: "ThemesBundlesImportSpaceParamsThemeComponentsSyntaxDark"


class ThemesBundlesImportSpaceParamsThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class ThemesBundlesImportSpaceParamsThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class ThemesBundlesImportSpaceParamsThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemesBundlesImportSpaceParamsThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class ThemesBundlesImportSpaceParamsThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class ThemesBundlesImportSpaceParamsThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["ThemesBundlesImportSpaceParamsThemeMotionKeyframeStep"]


class ThemesBundlesImportSpaceParamsThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "ThemesBundlesImportSpaceParamsThemeMotionReveal"
    hover: "ThemesBundlesImportSpaceParamsThemeMotionHover"
    header: "ThemesBundlesImportSpaceParamsThemeMotionHeader"
    ambient: "ThemesBundlesImportSpaceParamsThemeMotionAmbient"
    keyframes: List["ThemesBundlesImportSpaceParamsThemeMotionKeyframe"]
    targets: Dict[str, Any]


class ThemesBundlesImportSpaceParamsThemeMobile(TypedDict, total=False):
    fontScale: float
    density: str
    logoUrl: Any
    hide: List[str]
    css: str


class ThemesBundlesImportSpaceParamsTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "ThemesBundlesImportSpaceParamsThemePalette"
    paletteDark: "ThemesBundlesImportSpaceParamsThemePaletteDark"
    font: str
    colorScheme: str
    contentWidth: str
    onThisPage: str
    layout: "ThemesBundlesImportSpaceParamsThemeLayout"
    customFontUrl: Any
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    typography: "ThemesBundlesImportSpaceParamsThemeTypography"
    fonts: "ThemesBundlesImportSpaceParamsThemeFonts"
    customCss: str
    showLanguageSwitcher: bool
    elementStyles: List["ThemesBundlesImportSpaceParamsThemeElementStyle"]
    settingsSchema: List["ThemesBundlesImportSpaceParamsThemeSettingsSchemaItem"]
    settings: Dict[str, Any]
    stringOverrides: Dict[str, Any]
    cssSnippets: List["ThemesBundlesImportSpaceParamsThemeCssSnippet"]
    chrome: "ThemesBundlesImportSpaceParamsThemeChrome"
    components: "ThemesBundlesImportSpaceParamsThemeComponents"
    motion: "ThemesBundlesImportSpaceParamsThemeMotion"
    mobile: "ThemesBundlesImportSpaceParamsThemeMobile"


class ThemesBundlesImportSpaceParamsComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesBundlesImportSpaceParamsComponentMetaPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesBundlesImportSpaceParamsComponentMeta(TypedDict, total=False):
    name: str
    slug: str
    description: str
    author: "ThemesBundlesImportSpaceParamsComponentMetaAuthor"
    version: str
    license: str
    homepage: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesBundlesImportSpaceParamsComponentMetaPreviewImage"]


class ThemesBundlesImportSpaceParamsComponent(TypedDict, total=False):
    format: str
    formatVersion: float
    meta: "ThemesBundlesImportSpaceParamsComponentMeta"
    css: str
    outlets: Dict[str, Any]
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ThemesBundlesImportSpaceParams(TypedDict, total=False):
    format: str
    formatVersion: float
    meta: "ThemesBundlesImportSpaceParamsMeta"
    requiredOrigins: "ThemesBundlesImportSpaceParamsRequiredOrigins"
    theme: "ThemesBundlesImportSpaceParamsTheme"
    components: List["ThemesBundlesImportSpaceParamsComponent"]


class ThemesBundlesApplySpaceParams(TypedDict, total=False):
    componentId: str
    firstParty: str


class ThemesBundlesImportSiteParamsMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesBundlesImportSiteParamsMetaPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesBundlesImportSiteParamsMeta(TypedDict, total=False):
    name: str
    slug: str
    description: str
    author: "ThemesBundlesImportSiteParamsMetaAuthor"
    version: str
    license: str
    homepage: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesBundlesImportSiteParamsMetaPreviewImage"]


class ThemesBundlesImportSiteParamsRequiredOrigins(TypedDict, total=False):
    fonts: List[str]
    images: List[str]


class ThemesBundlesImportSiteParamsThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ThemesBundlesImportSiteParamsThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ThemesBundlesImportSiteParamsThemeLayout(TypedDict, total=False):
    measure: str


class ThemesBundlesImportSiteParamsThemeTypographyFluid(TypedDict, total=False):
    enabled: bool
    minViewport: int
    maxViewport: int
    minScale: float
    bodyMinScale: float


class ThemesBundlesImportSiteParamsThemeTypographyLevelsH1(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSiteParamsThemeTypographyLevelsH2(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSiteParamsThemeTypographyLevelsH3(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSiteParamsThemeTypographyLevelsH4(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSiteParamsThemeTypographyLevelsH5(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSiteParamsThemeTypographyLevelsH6(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSiteParamsThemeTypographyLevelsBody(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSiteParamsThemeTypographyLevelsSmall(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSiteParamsThemeTypographyLevelsCode(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesBundlesImportSiteParamsThemeTypographyLevels(TypedDict, total=False):
    h1: "ThemesBundlesImportSiteParamsThemeTypographyLevelsH1"
    h2: "ThemesBundlesImportSiteParamsThemeTypographyLevelsH2"
    h3: "ThemesBundlesImportSiteParamsThemeTypographyLevelsH3"
    h4: "ThemesBundlesImportSiteParamsThemeTypographyLevelsH4"
    h5: "ThemesBundlesImportSiteParamsThemeTypographyLevelsH5"
    h6: "ThemesBundlesImportSiteParamsThemeTypographyLevelsH6"
    body: "ThemesBundlesImportSiteParamsThemeTypographyLevelsBody"
    small: "ThemesBundlesImportSiteParamsThemeTypographyLevelsSmall"
    code: "ThemesBundlesImportSiteParamsThemeTypographyLevelsCode"


class ThemesBundlesImportSiteParamsThemeTypographyVariation(TypedDict, total=False):
    heading: str
    body: str
    code: str


class ThemesBundlesImportSiteParamsThemeTypographyFeatures(TypedDict, total=False):
    heading: str
    body: str
    code: str


class ThemesBundlesImportSiteParamsThemeTypography(TypedDict, total=False):
    scale: str
    baseSize: float
    fluid: "ThemesBundlesImportSiteParamsThemeTypographyFluid"
    levels: "ThemesBundlesImportSiteParamsThemeTypographyLevels"
    headingTransform: str
    variation: "ThemesBundlesImportSiteParamsThemeTypographyVariation"
    features: "ThemesBundlesImportSiteParamsThemeTypographyFeatures"
    opticalSizing: str
    headingWrap: str
    bodyWrap: str


class ThemesBundlesImportSiteParamsThemeFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class ThemesBundlesImportSiteParamsThemeFonts(TypedDict, total=False):
    faces: List["ThemesBundlesImportSiteParamsThemeFontsFace"]


class ThemesBundlesImportSiteParamsThemeElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class ThemesBundlesImportSiteParamsThemeSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class ThemesBundlesImportSiteParamsThemeCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class ThemesBundlesImportSiteParamsThemeChromeCta(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSiteParamsThemeChromeSecondaryCta(TypedDict, total=False):
    label: str
    href: str
    style: str


class ThemesBundlesImportSiteParamsThemeChromeHeader(TypedDict, total=False):
    overlay: bool
    overlayInk: str
    height: int
    border: str
    borderColor: str
    shadow: str
    blur: int
    opacity: float
    logoHeight: int
    navGap: int
    navWeight: int
    navSize: float
    navCase: str
    navTracking: float


class ThemesBundlesImportSiteParamsThemeChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelFooterLink(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List["ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelFooterLink"]
    cta: "ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelFooterCta"


class ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List["ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelColumn"]
    featured: "ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelFeatured"
    footer: "ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class ThemesBundlesImportSiteParamsThemeChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["ThemesBundlesImportSiteParamsThemeChromeHeaderLinkChildrenItem"]
    panel: "ThemesBundlesImportSiteParamsThemeChromeHeaderLinkPanel"
    style: str
    highlight: bool


class ThemesBundlesImportSiteParamsThemeChromeNavMenu(TypedDict, total=False):
    trigger: str
    openDelay: int
    closeDelay: int
    animation: str
    radius: float
    shadow: str
    background: str
    ink: str
    border: str
    width: int


class ThemesBundlesImportSiteParamsThemeChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSiteParamsThemeChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class ThemesBundlesImportSiteParamsThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["ThemesBundlesImportSiteParamsThemeChromeFooterColumnLink"]


class ThemesBundlesImportSiteParamsThemeChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class ThemesBundlesImportSiteParamsThemeChromeFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class ThemesBundlesImportSiteParamsThemeChromeFooter(TypedDict, total=False):
    logo: Any
    logoMark: Any
    cookieLinkPlacement: str
    html: str
    css: str
    htmlPlacement: str
    newsletter: "ThemesBundlesImportSiteParamsThemeChromeFooterNewsletter"


class ThemesBundlesImportSiteParamsThemeChromeThemeToggle(TypedDict, total=False):
    show: bool
    style: str
    position: str
    radius: float
    activeColor: str


class ThemesBundlesImportSiteParamsThemeChrome(TypedDict, total=False):
    cta: "ThemesBundlesImportSiteParamsThemeChromeCta"
    secondaryCta: "ThemesBundlesImportSiteParamsThemeChromeSecondaryCta"
    header: "ThemesBundlesImportSiteParamsThemeChromeHeader"
    headerLinks: List["ThemesBundlesImportSiteParamsThemeChromeHeaderLink"]
    navMenu: "ThemesBundlesImportSiteParamsThemeChromeNavMenu"
    footerLinks: List["ThemesBundlesImportSiteParamsThemeChromeFooterLink"]
    footerDescription: str
    footerColumns: List["ThemesBundlesImportSiteParamsThemeChromeFooterColumn"]
    socialLinks: List["ThemesBundlesImportSiteParamsThemeChromeSocialLink"]
    copyright: str
    footer: "ThemesBundlesImportSiteParamsThemeChromeFooter"
    mobileNav: str
    sticky: bool
    height: str
    align: str
    ctaStyle: str
    showSignIn: bool
    themeToggle: "ThemesBundlesImportSiteParamsThemeChromeThemeToggle"
    sidebarBrand: str


class ThemesBundlesImportSiteParamsThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class ThemesBundlesImportSiteParamsThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ThemesBundlesImportSiteParamsThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ThemesBundlesImportSiteParamsThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class ThemesBundlesImportSiteParamsThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class ThemesBundlesImportSiteParamsThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemesBundlesImportSiteParamsThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class ThemesBundlesImportSiteParamsThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ThemesBundlesImportSiteParamsThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ThemesBundlesImportSiteParamsThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "ThemesBundlesImportSiteParamsThemeComponentsFocus"
    code: "ThemesBundlesImportSiteParamsThemeComponentsCode"
    input: "ThemesBundlesImportSiteParamsThemeComponentsInput"
    button: "ThemesBundlesImportSiteParamsThemeComponentsButton"
    spacing: "ThemesBundlesImportSiteParamsThemeComponentsSpacing"
    selection: "ThemesBundlesImportSiteParamsThemeComponentsSelection"
    scrollbar: "ThemesBundlesImportSiteParamsThemeComponentsScrollbar"
    syntax: "ThemesBundlesImportSiteParamsThemeComponentsSyntax"
    syntaxDark: "ThemesBundlesImportSiteParamsThemeComponentsSyntaxDark"


class ThemesBundlesImportSiteParamsThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class ThemesBundlesImportSiteParamsThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class ThemesBundlesImportSiteParamsThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemesBundlesImportSiteParamsThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class ThemesBundlesImportSiteParamsThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class ThemesBundlesImportSiteParamsThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["ThemesBundlesImportSiteParamsThemeMotionKeyframeStep"]


class ThemesBundlesImportSiteParamsThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "ThemesBundlesImportSiteParamsThemeMotionReveal"
    hover: "ThemesBundlesImportSiteParamsThemeMotionHover"
    header: "ThemesBundlesImportSiteParamsThemeMotionHeader"
    ambient: "ThemesBundlesImportSiteParamsThemeMotionAmbient"
    keyframes: List["ThemesBundlesImportSiteParamsThemeMotionKeyframe"]
    targets: Dict[str, Any]


class ThemesBundlesImportSiteParamsThemeMobile(TypedDict, total=False):
    fontScale: float
    density: str
    logoUrl: Any
    hide: List[str]
    css: str


class ThemesBundlesImportSiteParamsTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "ThemesBundlesImportSiteParamsThemePalette"
    paletteDark: "ThemesBundlesImportSiteParamsThemePaletteDark"
    font: str
    colorScheme: str
    contentWidth: str
    onThisPage: str
    layout: "ThemesBundlesImportSiteParamsThemeLayout"
    customFontUrl: Any
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    typography: "ThemesBundlesImportSiteParamsThemeTypography"
    fonts: "ThemesBundlesImportSiteParamsThemeFonts"
    customCss: str
    showLanguageSwitcher: bool
    elementStyles: List["ThemesBundlesImportSiteParamsThemeElementStyle"]
    settingsSchema: List["ThemesBundlesImportSiteParamsThemeSettingsSchemaItem"]
    settings: Dict[str, Any]
    stringOverrides: Dict[str, Any]
    cssSnippets: List["ThemesBundlesImportSiteParamsThemeCssSnippet"]
    chrome: "ThemesBundlesImportSiteParamsThemeChrome"
    components: "ThemesBundlesImportSiteParamsThemeComponents"
    motion: "ThemesBundlesImportSiteParamsThemeMotion"
    mobile: "ThemesBundlesImportSiteParamsThemeMobile"


class ThemesBundlesImportSiteParamsComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesBundlesImportSiteParamsComponentMetaPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesBundlesImportSiteParamsComponentMeta(TypedDict, total=False):
    name: str
    slug: str
    description: str
    author: "ThemesBundlesImportSiteParamsComponentMetaAuthor"
    version: str
    license: str
    homepage: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesBundlesImportSiteParamsComponentMetaPreviewImage"]


class ThemesBundlesImportSiteParamsComponent(TypedDict, total=False):
    format: str
    formatVersion: float
    meta: "ThemesBundlesImportSiteParamsComponentMeta"
    css: str
    outlets: Dict[str, Any]
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ThemesBundlesImportSiteParams(TypedDict, total=False):
    format: str
    formatVersion: float
    meta: "ThemesBundlesImportSiteParamsMeta"
    requiredOrigins: "ThemesBundlesImportSiteParamsRequiredOrigins"
    theme: "ThemesBundlesImportSiteParamsTheme"
    components: List["ThemesBundlesImportSiteParamsComponent"]


class ThemesBundlesApplySiteParams(TypedDict, total=False):
    componentId: str
    firstParty: str


class ThemesBundlesPublishSiteDraftParams(TypedDict, total=False):
    force: bool


class ThemesBundlesPublishSiteDraftResponseThemeAds(TypedDict, total=False):
    configJson: Dict[str, Any]
    configVar: str
    enabled: bool
    network: str
    publisherId: str
    scriptUrl: str
    size: str
    slotHtml: str
    slotId: str


class ThemesBundlesPublishSiteDraftResponseThemeAnnouncement(TypedDict, total=False):
    href: str
    level: str
    text: str


class ThemesBundlesPublishSiteDraftResponseThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class ThemesBundlesPublishSiteDraftResponseThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemesBundlesPublishSiteDraftResponseThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class ThemesBundlesPublishSiteDraftResponseThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class ThemesBundlesPublishSiteDraftResponseThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class ThemesBundlesPublishSiteDraftResponseThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class ThemesBundlesPublishSiteDraftResponseThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class ThemesBundlesPublishSiteDraftResponseThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "ThemesBundlesPublishSiteDraftResponseThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["ThemesBundlesPublishSiteDraftResponseThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["ThemesBundlesPublishSiteDraftResponseThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["ThemesBundlesPublishSiteDraftResponseThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "ThemesBundlesPublishSiteDraftResponseThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["ThemesBundlesPublishSiteDraftResponseThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "ThemesBundlesPublishSiteDraftResponseThemeChromeThemeToggle"


class ThemesBundlesPublishSiteDraftResponseThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ThemesBundlesPublishSiteDraftResponseThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class ThemesBundlesPublishSiteDraftResponseThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemesBundlesPublishSiteDraftResponseThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class ThemesBundlesPublishSiteDraftResponseThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class ThemesBundlesPublishSiteDraftResponseThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class ThemesBundlesPublishSiteDraftResponseThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemesBundlesPublishSiteDraftResponseThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class ThemesBundlesPublishSiteDraftResponseThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemesBundlesPublishSiteDraftResponseThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class ThemesBundlesPublishSiteDraftResponseThemeComponents(TypedDict, total=False):
    button: "ThemesBundlesPublishSiteDraftResponseThemeComponentsButton"
    code: "ThemesBundlesPublishSiteDraftResponseThemeComponentsCode"
    focus: "ThemesBundlesPublishSiteDraftResponseThemeComponentsFocus"
    input: "ThemesBundlesPublishSiteDraftResponseThemeComponentsInput"
    radius: float
    scrollbar: "ThemesBundlesPublishSiteDraftResponseThemeComponentsScrollbar"
    selection: "ThemesBundlesPublishSiteDraftResponseThemeComponentsSelection"
    shadow: str
    spacing: "ThemesBundlesPublishSiteDraftResponseThemeComponentsSpacing"
    syntax: "ThemesBundlesPublishSiteDraftResponseThemeComponentsSyntax"
    syntaxDark: "ThemesBundlesPublishSiteDraftResponseThemeComponentsSyntaxDark"


class ThemesBundlesPublishSiteDraftResponseThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class ThemesBundlesPublishSiteDraftResponseThemeLayout(TypedDict, total=False):
    measure: str


class ThemesBundlesPublishSiteDraftResponseThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class ThemesBundlesPublishSiteDraftResponseThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class ThemesBundlesPublishSiteDraftResponseThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemesBundlesPublishSiteDraftResponseThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class ThemesBundlesPublishSiteDraftResponseThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class ThemesBundlesPublishSiteDraftResponseThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


ThemesBundlesPublishSiteDraftResponseThemeMotionTargets = TypedDict("ThemesBundlesPublishSiteDraftResponseThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class ThemesBundlesPublishSiteDraftResponseThemeMotion(TypedDict, total=False):
    ambient: "ThemesBundlesPublishSiteDraftResponseThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "ThemesBundlesPublishSiteDraftResponseThemeMotionHeader"
    hover: "ThemesBundlesPublishSiteDraftResponseThemeMotionHover"
    keyframes: List["ThemesBundlesPublishSiteDraftResponseThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "ThemesBundlesPublishSiteDraftResponseThemeMotionReveal"
    speed: float
    targets: "ThemesBundlesPublishSiteDraftResponseThemeMotionTargets"


class ThemesBundlesPublishSiteDraftResponseThemeNotFoundLink(TypedDict, total=False):
    href: str
    label: str


class ThemesBundlesPublishSiteDraftResponseThemeNotFound(TypedDict, total=False):
    body: str
    hidePage: bool
    hideSearch: bool
    links: List["ThemesBundlesPublishSiteDraftResponseThemeNotFoundLink"]
    pageId: str
    pageSpaceId: str
    showSearch: bool
    showSections: bool
    title: str


class ThemesBundlesPublishSiteDraftResponseThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemesBundlesPublishSiteDraftResponseThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class ThemesBundlesPublishSiteDraftResponseThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class ThemesBundlesPublishSiteDraftResponseTheme(TypedDict, total=False):
    accentColor: str
    ads: "ThemesBundlesPublishSiteDraftResponseThemeAds"
    announcement: "ThemesBundlesPublishSiteDraftResponseThemeAnnouncement"
    apiOrigins: List[str]
    bodyFontFamily: str
    brandName: Any
    chrome: "ThemesBundlesPublishSiteDraftResponseThemeChrome"
    colorScheme: str
    componentInstalls: List["ThemesBundlesPublishSiteDraftResponseThemeComponentInstall"]
    components: "ThemesBundlesPublishSiteDraftResponseThemeComponents"
    contentWidth: str
    cssSnippets: List["ThemesBundlesPublishSiteDraftResponseThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    customJs: str
    elementStyles: List["ElementStyleRule"]
    faviconUrl: str
    font: str
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    fonts: "ThemeFonts"
    frameOrigins: List[str]
    headingFontFamily: str
    imgOrigins: List[str]
    layout: "ThemesBundlesPublishSiteDraftResponseThemeLayout"
    logoMark: str
    logoUrl: str
    mediaOrigins: List[str]
    mobile: "ThemesBundlesPublishSiteDraftResponseThemeMobile"
    monoFontFamily: str
    motion: "ThemesBundlesPublishSiteDraftResponseThemeMotion"
    notFound: "ThemesBundlesPublishSiteDraftResponseThemeNotFound"
    onThisPage: str
    palette: "ThemesBundlesPublishSiteDraftResponseThemePalette"
    paletteDark: "ThemesBundlesPublishSiteDraftResponseThemePaletteDark"
    primaryColor: str
    scriptOrigins: List[str]
    settings: Dict[str, Any]
    settingsSchema: List["ThemesBundlesPublishSiteDraftResponseThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"
    whiteLabel: bool


class ThemesBundlesPublishSiteDraftResponse(TypedDict, total=False):
    theme: "ThemesBundlesPublishSiteDraftResponseTheme"
    warnings: List[str]


class ThemesLibraryListResponse(TypedDict, total=False):
    themes: List["ThemeLibraryItem"]
    page: "PageInfo"


class ThemesLibrarySaveParamsPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesLibrarySaveParams(TypedDict, total=False):
    name: str
    description: str
    spaceId: str
    siteId: str
    version: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesLibrarySaveParamsPreviewImage"]


class ThemesLibraryImportParamsMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesLibraryImportParamsMetaPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesLibraryImportParamsMeta(TypedDict, total=False):
    name: str
    slug: str
    description: str
    author: "ThemesLibraryImportParamsMetaAuthor"
    version: str
    license: str
    homepage: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesLibraryImportParamsMetaPreviewImage"]


class ThemesLibraryImportParamsRequiredOrigins(TypedDict, total=False):
    fonts: List[str]
    images: List[str]


class ThemesLibraryImportParamsThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ThemesLibraryImportParamsThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class ThemesLibraryImportParamsThemeLayout(TypedDict, total=False):
    measure: str


class ThemesLibraryImportParamsThemeTypographyFluid(TypedDict, total=False):
    enabled: bool
    minViewport: int
    maxViewport: int
    minScale: float
    bodyMinScale: float


class ThemesLibraryImportParamsThemeTypographyLevelsH1(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesLibraryImportParamsThemeTypographyLevelsH2(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesLibraryImportParamsThemeTypographyLevelsH3(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesLibraryImportParamsThemeTypographyLevelsH4(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesLibraryImportParamsThemeTypographyLevelsH5(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesLibraryImportParamsThemeTypographyLevelsH6(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesLibraryImportParamsThemeTypographyLevelsBody(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesLibraryImportParamsThemeTypographyLevelsSmall(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesLibraryImportParamsThemeTypographyLevelsCode(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class ThemesLibraryImportParamsThemeTypographyLevels(TypedDict, total=False):
    h1: "ThemesLibraryImportParamsThemeTypographyLevelsH1"
    h2: "ThemesLibraryImportParamsThemeTypographyLevelsH2"
    h3: "ThemesLibraryImportParamsThemeTypographyLevelsH3"
    h4: "ThemesLibraryImportParamsThemeTypographyLevelsH4"
    h5: "ThemesLibraryImportParamsThemeTypographyLevelsH5"
    h6: "ThemesLibraryImportParamsThemeTypographyLevelsH6"
    body: "ThemesLibraryImportParamsThemeTypographyLevelsBody"
    small: "ThemesLibraryImportParamsThemeTypographyLevelsSmall"
    code: "ThemesLibraryImportParamsThemeTypographyLevelsCode"


class ThemesLibraryImportParamsThemeTypographyVariation(TypedDict, total=False):
    heading: str
    body: str
    code: str


class ThemesLibraryImportParamsThemeTypographyFeatures(TypedDict, total=False):
    heading: str
    body: str
    code: str


class ThemesLibraryImportParamsThemeTypography(TypedDict, total=False):
    scale: str
    baseSize: float
    fluid: "ThemesLibraryImportParamsThemeTypographyFluid"
    levels: "ThemesLibraryImportParamsThemeTypographyLevels"
    headingTransform: str
    variation: "ThemesLibraryImportParamsThemeTypographyVariation"
    features: "ThemesLibraryImportParamsThemeTypographyFeatures"
    opticalSizing: str
    headingWrap: str
    bodyWrap: str


class ThemesLibraryImportParamsThemeFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class ThemesLibraryImportParamsThemeFonts(TypedDict, total=False):
    faces: List["ThemesLibraryImportParamsThemeFontsFace"]


class ThemesLibraryImportParamsThemeElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class ThemesLibraryImportParamsThemeSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class ThemesLibraryImportParamsThemeCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class ThemesLibraryImportParamsThemeChromeCta(TypedDict, total=False):
    label: str
    href: str


class ThemesLibraryImportParamsThemeChromeSecondaryCta(TypedDict, total=False):
    label: str
    href: str
    style: str


class ThemesLibraryImportParamsThemeChromeHeader(TypedDict, total=False):
    overlay: bool
    overlayInk: str
    height: int
    border: str
    borderColor: str
    shadow: str
    blur: int
    opacity: float
    logoHeight: int
    navGap: int
    navWeight: int
    navSize: float
    navCase: str
    navTracking: float


class ThemesLibraryImportParamsThemeChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class ThemesLibraryImportParamsThemeChromeHeaderLinkPanelColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class ThemesLibraryImportParamsThemeChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class ThemesLibraryImportParamsThemeChromeHeaderLinkPanelFooterLink(TypedDict, total=False):
    label: str
    href: str


class ThemesLibraryImportParamsThemeChromeHeaderLinkPanelFooterCta(TypedDict, total=False):
    label: str
    href: str


class ThemesLibraryImportParamsThemeChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List["ThemesLibraryImportParamsThemeChromeHeaderLinkPanelFooterLink"]
    cta: "ThemesLibraryImportParamsThemeChromeHeaderLinkPanelFooterCta"


class ThemesLibraryImportParamsThemeChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List["ThemesLibraryImportParamsThemeChromeHeaderLinkPanelColumn"]
    featured: "ThemesLibraryImportParamsThemeChromeHeaderLinkPanelFeatured"
    footer: "ThemesLibraryImportParamsThemeChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class ThemesLibraryImportParamsThemeChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["ThemesLibraryImportParamsThemeChromeHeaderLinkChildrenItem"]
    panel: "ThemesLibraryImportParamsThemeChromeHeaderLinkPanel"
    style: str
    highlight: bool


class ThemesLibraryImportParamsThemeChromeNavMenu(TypedDict, total=False):
    trigger: str
    openDelay: int
    closeDelay: int
    animation: str
    radius: float
    shadow: str
    background: str
    ink: str
    border: str
    width: int


class ThemesLibraryImportParamsThemeChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class ThemesLibraryImportParamsThemeChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class ThemesLibraryImportParamsThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["ThemesLibraryImportParamsThemeChromeFooterColumnLink"]


class ThemesLibraryImportParamsThemeChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class ThemesLibraryImportParamsThemeChromeFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class ThemesLibraryImportParamsThemeChromeFooter(TypedDict, total=False):
    logo: Any
    logoMark: Any
    cookieLinkPlacement: str
    html: str
    css: str
    htmlPlacement: str
    newsletter: "ThemesLibraryImportParamsThemeChromeFooterNewsletter"


class ThemesLibraryImportParamsThemeChromeThemeToggle(TypedDict, total=False):
    show: bool
    style: str
    position: str
    radius: float
    activeColor: str


class ThemesLibraryImportParamsThemeChrome(TypedDict, total=False):
    cta: "ThemesLibraryImportParamsThemeChromeCta"
    secondaryCta: "ThemesLibraryImportParamsThemeChromeSecondaryCta"
    header: "ThemesLibraryImportParamsThemeChromeHeader"
    headerLinks: List["ThemesLibraryImportParamsThemeChromeHeaderLink"]
    navMenu: "ThemesLibraryImportParamsThemeChromeNavMenu"
    footerLinks: List["ThemesLibraryImportParamsThemeChromeFooterLink"]
    footerDescription: str
    footerColumns: List["ThemesLibraryImportParamsThemeChromeFooterColumn"]
    socialLinks: List["ThemesLibraryImportParamsThemeChromeSocialLink"]
    copyright: str
    footer: "ThemesLibraryImportParamsThemeChromeFooter"
    mobileNav: str
    sticky: bool
    height: str
    align: str
    ctaStyle: str
    showSignIn: bool
    themeToggle: "ThemesLibraryImportParamsThemeChromeThemeToggle"
    sidebarBrand: str


class ThemesLibraryImportParamsThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class ThemesLibraryImportParamsThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ThemesLibraryImportParamsThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class ThemesLibraryImportParamsThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class ThemesLibraryImportParamsThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class ThemesLibraryImportParamsThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class ThemesLibraryImportParamsThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class ThemesLibraryImportParamsThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ThemesLibraryImportParamsThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class ThemesLibraryImportParamsThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "ThemesLibraryImportParamsThemeComponentsFocus"
    code: "ThemesLibraryImportParamsThemeComponentsCode"
    input: "ThemesLibraryImportParamsThemeComponentsInput"
    button: "ThemesLibraryImportParamsThemeComponentsButton"
    spacing: "ThemesLibraryImportParamsThemeComponentsSpacing"
    selection: "ThemesLibraryImportParamsThemeComponentsSelection"
    scrollbar: "ThemesLibraryImportParamsThemeComponentsScrollbar"
    syntax: "ThemesLibraryImportParamsThemeComponentsSyntax"
    syntaxDark: "ThemesLibraryImportParamsThemeComponentsSyntaxDark"


class ThemesLibraryImportParamsThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class ThemesLibraryImportParamsThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class ThemesLibraryImportParamsThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class ThemesLibraryImportParamsThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class ThemesLibraryImportParamsThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class ThemesLibraryImportParamsThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["ThemesLibraryImportParamsThemeMotionKeyframeStep"]


class ThemesLibraryImportParamsThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "ThemesLibraryImportParamsThemeMotionReveal"
    hover: "ThemesLibraryImportParamsThemeMotionHover"
    header: "ThemesLibraryImportParamsThemeMotionHeader"
    ambient: "ThemesLibraryImportParamsThemeMotionAmbient"
    keyframes: List["ThemesLibraryImportParamsThemeMotionKeyframe"]
    targets: Dict[str, Any]


class ThemesLibraryImportParamsThemeMobile(TypedDict, total=False):
    fontScale: float
    density: str
    logoUrl: Any
    hide: List[str]
    css: str


class ThemesLibraryImportParamsTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "ThemesLibraryImportParamsThemePalette"
    paletteDark: "ThemesLibraryImportParamsThemePaletteDark"
    font: str
    colorScheme: str
    contentWidth: str
    onThisPage: str
    layout: "ThemesLibraryImportParamsThemeLayout"
    customFontUrl: Any
    customFontFamily: str
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    typography: "ThemesLibraryImportParamsThemeTypography"
    fonts: "ThemesLibraryImportParamsThemeFonts"
    customCss: str
    showLanguageSwitcher: bool
    elementStyles: List["ThemesLibraryImportParamsThemeElementStyle"]
    settingsSchema: List["ThemesLibraryImportParamsThemeSettingsSchemaItem"]
    settings: Dict[str, Any]
    stringOverrides: Dict[str, Any]
    cssSnippets: List["ThemesLibraryImportParamsThemeCssSnippet"]
    chrome: "ThemesLibraryImportParamsThemeChrome"
    components: "ThemesLibraryImportParamsThemeComponents"
    motion: "ThemesLibraryImportParamsThemeMotion"
    mobile: "ThemesLibraryImportParamsThemeMobile"


class ThemesLibraryImportParamsComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesLibraryImportParamsComponentMetaPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesLibraryImportParamsComponentMeta(TypedDict, total=False):
    name: str
    slug: str
    description: str
    author: "ThemesLibraryImportParamsComponentMetaAuthor"
    version: str
    license: str
    homepage: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesLibraryImportParamsComponentMetaPreviewImage"]


class ThemesLibraryImportParamsComponent(TypedDict, total=False):
    format: str
    formatVersion: float
    meta: "ThemesLibraryImportParamsComponentMeta"
    css: str
    outlets: Dict[str, Any]
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ThemesLibraryImportParams(TypedDict, total=False):
    format: str
    formatVersion: float
    meta: "ThemesLibraryImportParamsMeta"
    requiredOrigins: "ThemesLibraryImportParamsRequiredOrigins"
    theme: "ThemesLibraryImportParamsTheme"
    components: List["ThemesLibraryImportParamsComponent"]


class ThemesLibraryGetResponse(TypedDict, total=False):
    theme: "ThemeLibraryItem"


class ThemesLibraryPatchParamsAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesLibraryPatchParamsPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesLibraryPatchParams(TypedDict, total=False):
    slug: str
    author: "ThemesLibraryPatchParamsAuthor"
    version: str
    license: str
    homepage: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesLibraryPatchParamsPreviewImage"]
    name: str
    description: Optional[str]


class ThemesLibraryPatchResponse(TypedDict, total=False):
    theme: "ThemeLibraryItem"
    warnings: List[str]


class ThemesLibraryRemoveResponse(TypedDict, total=False):
    ok: bool


class ThemesMarketplaceDetailResponse(TypedDict, total=False):
    theme: "ThemeListingDetail"


class ThemesMarketplaceInstallParams(TypedDict, total=False):
    spaceId: str
    siteId: str


class ThemesMarketplacePurchaseResponse(TypedDict, total=False):
    checkoutUrl: str
    entitled: bool


class ThemesMarketplaceMineResponse(TypedDict, total=False):
    listings: List["OwnThemeListing"]
    page: "PageInfo"


class ThemesMarketplaceSubmitParams(TypedDict, total=False):
    componentId: str
    pricing: str
    priceCents: int
    currency: str


class ThemesMarketplaceSubmitResponse(TypedDict, total=False):
    listing: "OwnThemeListing"
    data: "OwnThemeListing"
    warnings: List[str]


class ThemesMarketplacePricingParams(TypedDict, total=False):
    pricing: str
    priceCents: int
    currency: str


class ThemesMarketplacePricingResponse(TypedDict, total=False):
    priceCents: float
    pricing: str
    warnings: List[str]


class ThemesMarketplaceWithdrawResponse(TypedDict, total=False):
    ok: bool


class ThemesMarketplaceBrowseRegistryResponse(TypedDict, total=False):
    themes: List["RegistryTheme"]
    page: "PageInfo"


class ThemesMarketplacePublishParams(TypedDict, total=False):
    componentId: str
    description: str


class ThemesMarketplacePublishResponse(TypedDict, total=False):
    theme: "RegistryTheme"
    data: "RegistryTheme"
    warnings: List[str]


class ThemesMarketplaceLegacyInstallResponseComponent(TypedDict, total=False):
    id: str
    name: str


class ThemesMarketplaceLegacyInstallResponse(TypedDict, total=False):
    component: "ThemesMarketplaceLegacyInstallResponseComponent"


class ThemesMarketplaceUnpublishResponse(TypedDict, total=False):
    ok: bool


class PublicThemeRegistryDetailResponse(TypedDict, total=False):
    theme: "ThemeListingDetail"


class PublicThemeRegistryBundleResponseComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class PublicThemeRegistryBundleResponseComponentMeta(TypedDict, total=False):
    author: "PublicThemeRegistryBundleResponseComponentMetaAuthor"
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List[Dict[str, Any]]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


PublicThemeRegistryBundleResponseComponentOutlets = TypedDict("PublicThemeRegistryBundleResponseComponentOutlets", {"above-main": Any, "below-main": Any, "blog-index-above-list": Any, "blog-post-after": Any, "blog-post-before": Any, "careers-above-list": Any, "category-header": Any, "changelog-above-list": Any, "courses-above-list": Any, "docs-page-footer": Any, "docs-page-header": Any, "events-above-list": Any, "faq-above-list": Any, "footer-after": Any, "footer-before": Any, "forum-index-above-list": Any, "forum-index-below-list": Any, "forum-post-after-body": Any, "forum-sidebar-bottom": Any, "forum-sidebar-top": Any, "forum-topic-above-title": Any, "forum-topic-below-first-post": Any, "forum-topic-below-title": Any, "forum-topic-bottom": Any, "header-after": Any, "header-before": Any, "roadmap-above-board": Any, "status-above-board": Any, "user-card": Any}, total=False)


class PublicThemeRegistryBundleResponseComponent(TypedDict, total=False):
    css: str
    format: str
    formatVersion: float
    meta: "PublicThemeRegistryBundleResponseComponentMeta"
    outlets: "PublicThemeRegistryBundleResponseComponentOutlets"
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class PublicThemeRegistryBundleResponseMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class PublicThemeRegistryBundleResponseMetaPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class PublicThemeRegistryBundleResponseMeta(TypedDict, total=False):
    author: "PublicThemeRegistryBundleResponseMetaAuthor"
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List["PublicThemeRegistryBundleResponseMetaPreviewImage"]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


class PublicThemeRegistryBundleResponseRequiredOrigins(TypedDict, total=False):
    fonts: List[str]
    images: List[str]


class PublicThemeRegistryBundleResponseThemeChromeCta(TypedDict, total=False):
    href: str
    label: str


class PublicThemeRegistryBundleResponseThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List[Dict[str, Any]]


class PublicThemeRegistryBundleResponseThemeChromeFooterLink(TypedDict, total=False):
    href: str
    label: str


class PublicThemeRegistryBundleResponseThemeChromeHeaderLink(TypedDict, total=False):
    children: List[Dict[str, Any]]
    highlight: bool
    href: str
    label: str
    panel: Dict[str, Any]
    style: str


class PublicThemeRegistryBundleResponseThemeChromeNavMenu(TypedDict, total=False):
    animation: str
    background: str
    border: str
    closeDelay: float
    ink: str
    openDelay: float
    radius: float
    shadow: str
    trigger: str
    width: float


class PublicThemeRegistryBundleResponseThemeChromeSocialLink(TypedDict, total=False):
    href: str
    platform: str


class PublicThemeRegistryBundleResponseThemeChromeThemeToggle(TypedDict, total=False):
    activeColor: str
    position: str
    radius: float
    show: bool
    style: str


class PublicThemeRegistryBundleResponseThemeChrome(TypedDict, total=False):
    align: str
    copyright: str
    cta: "PublicThemeRegistryBundleResponseThemeChromeCta"
    ctaStyle: str
    footer: "ChromeFooter"
    footerColumns: List["PublicThemeRegistryBundleResponseThemeChromeFooterColumn"]
    footerDescription: str
    footerLinks: List["PublicThemeRegistryBundleResponseThemeChromeFooterLink"]
    header: "ChromeHeader"
    headerLinks: List["PublicThemeRegistryBundleResponseThemeChromeHeaderLink"]
    height: str
    mobileNav: str
    navMenu: "PublicThemeRegistryBundleResponseThemeChromeNavMenu"
    secondaryCta: "ChromeSecondaryCta"
    showSignIn: bool
    sidebarBrand: str
    socialLinks: List["PublicThemeRegistryBundleResponseThemeChromeSocialLink"]
    sticky: bool
    themeToggle: "PublicThemeRegistryBundleResponseThemeChromeThemeToggle"


class PublicThemeRegistryBundleResponseThemeComponentsButton(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float
    shadow: str
    weight: str


class PublicThemeRegistryBundleResponseThemeComponentsCode(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class PublicThemeRegistryBundleResponseThemeComponentsFocus(TypedDict, total=False):
    color: str
    offset: float
    width: float


class PublicThemeRegistryBundleResponseThemeComponentsInput(TypedDict, total=False):
    background: str
    border: str
    ink: str
    radius: float


class PublicThemeRegistryBundleResponseThemeComponentsScrollbar(TypedDict, total=False):
    thumb: str
    track: str
    width: str


class PublicThemeRegistryBundleResponseThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class PublicThemeRegistryBundleResponseThemeComponentsSpacing(TypedDict, total=False):
    block: float
    pad: float
    scale: float
    section: float


class PublicThemeRegistryBundleResponseThemeComponentsSyntax(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class PublicThemeRegistryBundleResponseThemeComponentsSyntaxDark(TypedDict, total=False):
    attr: str
    built_in: str
    comment: str
    emphasis: str
    keyword: str
    meta: str
    number: str
    string: str
    tag: str
    title: str


class PublicThemeRegistryBundleResponseThemeComponents(TypedDict, total=False):
    button: "PublicThemeRegistryBundleResponseThemeComponentsButton"
    code: "PublicThemeRegistryBundleResponseThemeComponentsCode"
    focus: "PublicThemeRegistryBundleResponseThemeComponentsFocus"
    input: "PublicThemeRegistryBundleResponseThemeComponentsInput"
    radius: float
    scrollbar: "PublicThemeRegistryBundleResponseThemeComponentsScrollbar"
    selection: "PublicThemeRegistryBundleResponseThemeComponentsSelection"
    shadow: str
    spacing: "PublicThemeRegistryBundleResponseThemeComponentsSpacing"
    syntax: "PublicThemeRegistryBundleResponseThemeComponentsSyntax"
    syntaxDark: "PublicThemeRegistryBundleResponseThemeComponentsSyntaxDark"


class PublicThemeRegistryBundleResponseThemeCssSnippet(TypedDict, total=False):
    css: str
    enabled: bool
    name: str


class PublicThemeRegistryBundleResponseThemeLayout(TypedDict, total=False):
    measure: str


class PublicThemeRegistryBundleResponseThemeMobile(TypedDict, total=False):
    css: str
    density: str
    fontScale: float
    hide: List[str]
    logoUrl: str


class PublicThemeRegistryBundleResponseThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    focusRing: bool
    scrollProgress: bool
    smoothScroll: bool


class PublicThemeRegistryBundleResponseThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class PublicThemeRegistryBundleResponseThemeMotionHover(TypedDict, total=False):
    button: str
    card: str
    image: str
    link: str


class PublicThemeRegistryBundleResponseThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List[Dict[str, Any]]


class PublicThemeRegistryBundleResponseThemeMotionReveal(TypedDict, total=False):
    distance: float
    effect: str
    once: bool
    stagger: float
    targets: List[str]


PublicThemeRegistryBundleResponseThemeMotionTargets = TypedDict("PublicThemeRegistryBundleResponseThemeMotionTargets", {"article": Any, "aside": Any, "brand-name": Any, "button": Any, "card": Any, "carousel": Any, "carousel-slide": Any, "compare": Any, "component": Any, "cookie-settings": Any, "cta": Any, "cta-secondary": Any, "footer": Any, "footer-col": Any, "footer-html": Any, "footer-newsletter": Any, "gallery": Any, "header": Any, "input": Any, "lightbox": Any, "logo": Any, "logo-wall": Any, "main": Any, "marquee": Any, "modal": Any, "nav": Any, "nav-featured": Any, "nav-item": Any, "nav-link": Any, "nav-panel": Any, "outlet": Any, "page-title": Any, "pricing": Any, "pricing-plan": Any, "search": Any, "sidebar": Any, "sidebar-logo": Any, "stat": Any, "stats": Any, "testimonial": Any, "testimonials": Any, "theme-toggle": Any}, total=False)


class PublicThemeRegistryBundleResponseThemeMotion(TypedDict, total=False):
    ambient: "PublicThemeRegistryBundleResponseThemeMotionAmbient"
    easing: str
    enabled: bool
    header: "PublicThemeRegistryBundleResponseThemeMotionHeader"
    hover: "PublicThemeRegistryBundleResponseThemeMotionHover"
    keyframes: List["PublicThemeRegistryBundleResponseThemeMotionKeyframe"]
    pageTransition: str
    preset: str
    respectReducedMotion: bool
    reveal: "PublicThemeRegistryBundleResponseThemeMotionReveal"
    speed: float
    targets: "PublicThemeRegistryBundleResponseThemeMotionTargets"


class PublicThemeRegistryBundleResponseThemePalette(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class PublicThemeRegistryBundleResponseThemePaletteDark(TypedDict, total=False):
    background: str
    danger: str
    header_background: str
    header_primary: str
    highlight: str
    love: str
    primary: str
    quaternary: str
    secondary: str
    success: str
    surface: str
    tertiary: str


class PublicThemeRegistryBundleResponseThemeSettingsSchemaItem(TypedDict, total=False):
    default: Any
    key: str
    label: str
    options: List[str]
    type: str


class PublicThemeRegistryBundleResponseTheme(TypedDict, total=False):
    accentColor: str
    bodyFontFamily: str
    chrome: "PublicThemeRegistryBundleResponseThemeChrome"
    colorScheme: str
    components: "PublicThemeRegistryBundleResponseThemeComponents"
    contentWidth: str
    cssSnippets: List["PublicThemeRegistryBundleResponseThemeCssSnippet"]
    customCss: str
    customFontFamily: str
    customFontUrl: str
    elementStyles: List["ElementStyleRule"]
    font: str
    fonts: "ThemeFonts"
    headingFontFamily: str
    layout: "PublicThemeRegistryBundleResponseThemeLayout"
    mobile: "PublicThemeRegistryBundleResponseThemeMobile"
    monoFontFamily: str
    motion: "PublicThemeRegistryBundleResponseThemeMotion"
    onThisPage: str
    palette: "PublicThemeRegistryBundleResponseThemePalette"
    paletteDark: "PublicThemeRegistryBundleResponseThemePaletteDark"
    primaryColor: str
    settings: Dict[str, Any]
    settingsSchema: List["PublicThemeRegistryBundleResponseThemeSettingsSchemaItem"]
    showLanguageSwitcher: bool
    stringOverrides: Dict[str, Any]
    typography: "SpaceTypography"


class PublicThemeRegistryBundleResponse(TypedDict, total=False):
    components: List["PublicThemeRegistryBundleResponseComponent"]
    format: str
    formatVersion: Any
    meta: "PublicThemeRegistryBundleResponseMeta"
    requiredOrigins: "PublicThemeRegistryBundleResponseRequiredOrigins"
    theme: "PublicThemeRegistryBundleResponseTheme"


class ThemesComponentsListResponse(TypedDict, total=False):
    components: List["ComponentInstallItem"]
    page: "PageInfo"


class ThemesComponentsCreateParamsComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesComponentsCreateParamsComponentMetaPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesComponentsCreateParamsComponentMeta(TypedDict, total=False):
    name: str
    slug: str
    description: str
    author: "ThemesComponentsCreateParamsComponentMetaAuthor"
    version: str
    license: str
    homepage: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesComponentsCreateParamsComponentMetaPreviewImage"]


class ThemesComponentsCreateParamsComponent(TypedDict, total=False):
    format: str
    formatVersion: float
    meta: "ThemesComponentsCreateParamsComponentMeta"
    css: str
    outlets: Dict[str, Any]
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ThemesComponentsCreateParams(TypedDict, total=False):
    component: "ThemesComponentsCreateParamsComponent"
    settings: Dict[str, Any]
    enabled: bool


class ThemesComponentsGetResponse(TypedDict, total=False):
    install: "ComponentInstallItem"


class ThemesComponentsUpdateParamsComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesComponentsUpdateParamsComponentMetaPreviewImage(TypedDict, total=False):
    url: str
    alt: str
    scheme: str


class ThemesComponentsUpdateParamsComponentMeta(TypedDict, total=False):
    name: str
    slug: str
    description: str
    author: "ThemesComponentsUpdateParamsComponentMetaAuthor"
    version: str
    license: str
    homepage: str
    tags: List[str]
    spaceTypes: List[str]
    previewImages: List["ThemesComponentsUpdateParamsComponentMetaPreviewImage"]


class ThemesComponentsUpdateParamsComponent(TypedDict, total=False):
    format: str
    formatVersion: float
    meta: "ThemesComponentsUpdateParamsComponentMeta"
    css: str
    outlets: Dict[str, Any]
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ThemesComponentsUpdateParams(TypedDict, total=False):
    component: "ThemesComponentsUpdateParamsComponent"
    settings: Dict[str, Any]
    enabled: bool


class ThemesComponentsUpdateResponse(TypedDict, total=False):
    install: "ComponentInstallItem"
    warnings: List[str]


class ThemesComponentsComponentinstallsResponse(TypedDict, total=False):
    ok: bool


class ThemesComponentsPackageResponseComponentMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class ThemesComponentsPackageResponseComponentMetaPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class ThemesComponentsPackageResponseComponentMeta(TypedDict, total=False):
    author: "ThemesComponentsPackageResponseComponentMetaAuthor"
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List["ThemesComponentsPackageResponseComponentMetaPreviewImage"]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


ThemesComponentsPackageResponseComponentOutlets = TypedDict("ThemesComponentsPackageResponseComponentOutlets", {"above-main": Any, "below-main": Any, "blog-index-above-list": Any, "blog-post-after": Any, "blog-post-before": Any, "careers-above-list": Any, "category-header": Any, "changelog-above-list": Any, "courses-above-list": Any, "docs-page-footer": Any, "docs-page-header": Any, "events-above-list": Any, "faq-above-list": Any, "footer-after": Any, "footer-before": Any, "forum-index-above-list": Any, "forum-index-below-list": Any, "forum-post-after-body": Any, "forum-sidebar-bottom": Any, "forum-sidebar-top": Any, "forum-topic-above-title": Any, "forum-topic-below-first-post": Any, "forum-topic-below-title": Any, "forum-topic-bottom": Any, "header-after": Any, "header-before": Any, "roadmap-above-board": Any, "status-above-board": Any, "user-card": Any}, total=False)


class ThemesComponentsPackageResponseComponent(TypedDict, total=False):
    css: str
    format: str
    formatVersion: float
    meta: "ThemesComponentsPackageResponseComponentMeta"
    outlets: "ThemesComponentsPackageResponseComponentOutlets"
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ThemesComponentsPackageResponse(TypedDict, total=False):
    component: "ThemesComponentsPackageResponseComponent"
    strippedScripts: List["ComponentScriptNotice"]


class ThemesComponentsSetSpaceComponentsParamsComponent(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ThemesComponentsSetSpaceComponentsParams(TypedDict, total=False):
    components: List["ThemesComponentsSetSpaceComponentsParamsComponent"]


class ThemesComponentsSetSiteComponentsParamsComponent(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class ThemesComponentsSetSiteComponentsParams(TypedDict, total=False):
    components: List["ThemesComponentsSetSiteComponentsParamsComponent"]


class ThemesComponentMarketplaceBrowseResponseFacetsOutlet(TypedDict, total=False):
    count: float
    outlet: str


class ThemesComponentMarketplaceBrowseResponseFacetsTag(TypedDict, total=False):
    count: float
    tag: str


class ThemesComponentMarketplaceBrowseResponseFacets(TypedDict, total=False):
    outlets: List["ThemesComponentMarketplaceBrowseResponseFacetsOutlet"]
    tags: List["ThemesComponentMarketplaceBrowseResponseFacetsTag"]


class ThemesComponentMarketplaceBrowseResponse(TypedDict, total=False):
    components: List["OrgComponentListing"]
    facets: "ThemesComponentMarketplaceBrowseResponseFacets"


class ThemesComponentMarketplaceDetailResponse(TypedDict, total=False):
    component: "ComponentListingDetail"


class ThemesComponentMarketplaceInstallParams(TypedDict, total=False):
    spaceId: str
    siteId: str


class ThemesComponentMarketplaceMineResponse(TypedDict, total=False):
    listings: List["OwnComponentListing"]
    page: "PageInfo"


class ThemesComponentMarketplaceSubmitParams(TypedDict, total=False):
    installId: str


class ThemesComponentMarketplaceSubmitResponse(TypedDict, total=False):
    listing: "OwnComponentListing"
    data: "OwnComponentListing"
    warnings: List[str]


class ThemesComponentMarketplaceWithdrawResponse(TypedDict, total=False):
    ok: bool


class PublicThemeComponentRegistryBrowseResponseFacetsOutlet(TypedDict, total=False):
    count: float
    outlet: str


class PublicThemeComponentRegistryBrowseResponseFacetsTag(TypedDict, total=False):
    count: float
    tag: str


class PublicThemeComponentRegistryBrowseResponseFacets(TypedDict, total=False):
    outlets: List["PublicThemeComponentRegistryBrowseResponseFacetsOutlet"]
    tags: List["PublicThemeComponentRegistryBrowseResponseFacetsTag"]


class PublicThemeComponentRegistryBrowseResponse(TypedDict, total=False):
    components: List["ComponentListing"]
    facets: "PublicThemeComponentRegistryBrowseResponseFacets"


class PublicThemeComponentRegistryDetailResponse(TypedDict, total=False):
    component: "ComponentListingDetail"


class PublicThemeComponentRegistryPackageResponseMetaAuthor(TypedDict, total=False):
    name: str
    url: str


class PublicThemeComponentRegistryPackageResponseMetaPreviewImage(TypedDict, total=False):
    alt: str
    scheme: str
    url: str


class PublicThemeComponentRegistryPackageResponseMeta(TypedDict, total=False):
    author: "PublicThemeComponentRegistryPackageResponseMetaAuthor"
    description: str
    homepage: str
    license: str
    name: str
    previewImages: List["PublicThemeComponentRegistryPackageResponseMetaPreviewImage"]
    slug: str
    spaceTypes: List[str]
    tags: List[str]
    version: str


PublicThemeComponentRegistryPackageResponseOutlets = TypedDict("PublicThemeComponentRegistryPackageResponseOutlets", {"above-main": Any, "below-main": Any, "blog-index-above-list": Any, "blog-post-after": Any, "blog-post-before": Any, "careers-above-list": Any, "category-header": Any, "changelog-above-list": Any, "courses-above-list": Any, "docs-page-footer": Any, "docs-page-header": Any, "events-above-list": Any, "faq-above-list": Any, "footer-after": Any, "footer-before": Any, "forum-index-above-list": Any, "forum-index-below-list": Any, "forum-post-after-body": Any, "forum-sidebar-bottom": Any, "forum-sidebar-top": Any, "forum-topic-above-title": Any, "forum-topic-below-first-post": Any, "forum-topic-below-title": Any, "forum-topic-bottom": Any, "header-after": Any, "header-before": Any, "roadmap-above-board": Any, "status-above-board": Any, "user-card": Any}, total=False)


class PublicThemeComponentRegistryPackageResponse(TypedDict, total=False):
    css: str
    format: str
    formatVersion: float
    meta: "PublicThemeComponentRegistryPackageResponseMeta"
    outlets: "PublicThemeComponentRegistryPackageResponseOutlets"
    settings: Dict[str, Any]
    strings: Dict[str, Any]


class ThemesOutletsResponse(TypedDict, total=False):
    outlets: List["OutletSpec"]
    positions: List[str]
    settingTypes: List[str]


class OnboardingSurfacesResponseSurface(TypedDict, total=False):
    name: str
    slug: str
    type: str


class OnboardingSurfacesResponse(TypedDict, total=False):
    surfaces: List["OnboardingSurfacesResponseSurface"]
    page: "PageInfo"


class OnboardingProvisionParams(TypedDict, total=False):
    orgName: str
    slug: str
    subdomain: str
    surfaces: List[str]
    legal: bool


class ConsentRotateWebhookSecretResponse(TypedDict, total=False):
    secret: str
    webhookUrl: str


class ConsentExecutorKeyStatusResponse(TypedDict, total=False):
    enabled: bool
    executorUrl: str


class ConsentRotateExecutorKeyResponse(TypedDict, total=False):
    executorUrl: str
    secret: str


class ConsentSendTestEventResponse(TypedDict, total=False):
    delivered: bool
    event: str
    webhookUrl: str


class PublicConsentRecordParams(TypedDict, total=False):
    subjectId: str
    categories: Dict[str, Any]
    adapterId: str
    policyVersion: str
    receipt: str


class PublicConsentRecordResponse(TypedDict, total=False):
    ok: bool
    warnings: List[str]


class BillingCheckoutParams(TypedDict, total=False):
    plan: str


class BillingCheckoutResponse(TypedDict, total=False):
    url: str
    warnings: List[str]


class BillingPortalResponse(TypedDict, total=False):
    url: str


class IntegrationsSlackStatusResponse(TypedDict, total=False):
    connected: bool
    oauthConfigured: bool
    teamId: Any
    teamName: Any


class IntegrationsSlackConnectParams(TypedDict, total=False):
    teamId: str
    teamName: str
    botToken: str
    botUserId: str


class IntegrationsSlackDisconnectResponse(TypedDict, total=False):
    ok: bool


class IntegrationsSlackInstallUrlResponse(TypedDict, total=False):
    url: Any


class PublicMcpInfoResponse(TypedDict, total=False):
    server: str
    transport: str


class McpInfoResponse(TypedDict, total=False):
    server: str
    transport: str


class OrgsApplyParamsSpaceShape(TypedDict, total=False):
    index: str
    order: str
    nav: str
    whoCreates: str


class OrgsApplyParamsSpaceThemePalette(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class OrgsApplyParamsSpaceThemePaletteDark(TypedDict, total=False):
    primary: str
    secondary: str
    tertiary: str
    quaternary: str
    header_background: str
    header_primary: str
    highlight: str
    danger: str
    success: str
    love: str
    background: str
    surface: str


class OrgsApplyParamsSpaceThemeLayout(TypedDict, total=False):
    measure: str


class OrgsApplyParamsSpaceThemeTypographyFluid(TypedDict, total=False):
    enabled: bool
    minViewport: int
    maxViewport: int
    minScale: float
    bodyMinScale: float


class OrgsApplyParamsSpaceThemeTypographyLevelsH1(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class OrgsApplyParamsSpaceThemeTypographyLevelsH2(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class OrgsApplyParamsSpaceThemeTypographyLevelsH3(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class OrgsApplyParamsSpaceThemeTypographyLevelsH4(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class OrgsApplyParamsSpaceThemeTypographyLevelsH5(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class OrgsApplyParamsSpaceThemeTypographyLevelsH6(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class OrgsApplyParamsSpaceThemeTypographyLevelsBody(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class OrgsApplyParamsSpaceThemeTypographyLevelsSmall(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class OrgsApplyParamsSpaceThemeTypographyLevelsCode(TypedDict, total=False):
    size: float
    lineHeight: float
    tracking: float
    weight: int


class OrgsApplyParamsSpaceThemeTypographyLevels(TypedDict, total=False):
    h1: "OrgsApplyParamsSpaceThemeTypographyLevelsH1"
    h2: "OrgsApplyParamsSpaceThemeTypographyLevelsH2"
    h3: "OrgsApplyParamsSpaceThemeTypographyLevelsH3"
    h4: "OrgsApplyParamsSpaceThemeTypographyLevelsH4"
    h5: "OrgsApplyParamsSpaceThemeTypographyLevelsH5"
    h6: "OrgsApplyParamsSpaceThemeTypographyLevelsH6"
    body: "OrgsApplyParamsSpaceThemeTypographyLevelsBody"
    small: "OrgsApplyParamsSpaceThemeTypographyLevelsSmall"
    code: "OrgsApplyParamsSpaceThemeTypographyLevelsCode"


class OrgsApplyParamsSpaceThemeTypographyVariation(TypedDict, total=False):
    heading: str
    body: str
    code: str


class OrgsApplyParamsSpaceThemeTypographyFeatures(TypedDict, total=False):
    heading: str
    body: str
    code: str


class OrgsApplyParamsSpaceThemeTypography(TypedDict, total=False):
    scale: str
    baseSize: float
    fluid: "OrgsApplyParamsSpaceThemeTypographyFluid"
    levels: "OrgsApplyParamsSpaceThemeTypographyLevels"
    headingTransform: str
    variation: "OrgsApplyParamsSpaceThemeTypographyVariation"
    features: "OrgsApplyParamsSpaceThemeTypographyFeatures"
    opticalSizing: str
    headingWrap: str
    bodyWrap: str


class OrgsApplyParamsSpaceThemeFontsFace(TypedDict, total=False):
    family: str
    src: str
    format: str
    weight: str
    style: str
    display: str
    unicodeRange: str


class OrgsApplyParamsSpaceThemeFonts(TypedDict, total=False):
    faces: List["OrgsApplyParamsSpaceThemeFontsFace"]


class OrgsApplyParamsSpaceThemeAds(TypedDict, total=False):
    network: str
    publisherId: str
    slotId: str
    size: str
    enabled: bool
    scriptUrl: str
    slotHtml: str
    configVar: str
    configJson: Dict[str, Any]


class OrgsApplyParamsSpaceThemeElementStyle(TypedDict, total=False):
    selector: str
    declarations: Dict[str, Any]
    media: str
    state: str
    scheme: str
    page: str


class OrgsApplyParamsSpaceThemeSettingsSchemaItem(TypedDict, total=False):
    key: str
    type: str
    label: str
    default: Any
    options: List[str]


class OrgsApplyParamsSpaceThemeCssSnippet(TypedDict, total=False):
    name: str
    css: str
    enabled: bool


class OrgsApplyParamsSpaceThemeAnnouncement(TypedDict, total=False):
    text: str
    level: str
    href: Any


class OrgsApplyParamsSpaceThemeChromeCta(TypedDict, total=False):
    label: str
    href: str


class OrgsApplyParamsSpaceThemeChromeSecondaryCta(TypedDict, total=False):
    label: str
    href: str
    style: str


class OrgsApplyParamsSpaceThemeChromeHeader(TypedDict, total=False):
    overlay: bool
    overlayInk: str
    height: int
    border: str
    borderColor: str
    shadow: str
    blur: int
    opacity: float
    logoHeight: int
    navGap: int
    navWeight: int
    navSize: float
    navCase: str
    navTracking: float


class OrgsApplyParamsSpaceThemeChromeHeaderLinkChildrenItem(TypedDict, total=False):
    label: str
    href: str
    description: str
    icon: str
    badge: str


class OrgsApplyParamsSpaceThemeChromeHeaderLinkPanelFeatured(TypedDict, total=False):
    image: str
    title: str
    text: str
    href: str


class OrgsApplyParamsSpaceThemeChromeHeaderLinkPanelFooter(TypedDict, total=False):
    links: List[Dict[str, Any]]
    cta: Dict[str, Any]


class OrgsApplyParamsSpaceThemeChromeHeaderLinkPanel(TypedDict, total=False):
    columns: List[Dict[str, Any]]
    featured: "OrgsApplyParamsSpaceThemeChromeHeaderLinkPanelFeatured"
    footer: "OrgsApplyParamsSpaceThemeChromeHeaderLinkPanelFooter"
    html: str
    css: str
    width: str
    align: str


class OrgsApplyParamsSpaceThemeChromeHeaderLink(TypedDict, total=False):
    label: str
    href: str
    children: List["OrgsApplyParamsSpaceThemeChromeHeaderLinkChildrenItem"]
    panel: "OrgsApplyParamsSpaceThemeChromeHeaderLinkPanel"
    style: str
    highlight: bool


class OrgsApplyParamsSpaceThemeChromeNavMenu(TypedDict, total=False):
    trigger: str
    openDelay: int
    closeDelay: int
    animation: str
    radius: float
    shadow: str
    background: str
    ink: str
    border: str
    width: int


class OrgsApplyParamsSpaceThemeChromeFooterLink(TypedDict, total=False):
    label: str
    href: str


class OrgsApplyParamsSpaceThemeChromeFooterColumnLink(TypedDict, total=False):
    label: str
    href: str


class OrgsApplyParamsSpaceThemeChromeFooterColumn(TypedDict, total=False):
    heading: str
    links: List["OrgsApplyParamsSpaceThemeChromeFooterColumnLink"]


class OrgsApplyParamsSpaceThemeChromeSocialLink(TypedDict, total=False):
    platform: str
    href: str


class OrgsApplyParamsSpaceThemeChromeFooterNewsletter(TypedDict, total=False):
    formId: str
    heading: str


class OrgsApplyParamsSpaceThemeChromeFooter(TypedDict, total=False):
    logo: Any
    logoMark: Any
    cookieLinkPlacement: str
    html: str
    css: str
    htmlPlacement: str
    newsletter: "OrgsApplyParamsSpaceThemeChromeFooterNewsletter"


class OrgsApplyParamsSpaceThemeChromeThemeToggle(TypedDict, total=False):
    show: bool
    style: str
    position: str
    radius: float
    activeColor: str


class OrgsApplyParamsSpaceThemeChrome(TypedDict, total=False):
    cta: "OrgsApplyParamsSpaceThemeChromeCta"
    secondaryCta: "OrgsApplyParamsSpaceThemeChromeSecondaryCta"
    header: "OrgsApplyParamsSpaceThemeChromeHeader"
    headerLinks: List["OrgsApplyParamsSpaceThemeChromeHeaderLink"]
    navMenu: "OrgsApplyParamsSpaceThemeChromeNavMenu"
    footerLinks: List["OrgsApplyParamsSpaceThemeChromeFooterLink"]
    footerDescription: str
    footerColumns: List["OrgsApplyParamsSpaceThemeChromeFooterColumn"]
    socialLinks: List["OrgsApplyParamsSpaceThemeChromeSocialLink"]
    copyright: str
    footer: "OrgsApplyParamsSpaceThemeChromeFooter"
    mobileNav: str
    sticky: bool
    height: str
    align: str
    ctaStyle: str
    showSignIn: bool
    themeToggle: "OrgsApplyParamsSpaceThemeChromeThemeToggle"
    sidebarBrand: str


class OrgsApplyParamsSpaceThemeNotFoundLink(TypedDict, total=False):
    label: str
    href: str


class OrgsApplyParamsSpaceThemeNotFound(TypedDict, total=False):
    title: str
    body: str
    pageId: str
    pageSpaceId: str
    hidePage: bool
    links: List["OrgsApplyParamsSpaceThemeNotFoundLink"]
    showSearch: bool
    showSections: bool
    hideSearch: bool


class OrgsApplyParamsSpaceThemeComponentsFocus(TypedDict, total=False):
    color: str
    width: float
    offset: float


class OrgsApplyParamsSpaceThemeComponentsCode(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class OrgsApplyParamsSpaceThemeComponentsInput(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float


class OrgsApplyParamsSpaceThemeComponentsButton(TypedDict, total=False):
    background: str
    ink: str
    border: str
    radius: float
    shadow: str
    weight: str


class OrgsApplyParamsSpaceThemeComponentsSpacing(TypedDict, total=False):
    scale: float
    block: float
    section: float
    pad: float


class OrgsApplyParamsSpaceThemeComponentsSelection(TypedDict, total=False):
    background: str
    ink: str


class OrgsApplyParamsSpaceThemeComponentsScrollbar(TypedDict, total=False):
    width: str
    thumb: str
    track: str


class OrgsApplyParamsSpaceThemeComponentsSyntax(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class OrgsApplyParamsSpaceThemeComponentsSyntaxDark(TypedDict, total=False):
    comment: str
    keyword: str
    string: str
    number: str
    title: str
    built_in: str
    tag: str
    attr: str
    meta: str
    emphasis: str


class OrgsApplyParamsSpaceThemeComponents(TypedDict, total=False):
    radius: float
    shadow: str
    focus: "OrgsApplyParamsSpaceThemeComponentsFocus"
    code: "OrgsApplyParamsSpaceThemeComponentsCode"
    input: "OrgsApplyParamsSpaceThemeComponentsInput"
    button: "OrgsApplyParamsSpaceThemeComponentsButton"
    spacing: "OrgsApplyParamsSpaceThemeComponentsSpacing"
    selection: "OrgsApplyParamsSpaceThemeComponentsSelection"
    scrollbar: "OrgsApplyParamsSpaceThemeComponentsScrollbar"
    syntax: "OrgsApplyParamsSpaceThemeComponentsSyntax"
    syntaxDark: "OrgsApplyParamsSpaceThemeComponentsSyntaxDark"


class OrgsApplyParamsSpaceThemeMotionReveal(TypedDict, total=False):
    effect: str
    stagger: int
    distance: int
    once: bool
    targets: List[str]


class OrgsApplyParamsSpaceThemeMotionHover(TypedDict, total=False):
    link: str
    button: str
    card: str
    image: str


class OrgsApplyParamsSpaceThemeMotionHeader(TypedDict, total=False):
    behavior: str
    blur: bool


class OrgsApplyParamsSpaceThemeMotionAmbient(TypedDict, total=False):
    background: str
    cursorGlow: bool
    scrollProgress: bool
    smoothScroll: bool
    focusRing: bool


class OrgsApplyParamsSpaceThemeMotionKeyframeStep(TypedDict, total=False):
    at: int
    opacity: float
    transform: str
    filter: str
    color: str
    backgroundColor: str
    clipPath: str


class OrgsApplyParamsSpaceThemeMotionKeyframe(TypedDict, total=False):
    name: str
    steps: List["OrgsApplyParamsSpaceThemeMotionKeyframeStep"]


class OrgsApplyParamsSpaceThemeMotion(TypedDict, total=False):
    preset: str
    enabled: bool
    respectReducedMotion: bool
    speed: float
    easing: str
    pageTransition: str
    reveal: "OrgsApplyParamsSpaceThemeMotionReveal"
    hover: "OrgsApplyParamsSpaceThemeMotionHover"
    header: "OrgsApplyParamsSpaceThemeMotionHeader"
    ambient: "OrgsApplyParamsSpaceThemeMotionAmbient"
    keyframes: List["OrgsApplyParamsSpaceThemeMotionKeyframe"]
    targets: Dict[str, Any]


class OrgsApplyParamsSpaceThemeComponentInstall(TypedDict, total=False):
    id: str
    settings: Dict[str, Any]


class OrgsApplyParamsSpaceThemeMobile(TypedDict, total=False):
    fontScale: float
    density: str
    logoUrl: Any
    hide: List[str]
    css: str


class OrgsApplyParamsSpaceTheme(TypedDict, total=False):
    primaryColor: str
    accentColor: str
    palette: "OrgsApplyParamsSpaceThemePalette"
    paletteDark: "OrgsApplyParamsSpaceThemePaletteDark"
    font: str
    colorScheme: str
    contentWidth: str
    onThisPage: str
    layout: "OrgsApplyParamsSpaceThemeLayout"
    customFontUrl: Any
    customFontFamily: str
    brandName: Any
    headingFontFamily: str
    bodyFontFamily: str
    monoFontFamily: str
    typography: "OrgsApplyParamsSpaceThemeTypography"
    fonts: "OrgsApplyParamsSpaceThemeFonts"
    logoUrl: Any
    logoMark: Any
    faviconUrl: Any
    customCss: str
    customJs: str
    scriptOrigins: List[str]
    ads: "OrgsApplyParamsSpaceThemeAds"
    whiteLabel: bool
    showLanguageSwitcher: bool
    apiOrigins: List[str]
    fontOrigins: List[str]
    fontOriginsRemoved: List[str]
    imgOrigins: List[str]
    mediaOrigins: List[str]
    frameOrigins: List[str]
    elementStyles: List["OrgsApplyParamsSpaceThemeElementStyle"]
    settingsSchema: List["OrgsApplyParamsSpaceThemeSettingsSchemaItem"]
    settings: Dict[str, Any]
    stringOverrides: Dict[str, Any]
    cssSnippets: List["OrgsApplyParamsSpaceThemeCssSnippet"]
    announcement: "OrgsApplyParamsSpaceThemeAnnouncement"
    chrome: "OrgsApplyParamsSpaceThemeChrome"
    notFound: "OrgsApplyParamsSpaceThemeNotFound"
    components: "OrgsApplyParamsSpaceThemeComponents"
    motion: "OrgsApplyParamsSpaceThemeMotion"
    componentInstalls: List["OrgsApplyParamsSpaceThemeComponentInstall"]
    mobile: "OrgsApplyParamsSpaceThemeMobile"


class OrgsApplyParamsSpaceRedirectMatch(TypedDict, total=False):
    query: Any


OrgsApplyParamsSpaceRedirect = TypedDict("OrgsApplyParamsSpaceRedirect", {"from": str, "to": Any, "type": str, "status": float, "match": "OrgsApplyParamsSpaceRedirectMatch", "passQuery": bool}, total=False)


class OrgsApplyParamsSpaceCollection(TypedDict, total=False):
    name: str
    slug: str


class OrgsApplyParamsSpaceCategoryRequiredTagGroup(TypedDict, total=False):
    tagGroupId: str
    minCount: int


class OrgsApplyParamsSpaceCategory(TypedDict, total=False):
    name: str
    description: str
    color: Optional[str]
    parentId: Optional[str]
    sortOrder: int
    defaultNotificationLevel: str
    topicTemplate: Optional[Dict[str, Any]]
    minimumRequiredTags: int
    defaultTags: List[str]
    allowedTags: List[str]
    defaultSort: Optional[str]
    logoUrl: Optional[str]
    backgroundUrl: Optional[str]
    numFeaturedTopics: Optional[int]
    showSubcategoryList: bool
    autoCloseHours: Optional[int]
    defaultSlowModeSeconds: Optional[int]
    requiredTagGroups: List["OrgsApplyParamsSpaceCategoryRequiredTagGroup"]
    navigateToFirstPost: Any
    defaultListFilter: Optional[str]


class OrgsApplyParamsSpaceMonitor(TypedDict, total=False):
    name: str
    url: str
    method: str
    kind: str
    intervalSeconds: int
    visible: bool
    alertsEnabled: bool
    failureThreshold: int
    successThreshold: int
    keyword: Optional[str]
    certExpiryDays: Optional[int]
    expectStatus: Optional[int]
    maxLatencyMs: Optional[int]
    requestHeaders: Optional[Dict[str, Any]]
    requestBody: Optional[str]
    bodyPath: Optional[str]
    bodyExpect: Optional[str]
    group: Optional[str]
    declaredState: Optional[str]


class OrgsApplyParamsSpace(TypedDict, total=False):
    name: str
    slug: str
    type: str
    visibility: str
    seed: bool
    preset: str
    shape: "OrgsApplyParamsSpaceShape"
    settings: Dict[str, Any]
    theme: "OrgsApplyParamsSpaceTheme"
    redirects: List["OrgsApplyParamsSpaceRedirect"]
    collections: List["OrgsApplyParamsSpaceCollection"]
    categories: List["OrgsApplyParamsSpaceCategory"]
    monitors: List["OrgsApplyParamsSpaceMonitor"]


class OrgsApplyParamsSource(TypedDict, total=False):
    spaceId: Optional[str]
    kind: str
    title: str
    url: str
    content: str


class OrgsApplyParams(TypedDict, total=False):
    version: float
    spaces: List["OrgsApplyParamsSpace"]
    sources: List["OrgsApplyParamsSource"]
