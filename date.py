import pandas as pd
start_date = '2024-11-20'
end_date = '2024-11-24'
date_series = pd.date_range(start=start_date, end=end_date)
print("Formatted Date Series:")
for date in date_series:
    print(date.strftime('%d-%b-%Y'))