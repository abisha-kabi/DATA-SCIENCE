import pandas as pd
import numpy as np
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, np.nan, 78, np.nan],
    'Age': [25, 30, np.nan, 22]
}
df = pd.DataFrame(data)
print("Original DataFrame with NaN values:\n")
print(df)
df_filled = df.fillna(0)
print("\nDataFrame after filling NaN values with 0:\n")
print(df_filled)
