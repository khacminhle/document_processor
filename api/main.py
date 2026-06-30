import datetime
from fastapi import FastAPI, File, UploadFile
from src.services.ingestion import process_document
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health-check")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    }


@app.post("/upload-document")
async def upload_document_file(file: UploadFile = File(...)):
    
    processed_document_chunks = await process_document(file)
   
    return JSONResponse(content=processed_document_chunks)
