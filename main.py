from sources.youtube import fetch

posts = fetch()

print(f"Found {len(posts)} videos")

for post in posts:
    print(post["title"])
