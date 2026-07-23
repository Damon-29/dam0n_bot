from sources.youtube import fetch
from utils.storage import (
    load,
    initialize,
    is_initialized,
    add_post,
    already_posted
)

videos = fetch()

if not is_initialized():

    print("First run detected.")

    for video in videos:
        add_post("youtube", video)

    initialize()

    print(f"Stored {len(videos)} existing videos.")
    print("Nothing will be sent to Discord.")

else:

    print("Checking for new videos...\n")

    for video in videos:

        if already_posted("youtube", video["id"]):
            continue

        print("NEW VIDEO FOUND!")
        print(video["title"])

        add_post("youtube", video)
