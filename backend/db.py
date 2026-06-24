import psycopg2

conn = psycopg2.connect(
    host="db",
    database="appdb",
    user="admin"
    password="password")

def get_conn():
    return conn
