import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect('webshop.db')

# Saját adatok létrehozása (szándékos hibákkal)
data = {
    'transaction_id': range(1, 11),
    'customer_id': [101, 102, 101, 103, 104, 102, 105, 101, 106, 104],
    'product_id': [1, 2, 1, 3, 2, 1, 4, 3, 2, 1],
    'amount': [150.5, 200.0, 150.5, 50.0, 200.0, 150.5, 300.0, 50.0, 200.0, 150.5],
    'order_date': ['2023-01-10', '2023-01-11', '2023-01-10', '2023-01-12', '2023-01-13', '2023-01-11', None, '2023-01-15', '2023-01-16', '2023-01-13'],
    'status': ['delivered', 'delivered', 'delivered', 'shipped', 'delivered', 'delivered', 'cancelled', 'delivered', 'delivered', 'delivered']
}

df = pd.DataFrame(data)

df.to_sql('bronze_transactions', conn, if_exists='replace', index=False)

print("Az adatbázis elkészült, 'bronze_transactions' elkészült.")
conn.close()