import pandas as pd

class Shop:
    def __init__(self, path) -> None:
        try:
            self.df = pd.read_csv(path)
        except:
            print("Error trying to open the files.")
            return