import sqlite3
import pandas as pd

conn = sqlite3.connect('webshop.db')

# 1. Report: Vásárlói rangsor (legértékesebb vásárló)
customer_report_query = """ CREATE TABLE IF NOT EXISTS gold_customer_metrics AS 
                            SELECT customer_id, COUNT(transaction_id) as total_orders, SUM(amount) as total_spent, ROUND(AVG(amount), 2) as avg_order_value
                            FROM silver_transactions
                            GROUP BY customer_id
                            ORDER BY total_spent DESC; """
                            
                            
# 2. Report: Termék analitika (melyik termék a legkeresettebb)
product_report_query = """CREATE TABLE IF NOT EXISTS gold_product_metrics AS
                            SELECT product_id, COUNT(*) as sales_count, SUM(amount) as total_revenue
                            FROM silver_transactions
                            GROUP BY product_id
                            ORDER BY sales_count DESC; """
                            
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS gold_customer_metrics")
cursor.execute("DROP TABLE IF EXISTS gold_product_metrics")
cursor.execute(customer_report_query)
cursor.execute(product_report_query)

print("Gold Layer reportok elkészültek.")

print("Legjobb vásárlók:")
print(pd.read_sql("SELECT * FROM gold_customer_metrics", conn))

conn.close()