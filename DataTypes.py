import pandas as pd

df = pd.read_csv('data_types.csv')
print(df.dtypes)
df['treatment b'] = df['treatment b'].astype(str)
df['sex'] = df['sex'].astype('category')
print(df.dtypes)

df['treatment a'] = pd.to_numeric(df['treatment a'], errors='coerce')
print(df.dtypes)
print(df['treatment a'])
