import os
import psycopg2

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def clear_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE data")
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    clear_db()
