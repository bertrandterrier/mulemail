import logging
import os
from datetime import datetime
from pathlib import Path
import toml
from typing import Literal

import mulemail as mule
from mulemail.schemes import PathStr

def makelogger(
    level: int = logging.INFO,
    fmt: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    file_date_fmt: str = "%Y-%m-%d_%H%M%S"
) -> logging.Logger:
    """Set up file loger.

    level: int
        Log level. Defaults to logging.INFO
    fmt: str
        Format for logging.Formatter. Defaults to standard.
    file_date_fmt:
        Format for date in log file name.
        Defaults to "%Y-%m-%d_%H%M%S"
    """
    logger = logging.getLogger(mule.APP_NAME)

    formatter = logging.Formatter(fmt)

    file_name= f"{datetime.now().strftime(file_date_fmt)}"
    path = Path(mule.DATA_CACHE) / ".logs" / f"{file_name}.log"
    file_handler = logging.FileHandler(path)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    logger.addHandler(file_handler)
    return logger


def get_xdg_path(name: str) -> Path:
    XDG_LEX: dict = {
        "data": ("XDG_DATA_HOME", ["$HOME", ".local", "share"]),
        "config": ("XDG_DATA_HOME", ["$HOME", ".config"]),
        "cache": ("XDG_CACHE_HOME", ["$HOME", ".cache"]),
        "state": ("XDG_STATE_HOME", ["$HOME",".local", "state"]),
        "runtime": ("XDG_RUNTIME_DIR", ["run","user","$UID"]),
    }
    loc = os.environ.get(
        XDG_LEX.get(name.lower(), (name,))[0]
    )
    if loc:
        return Path(loc)
    loc = Path()
    for part in XDG_LEX[name]:
        loc = loc / os.path.expandvars(part)
    return loc

    
def merge_dicts(
    mode: Literal['force', 'keep', 'break'],
    l: dict,
    r: dict,
    replace_lists: bool = False
) -> dict:
    result = {k: v for k, v in l.items()}
    for key, val in r.items():
        if isinstance(val, dict) and key in result.keys():
            result[key] = merge_dicts(
                mode,
                result[key],
                val,
                replace_lists
            )
        elif isinstance(val, list) and key in result.keys():
            if not isinstance(result[key], list):
                mule.LOGGER.error(
f"""FAILED for key \"{key}\"
Values of different types:
LEFT["l"]   :: {type(result[key])}
RIGHT["r"]  :: {type(val)}"""
                )
                raise RuntimeError()
            elif replace_lists:
                result[key] = val
            else:
                result[key] += [e for e in val]
        elif not key in result.keys() or mode == 'force':
            result[key] = val
        elif mode == 'break':
            mule.LOGGER.error(f"Key \"{key}\" already existing (mode: 'break')")
            raise RuntimeError()
    return result

def get_config(
    file: PathStr,
    defaults: dict = {},
    merge_mode: Literal['force', 'keep', 'break'] = 'force',
) -> dict:
    if not Path(file).exists():
        mule.LOGGER.error(f"No config file.\nInvalid path {file}")
        return defaults
    with open(file, 'r') as f:
        raw = toml.load(f)

    mule.LOGGER.debug(f"User config:\n{raw}\nMERGE configs...")
    return merge_dicts(merge_mode, defaults, raw)
