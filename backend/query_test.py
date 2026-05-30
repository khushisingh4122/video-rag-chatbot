import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("video_comparison")

question = input("Ask a question: ")

results = collection.query(
    query_texts=[question],
    n_results=5
)

print("\nRESULTS:\n")

for i, doc in enumerate(results["documents"][0]):
    print(f"\nChunk {i+1}")
    print(doc)

    metadata = results["metadatas"][0][i]

    print(f"Source Video: {metadata['video_id']}")

    print("\n----------------")