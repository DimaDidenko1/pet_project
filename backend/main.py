from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_db():
    return psycopg2.connect(
        host="db",
        database="appdb",
        user="app",
        password="app"
    )

@app.get("/api/todos")
def get_todos():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT id, text FROM todos;")
    rows = cur.fetchall()

    return [{"id": r[0], "text": r[1]} for r in rows]