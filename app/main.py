from app.collectors.youtube import get_video_data


def main():
    videos = get_video_data("Python")

    for video in videos:
        print("Title:", video["title"])
        print("Channel:", video["channel"])
        print("Published:", video["published_at"])
        print("URL:", video["url"])
        print("-" * 50)


if __name__ == "__main__":
    main()