import os
from pathlib import Path

APP_NAME = "mulemail"

BASE_DIR = Path(__file__).parent 


# DIRECTORIES
MAIL_HOME = Path(
    os.environ.get("HOME", os.path.expanduser("~"))
) / "Mails"

DATA_CACHE = Path(os.environ.get(
    "XDG_CACHE_HOME", os.path.expanduser("~/.cache/")
)) / APP_NAME 

DATA_STORAGE = Path(os.environ.get(
    "XDG_DATA_HOME", os.path.expanduser("~/.local/share")
)) / APP_NAME

APP_CONFIG = Path(os.environ.get(
    "XDG_CONFIG_HOME", os.path.expanduser("~/.config")
)) / APP_NAME
