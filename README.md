# Tourism & Culture Guide RAG Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot that answers tourism-related questions using curated data from Wikipedia (via scraping), tourism PDFs, and text sources. 
Built with Python, LangChain, FAISS, and Google Gemini 2.0 Flash.

# How This Project Works

The project follows a Retrieval-Augmented Generation (RAG) workflow to deliver accurate, context-aware answers for tourism-related queries. First, data about each city is collected from multiple sources — Wikipedia articles (scraped as text from URLs), tourism brochures in PDF format, and plain text files or online text URLs. This content is split into smaller chunks, embedded into numerical vectors using a sentence-transformer model, and stored in a FAISS vector database for efficient similarity search. When a user asks a question, the system retrieves the most relevant chunks from the database and passes them, along with the question, to Google’s Gemini 2.0 Flash model. The LLM then generates a coherent answer using only the retrieved context, ensuring factual and source-grounded responses.


# Features

Fetches tourism and cultural data from:

    Wikipedia articles

    Tourism brochures (PDF)

    Plain text URLs

Chunks and embeds documents using FAISS

Uses Gemini 2.0 Flash LLM for generating context-aware answers

Supports multiple cities in one searchable index

Can run entirely locally (LLM call still requires internet)

# Project Structure

📂 Tourism & Culture Guide RAG Chatbot
├── main.py                # Entry point of the application

├── ingest.py              # Fetches and loads documents

├── chunk.py               # Splits documents into chunks

├── embed_store.py         # Embeds and stores chunks in FAISS

├── retrieve.py            # Retrieves top relevant chunks

├── generate.py            # Generates final answers using Gemini

├── requirements.txt       # Dependencies list

├── .env                   # API key storage

└── README.md              # Project documentation

# Prerequisites

Python 3.10+

8GB+ RAM (Recommended: 16GB)

Google Gemini API key

# Installation


git clone https://github.com/ktj709/Tourism-Culture-Guide---RAG-Chatbot

cd Tourism-Culture-Guide---RAG-Chatbot

pip install -r requirements.txt

# Environment Variables

Create a .env file in the root directory:

     GOOGLE_API_KEY=your_gemini_api_key_here


# Running the Project

python main.py

Upon running for the first time, the script will process and embed all source documents into batches before it becomes ready to answer questions.
This may take a few minutes, depending on the number and size of PDFs/URLs being loaded. Once completed, you will see the prompt:

        Ask your tourism question (or type 'exit' to quit):


# Once running, type your tourism question, e.g.:

"cultural festivals in Jaipur"

"museums in Mumbai"

"food to try in Delhi"

# Adding New Cities

Edit the cities list in main.py:
     for example:

       cities = [
    {
        "name": "Paris",
        "wiki": "https://en.wikipedia.org/wiki/Paris",
        "pdf": ["any pdf having relevant data.pdf"],
        "text_url": None
    }
    ]


# Some important points

Current Cities: The dataset currently includes only Delhi, Mumbai, and Jaipur.

      Easy Expansion: Adding more cities is simple:

        Add the new city’s details in the cities list in main.py.

        Provide the city name, a valid Wikipedia link (optional), and at least one tourism-related PDF containing relevant data about that city.

        Run the ingestion pipeline again to rebuild the FAISS index.

        Document Sources: The RAG pipeline supports PDFs, Wikipedia articles, and plain-text URLs.

        Custom Data: You can mix and match multiple data sources per city — the retrieval system will merge them into one searchable index.
