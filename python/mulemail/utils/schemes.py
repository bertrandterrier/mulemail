from dataclasses import dataclass, field, asdict
import os
import pathlib
from typing import Union, Any

PathStr = Union[str, pathlib.Path, os.PathLike]

@dataclass
class UserCache:
    email: str
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
    accounts: dict[str, UserCache] = field(default_factory = dict)

class Cache:
    def __init__(self, app: ConfigCache, user: str|None = None):
        self._app: ConfigCache = app
        self._user: str|None = user 

    def isuser(self) -> bool:
        return self._user != None

    @property
    def user(self) -> UserCache|None:
        if not self._user:
            return None
        return self._app.accounts.get(self._user, None)

    def get(self, key: str, user_value_first: bool = True, default: Any = None) -> Any:
        if user_value_first:
            result = getattr(
                self._app, key, getattr(
                    self._user, key, default
            ))
        else:
            result = getattr(self._app, key, default)
        return result

    @property
    def app(self) -> ConfigCache:
        return self._app

    def set_user(self, name: str) -> int:
        user = self.app.accounts.get(name, None)
        
        if user != None:
            self._user = user.name
            return 0

        for user in self.app.accounts.values():
            if name == user.email:
                self._user = user.name
                return 0
        return 1

    def user_lookup(self, name: str) -> bool:
        if self._app.accounts.get(name):
            return True
        for acc in self._app.accounts.values():
            if name == acc.email:
                return True
        return False
