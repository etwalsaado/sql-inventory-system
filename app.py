import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# جلب كل البيانات
cursor.execute("SELECT * FROM products")
all_rows = cursor.fetchall()

# فلترة
cursor.execute("SELECT * FROM products WHERE status = 'Success'")
success_rows = cursor.fetchall()

cursor.execute("SELECT * FROM products WHERE status = 'Failed'")
failed_rows = cursor.fetchall()

# حساب الإحصائيات
total = len(all_rows)
success_count = len(success_rows)
failed_count = len(failed_rows)

success_rate = (success_count / total) * 100

# عرض النتائج
print("\n--- Manufacturing KPIs ---")
print(f"Total Products: {total}")
print(f"Successful: {success_count}")
print(f"Failed: {failed_count}")
print(f"Success Rate: {success_rate:.2f}%")

conn.close()