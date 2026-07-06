import datetime
from fastapi import FastAPI, File, UploadFile, HTTPException
from services.chunking import chunking_document
from fastapi.responses import JSONResponse
from app_logging import configure_logging 

configure_logging()

app = FastAPI()

@app.get("/health-check")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    }


@app.post("/upload-document")
async def upload_document_file(file: UploadFile = File(...)):
    
    try:
        processed_document_chunks = await chunking_document(file)
        return JSONResponse(content=processed_document_chunks)

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


    
