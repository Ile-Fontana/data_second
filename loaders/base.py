import pandas as pd
from abc import ABC, abstractmethod

class BaseLoader(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        pass