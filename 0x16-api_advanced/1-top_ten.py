#!/usr/bin/python3

"""Reddit API - Fetch top 10 hot posts"""
import requests

def top_ten(subreddit):
    """Fetches and prints the titles of the first 10 hot posts for a given subreddit."""
    user_agent = "linux:0x16-api_advanced  (by Defiant-Yellow2860)"
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": user_agent}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 OK
        if response.status_code != 200:
            print("None")
            return
        
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        # If there are no posts, print None
        if not posts:
            print("None")
            return
        
        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post.get("data", {}).get("title", "No Title"))

    except requests.exceptions.RequestException as e:
        print("None")

    except ValueError as e:
        print("None")
