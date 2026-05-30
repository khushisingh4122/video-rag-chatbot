from langchain_core.documents import Document

doc = Document(
    page_content="This is a test document.",
    metadata={
        "video_id": "A"
    }
)

print(doc)