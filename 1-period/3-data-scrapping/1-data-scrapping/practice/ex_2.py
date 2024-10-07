import requests

users = requests.get("https://api.github.com/users").json()

for user in users:
    print(f"{user['login']} {user['url']}")
