import sqlite3
import pandas as pd

conn = sqlite3.connect('webshop.db')

# Coalesce -> hiányzó adat pótlás
clean_query = """ CREATE TABLE IF NOT EXISTS silver_transactions AS 
                    SELECT DISTINCT transaction_id, customer_id, product_id, amount, COALESCE(order_date, '1900-01-01') as order_date
                    FROM bronze_transactions
                    WHERE status != 'cancelled';
"""

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS silver_transactions")
cursor.execute(clean_query)

print("A 'silver_transactions' tábla elkészült!")
conn.close()