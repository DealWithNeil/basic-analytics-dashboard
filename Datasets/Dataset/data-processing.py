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
df['SALES_NORMALIZED'] = (df['SALES'] - df['SALES'].mean()) / df['SALES'].std()

Q1 = df['SALES'].quantile(0.25)
Q3 = df['SALES'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['SALES'] >= Q1 - 1.5*IQR) & (df['SALES'] <= Q3 + 1.5*IQR)]

df['REVENUE_PER_ITEM'] = df['SALES'] / df['QUANTITYORDERED']

df.to_csv(r"C:\Users\Maranello Nacionales\analytics-dashboard\basic-analytics-dashboard\processed_sales_data.csv", index=False)