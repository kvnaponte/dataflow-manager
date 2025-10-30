import sqlite3

# Conexión básica a la base de datos local
def get_connection():
    conn = sqlite3.connect("dataflow.db")
    return conn

# Crear tabla si no existe
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL,
        area TEXT NOT NULL,
        salary REAL NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()
