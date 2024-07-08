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
    #df = load_csv()
    array = np.genfromtxt("datos_meteorologicos.csv", delimiter=',', \
        filling_values=0, skip_header=1)
    print(array)

if __name__ == '__main__':
    main()