import pandas as pd
from model.source import Source
from model.cleaner import DataCleaner
from model.countries import Golden, Medals

def main():
    source = Source("./medallas.csv")
    clean = DataCleaner(source.df)
    gold = Golden(clean.clean_data)
    print("\n\nCountries with the highest number of golden medals:")
    print(gold.gold)
    medals = Medals(clean.clean_data)
    print("\n\nCountries with more than 10 medals in total:")
    print(medals.medals)
    print("Average number of medals per country: ", "{:.5f}".format(clean.clean_data['Total'].std()))

if __name__ == '__main__':
    main()