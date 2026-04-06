from fastapi import FastAPI

app = FastAPI()

# Get list of jobs route 
@app.get("/jobs")
def get_jobs():
    return {"jobs": []}


# Status updating route
@app.get("/status")
def update_status():
    return {"status": "updated"}


# Trigger for scraper
@app.get("/run-scrapper")
def run_scrapper():
    return {"message": "Scrapper triggered"}

