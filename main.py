from sources.youtube import fetch as fetch_youtube
from sources.website import (
    fetch as fetch_website,
    get_thumbnail,
)
from sources.x import fetch_x

from utils.storage import (
    is_first_run,
    add_post,
    already_posted,
)

from utils.discord import send_post


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

# Only fetch the thumbnail for new website articles
        if source_name == "website":
            post["thumbnail"] = get_thumbnail(post["article_id"])

        send_post(source_name, post)

        add_post(source_name, post)

        new_posts += 1

    if new_posts == 0:
        print(f"No new {source_name} posts.\n")


def run_source(source_name, fetch_function):
    try:
        posts = fetch_function()
        process_source(source_name, posts)

    except Exception as e:
        print(f"ERROR processing {source_name}: {e}\n")


def main():
    run_source("youtube", fetch_youtube)
    run_source("website", fetch_website)

    # Uncomment when X is implemented
    run_source("x", fetch_x)


if __name__ == "__main__":
    main()
