import pandas as pd
from model.shop import Shop

def merge_and_remove_duplicated_rows(shop1, shop2):
    shop = pd.concat([shop1.df, shop2.df], ignore_index=True)
    dup = shop.duplicated()
    print("Removing duplicated rows...")
    print(shop[dup])
    shop = shop.drop_duplicates()
    print("Duplicated rows were removed.")
    shop.reset_index(drop=True, inplace=True)
    return shop

def clean_data(shop):
    # Converting dates to date format instead of strings
    shop['Fecha'] = pd.to_datetime(shop['Fecha'], format='%m/%d/%Y')
    # Check if the total is equeal to cantidad (amount) * precio (price)
    checker = shop['Precio Unitario'] * shop['Cantidad'] != shop['Total Venta']
    if shop[checker].empty:
        print("The calculations are correct.")
    else:
        print("Rows whit wrong calculations:")
        print(shop[checker])
        # Here should be the code to clean the data on these rows, but in our case everything is correct)
    return shop

def show_highest_sales(shop_cleaned):
    # Show which was the mostly sold product
    print("Producto más vendido:")
    print(shop_cleaned.sort_values(by='Cantidad', ascending=False).head(1))
    # Show the month with highest number of sales and create months column
    print("Mes con mayor número de ventas:")
    shop_cleaned['Mes'] = shop_cleaned['Fecha'].dt.month_name()
    months = shop_cleaned.groupby(['Mes'])
    print(months['Cantidad'].sum().sort_values(ascending=False).head(1))

def main():
    shop1 = Shop("./Datos_Ventas_Tienda.csv")
    shop2 = Shop("./Datos_Ventas_Tienda2.csv")
    # Merging both dataframes and removing duplicated rows 
    shop = merge_and_remove_duplicated_rows(shop1, shop2)
    shop_cleaned = clean_data(shop)
    show_highest_sales(shop_cleaned)
    # Group products by categories
    groups = shop_cleaned.groupby(['Producto'])
    print("Ventas por categoría de producto:")
    print(groups['Cantidad'].sum())
    # Create a column to show months
    shop_cleaned.to_csv("./Datos_Ventas_Final.csv", index=False)

if __name__ == '__main__':
    main()