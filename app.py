
import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Calculate manufacturing KPIs
cursor.execute("""
    SELECT
        COUNT(*),
        SUM(CASE WHEN status = 'Success' THEN 1 ELSE 0 END),
        SUM(CASE WHEN status = 'Failed' THEN 1 ELSE 0 END)
    FROM products
""")

total, successful, failed = cursor.fetchone()

successful = successful or 0
failed = failed or 0
success_rate = successful / total * 100 if total else 0

print("\n--- Manufacturing KPIs ---")
print(f"Total Products: {total}")
print(f"Successful: {successful}")
print(f"Failed: {failed}")
print(f"Success Rate: {success_rate:.2f}%")

# Join products with their machines
cursor.execute("""
    SELECT products.name, machines.machine_name
    FROM products
    JOIN machines
        ON products.machine_id = machines.id
""")

print("\n--- Products and Machines ---")
for product_name, machine_name in cursor.fetchall():
    print(f"{product_name} - {machine_name}")

conn.close()
