import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Task 2

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")  
    cursor = conn.cursor()
    cursor.execute ("""
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o 
    JOIN line_items li ON o.order_id = li.order_id 
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id 
    LIMIT 5;
    """)
    print("Tables joined successfully.")
    results = cursor.fetchall()
    print("Task 2: ")
    for order_id, total_price in results:
        print(f"Order ID: {order_id}, Total Price: {total_price:.2f}")
    
    df = pd.DataFrame(results, columns=["order_id", "total_price"])

    # option 1
    def cumulative(row):
        totals_above = df['total_price'][0:row.name+1]
        return totals_above.sum()

    df['cumulative'] = df.apply(cumulative, axis=1)

    # option 2
    # df['cumulative'] = df['total_price'].cumsum()

    plt.figure(figsize=(10, 6))
    plt.plot(df["order_id"], df['cumulative'], color = "green", marker='o')
    plt.title("Cumulative Revenue by Order")
    plt.ylabel("Cumulative Revenue ($)")
    plt.xlabel("order_id")
    plt.tight_layout()
    plt.grid(True)
    plt.show()