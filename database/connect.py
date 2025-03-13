import psycopg2

def connection_db():
    conn = psycopg2.connect(
        database="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
        )

    return conn

#connect = connection_db()
#print(connect)
#connect.close()
#print(connect)

