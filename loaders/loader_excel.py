import pandas as pd
from .base import BaseLoader

class ExcelLoader(BaseLoader):
    def load_data(self):
        return pd.read_excel(self.path)