import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="videos"
)

collection.add(
    documents=[
        "This is my first transcript chunk"
    ],
    ids=[
        "chunk1"
    ]
)

results = collection.query(
    query_texts=[
        "transcript"
    ],
    n_results=1
)

print(results)