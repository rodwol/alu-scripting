#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
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
