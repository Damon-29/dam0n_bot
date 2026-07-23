from sources.youtube import fetch as fetch_youtube
# from sources.website import fetch as fetch_website
# from sources.x import fetch as fetch_x

from utils.storage import (
    is_first_run,
    add_post,
    already_posted,
)

from utils.discord import send_post  # Change if your function name differs


def process_source(source_name, posts):
    if is_first_run(source_name):
        print(f"First run detected for {source_name}.")

        for post in posts:
            add_post(source_name, post)

        print(f"Stored {len(posts)} existing posts.")
        print("Nothing will be sent to Discord.\n")
        return

    print(f"Checking {source_name}...\n")

    new_posts = 0

    for post in posts:

        if already_posted(source_name, post["id"]):
            continue

        print(f"NEW {source_name.upper()} POST!")
        print(post["title"])

        send_post(source_name,post)

        add_post(source_name, post)

        new_posts += 1

    if new_posts == 0:
        print(f"No new {source_name} posts.\n")


def main():

    process_source(
        "youtube",
        fetch_youtube()
    )

    # process_source(
    #     "website",
    #     fetch_website()
    # )

    # process_source(
    #     "x",
    #     fetch_x()
    # )


if __name__ == "__main__":
    main()
