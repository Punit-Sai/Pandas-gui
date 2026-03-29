import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None],
    'Marks': [85, None, 90]
})

df['Name'] = df['Name'].fillna('Unknown')
df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce')
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
df['Result'] = ['Pass' if m >= 40 else 'Fail' for m in df['Marks']]
print(df)