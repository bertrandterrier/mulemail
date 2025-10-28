from email.message import EmailMessage
from pathlib import Path

from mulemail.utils.schemes import PathStr
import mulemail as mule


def makemsg(src: PathStr, **kwargs) -> EmailMessage:
    _def_pttrns: dict = {
        'content': "body[^/]*$",
        'head': "head"
    }
    dir_path = Path(src)

