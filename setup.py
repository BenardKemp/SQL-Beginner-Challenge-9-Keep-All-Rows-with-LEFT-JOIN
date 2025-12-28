import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, " \
"name TEXT, " \
"category TEXT, " \
"price NUMBER, " \
"supplier_id INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS suppliers (supplier_id INTEGER PRIMARY KEY, " \
"supplier_name TEXT)")

cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_id) " \
" VALUES (101, 'Wireless Mouse', 'Accessories', 24.99, 1)")
cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_id) " \
" VALUES (102, 'Mechanical Keyboard', 'Accessories', 89.00, 1)")
cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_id) " \
" VALUES (103, '27-inch Monitor', 'Displays', 299.99, 2)")
cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_id) " \
" VALUES (104, 'USB-C Hub', 'Accessories', 34.50, NULL)")
cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_id) " \
" VALUES (105, 'Laptop Stand', 'Workspace', 39.90, 2)")

cursor.execute("INSERT INTO suppliers (supplier_id, supplier_name) " \
" VALUES (1, 'TechSource')")
cursor.execute("INSERT INTO suppliers (supplier_id, supplier_name) " \
" VALUES (2, 'DisplayWorks')")
cursor.execute("INSERT INTO suppliers (supplier_id, supplier_name) " \
" VALUES (3, 'GadgetCo')")
conn.commit()
conn.close()