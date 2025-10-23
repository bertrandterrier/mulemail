from dataclasses import dataclass
import os
from pathlib import Path
import toml
import json

from mulemail._types import PathStr

_name = "mulemail"
_home = Path(os.getenv("$HOME", os.path.expanduser("~")))

CONF_DIR = Path(os.getenv("$XDG_CONFIG_HOME", _home/".config")).joinpath(_name)
CONF_FILE_NAME = "config.toml"
CONF_FILE_PATH = CONF_DIR / CONF_FILE_NAME

MSG_STORAGE = Path(os.getenv("$XDG_DATA_HOME", _home/".local/share")).joinpath(_name)

STATE_CACHE = Path(os.getenv("$XDG_STATE_HOME", _home/".local/state")).joinpath(_name + ".json")

### CONFIG ###
@dataclass
class ConfigData:
    dir: PathStr = CONF_DIR

config: ConfigData = ConfigData()


def set_config_data(_path: PathStr = CONF_DIR) -> None:
    """Sets the global config data object."""
    if os.path.exists(_path):
        with open(_path, "r") as f:
            data = {k: v for k, v in toml.load(f).items() if hasattr(ConfigData, k)}
    else:
        data = {}

    global g_config
    g_config = ConfigData(**data)
    return


### RUNTIME STORAGE ###
memory: dict = {}


def load_cache(_path: PathStr = STATE_CACHE):
    try:
        with open(_path, "r") as f:
            cache = json.load(f)
    except:
        cache = {}

    global g_rts
    g_rts = cache
    return


def write_cache(_data: dict = g_rts, _path: PathStr = STATE_CACHE):
    with open(_path, 'w') as f:
        json.dump(_data, f)

