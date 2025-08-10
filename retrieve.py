from typing import List
from langchain.docstore.document import Document
from embed_store import EmbedStore

def retrieve_top_chunks(store: EmbedStore, query: str, k: int = 5) -> List[Document]:
    return store.search(query, k)
