import psycopg2
import os
import sys

print("password: ", os.getenv("POSTGRES_PASSWORD"))
try:
    conn = psycopg2.connect(
        host = os.getenv("POSTGRES_HOST"),
        dbname = os.getenv("POSTGRES_DB"),
        user = os.getenv("POSTGRES_USER"),
        password = os.getenv("POSTGRES_PASSWORD"),
        port = os.getenv("POSTGRES_PORT")
            )
except psycopg2.OperationalError as e:
    print(f"Could not connect to Database: {e}")
    sys.exit(1)

with conn:
    conn.set_session(autocommit=True)
    with conn.cursor() as cur:
        cur.execute(open("db_setup.sql", "r").read())

with conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT * FROM genre
        """)

        print(cur.fetchall())
        
        conn.commit()

        