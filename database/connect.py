import psycopg2 

def connection_db():
    conn = psycopg2.connect(
        database="the_bear",
        user="maria",
        password="maria2003",
        host="localhost",
        port="5432"
    )
    return conn