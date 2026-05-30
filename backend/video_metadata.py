import yt_dlp

url = input("Video URL: ")

ydl_opts = {
    "quiet": True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:

    info = ydl.extract_info(
        url,
        download=False
    )

    print("\nTITLE:")
    print(info.get("title"))

    print("\nCHANNEL:")
    print(info.get("channel"))

    print("\nVIEWS:")
    print(info.get("view_count"))

    print("\nLIKES:")
    print(info.get("like_count"))

    print("\nDURATION:")
    print(info.get("duration"))

    print("\nUPLOAD DATE:")
    print(info.get("upload_date"))