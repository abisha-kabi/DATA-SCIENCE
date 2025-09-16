import pandas as pd
data = {
    'ID': [101, 102, 103],
    'Name': ['Ali', 'Pythu', 'Charls'],
    'Score': [85, 90, 78]
}
df = pd.DataFrame(data)
print("Converted DataFrame:")
print(df)
