import pandas as pd

data = {
    'Location': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Date': pd.to_datetime(['2023-01-15', '2023-01-15', '2023-02-20', '2023-02-20', '2023-03-10', '2023-03-10', '2023-04-05', '2023-04-05']),
    'Transaction Value': [100, 150, 120, 200, 180, 220, 130, 170]
}

df = pd.DataFrame(data)

df['Quarter'] = df['Date'].dt.to_period('Q')

pivot_table = pd.pivot_table(df, values='Transaction Value', index=['Location', 'Date'], columns='Quarter', aggfunc='sum', fill_value=0)

print(pivot_table)
