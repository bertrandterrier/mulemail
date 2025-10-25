import toml
from pathlib import Path

from mulemail.utils.schemes import PathStr, ConfigCache,AccountCache 
import mulemail as mule


global global_cache 

def update_config(path: PathStr = mule.APP_CONFIG) -> None:
    path = Path(path)

    with open(path, "r") as f:
        raw = toml.load(f)

    data = { k: v for k, v in raw.items() if not k == "account" }

    data['accounts'] = {}
    for account in raw.get('account', []):
        for attr in ['server', 'imap', 'smtp', 'password']:
            account[attr] = account.get(attr, raw.get(attr))
        data['accounts'][account['email']].append(AccountCache(**account))

    global g_cache
    g_cache = ConfigCache(**data)
    return
