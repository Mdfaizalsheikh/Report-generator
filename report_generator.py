import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


conn = sqlite3.connect('sales.db')

# Read data from the database into a DataFrame
df = pd.read_sql_query("SELECT * FROM sales", conn)
file

conn.close()


summary = df.groupby('product')['amount'].agg(['sum', 'mean', 'count'])
summary.columns = ['Total Sales', 'Average Sale', 'Number of Sales']
print("Summary Report")
print(summary)


summary.to_csv('summary_report.csv')


df['date'] = pd.to_datetime(df['date'])
sales_over_time = df.groupby(df['date'].dt.to_period('M')).sum()


plt.figure(figsize=(10, 6))
sales_over_time['amount'].plot(kind='bar')
plt.title('Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.savefig('sales_over_time.png')
plt.show()

print("Reports generated successfully: 'summary_report.csv' and 'sales_over_time.png'")
