import typer
from typing_extensions import Annotated
from rich import print

app = typer.Typer()


@app.callback()
def main(
    version: Annotated[bool, typer.Option(False, "--version", "-v")],
    show: Annotated[bool, typer.Option(False, "--show", "-s")],
):
    if show:
        print("show")
    elif version:
        print("version")
    return



if __name__ == "__main__":
    app()
