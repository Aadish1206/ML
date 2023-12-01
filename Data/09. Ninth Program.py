import pandas as pd

from sklearn.metrics import mean_absolute_error

data = {
    'Actual': [15, 22, 18, 25, 30, 28, 20, 24, 35, 18],
    'Predicted': [14, 20, 18, 28, 32, 26, 22, 23, 34, 20]
}

df = pd.DataFrame(data)

actual_values = df['Actual']
predicted_values = df['Predicted']

mae = mean_absolute_error(actual_values, predicted_values)

print(f"Mean Absolute Error (MAE): {mae}")
