import psycpg2

def connection_db():
    conn = psycopg2.connect(
        database="the bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )

    return conn

conn = connection_db()