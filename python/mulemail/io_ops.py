from pathlib import Path
import toml

def get_root_dir(file: str = str(Path(__file__))) -> Path:
    """Extracts the root directory starting from file."""
    result = Path(file).parent
    if not "mulemail" in str(file).lower():
        raise RuntimeError("Unknown directory structure. Missing \"mulemail\".")
    while str(result).lower().count("mulemail") > 2:
        result = result.parent
    return result

root_dir: Path = get_root_dir()
_INF_KEYS = [
        'name', 'version', 'summary', 'homepage',
        'author', 'email', 'license', 'requirements'
    ]
