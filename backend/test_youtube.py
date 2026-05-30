from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()

transcript = api.fetch("dQw4w9WgXcQ")

for item in transcript[:5]:
    print(item)