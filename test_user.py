from sources.x_client import XClient

client = XClient()

client.activate_guest()

user_id = client.get_user_id("Wuthering_Waves")
print("User ID:", user_id)

timeline = client.get_user_tweets(user_id)

print(type(timeline))
