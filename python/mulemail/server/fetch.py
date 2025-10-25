import getpass
from imaplib import IMAP4_SSL
from pathlib import Path

from mulemail import status_printer
from mulemail.config import g_config
from mulemail.utils import MessageLog

def fetch(
    account: str,
    boxes: list[str] = [ 'INBOX' ],
) -> list[Path]:
    """Fetch one or multiple boxes from email server (IMAP port)"""
    result = []
    conf = g_config.accounts[account]
    connection = IMAP4_SSL(str(conf.imap))

    connection.login(
        getattr(conf, "login", account),
        conf.password or getpass.getpass(f"Password [{ account }]: ")
    )
    # MessageLog call will filter the already downloaded uids
    msg_log = MessageLog(account)
    for box in boxes:
        msg_log.select('box', box.upper())
        connection.select(box.upper())
        data = status_printer(connection.uid('search', None, "ALL"))[0].split()
        uids = msg_log(data[0].split(), True)

    return result
