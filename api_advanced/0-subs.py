#!/usr/bin/python3
"""DOC"""
import requests


def number_of_subscribers(subreddit):
    """DOC"""
    user_agent = {'User-agent': 'rodwol'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        subscribers = response.json()
        return subscribers['data']['subscribers']
    elif response.status_code == 404:
        return 0
