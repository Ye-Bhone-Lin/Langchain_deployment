from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
import uvicorn
from langserve import add_routes
from dotenv import load_dotenv 

load_dotenv()

model = init_chat_model(model_name='groq:llama-3.3-70b-versatile')

prompt1 = ChatPromptTemplate.from_template("Write a code {topic} with Python")
prompt2 = ChatPromptTemplate.from_template("Research {topic} in latest news.")


app = FastAPI(
    title="Langchain LLM API",
    version="1.0",
    description="A Multi-LLM API with Langchain"
)

add_routes(app, prompt1 | model, path = "/coding")
add_routes(app, prompt2 | model, path = '/research')

if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port=8000)

