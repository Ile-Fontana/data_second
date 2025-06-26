import pandas as pd
from .base import BaseLoader

class JSONLoader(BaseLoader):
    def load_data(self):
        return pd.read_json(self.path)