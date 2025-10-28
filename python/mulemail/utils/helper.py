import logging
from datetime import datetime
from pathlib import Path
import toml
from typing import Any

from mulemail import DATA_CACHE, APP_NAME, APP_CONFIG
from mulemail.utils.schemes import Cache, UserCache, ConfigCache, PathStr

def set_logger(
    level: int = logging.INFO,
    fmt: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
) -> logging.Logger:
    logger = logging.getLogger(APP_NAME)

    formatter = logging.Formatter(APP_NAME)

    fname = f"{datetime.now().strftime("%Y-%m-%d_%H%M%S")}"
    path = Path(DATA_CACHE) / ".logs" / f"{fname}.log"

    file_handler = logging.FileHandler(path)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    logger.addHandler(file_handler)

    return logger

def get_cache(path: PathStr = APP_CONFIG) -> Cache:
    with open(path, 'r') as f:
        data = toml.load(f)

    user_configs: dict[str, UserCache] = {
        tbl.get(
            'name', tbl.get('email')
        ): UserCache(**tbl) for tbl in data.get("account", {})
    }
    app_config: dict[str, Any] = {k: v for k, v in data.items() if k != "account"}

    app_config['accounts'] = user_configs

    return Cache(**app_config)
