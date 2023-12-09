from fastapi import FastAPI, UploadFile, File, Form
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from transcriber import transcribe
app=FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/yuh")
# def post_yuh(input: args):
def post_yuh(name: Annotated[str, Form()], lines: Annotated[int, Form()], file: Annotated[UploadFile, Form()]):
    # transcribe(name, lines, file)
    return FileResponse(transcribe(name, lines, file))

@app.get("/healthcheck")
def read_root():
    return {"status": "ok"}
