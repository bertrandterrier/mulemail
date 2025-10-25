import pandas
from pathlib import Path

import mulemail as mule

def get_uid_log(account: str|None = None, box: str|None = None):
    path = Path(mule.APP_STATES) / "message_uids.csv"
    uids = pandas.read_csv(path)
    
    for col, val in zip(['account', 'box'], [account, box]):
        if not val:
            continue
        mask = uids.loc[:, col] == val
        uids = uids.loc[mask, :]

    return uids['uids'].to_list()
