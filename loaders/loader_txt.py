import pandas as pd
from .base import BaseLoader

class TxtLoader(BaseLoader):
    def load_data(self):
        return pd.read_csv(self.path, delimiter='\t')