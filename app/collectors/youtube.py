import requests

from app.config import YOUTUBE_API_KEY


YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"


def get_video_data(topic: str) -> list[dict]:
    params = {
        "part": "snippet",
        "q": topic,
        "type": "video",
        "maxResults": 5,
        "key": YOUTUBE_API_KEY,
    }

    response = requests.get(
        YOUTUBE_SEARCH_URL,
        params=params,
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()
    videos = []

    for item in data["items"]:
        video_id = item["id"]["videoId"]
        snippet = item["snippet"]

        video = {
            "video_id": video_id,
            "title": snippet["title"],
            "description": snippet["description"],
            "channel": snippet["channelTitle"],
            "published_at": snippet["publishedAt"],
            "url": f"https://www.youtube.com/watch?v={video_id}",
        }

        videos.append(video)

    return videos