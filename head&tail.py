from cgi import print_form

import pandas as pd
data = {
    'ID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Score': [85, 90, 78, 88, 76, 92, 80]
}
df = pd.DataFrame(data)
print("Head of data:")
print(df.head())
print("\nTail of data:")
print(df.tail())