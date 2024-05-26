from fastapi import APIRouter, UploadFile, File, HTTPException
from app.data.database import save_document
from app.utils.search_engine import add_document

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "text/plain":
        raise HTTPException(status_code=400, detail="Only text files are allowed")
    
    content = await file.read()
    text = content.decode("utf-8")
    save_document(file.filename, text)
    add_document(text, file.filename)
    
    return {"filename": file.filename, "status": "uploaded"}
