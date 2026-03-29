import pandas as pd

df = pd.read_csv('data.csv')
print("First 5 rows of the DataFrame:")
print(df.head())
print("\nLast 5 rows of the DataFrame:")
print(df.tail())
print("\nDataFrame Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())