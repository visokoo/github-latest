import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    response = requests.get(f"https://api.github.com/users/{username}/events")

    print(f"The first github event from user {username} was at {response.json()[0]['created_at']}.")
    