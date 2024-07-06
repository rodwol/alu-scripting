#!/usr/bin/python3
"""
This module provides a function to
retrieve the number of subscribers for a given subreddit
from Reddit's API
"""
import requests


def top_ten(subreddit):
    """
    fetches the number of subscribers for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        if 'children' in data:
            for post in data['children'][:10]:
                print(post['data']['title'])
    elif response.status_code == 404:
        return None
