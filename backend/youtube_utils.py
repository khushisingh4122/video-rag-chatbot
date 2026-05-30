from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    parsed = urlparse(url)

    if parsed.hostname == "youtu.be":
        return parsed.path[1:]

    if parsed.hostname in (
        "www.youtube.com",
        "youtube.com"
    ):
        return parse_qs(parsed.query)["v"][0]

    return None