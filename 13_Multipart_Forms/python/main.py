from fastapi import FastAPI, Form, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil
import time
import random

app = FastAPI()

# Serve static files (including index.html) from the parent directory
app.mount("/static", StaticFiles(directory="..", html=True), name="static")

UPLOAD_DIR = "./uploads"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Allowed file types
VALID_FILE_TYPES = ["image/png", "image/svg", "image/jpeg"]

# Maximum file size (20MB)
MAX_FILE_SIZE = 20 * 1024 * 1024


@app.post("/form")
def handle_form(username: str = Form(...), password: str = Form(...)):
    # Log the form data (excluding the password)
    print({"username": username})
    return {"username": username}  # Never return the password


@app.post("/fileform")
async def file_form(file: UploadFile = File(...), description: str = Form(...)):
    # Validate file type
    if file.content_type not in VALID_FILE_TYPES:
        raise HTTPException(status_code=400, detail=f"File type '{file.content_type}' not allowed")

    # Validate file size
    file_size = 0
    file.file.seek(0, os.SEEK_END)  # Move to the end of the file to get its size
    file_size = file.file.tell()
    file.file.seek(0)  # Reset the file pointer to the beginning
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds 20MB")

    # Generate a unique filename
    unique_prefix = f"{int(time.time())}-{random.randint(1, 1_000_000_000)}"
    unique_filename = f"{unique_prefix}__{file.filename}"

    # Save the file to the uploads directory
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Log the file upload
    print({"description": description, "filename": unique_filename})

    return {
        "filename": unique_filename,
        "content_type": file.content_type,
        "description": description,
        "file_path": file_path,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)