import pandas as pd
from model.source import Source
from model.cleaner import DataCleaner

def main():
    source = Source("./medallas.csv")
    clean = DataCleaner(source.df)

if __name__ == '__main__':
    main()