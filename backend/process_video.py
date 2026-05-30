from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled
from youtube_utils import get_video_id
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="video_comparison"
)

def process_video(url, video_label):

    video_id = get_video_id(url)

    api = YouTubeTranscriptApi()

    try:
        transcript = api.fetch(video_id)

    except TranscriptsDisabled:
        print(f"Video {video_label} has no transcript")
        return

    full_text = " ".join(
        [item.text for item in transcript]
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(full_text)

    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            ids=[f"{video_label}_{i}"],
            metadatas=[
                {
                    "video_id": video_label
                }
            ]
        )

    print(
        f"Stored {len(chunks)} chunks for Video {video_label}"
    )


url_a = input("Video A URL: ")
url_b = input("Video B URL: ")

process_video(url_a, "A")
process_video(url_b, "B")