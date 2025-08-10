import requests
from bs4 import BeautifulSoup
from langchain.docstore.document import Document
import pdfplumber
from typing import List

def fetch_wikipedia_page(url: str) -> Document:
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    paragraphs = [p.get_text().strip() for p in soup.find_all("p") if p.get_text().strip()]
    text = "\n\n".join(paragraphs)
    return Document(page_content=text, metadata={"source": url, "type": "html"})

def load_pdf(path: str, source: str = None) -> List[Document]:
    docs = []
    with pdfplumber.open(path) as pdf:
        pages_text = []
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                pages_text.append(t)
        if pages_text:
            text = "\n\n".join(pages_text)
            docs.append(Document(page_content=text, metadata={"source": source or path, "type": "pdf"}))
    return docs

def fetch_plain_text_url(url: str) -> Document:
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return Document(page_content=resp.text, metadata={"source": url, "type": "text"})
