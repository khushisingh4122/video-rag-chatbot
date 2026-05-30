from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
This is a long transcript.
Imagine this contains hundreds of words from a YouTube video.
We want to split it into chunkss.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk)