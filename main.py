from sources.youtube import fetch
from utils.storage import (
    is_first_run,
    add_post,
    already_posted
)

from utils.discord import send_post   # Adjust if your function has a different name

videos = fetch()

# First run
if is_first_run("youtube"):
    print("First run detected.")

    for video in videos:
        add_post("youtube", video)

    print(f"Stored {len(videos)} existing videos.")
    print("Nothing will be sent to Discord.")

# Normal run
else:
    print("Checking for new videos...\n")

    for video in videos:

        if already_posted("youtube", video["id"]):
            continue

        print("NEW VIDEO FOUND!")
        print(video["title"])

        send_post(video)        # Use your existing Discord function
        add_post("youtube", video)
