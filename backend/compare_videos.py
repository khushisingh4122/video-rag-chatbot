import yt_dlp
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_metadata(url):

    with yt_dlp.YoutubeDL({"quiet": True}) as ydl:

        info = ydl.extract_info(
            url,
            download=False
        )

        views = info.get("view_count") or 0
        likes = info.get("like_count") or 0
        comments = info.get("comment_count") or 0

        engagement_rate = (
            (likes + comments) / views * 100
        ) if views else 0

        return {
            "title": info.get("title"),
            "channel": info.get("channel"),
            "views": views,
            "likes": likes,
            "comments": comments,
            "engagement_rate": engagement_rate,
            "duration": info.get("duration"),
            "upload_date": info.get("upload_date")
        }


video_a = input("Video A URL: ")
video_b = input("Video B URL: ")

meta_a = get_metadata(video_a)
meta_b = get_metadata(video_b)

prompt = f"""
Compare these two videos.

VIDEO A:
{meta_a}

VIDEO B:
{meta_b}

Answer:

1. Engagement rate of each
2. Which video performed better
3. Why
4. Creator of each video
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\nANSWER:\n")
print(response.text)