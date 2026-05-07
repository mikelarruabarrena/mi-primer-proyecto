# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import pandas as pd


def csv_to_df(path):
    return pd.read_csv(path, sep=',')


df = csv_to_df("../../Downloads/SKUs_MAR_AR_PCB_1.csv")
#print(df)

def df_to_excel(df,path):
    return df.to_excel(path,index=False)

#df_to_excel(df,"../../Downloads/SKUs_MAR_AR_PCB_1.xlsx")


import polars as p
def csv_to_df_polars(path):
    return p.read_csv(path)


datos = p.read_csv("../../Downloads/SKUs_MAR_AR_PCB_1.csv")
print(datos)

def df_to_excel_polars(data,path):
    return data.write_excel(path)

df_to_excel_polars(datos,"../../Downloads/SKUs_MAR_AR_PCB_2.xlsx")
