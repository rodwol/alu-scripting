#!/usr/bin/python3
"""
 returns the number of subscribers if
 the request is successful.
 returns 0 if the subreddit is not found (HTTP 404)
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit
    """
    user_agent = {'User-agent': 'rodwol'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        subscribers = response.json()
        return subscribers['data']['subscribers']
    elif response.status_code == 404:
        return 0
