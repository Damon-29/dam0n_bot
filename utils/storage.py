import json

FILE = "posted.json"


def load():
    with open(FILE, "r") as f:
        return json.load(f)


def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def is_initialized():
    return load()["initialized"]


def initialize():
    data = load()
    data["initialized"] = True
    save(data)


def add_post(source, post):
    data = load()

    data[source][post["id"]] = {
        "title": post["title"],
        "url": post["url"],
        "published": post["published"]
    }

    save(data)


def already_posted(source, post_id):
    data = load()
    return post_id in data[source]
