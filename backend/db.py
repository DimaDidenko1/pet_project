import psycopg2

conn = psycopg2.connect(
    host="db",
    database="appdb",
    user="app"
    password="appdb")

def get_conn():
    return conn
