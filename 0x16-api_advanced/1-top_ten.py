#!/usr/bin/python3

"""Reddit API - Fetch top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Fetches and prints the titles"""
    user_agent = "linux:0x16-api_advanced (by Defiant-Yellow2860)"
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": user_agent}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get("data", {}).get("children", [])
        # Print the titles of the first 10 hot posts
        for post in data:
            print(post.get("data", {}).get("title", "No Title"))
    except (requests.RequestException, ValueError):
        print("None")
