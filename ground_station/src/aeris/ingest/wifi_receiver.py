from pathlib import Path
from fastapi import FastAPI, UploadFile, File
import uvicorn

from aeris.config import settings

app = FastAPI(title="Aeris Ingest")


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)
    dest = upload_dir / file.filename
    content = await file.read()
    dest.write_bytes(content)
    return {"status": "ok", "filename": file.filename, "size": len(content)}


def start_receiver():
    uvicorn.run(app, host=settings.ingest_host, port=settings.ingest_port)
