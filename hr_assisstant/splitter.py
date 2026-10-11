### Step 2: Stop the document into small, searchable chunks.

from langchain_text_splitters import RecursiveCharacterTextSplitter

from hr_assisstant import config

def split_into_chunks(documents):
    """
    Split the document into small overlapping chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = config.CHUNK_SIZE,
        chunk_overlap = config.CHUNK_OVERLAP
        )
    return text_splitter.split_documents(documents)

