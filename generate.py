import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_answer(query, top_chunks, max_output_tokens=500):
    context = "\n".join([chunk.page_content for chunk in top_chunks])
    prompt = f"Answer the following tourism-related question using only the provided context.\n\nContext:\n{context}\n\nQuestion: {query}"

    response = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": max_output_tokens,
            "temperature": 0.1
        }
    )
    return response.text
