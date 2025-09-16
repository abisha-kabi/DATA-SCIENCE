import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 92, 78, 90]
}
df = pd.DataFrame(data)
first_two_rows = df.head(2)
print("First 2 Rows of the DataFrame:\n")
print(first_two_rows)
