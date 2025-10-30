from dataclasses import dataclass
import os
import pathlib
from typing import Union

from email.utils import parseaddr

PathStr = Union[str, pathlib.Path, os.PathLike]


class mailstr(str):
    __slots__ = (
        "NAME", "LOCAL", "TLD", "SLD", "DOMAIN"
    )
    def __new__(cls, item) -> "mailstr":
        inst = super().__new__(cls, cls.unmunge(str(item)))

        inst.NAME, addr = parseaddr(str(item))

        if not addr:
            raise SyntaxError()

        inst.LOCAL, inst.DOMAIN = addr.split("@")

        inst.SLD, inst.TLD = inst.DOMAIN.split(".")

        return inst

    def clean(self) -> str:
        return self.munge(False, ("_", "_"))

    @classmethod
    def unmunge(cls, addr: str) -> str:
        result = addr.lower()

        for sym, lit in zip(["@", "."], ["at", "dot"]):
            for brackets in ["[]", "()"]:
                result.replace(f"{brackets[0]}{lit}{brackets[1]}", sym)
        return result

    def __str__(self):
        return f"{self.LOCAL}@{self.SLD}.{self.TLD}"

    def munge(self, soft: bool = True, brackets: tuple[str, str] = ("(", ")")) -> str:
        if not soft:
            return f"{self.LOCAL}{brackets[0]}at{brackets[1]}{self.SLD}{brackets[0]}.{brackets[1]}{self.TLD}"

        else:
            return str(self).replace("@", f"{brackets[0]}at{brackets[1]}")
        


##### CONFIG #####
@dataclass
class AccountConfig:
    email: str
    name: str|None
    server: str
    imap: int|str = 993
    smtp: int|str = 587
    password: str|None = None

@dataclass
class GlobalConfig:
    mail_dir: pathlib.Path = pathlib.Path("~/Mails")
    server: str|None = None
    imap: int|str = 993
    smtp: int|str = 587
    password: str|None = None
