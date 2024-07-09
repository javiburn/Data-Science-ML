import pandas as pd
import numpy as np

def load_csv():
    try:
        df = pd.read_csv("datos_meteorologicos.csv")
    except:
        print("Error when loading data")
        exit(1)
    return df

def show_mean_temp(array_temp):
    # We substitute the nan values with the mean() value of the other rows ignoring the other nan values too
    temp_mean = np.nanmean(array_temp)
    temp_nulo = np.isnan(array_temp)
    array_temp = np.where(temp_nulo, temp_mean, array_temp)
    print("Temperatura promedio: ")
    print(temp_mean)
    return array_temp

def show_total_prec(array_prec):
    prec_nulo = np.isnan(array_prec)
    prec_mean = np.nanmean(array_prec)
    array_prec = np.where(prec_nulo, prec_mean, array_prec)
    prec_total = np.nansum(array_prec)
    print("Total precipitaciones:")
    print(prec_total)
    return array_prec

def show_max_hum(array_hum):
    hum_nulo = np.isnan(array_hum)
    hum_mean = np.nanmean(array_hum)
    array_hum = np.where(hum_nulo, hum_mean, array_hum)
    hum_max = np.max(array_hum)
    print("Humedad máxima:")
    print(hum_max)
    return array_hum

def main():
    df = load_csv()
    # We convert the pd dataframe to a numpy array
    array_temp = df['Temperatura'].to_numpy()
    array_prec = df['Precipitación'].to_numpy()
    array_hum = df['Humedad'].to_numpy()

    # Clean the data converting NaN values into the mean() values
    clean_temp = show_mean_temp(array_temp)
    clean_prec = show_total_prec(array_prec)
    clean_hum = show_max_hum(array_hum)

    # Create the new and cleaned DataFrame
    df['Temperatura'] = clean_temp
    df['Precipitación'] = clean_prec
    df['Humedad'] = clean_hum

    # Print hottest and coldest day
    hot = df.sort_values(by='Temperatura', ascending=False).head(1)
    print("Día más caluroso:")
    print(hot['Fecha'].to_string(index=False))
    cold = df.sort_values(by='Temperatura').head(1)
    print("Día más frío:")
    print(cold['Fecha'].to_string(index=False))

    # Export the data to a new CSV
    df.to_csv("datos_meteo_limpios.csv")

if __name__ == '__main__':
    main()