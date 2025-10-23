from mulemail._types import PathStr

class Account:
    def __init__(
        self,
        address: str,
        server: str,
        pw: str|None = None,
        name: str|None = None,
        imap: int = 993,
        smtp: int = 587,
        as_default: bool = False,
        **meta,
    ):
        self._mail: str = address
        self.__pw: str|None = pw
        self._server: str = server
        self.imap: int = imap
        self.smtp: int = smtp

        self.name: str|None = name
        self.meta: dict = {k: v for k, v in meta.items()}
        
        self._is_def: bool = as_default

    def __str__(self) -> str:
        return self.name or self._mail

    @property
    def address(self) -> str:
        return self._mail

    @property
    def server(self) -> str:
        return self._server

    @property
    def is_default(self) -> bool:
        return self._is_def

accounts: list[Account] = []
