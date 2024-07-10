import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def open_file():
    try:
        df = pd.read_csv("Datos+Meteorológicos_Arg_2023.csv")
    except:
        print("Error opening the file")
        exit(1)
    return df

def get_user_city(df):
    # Check the cities that are in the dataset
    cities_array = df['Ciudad'].drop_duplicates()
    string = "Select one city ("
    checker = []
    for city in cities_array:
        checker.append(city)
        string += city
        if city is not cities_array.iloc[-1]:
            string += ", "
    string += "): "
    while True:
        city = input(string)
        if city in checker:
            break
        else:
            print("The selected city is not in our database, try with another one.")
    return city

def get_user_month():
    while True:
        month = input("Select a month (in numeric style): ")
        try:
            num = int(month)
        except:
            print("Invalid month selected.")
        if num > 0 and num < 13:
            break
        else:
            print("Invalid month selected.")
    return num

def extract_data(df, city, month_num):
    months = ["None", "January", "February", "March", "April", "May", "June", "July", "August", "September", \
              "October", "November", "December"]
    city_values = df.loc[df['Ciudad'] == city]
    city_values = city_values.reset_index(drop=True)
    month = months[month_num]
    months_df = city_values
    months_df['Mes'] = city_values['Fecha'].dt.month_name()
    month_df = months_df.loc[months_df['Mes'] == month]
    return month_df

def show_data(df):
    x = df['Fecha'].dt.day
    y1 = df['Temperatura Maxima']
    y2 = df['Temperatura Minima']
    fig, ax = plt.subplots(ncols=3, nrows=2, sharey = True)
    plt.axis([1, 31, 0, 50])
    ax[0, 0].plot(x, y1, color='red')
    ax[0, 1].plot(x, y2, color='blue')
    ax[1, 0].bar(x, y1, color='red')
    ax[1, 1].bar(x, y2, color='blue')
    # set the title to subplots
    ax[0, 0].set_title("Temperatura Máxima")
    ax[0, 1].set_title("Temperatura Mínima")
    ax[0, 0].grid()
    ax[0, 1].grid()
    ax[1, 0].grid()
    ax[1, 1].grid()
    # set spacing
    fig.tight_layout()
    ax[0, 2].set_title("Comparación")
    ax[0, 2].plot(x, y1, color='red', alpha=0.5)
    ax[0, 2].plot(x, y2, color='blue', alpha=0.5)
    ax[1, 2].bar(x, y1, color='red', alpha=0.5)
    ax[1, 2].bar(x, y2, color='blue', alpha=0.5)
    plt.show()

def main():
    df = open_file()

    # Convert dates to datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True, errors="coerce")

    # Ask the user for a city and a month
    city = get_user_city(df)
    month_num = get_user_month()

    # Extract the data for that month and city
    month_df = extract_data(df, city, month_num)
    show_data(month_df)
    

if __name__ == '__main__':
    main()