import pandas as pd

df = pd.read_csv(r"C:\Users\Maranello Nacionales\analytics-dashboard\basic-analytics-dashboard\sales_data_sample.csv", encoding='latin-1')
df.head()

print(df.info())
print(df.isnull().sum())

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

df['ADDRESSLINE2'] = df['ADDRESSLINE2'].fillna("N/A")

df['STATE'] = df['STATE'].fillna("Unknown")

df['TERRITORY'] = df['TERRITORY'].fillna("Unknown")

df['POSTALCODE'] = df['POSTALCODE'].fillna("00000")