from ingest import fetch_wikipedia_page, load_pdf, fetch_plain_text_url
from chunk import chunk_documents
from embed_store import EmbedStore
from retrieve import retrieve_top_chunks
from generate import generate_answer
import os

def main():
    cities = [
        {
            "name": "Delhi",
            "wiki": "https://en.wikipedia.org/wiki/Delhi",
            "pdf": [
                "Art.pdf",
                "DELHI_HAAT_PITAMPURA_JANAKPURI.pdf",
                "Discover_India.pdf",
                "Faith.pdf",
                "Five_Senses_Brochure.pdf",
                "Metro.pdf",
                "Museums.pdf",
                "Shopping.pdf",
                "Taste.pdf"
            ],
            "text_url": None
        },
        {
            "name": "Mumbai",
            "wiki": "https://en.wikipedia.org/wiki/Mumbai",
            "pdf": "mumbai_tourism_brochure.pdf",
            "text_url": None
        },
        {
            "name": "Jaipur",
            "wiki": "https://en.wikipedia.org/wiki/Jaipur",
            "pdf": "jaipur_tourism_brochure.pdf",
            "text_url": None
        }
    ]

    docs = []

    for city in cities:
        if city["wiki"]:
            docs.append(fetch_wikipedia_page(city["wiki"]))

        if city["pdf"]:
            if isinstance(city["pdf"], list):
                for pdf_file in city["pdf"]:
                    if os.path.exists(pdf_file):
                        docs.extend(load_pdf(pdf_file, source=f"{city['name']} Tourism PDF"))
            else:
                if os.path.exists(city["pdf"]):
                    docs.extend(load_pdf(city["pdf"], source=f"{city['name']} Tourism PDF"))

        if city["text_url"]:
            docs.append(fetch_plain_text_url(city["text_url"]))

    chunks = chunk_documents(docs)

    store = EmbedStore()
    store.build_index(chunks)

    while True:
        query = input("\nAsk your tourism question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        top_chunks = retrieve_top_chunks(store, query)
        answer = generate_answer(query, top_chunks)
        print("\nAnswer:\n", answer)

if __name__ == "__main__":
    main()
