import pandas as pd
with open("sample.csv", "w") as file:
    file.write("name,mark\n")
    file.write("a,1\n")
    file.write("b,2\n")
    file.write("c,3\n")
df = pd.read_csv("sample.csv")
print("DataFrame from CSV file:")
print(df)
