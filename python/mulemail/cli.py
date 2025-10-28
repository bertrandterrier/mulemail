import os
import typer
from typing_extensions import Annotated, Optional

import mulemail as mule

app = typer.Typer()


@app.callback()
def main(
    conf_file: Annotated[str|None, typer.Option(
        "-c", "--config-file",
        help = "Alternative path for config file",
    )] = None,
    conf_dir: Annotated[str|None, typer.Option(
        "-C", "--config-dir",
        help = "Alternative path for config directory",
    )] = None,
):
    if conf_file:
        conf_file = os.path.expandvars(os.path.expanduser(conf_file))
    elif conf_dir:
        conf_file = os.path.join(conf_dir, mule.config.CONF_FILE_NAME)
    else:
        conf_file = str(mule.)

    return

_complete_acc_list = mule.accounts + ['all']
def complete_account(ctx: typer.Context, param:, text) -> list[str]:
    result: list[str] = []
    if 'all'.startswith(param)
    return


@app.command("fetch")
def fetch(
    account: Annotated[Optional[str], typer.Argument(
        help = "Account name or e-mail address",
    )]
):

if __name__ == "__main__":
    app()
