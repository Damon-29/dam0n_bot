from sources.x import fetch_x

posts = fetch_x()

print(f"Found {len(posts)} posts\n")

print(posts[0])
