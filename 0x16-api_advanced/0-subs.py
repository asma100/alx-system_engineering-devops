#!/usr/bin/python3

"""reddit """
import requests


def number_of_subscribers(subreddit):
    """Fetches information about a subreddit, including subscriber count."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'linux:0x16-api_advanced (by Defiant-Yellow2860)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Debugging: Print the response status code and URL
        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
        # Check if the response status code is 200 OK
        if response.status_code != 200:
            print(f"Error: Non-200 status code: {response.status_code}")
            return 0
        # Debugging: Print the response text
        print(f"Response text: {response.text}")
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        return 0
    except ValueError as e:
        print(f"ValueError: {e}")
        return 0
