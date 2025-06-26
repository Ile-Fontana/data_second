from validator.validator import DataValidator
from db.manager import DatabaseManager
from pathlib import Path
from loaders.loader__init__ import get_loader

files_dir = Path("files")
db = DatabaseManager()

def main():
    for file_path in files_dir.glob("*.*"):
        try:
            loaders = get_loader(file_path)
            df = loaders.load_data()
            validator = DataValidator(df)
            df = validator.validate()
            table_name = file_path.stem
            db.save_dataframe(df, table_name)
            print(f"✅ Cargado: {file_path.name} -> {table_name}")
        except Exception as e:
            print(f"❌ Error al cargar: {file_path.name}: {e}")

if __name__ == '__main__':
    main()