import chromadb
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client_gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

client_db = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client_db.get_collection(
    "video_comparison"
)

question = input("Ask a question: ")

results = collection.query(
    query_texts=[question],
    n_results=5
)

context = ""

for i, doc in enumerate(results["documents"][0]):

    video_id = results["metadatas"][0][i]["video_id"]

    context += f"\nVIDEO {video_id}:\n"
    context += doc
    context += "\n"

prompt = f"""
You are analyzing two videos.

VIDEO A and VIDEO B are different videos.

Use the transcript context below to answer.

Context:
{context}

Question:
{question}

Always mention which video your answer comes from.
"""

response = client_gemini.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\nANSWER:\n")
print(response.text)

print("\nSOURCES:\n")

for metadata in results["metadatas"][0]:
    print(
        f"Video {metadata['video_id']}"
    )