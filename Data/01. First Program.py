#How to load a sample data from a csv to a dataframe while loading, csv ignore the header- add empty inital 3 rows, 4th row shud start and 4thh row will be header, skip function
import pyspark

import pandas as pd

csv_file_path = r"C:\Users\aadis\Downloads\bankdataset.csv"

df = pd.read_csv(csv_file_path, skiprows=3, header=3)

print(df)

missingcount = df.isnull().sum()

print(missingcount)

df = df[['Location', 'Domain', 'Transaction_count', 'Value', 'Date']]

print(df)
