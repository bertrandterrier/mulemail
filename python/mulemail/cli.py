from enum import Enum
from pathlib import Path
import typer
from typer.models import CallbackParam
from typing_extensions import Annotated, Optional
from rich import print

#import mulemail as mule
#from mulemail.schemes import PathStr

cli = typer.Typer()

class SetupOps(str, Enum):
    show = "show"
    update = "update"
    reset = "reset"

def autocomplete(ctxt, callback: CallbackParam, arg):
    caller = callback.human_readable_name


@cli.command(name = "config")
def setup(
    operation: Annotated[SetupOps, typer.Argument(
        show_choices = True,
        autocompletion = lambda: ["show", "update", "reset"]
    )],
):
    print(operation)



if __name__ == "__main__":
    #mule.LOGGER.info("START mulemail..")
    #mule.LOGGER.info("LOAD config..")

    #global CONFIG
    #CONFIG = mule.helper.get_config(mule.CONFIG_DIR)
    cli()
