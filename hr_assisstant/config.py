## All settings for the HR assistant app live are defined in this file.

import os
from dotenv import load_dotenv

load_dotenv()

# Env variables loading
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
JINA_API_KEY = os.getenv('JINA_API_KEY')


## paths
DATA_FILE_PATH = os.path.join("data", "hr_text.txt")

# Vector store path
VECTOR_STORE_PATH = os.path.join("data", "faiss_index")

LLM_MODEL_NAME = "openai/gpt-oss-120b"

EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"

## CHUNK / TEXT SPLITTING CONFIG
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# RETRIEVAL RESULTS
TOP_K_RESULTS = 3


## SYSTEM INSTRUCTIONS
SYSTEM_PROMPT = ("""
You are a friendly HR assistant. Always use the search_hr_policy tool to look
facts before answering any questions. If you cannot find the answer in the HR policy documents, 
politely inform the user that you do not have the information and suggest they contact the 
HR department for further assistance.
"""
)


## If the API keys are not there there is no meaning of running the code

def check_api_keys() -> None:
    """ Stop early with a clear message if a requered API key is missing. """
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY environment variable. Please set it in your .env file.")
    if not JINA_API_KEY:
        raise ValueError("Missing JINA_API_KEY environment variable. Please set it in your .env file.") 



