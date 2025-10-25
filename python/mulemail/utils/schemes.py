from dataclasses import dataclass, field
import os
import pathlib
from typing import Union

PathStr = Union[str, pathlib.Path, os.PathLike]

@dataclass
class AccountCache:
    address: str
    name: str
    server: str
    imap: int|str = 993
    smtp: int|str = 587
    password: str|None = None

@dataclass
class ConfigCache:
    mail_dir: pathlib.Path = pathlib.Path("~/Mails")
    server: str|None = None
    imap: int|str = 993
    smtp: int|str = 587
    password: str|None = None
    accounts: dict[str, AccountCache] = field(default_factory = dict)

class Cache:
    def __init__(self, config: dict|ConfigCache):
        """"""

    @wrap
