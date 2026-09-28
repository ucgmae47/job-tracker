from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Job Tracker API"}

@app.get("/applications")
def applications():
    return [
        {
            "id": 1,
            "company": "Raytheon",
            "role": "Software Engineer 1",
            "status": "offer",
            "date_applied": "2026-09-05"
        },
        {
            "id": 2,
            "company": "JPMorgan",
            "role": "Data Scientist",
            "status": "interviewing",
            "date_applied": "2026-09-14"
        },
        {
            "id": 3,
            "company": "Fetch Freight",
            "role": "AI Solutions Engineer",
            "status": "rejected",
            "date_applied": "2026-09-01"
        }
    ]
