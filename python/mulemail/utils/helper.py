import pandas
from pandas import DataFrame
from pathlib import Path
from typing import Literal, Any, Iterable, Callable
from rich import print

import mulemail as mule
from mulemail.utils.schemes import PathStr


class StatusPrinter:
    def __init__(self, _fmt_func: Callable[..., str]|None = None, _print_func: Callable = print, **kwargs):
        self._print_func: Callable = print
        self._fmt_func: Callable[..., str] = None or self.fmt
        self._config: dict = {k: v for k, v in kwargs.keys()}

    def __call__(self, output: Any) -> Any:
        if isinstance(output, str):
            status, *rest = output
            self._print_func(self._fmt_func(status, **self._config))
            return rest

    def fmt(self, arg: str|Iterable, title: str|None = "[status]", prefix: str = ":: ", _level: int = 0) -> str:
        result = []

        if title:
            result.append([_level * "\t" + title])
        if _level > 0 and title:
            _level += 1
        if isinstance(arg, str) and not "\n" in arg:
            result.append(f"{ _level * '\t' }{ prefix }{ arg }")
            return "\n".join(result)
        if isinstance(arg, str):
            arg = arg.split("\n")
        for line in arg:
            result.append(
                self.fmt(line, title = None, prefix = prefix, _level = _level)
            )
        return "\n".join(result)

class MessageLog:

    def __init__(
        self,
        address: str|None = None,
        box: str|None = None, _path: PathStr = Path(mule.APP_STATES)
    ):
        self._path: Path = Path(_path)
        self._slct_mail: str|None = address
        self._slct_box: str|None = box

        if not self._path.exists():
            self._df_raw = pandas.read_csv(self._path)
        else:
            self._df_raw = pandas.DataFrame()
        self._df_raw.columns = ['UID', 'ADDRESS', 'BOX']
        self._df= self._df_raw.dropna(subset = ['UID'])
        self._df['UID'] = self._df['UID'].astype(int)

    def uids(self) -> list[int]:
        iter_df: DataFrame = self._df
        for col, val in zip(
            ['ADDRESS', 'BOX'],
            [self._slct_mail, self._slct_box]
        ):
            if not val:
                continue
            mask = iter_df.loc[:, col] == val
            iter_df = iter_df.loc[mask,:]
        return iter_df['UID'].to_list()

    def select(
        self,
        field: Literal['box', 'address'],
        _to: str|None = None
    ):
        setattr(self, f"_slct_{field}", _to)

    def update(self, new: list[int], address, box):
        for uid in new:
            self._df[len(self._df)] = [uid, address, box]
        self._df.to_csv(self._path)
        return

    def __call__(self, other: list, update: bool = False) -> list[int]:
        new: list[int] = []
        old: list[int] = self.uids()

        for i in other:
            if not int(i) in old:
                new.append(int(i))
        if update:
            self.update(new, self._slct_mail, self._slct_box)
        return new
