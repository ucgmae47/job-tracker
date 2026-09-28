from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Job Tracker API"}

@app.get("/applications")
def applications():
    return [
        {
            "id": "12345",
            "company": "Raytheon",
            "role": "Software Engineer 1",
            "status": "Pending",
            "date_applied": "09-05-2026"
        },
        {
            "id": "12345",
            "company": "Raytheon",
            "role": "Software Engineer 1",
            "status": "Pending",
            "date_applied": "09-05-2026"
        },
        {
            "id": "12345",
            "company": "Raytheon",
            "role": "Software Engineer 1",
            "status": "Pending",
            "date_applied": "09-05-2026"
        }
    ]
        

