# Forumulate Python SDK

The official Python client for the [Forumulate](https://forumulate.com) API: docs, forum, blog and every other space type, plus the organization around them. Every operation of the API (v1.1.0) is a typed method, grouped the way the product is: `client.spaces`, `client.docs.pages`, `client.forum.topics`, `client.blog.articles`, …

- Python 3.8+, one dependency (`requests`), fully typed (`py.typed`; request and response shapes are `TypedDict`s in `forumulate.types`).
- Retries rate limits and server errors with backoff, honouring `Retry-After`.
- Auto-pagination (`list_all`), server-sent events (`*_stream`), a typed error per status.
- Pinned to API version `2026-11-01`: every request sends `Forumulate-Version: 2026-11-01`, so the response shapes in `forumulate.types` are the ones you receive.

## Install

```sh
pip install forumulate
```

## Authenticate

Create a token under **Account → Tokens** and put it in the environment:

```sh
export FORUMULATE_TOKEN=ak_...
```

```python
from forumulate import Forumulate

client = Forumulate()  # reads FORUMULATE_TOKEN / FORUMULATE_URL / FORUMULATE_API_URL
# or explicitly:
client = Forumulate(token="ak_...", base_url="https://forumulate.com/api")
```

| Variable | Meaning |
| --- | --- |
| `FORUMULATE_TOKEN` | Your API token (Account → Tokens: `ak_…` or `cft_…`), sent as `Authorization: Bearer`. |
| `FORUMULATE_URL` | Your site, default `https://forumulate.com`. The API is its `/api` (a value already ending in `/api` is used as is). |
| `FORUMULATE_API_URL` | The exact API base, e.g. `http://localhost:4000`. Wins over `FORUMULATE_URL`. |

These are the names `@forumulate/sdk`, the CLI and `@forumulate/mcp` read, so one `.env` drives all of them.

Organizations and spaces take an id or a slug wherever the API asks for one.

## Quickstart: the five most common tasks

### 1. List your organizations and their spaces

```python
for org in client.orgs.list_all():
    print(org["slug"])
    for space in client.spaces.list_all(org["id"]):
        print("  ", space["type"], space["slug"], space["name"])
```

`list_all` follows the cursor for you; `list` returns one page (`{"spaces": [...], "page": {...}}`).

### 2. Write a docs page and publish it

```python
created = client.docs.pages.create(
    "acme", "handbook", "guides",          # org, space, collection
    title="Getting started",
    slug="getting-started",
    body="# Getting started\n\nInstall the CLI, then sign in.",  # markdown
)
page = created["page"]
client.docs.pages.publish("acme", "handbook", page["id"])
```

### 3. Read and start forum topics

```python
for topic in client.forum.topics.list_all("acme", "community", sort="latest", limit=50):
    print(topic["title"])

client.forum.topics.create(
    "acme", "community",
    title="How do I rotate a token?",
    markdown="I want to rotate the token my CI uses without downtime.",
    tags=["tokens"],
)
```

### 4. Search everything in an organization

```python
results = client.search.query("acme", q="rotate token", limit=10)
```

### 5. Verify a webhook delivery

```python
from forumulate.webhooks import verify_signature

ok = verify_signature(
    secret=os.environ["FORUMULATE_WEBHOOK_SECRET"],
    body=request.get_data(),                       # the RAW body, before json.loads
    signature=request.headers["X-Forumulate-Signature"],
    timestamp=request.headers["X-Forumulate-Timestamp"],
)
if not ok:
    abort(401)
# X-Forumulate-Delivery is the key to dedupe on: retries reuse it.
```

## Errors

Every non-2xx answer raises a subclass of `forumulate.APIStatusError` carrying `status`, `code` (the API's machine-readable code), `message` and `request_id`:

```python
import forumulate

try:
    client.spaces.get("acme", "nope")
except forumulate.NotFoundError:
    ...
except forumulate.AuthenticationError as e:
    print(e.code, e.message)          # auth.unauthenticated  Authentication required.
```

| Status | Exception |
| --- | --- |
| 400 | `BadRequestError` |
| 401 | `AuthenticationError` |
| 403 | `PermissionDeniedError` |
| 404 | `NotFoundError` |
| 409 | `ConflictError` |
| 422 | `UnprocessableEntityError` |
| 429 | `RateLimitError` (after retries) |
| 5xx | `InternalServerError` (after retries) |

No answer at all raises `APIConnectionError` (`APITimeoutError` for a timeout). All of them derive from `forumulate.ForumulateError`.

## More

- **Per-call options.** Every method takes `extra_query`, `extra_headers`, `timeout` (and `extra_body` where it sends one) for anything the typed arguments do not cover, e.g. `extra_headers={"Idempotency-Key": key}`.
- **Client options.** `Forumulate(timeout=30, max_retries=2, default_headers={...}, http_session=requests.Session())`. Use it as a context manager (`with Forumulate() as client:`) or call `client.close()`.
- **Unset vs null.** Optional arguments default to `NOT_GIVEN` and are not sent; pass `None` to send an explicit `null`.
- **Reference.** Every method's docstring names its route; the API reference is at <https://forumulate.com/reference>.

This package is generated from Forumulate's OpenAPI document by Forumulate's own SDK generator — the same one that builds SDKs for the APIs our customers document with us. Do not edit it by hand: a fix belongs in the generator, and lands here on the next release. The source of truth is the private monorepo; this repository is a mirror (`forumulate-python`).

## License

MIT
