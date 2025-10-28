import logging
import os
from pathlib import Path
from datetime import datetime

from mulemail.utils.helper import set_logger, get_cache

APP_NAME = "mulemail"
BASE_DIR = Path(__file__).parent 

LOGGER = set_logger(logging.DEBUG)

# DIRECTORIES
MAIL_DIR = os.path.expandvars(os.path.expanduser("$HOME/Mails"))

DATA_CACHE = Path(os.environ.get("XDG_CACHE_HOME", os.path.expanduser("~/.cache/"))) / "mulemail"

DATA_STORAGE = os.path.expandvars("$XDG_DATA_HOME/mulemail")

APP_STATES = os.path.expandvars("$XDG_DATA_HOME/mulemail")

APP_CONFIG = os.path.expandvars("$XDG_CONFIG_HOME/mulemail")

MSG_CONTENT_NAME = "message.*"

MSG_DATA_FNAME = "head.toml"

MSG_ATTACH_DIR = "attachments/"

CACHE = get_cache()
