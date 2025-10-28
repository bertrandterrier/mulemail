from email.message import EmailMessage
from imaplib import IMAP4_SSL

import mulemail as mule
from mulemail.utils.schemes import UserCache

def server_connect(**data):
    ...


def fetch(
    *accounts: str|UserCache,
    limit_boxes: list[str]|None = None
):
    for acc in accounts:
        if not isinstance(acc, UserCache):
            if not mule.CACHE.user_lookup(acc):
                mule.LOGGER.warn(f"Unable to find account {acc}")
                continue
            acc = mule.CACHE.app.accounts.get(acc)
    return

