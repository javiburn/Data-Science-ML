import pandas as pd

class Source:
    def __init__(self, path):
        self.path  = path
        self.open_file()

    def open_file(self):
        try:
            self.df = pd.read_csv(self.path)
            self.created = True
        except IOError:
            print("Error opening the file.")
            self.created = False