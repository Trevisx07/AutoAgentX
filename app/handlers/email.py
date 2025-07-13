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

email_prompt = PromptTemplate(
    input_variables=["context", "instruction"],
    template="""
You are an assistant that writes professional and clear emails.

Instruction:
{instruction}

Based on this context:
{context}

Write the email:
"""
)
def generate_email(context: str, instruction: str) -> str:
    try:
        start = time.time()
        prompt = email_prompt.format(context=context, instruction=instruction)
        response = llm.invoke(prompt)
        email = response.content.strip()
        exec_time = time.time() - start
        log_task("email-draft", instruction, email, exec_time)
        return email
    except Exception as e:
        return f"Error generating email: {str(e)}"
