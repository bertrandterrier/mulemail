import os

MAIL_DIR = os.path.expandvars(os.path.expanduser("$HOME/Mails"))

DATA_CACHE = os.path.expandvars("$XDG_CACHE_HOME/mulemail")

DATA_STORAGE = os.path.expandvars("$XDG_DATA_HOME/mulemail")

APP_STATES = os.path.expandvars("$XDG_DATA_HOME/mulemail")

APP_CONFIG = os.path.expandvars("$XDG_CONFIG_HOME/mulemail")

from utils.helper import StatusPrinter
from mulemail.config import g_config

statprint: StatusPrinter = StatusPrinter()
