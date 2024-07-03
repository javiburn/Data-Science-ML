import pandas as pd

class DataCleaner:
    def __init__(self, df) -> None:
        self.fill_empty(df)
        self.check_sum()

    def fill_empty(self, df):
        print("Number of empty values before cleaning data:")
        filler = {"Oro": 0, "Plata":0, "Bronce":0}
        print(df.isnull().sum())
        print("Filling null values in the required fields...")
        print("Number of empty values after cleaning data:")
        self.clean_data = df.fillna(filler)
        print(self.clean_data.isnull().sum())

    def check_sum(self):
        gold = self.clean_data['Oro']
        silver = self.clean_data['Plata']
        bronze = self.clean_data['Bronce']
        total = self.clean_data['Total']
        filter = total != gold + silver + bronze
        error_total = self.clean_data[filter]
        print("Countries where the value in the 'total' column is different than the sum of their medals:")
        print(error_total)
        self.clean_data.loc[total != gold + silver + bronze, 'Total'] = gold + silver + bronze
        print("'Total' column values have been changed")
        error_total = self.clean_data[filter]
        print(error_total)
        gold = self.clean_data['Oro']
        silver = self.clean_data['Plata']
        bronze = self.clean_data['Bronce']
        total = self.clean_data['Total']
        filter = total != gold + silver + bronze
        error_total = self.clean_data[filter]
        if error_total.empty:
            print("The values were successfully converted")
        else:
            print(error_total)
