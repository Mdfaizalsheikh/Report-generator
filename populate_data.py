import sqlite3
import random
from datetime import datetime, timedelta


conn = sqlite3.connect('sales.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS sales
             (id INTEGER PRIMARY KEY, date TEXT, product TEXT, amount REAL)''')
conn.commit()


products = ['Product A', 'Product B', 'Product C']
start_date = datetime(2023, 1, 1)

for _ in range(100):
    date = start_date + timedelta(days=random.randint(0, 365))
    product = random.choice(products)
    amount = round(random.uniform(10, 1000), 2)
    c.execute("INSERT INTO sales (date, product, amount) VALUES (?, ?, ?)",
              (date.strftime('%Y-%m-%d'), product, amount))
    conn.commit()

conn.close()
