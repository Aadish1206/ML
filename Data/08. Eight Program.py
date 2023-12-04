import numpy as np
import pandas as pd

csv_file_path = r"C:\Users\aadis\Desktop\Category.csv"
df = pd.read_csv(csv_file_path)

quantity_column = df['Quantity']

#to calculate Minimum,Median,Percentile_25 and maximum
minimum = np.min(quantity_column)
median = np.median(quantity_column)
percentile_25 = np.percentile(quantity_column, 25)
maximum = np.max(quantity_column)

print("Minimum: {minimum}")
print("Median: {median}")
print("25th Percentile: {percentile_25}")
print("Maximum: {maximum}")

#Print Unique Items
unique_items = df['Item'].unique()

print("Unique Items:")
for item in unique_items:
    print(item)
