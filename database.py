import os 
import sys
import psycopg2

class Database:
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        """
        Connect to database and return connection
        """
        print("Connecting to PostgreSQL Database...")

        try:
            conn = psycopg2.connect(
                host = os.getenv("HOST"),
                dbname = os.getenv("DATABASE"),
                user = os.getenv("USER"),
                password = os.getenv("PASSWORD"),
                port = os.getenv("PORT")
            )
        except psycopg2.OperationalError as e:
            print(f"Could not connect to Database: {e}")
            sys.exit(1)

        return conn

    def get_table(self, table_name):
        """ Retrieves all rows from a table """
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {table_name}")
                data = cur.fetchall()
                return data

    #############################################################

    def insert_us_state(self, state_name):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO us_state (state_name) 
                    VALUES (%s)
                    """,
                    (state_name,))
                conn.commit()

    def delete_us_state(self, state_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM us_state 
                    WHERE state_id = %s
                    """,
                    (state_id,))
                conn.commit()

    #############################################################

    def insert_genre(self, genre_name):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO genre (genre_name) 
                    VALUES (%s)
                    """,
                    (genre_name,))
                conn.commit()

    def update_genre(self, genre_id, genre_name):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE genre SET genre_name = %s 
                    WHERE genre_id = %s
                    """,
                    (genre_name, genre_id))
                conn.commit()

    def delete_genre(self, genre_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM genre 
                    WHERE genre_id = %s
                    """,
                    (genre_id,))
                conn.commit()

    #############################################################

    def create_user(self, f_name, l_name, email, state_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO app_user (f_name, l_name, email, state_id) 
                    VALUES (%s, %s, %s, %s)
                    """,
                    (f_name, l_name, email, state_id))
                conn.commit()

    def update_user(self, user_id, f_name, l_name, email, state_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE app_user SET f_name = %s, l_name = %s, email = %s, state_id = %s 
                    WHERE app_user_id = %s
                    """,
                    (f_name, l_name, email, state_id, user_id))
                conn.commit()

    def delete_user(self, user_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM app_user 
                    WHERE app_user_id = %s
                    """,
                    (user_id,))
                conn.commit()

    #############################################################

    def create_festival(self, festival_name, price, state_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO festival (festival_name, price, state_id) 
                    VALUES (%s, %s, %s)
                    """,
                    (festival_name, price, state_id))
                conn.commit()

    def update_festival(self, festival_id, festival_name, price, state_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE festival SET 
                    festival_name = %s, price = %s, state_id =%s 
                    WHERE festival_id = %s
                    """,
                    (festival_name, price, state_id, festival_id))
                conn.commit()

    def delete_festival(self, festival_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM festival 
                    WHERE festival_id = %s
                    """,
                    (festival_id,))
                conn.commit()

    #############################################################

    def create_artist(self, artist_name, genre_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO artist (artist_name, genre_id) 
                    VALUES (%s, %s)
                    """,
                    (artist_name, genre_id))
                conn.commit()

    def update_artist(self, artist_id, artist_name, genre_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE artist SET 
                    artist_name = %s, genre_id = %s
                    WHERE festival_id = %s
                    """,
                    (artist_id, artist_name, genre_id))
                conn.commit()

    def delete_artist(self, artist_id):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM artist 
                    WHERE artist_id = %s
                    """,
                    (artist_id,))
                conn.commit()

    #############################################################

    def create_favorite_artist(self, user_id, artist_id, score):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO favorite_artist (app_user_id, artist_id, score)
                    VALUES (%s, %s, %s)
                    """,
                    (user_id, artist_id, score))
                conn.commit()

    def create_favorite_artist(self, user_id, artist_id, score):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO favorite_artist (app_user_id, artist_id, score)
                    VALUES (%s, %s, %s)
                    """,
                    (user_id, artist_id, score))
                conn.commit()

    def close_connection(self):
        """
        Close the connection
        """
        self.conn.close()
        print("DB Connection closed")

