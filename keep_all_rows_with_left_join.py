import sqlite3

def keep_all_rows_with_left_join():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #9
    query = "SELECT p.name, s.supplier_name FROM products p LEFT JOIN suppliers s ON p.supplier_id = s.supplier_id"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    keep_all_rows_with_left_join()