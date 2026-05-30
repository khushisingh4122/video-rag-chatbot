from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from yt_dlp import YoutubeDL

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VideoRequest(BaseModel):
    youtube_url: str
    instagram_url: str


@app.get("/")
def home():
    return {
        "message": "Video RAG Backend Running"
    }


def get_metadata(url):
    ydl_opts = {
        "quiet": True,
        "noplaylist": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(
            url,
            download=False
        )

    views = info.get("view_count", 0)
    likes = info.get("like_count", 0)

    engagement = 0

    if views > 0:
        engagement = round(
            (likes / views) * 100,
            2
        )

    score = round(
        (views * 0.7) +
        (likes * 0.3),
        2
    )

    duration = info.get("duration", 0)

    minutes = duration // 60
    seconds = duration % 60

    formatted_duration = f"{minutes}m {seconds}s"

    return {
        "title": info.get("title"),
        "channel": info.get("uploader"),
        "views": views,
        "likes": likes,
        "duration": formatted_duration,
        "thumbnail": info.get("thumbnail"),
        "engagement": engagement,
        "score": score
    }


@app.post("/analyze")
def analyze_videos(data: VideoRequest):
    try:

        video_a = get_metadata(
            data.youtube_url
        )

        video_b = get_metadata(
            data.instagram_url
        )

        score_a = video_a["score"]
        score_b = video_b["score"]

        winner = (
            "Video A"
            if score_a > score_b
            else "Video B"
        )

        engagement_winner = (
            "Video A"
            if video_a["engagement"] > video_b["engagement"]
            else "Video B"
        )

        views_difference = abs(
            video_a["views"] -
            video_b["views"]
        )

        likes_difference = abs(
            video_a["likes"] -
            video_b["likes"]
        )

        engagement_difference = round(
            abs(
                video_a["engagement"] -
                video_b["engagement"]
            ),
            2
        )

        if video_a["engagement"] > video_b["engagement"]:
            insight = (
                f"{video_a['title']} has stronger audience engagement."
            )
        else:
            insight = (
                f"{video_b['title']} has stronger audience engagement."
            )

        summary = f"""
 VIDEO COMPARISON REPORT

 Video A
Title: {video_a['title']}
Channel: {video_a['channel']}
Views: {video_a['views']:,}
Likes: {video_a['likes']:,}
Engagement: {video_a['engagement']}%
Score: {video_a['score']:,.2f}

🎬 Video B
Title: {video_b['title']}
Channel: {video_b['channel']}
Views: {video_b['views']:,}
Likes: {video_b['likes']:,}
Engagement: {video_b['engagement']}%
Score: {video_b['score']:,.2f}

 Overall Winner: {winner}

 Best Engagement: {engagement_winner}

 Views Difference:
{views_difference:,}

 Likes Difference:
{likes_difference:,}

 Engagement Difference:
{engagement_difference}%

 Insight:
{insight}

 Recommendation:
Focus on engagement rate and audience quality, not only view count.
"""

        return {
            "success": True,
            "video_a": video_a,
            "video_b": video_b,
            "winner": winner,
            "engagement_winner": engagement_winner,
            "summary": summary,
            "score_a": score_a,
            "score_b": score_b,
            "views_difference": views_difference,
            "likes_difference": likes_difference,
            "engagement_difference": engagement_difference
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }