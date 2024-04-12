# Pandas: Select first N columns of DataFrame

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'experience': [1, 1, 5, 7, 7],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
})

print(df)

print('-' * 50)

first_2_columns = df.iloc[:, :2]
print(first_2_columns)