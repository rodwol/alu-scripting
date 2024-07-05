#!/usr/bin/python3
"""docs"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """"Doc"""
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-Agent': 'rodwol'}
    param = {'after': after}
    response = requests.get(url, headers=header, params=param)

    if response.status_code != 200:
        return None
    else:
        data_js = response.json()
        after = data_js.get('data').get('after')
        has_next = \
            data_js.get('data').get('after') is not None
        hot_articles = data_js.get('data').get('children')
        [hot_list.append(article.get('data').get('title'))
         for article in hot_articles]

        return recurse(subreddit, hot_list, after=after) \
            if has_next else hot_list
