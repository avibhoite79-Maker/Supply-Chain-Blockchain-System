import sqlite3
def create_table():
    conn = sqlite3.connect("supplychain.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS supplychain(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id TEXT,
        stage TEXT,
        owner TEXT,
        location TEXT,
        hash TEXT
    )
    """)
    conn.commit()
    conn.close()
def insert_data(product_id, stage, owner, location, hash_value):
    conn = sqlite3.connect("supplychain.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO supplychain
    (product_id, stage, owner, location, hash)
    VALUES (?, ?, ?, ?, ?)
    """,
    (product_id, stage, owner, location, hash_value))
    conn.commit()
    conn.close()