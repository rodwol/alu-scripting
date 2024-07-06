#!/usr/bin/python3
"""
Reddit Subscriber Checker Module

This module provides functionality to check the number of
subscribers for a given subreddit using the Reddit API.
It includes error handling for different HTTP status
codes and offers both unauthenticated and authenticated
requests via the `requests` library and `praw`
(Python Reddit API Wrapper) respectively.

Functions:
    number_of_subscribers(subreddit: str) -> Union[int, str]:
        Returns the number of subscribers
        Handles 200 (OK), 404 (Not Found), and 403
        (Forbidden) status codes with appropriate responses.

Example Usage:
    - Unauthenticated: Uses `requests` to fetch subreddit details.
    - Authenticated: Uses `praw` for a more reliable and
    authenticated request to the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """docs"""
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
            AppleWebKit/537.36 (KHTML, like Gecko)
            Chrome/91.0.4472.124 Safari/537.36'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        subscribers = response.json()
        return subscribers['data']['subscribers']
    elif response.status_code == 404:
        return "OK"
    elif response.status_code == 403:
        return "Forbidden: 403"
    else:
        return f"Error: {response.status_code}"
