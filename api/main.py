from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/health-check")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    }

