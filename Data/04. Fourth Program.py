#check the equality of 2 series

import pandas as pd


Series1 = pd.Series([1, 2, 3, 4])
Series2 = pd.Series([1, 2, 3, 4])


equal = Series1.equals(Series2)


print("\nare they equal?", equal)

#Split a string column into multiple columns

data = {'Name': ['Sathiya Sugumaran Subramanian', 'Aadishwar Ramesh', 'Sudha Ramesh']}
df = pd.DataFrame(data)

df[['First Name', 'Middle Name', 'Last Name']] = df['Name'].str.split(expand=True)


print(df)

#renaming columns names
df = df.rename(columns={'Name': 'Full Name', 'Last Name': 'Name Last'})

print(df)
