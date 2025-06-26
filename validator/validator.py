import pandas as pd

class DataValidator:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.errors = []

    def validate(self, validate_required=False, required_columns=None) -> pd.DataFrame:
        self.df = self.df.drop_duplicates()
        self.df = self.df.dropna(how='all')
        if validate_required and required_columns:
            self.validate_required_fields(required_columns)

        expected_types = {
            "nombre": str,
            "edad": int,
            "email": str,
            "fecha_nacimiento": "date"  
        }
        self.validate_column_types(expected_types)

        if self.errors:
            raise ValueError("Errores encontrados:\n" + "\n".join(self.errors))

        return self.df

    def validate_required_fields(self, columns: list):
        for col in columns:
            if col not in self.df.columns:
                self.errors.append(f"Columna requerida '{col}' no está presente")
            elif self.df[col].isnull().any():
                self.errors.append(f"Columna '{col}' contiene valores nulos")

    def validate_column_types(self, expected_types: dict):
        for col, expected in expected_types.items():
            if col not in self.df.columns:
                continue
            series = self.df[col].dropna()
            if expected == "date":
                if not series.map(self.is_date).all():
                    self.errors.append(f"'{col}' contiene valores que no son fechas válidas")
            else:
                if not series.map(lambda x: isinstance(x, expected)).all():
                    self.errors.append(f"'{col}' contiene valores que no son del tipo {expected.__name__}")

    def is_date(self, value):
        if isinstance(value, pd.Timestamp):
            return True
        try:
            pd.to_datetime(value)
            return True
        except Exception:
            return False
