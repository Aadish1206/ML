#New aggregation function -last ()
import pandas as pd

data = {
    'name': ['Aadishwar', 'Sudha', 'Ramesh'],
    'City': ['Bangalore', 'Pondichherry', 'Chennai'],
    'Age': [21, 40, 49],
    'height': [169, 156, 170],
    'student': [True, False, False],
    'grades': [95.5, 88.0, 92.5]
}

df = pd.DataFrame(data)

def last(series):
    return series.iloc[-1]

last_age = df['Age'].agg(last)

last_row = df.agg({col: last for col in df.columns})

print("Last Age:", last_age)
print("\nLast Row:")
print(last_row)
