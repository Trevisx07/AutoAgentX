import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from app.logging_utils.logger import log_task
import time
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

qa_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a smart assistant. Based on the following document, answer the user's question as accurately as possible.

Document:
{context}

Question:
{question}

Answer:
"""
)

def answer_question(context: str, question: str) -> str:
    try:
        start = time.time()
        prompt = qa_prompt.format(context=context, question=question)
        response = llm.invoke(prompt)
        answer = response.content.strip()
        exec_time = time.time() - start
        log_task("qna", question, answer, exec_time)
        return answer
    except Exception as e:
        return f"Error during question answering: {str(e)}"