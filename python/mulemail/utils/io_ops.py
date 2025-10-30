import pandas
from pathlib import Path

import mulemail as mule
from mulemail.schemes import PathStr

_path_lex: dict[str, PathStr] = {}

def get_uid_log(account: str|None = None, box: str|None = None):
    path = Path(mule.DATA_CACHE) / "message_uids.csv"
    uids = pandas.read_csv(path)
    
    for col, val in zip(['account', 'box'], [account, box]):
        if not val:
            continue
        mask = uids.loc[:, col] == val
        uids = uids.loc[mask, :]

    return uids['uids'].to_list()

