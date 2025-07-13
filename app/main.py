from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

# Load env vars
load_dotenv()

# Import handlers
from app.handlers.summarize import summarize_text
from app.handlers.qna import answer_question
from app.handlers.email import generate_email

app = FastAPI(title="AutoAgentX")

@app.get("/")
def root():
    return {"message": "Welcome to AutoAgentX - Smart AI Agent"}

@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    contents = await file.read()
    text = contents.decode("utf-8")
    summary = summarize_text(text)
    return JSONResponse(content={"summary": summary})

@app.post("/ask")
async def ask_question(
    file: UploadFile = File(...),
    question: str = Form(...)
):
    contents = await file.read()
    text = contents.decode("utf-8")
    answer = answer_question(text, question)
    return JSONResponse(content={"answer": answer})

@app.post("/email-draft")
async def draft_email(
    context: str = Form(...),
    instruction: str = Form(...)
):
    email = generate_email(context, instruction)
    return JSONResponse(content={"email": email})
