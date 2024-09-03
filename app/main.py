from fastapi import FastAPI, File, UploadFile
from typing_extensions import Annotated

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    """example 1 with request files"""
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """example 2 with request files"""
    return {"filename": file.filename}
