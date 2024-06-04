#!/usr/bin/python3

"""Reddit API - Fetch all hot post titles recursively"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive fetche."""
    user_agent = "linux:0x16-api_advanced  (by Defiant-Yellow2860)"
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": user_agent}
    params = {"limit": 100}  # Fetch up to 100 posts at a time

    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        # Check if the response status code is 200 OK
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
        posts = data.get("children", [])
        # Add the titles of the current batch of posts to the hot_list
        for post in posts:
            hot_list.append(post.get("data", {}).get("title", "No Title"))
        # Check if there is a next page
        after = data.get("after", None)
        if after:
            # Recursively fetch the next page
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except requests.exceptions.RequestException as e:
        return None
    except ValueError as e:
        return None
