#!/usr/bin/python3
"""Fetch and print titles of top ten hot posts in a given subreddit."""
import requests


def top_ten(subreddit):
    """Fetch and print titles of top ten hot posts in a given subreddit."""
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        for post in children[:10]:
            print(post['data'].get('title', 'No title'))
    else:
        return None


