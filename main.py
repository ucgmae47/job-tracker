from fastapi import FastAPI
import psycopg

app = FastAPI()
conn_string = "postgresql://jobtracker:devpassword@localhost:5432/jobtracker"

@app.get("/")
def root():
    return {"message": "Job Tracker API"}

@app.get("/applications")
def applications():
    with psycopg.connect(conn_string) as conn:
        with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
            cur.execute("SELECT id, company, role, status, date_applied FROM applications")
            return cur.fetchall()
