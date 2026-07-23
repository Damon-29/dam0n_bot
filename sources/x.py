import feedparser

RSS_URL = "https://<rss-bridge-instance>/?action=display&bridge=Twitter&context=By+username&u=Wuthering_Waves&norep=on&noretweet=on&nopinned=on&format=Atom"


def fetch():
    feed = feedparser.parse(RSS_URL)

    posts = []

    for entry in feed.entries:
        # Build post object
        posts.append(...)

    return posts
