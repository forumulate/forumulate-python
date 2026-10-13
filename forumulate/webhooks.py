"""Verify Forumulate webhook deliveries.

The ``X-Forumulate-Signature`` header is a comma-separated LIST, not one
value::

    v1,sha256=<a>, v1,sha256=<b>, sha256=<c>, sha256=<d>

During a secret rotation both secrets sign, and while an endpoint's
``signatureVersion`` is ``both`` the legacy body-only ``sha256=`` rides along.
A delivery is genuine if ANY entry matches. ``v1`` signs
``<timestamp>.<raw body>``, which is what makes a captured delivery
un-replayable; the legacy one covers the body alone, so it is accepted only
when you ask for it.
"""
import hashlib
import hmac
import re
import time
from typing import Optional, Union

__all__ = ["verify_signature"]

_ENTRY = re.compile(r"(v1,)?sha256=([0-9a-fA-F]+)")


def _hex(secret: bytes, message: bytes) -> str:
    return hmac.new(secret, message, hashlib.sha256).hexdigest()


def verify_signature(
    secret: str,
    body: Union[str, bytes],
    signature: Optional[str],
    timestamp: Union[str, int, None],
    *,
    tolerance_seconds: int = 300,
    accept_legacy: bool = False,
    now: Optional[float] = None,
) -> bool:
    """True when ``signature`` proves Forumulate sent ``body`` at ``timestamp``.

    :param secret: the endpoint's signing secret.
    :param body: the raw request body, exactly as received (verify BEFORE json.loads).
    :param signature: the whole ``X-Forumulate-Signature`` header.
    :param timestamp: the ``X-Forumulate-Timestamp`` header (unix seconds).
    :param tolerance_seconds: how old (or how far in the future) a delivery may be; 0 skips the check.
    :param accept_legacy: also accept the replayable body-only ``sha256=`` signature.
    """
    if not secret or not signature:
        return False
    try:
        ts = int(str(timestamp).strip())
    except (TypeError, ValueError):
        return False
    if ts <= 0:
        return False
    if tolerance_seconds > 0:
        current = int(now if now is not None else time.time())
        if abs(current - ts) > tolerance_seconds:
            return False
    raw = body.encode("utf-8") if isinstance(body, str) else bytes(body)
    key = secret.encode("utf-8")
    v1 = _hex(key, str(ts).encode("ascii") + b"." + raw)
    legacy = _hex(key, raw) if accept_legacy else None
    ok = False
    for match in _ENTRY.finditer(signature):
        offered = match.group(2).lower()
        if match.group(1):
            ok = hmac.compare_digest(offered, v1) or ok
        elif legacy is not None:
            ok = hmac.compare_digest(offered, legacy) or ok
    return ok
