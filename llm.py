from langchain_ollama import ChatOllama

def get_llm():
    return ChatOllama(
        model="llama3.2:3b",
        base_url="http://localhost:11434",
        temperature=0
    )
