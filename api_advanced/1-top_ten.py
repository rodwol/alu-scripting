#!/usr/bin/python3
"""Reddit Top Ten Posts Module"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API to get the top 10 hot posts"""
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
