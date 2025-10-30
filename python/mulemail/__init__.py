import logging
import os

from mulemail.utils import helper
from mulemail.settings import *

LOGGER = helper.makelogger(logging.DEBUG)

APP = "mulemail"

HOME = Path().home()

CONFIG_DIR = helper.get_xdg_path("config") / APP

CACHE_DIR = helper.get_xdg_path("cache") / APP

DATA_DIR = helper.get_xdg_path("data") / APP

STATE_DIR = helper.get_xdg_path("state") / APP
