class DataValidator:
    def __init__(self, df):
        self.df = df

    def validate(self):
        self.df = self.df.drop_duplicates()
        self.df = self.df.dropna()
        return self.df

