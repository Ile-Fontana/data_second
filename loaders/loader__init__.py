from .loader_csv import CSVLoader
from .loader_json import JSONLoader
from .loader_excel import ExcelLoader
from .loader_txt import TxtLoader

from pathlib import Path

def get_loader(path: Path):
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return CSVLoader(path)
    elif suffix == ".json":
        return JSONLoader(path)
    elif suffix in [".xls", ".xlsx"]:
        return ExcelLoader(path)
    elif suffix == ".txt":
        return TxtLoader(path)
    else:
        raise ValueError("Tipo de archivo no soportado")
