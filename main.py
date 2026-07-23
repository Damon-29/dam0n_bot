from sources.youtube import fetch

videos = fetch()

print(f"Found {len(videos)} videos\n")

for video in videos:
    print("--------------------------------")
    print(video["title"])
    print(video["published"])
    print(video["url"])
