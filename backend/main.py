from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


class Todo(BaseModel):
    text: str

def get_db():
    return psycopg2.connect(
        host="db",
        database="appdb",
        user="app",
        password="app"
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # для dev ок
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/todos")
def get_todos():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT id, text FROM todos;")
    rows = cur.fetchall()

    return [Todo(id=r[0], text=r[1]) for r in rows]

@app.post("/api/todos")
def create_todo(todo: Todo):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO todos (text) VALUES (%s) RETURNING id;",
        (todo.text,)
    )

    todo_id = cur.fetchone()[0]
    conn.commit()

    return {"id": todo_id, "text": todo.text}

@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: int):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM todos WHERE id = %s;", (todo_id,))
    conn.commit()

    return {"status": "deleted"}