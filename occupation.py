import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Occupation': ['Engineer', 'Doctor', 'Engineer', 'Artist', 'Doctor', 'Artist'],
    'Salary': [70000, 120000, 80000, 50000, 110000, 55000]
}
df = pd.DataFrame(data)
avg_salary = df.groupby('Occupation')['Salary'].mean().reset_index()
# avg_salary.columns = ['Occupationolumns for clar', 'Average_Salary']
print("Average Salary per Occupation:\n")
print(avg_salary)


