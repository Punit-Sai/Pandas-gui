import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 35, 28],
    'Marks': [85, 90, 78, 88, 92]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
sorted_df = df.sort_values(by='Age')
print("\nSorted by Age (Ascending):")
print(sorted_df)
print("\nFirst 3 rows:")
print(df[:3])
print("\nSlicing using loc:")
print(df.loc[1:3, ['Name', 'Marks']])

print("\nSlicing using iloc:")
print(df.iloc[0:3, [0, 2]])