import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Alice'],
    'Score': [85, 95, 70, 90, 92],
    'Age': [25, 30, 25, 22, 30]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
