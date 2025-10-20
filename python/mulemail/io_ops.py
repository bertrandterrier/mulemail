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

def get_inf() -> dict:
    keys = _INF_KEYS
    replace = {
        "author-email": "email",
        "requires": "requirements"
    }
    inf_file = root_dir.joinpath("docs", "meta.toml")

    with open(inf_file, "r") as f:
        data = toml.load(f)

    result: dict = {}
    key_col_width: int = 1
    for field in keys:
        key_col_width = max(key_col_width, len(field))
        key = replace.get(field, field)

        if data.get(key):
            result[key] = (field.title(), data[key],)
        else:
            for _, v in data.items():
                if not isinstance(v, dict):
                    continue
                if v.get(key):
                    result[key] = (field.title(), data[key],)
                    break
        if not key in result.keys():
            result[key] = (field.title(), None)
    return result

def inf_txt() -> str:
    data: dict[str, dict] = get_inf()
    result = ""
    
    width = 1
    for k in _INF_KEYS:
        width = max(len(data[k][0]) + 1, width)

    for key in _INF_KEYS:
        name, value = data[key]
        result += f"{ name }{ (width - len(name)) * ' ' }:: {value}\n"
    return result
