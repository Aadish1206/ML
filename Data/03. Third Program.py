#Select columns by dtype

import pandas as pd

data = {
    'name': ['Aadishwar', 'Sudha', 'Ramesh'],
    'City': ['Bangalore', 'Pondichherry', 'Chennai'],
    'age': [21, 40, 49],
    'height': [169, 156, 170],
    'student': [True, False, False],
    'grades': [95.5, 88.0, 92.5]
}

df = pd.DataFrame(data)


int_columns = df.select_dtypes(include='int64')


numeric_columns = df.select_dtypes(include=['int64', 'float64'])


object_columns = df.select_dtypes(include='object')


print("\nInteger columns:")
print(int_columns)

print("\nNumeric columns:")
print(numeric_columns)

print("\nObject columns:")
print(object_columns)


#Pandas slicing loc and iloc

filtered_df = df.query('age > 30').loc[:, ['name', 'City']]
print("\nFiltered columns:")
print(filtered_df)



