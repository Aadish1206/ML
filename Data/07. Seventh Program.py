#Memory usage - Referred From CHATGPT
import pandas as pd

data = {
    'A': range(1, 100001),
    'B': range(100001, 200001),
    'C': ['text'] * 100000
}

df = pd.DataFrame(data)

print("Initial Memory Usage:")
df.info(memory_usage='deep')

df['A'] = df['A'].astype('int32')
df['B'] = df['B'].astype('int32')
df['C'] = df['C'].astype('category')

print("\nReduced Memory Usage:")
df.info(memory_usage='deep')
