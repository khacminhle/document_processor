import datetime
from fastapi import FastAPI, File, UploadFile
from src.doc_processor.loader import load_document
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
    
    processed_document = await process_document(file)
    print("--------")
    print(processed_document)
    print("--------")
    return JSONResponse(content=processed_document)
