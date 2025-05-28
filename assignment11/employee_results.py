import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Task 1

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")  
    cursor = conn.cursor()
    cursor.execute ("""
    SELECT last_name, 
    SUM(price * quantity) AS revenue 
    FROM employees e 
    JOIN orders o ON e.employee_id = o.employee_id 
    JOIN line_items l ON o.order_id = l.order_id 
    JOIN products p ON l.product_id = p.product_id 
    GROUP BY e.employee_id;
    """)

    print("Tables joined successfully.")
    results = cursor.fetchall()
    print("Task 1: ")

    for employee_id, revenue in results:
        print(f"Employee ID: {employee_id}, Revenue: {revenue:.2f}")
    
    df = pd.DataFrame(results, columns=["last_name", "revenue"])
    plt.figure(figsize=(10, 6))
    plt.bar(df["last_name"], df["revenue"], color = "skyblue")
    plt.title("Employees revenue results")
    plt.xlabel("Employee name")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    