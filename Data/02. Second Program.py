#comb = 2019350 , if one digit thhen value should be 2003001, combine the data thhen 4th column change into to Date, time format: only pandas and pandas built in function.
import pyspark

import pandas as pd

d = {
    "year": [2020, 2021, 2003, 2008],
    "dayofyear": [350, 365, 1, 100]
}


df = pd.DataFrame(d)

df['joined'] = df['year'].astype(str) + df['dayofyear'].astype(str)


df['joined'] = pd.to_datetime(df['joined'], format='%Y%j')


print(df)
