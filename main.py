import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('webshop.db')

# Adat lekérés a Gold táblából
df = pd.read_sql("SELECT customer_id, total_spent FROM gold_customer_metrics", conn)

# Grafikon
plt.figure(figsize=(10, 6))
plt.bar(df['customer_id'].astype(str), df['total_spent'], color='skyblue', edgecolor='navy')

# Design
plt.title('Vásárlói Élettartam Érték', fontsize = 14)
plt.xlabel('Vásárló ID', fontsize=12)
plt.ylabel('Elköltött összeg (HUF)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('customer_revenue.png')
print("A grafikon 'customer_revenue.png' elmentve")
plt.show()

conn.close()