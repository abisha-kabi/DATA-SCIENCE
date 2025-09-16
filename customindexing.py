import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 92, 78, 90]
}
custom_index = ['A1', 'B2', 'C3', 'D4']
df_custom = pd.DataFrame(data, index=custom_index)
print("📌 DataFrame with Custom Index:\n")
print(df_custom)
df_default = df_custom.reset_index(drop=True)
print("\n✅ DataFrame with Default Index:\n")
print(df_default)