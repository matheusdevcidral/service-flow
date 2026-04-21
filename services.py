from database import connect

def create_customer(name, service, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (name, service, price) VALUES (?, ?, ?)",
        (name, service, price)
    )
    conn.commit()
    conn.close()


def get_all_customers():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    data = cursor.fetchall()
    conn.close()
    return data


def delete_customer_by_id(customer_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


def update_customer(customer_id, name, service, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE customers
    SET name = ?, service = ?, price = ?
    WHERE id = ?
    """, (name, service, price, customer_id))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


def search_customer(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM customers WHERE name LIKE ?",
        (f"%{name}%",)
    )
    data = cursor.fetchall()
    conn.close()
    return data


def get_total_revenue():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(price) FROM customers")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0
