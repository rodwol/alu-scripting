#!/usr/bin/python3
"""
This module provides a function to retrieve the number of subscribers
for a given subreddit from Reddit's API.

Usage:
    To use this module, call number_of_subscribers(subreddit)
     with the name of the subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
       Args:
           subreddit (str): The name of the subreddit.

       Returns:
           int: The number of subscribers if the request is successful.
                Returns 0 if the subreddit is not found (HTTP 404).
       """
    user_agent = {'User-agent': 'rodwol'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        subscribers = response.json()
        return subscribers['data']['subscribers']
    elif response.status_code == 404:
        return 0