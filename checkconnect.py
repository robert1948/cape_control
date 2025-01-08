import psycopg2

try:
    conn = psycopg2.connect(
        dbname="cape_control",
        user="robert",
        password="stinkie",
        host="localhost",
        port="5432"
    )
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")
finally:
    if conn:
        conn.close()
