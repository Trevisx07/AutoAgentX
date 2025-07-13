import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from app.logging_utils.logger import log_task
import time
# Load environment variables
load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Prompt template for summarization
summary_prompt = PromptTemplate(
    input_variables=["text", "docx"],
    template="""
You are an intelligent assistant. Summarize the following text clearly and concisely:

{text}

Summary:
"""
)

def summarize_text(text: str) -> str:
    try:
        start = time.time()
        prompt = summary_prompt.format(text=text)
        response = llm.invoke(prompt)
        summary = response.content.strip()
        exec_time = time.time() - start
        log_task("summarize", text, summary, exec_time)
        return summary
    except Exception as e:
        return f"Error during summarization: {str(e)}"

