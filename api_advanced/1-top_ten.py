#!/usr/bin/python3
"""
a function that queries the Reddit API and
prints the titles of the first 10 hot posts listed
for a given subreddit
"""
import requests


def top_ten(subreddit):
    """DOCS"""
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
