from fastapi import FastAPI
import psycopg
from psycopg.rows import dict_row
from pydantic import BaseModel
from datetime import date

app = FastAPI()
conn_string = "postgresql://jobtracker:devpassword@localhost:5432/jobtracker"

class ApplicationCreate(BaseModel):
    company: str
    role: str
    status: str
    date_applied: date

@app.get("/")
def root():
    return {"message": "Job Tracker API"}

@app.get("/applications")
def applications():
    with psycopg.connect(conn_string) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT id, company, role, status, date_applied FROM applications;")
            return cur.fetchall()

@app.post("/applications", status_code=201)
def applications(app: ApplicationCreate):
    with psycopg.connect(conn_string) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("""
            INSERT INTO applications (company, role, status, date_applied)
            VALUES (%s, %s, %s, %s) RETURNING id, company, role, status, date_applied;
            """,
            (app.company, app.role, app.status, app.date_applied))
            return cur.fetchall()
