from langchain_ollama import OllamaEmbeddings

def get_embedding():
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    return embeddings

