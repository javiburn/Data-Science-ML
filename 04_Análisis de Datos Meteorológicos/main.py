import pandas as pd
import numpy as np

def load_csv():
    try:
        df = pd.read_csv("datos_meteorologicos.csv")
    except:
        print("Error when loading data")
        exit(1)
    return df

def main():
    df = load_csv()
    # We convert the pd dataframe to a numpy array
    array_temp = df['Temperatura'].to_numpy()
    array_prec = df['Precipitación'].to_numpy()
    array_hum = df['Humedad'].to_numpy()

    # We substitute the nan values with the mean() value of the other rows ignoring the other nan values too
    temp_nulo = np.isnan(array_temp)
    temp_mean = np.nanmean(array_temp)
    array_temp = np.where(temp_nulo, temp_mean, array_temp)
    print("Temperatura promedio: ")
    print(temp_mean)

if __name__ == '__main__':
    main()