import yt_dlp

url = input("Video URL: ")

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

    print("\nTITLE:")
    print(info.get("title"))

    print("\nENGAGEMENT RATE:")
    print(f"{engagement_rate:.4f}%")