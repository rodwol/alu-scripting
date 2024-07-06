#!/usr/bin/python3
""" 3-count.py """
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """ prints a sorted count of given keywords """

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'User-Agent': 'Mozilla/5.0'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format
                          (word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)

"""
def count_words(subreddit, word_list, results=None, after=None):
    if results is None:
        results = {}

    # Base case: If subreddit is not valid, print nothing
    if not is_valid_subreddit(subreddit):
        return

    # Construct the URL to fetch hot articles
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Define headers with User-Agent to avoid request blocking
    headers = {'User-agent': 'myredditapp'}

    # Parameters for the Reddit API request
    params = {'limit': 100}  # Number of posts per request

    if after:
        params['after'] = after  # Use 'after' token for pagination

    try:
        # Make the GET request to Reddit API
        response = requests.get(url,
        headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse JSON response
        data = response.json()

        # Extract posts from response
        posts = data['data']['children']

        # Process each post title
        for post in posts:
            title = post['data']['title'].lower()
            # Convert title to lowercase

            # Count occurrences of each word in title
            for word in word_list:
                if f' {word.lower()} ' in f' {title} ':
                    if word.lower() in results:
                        results[word.lower()] += 1
                    else:
                        results[word.lower()] = 1

        # Check if there are more posts to fetch
        after = data['data'].get('after')

        if after:
            # Recursively fetch next page of results
            count_words(subreddit, word_list, results, after)
        else:
            sorted_results = sorted(results.items(),
            key=lambda x: (-x[1], x[0]))
            for word, count in sorted_results:
                print(f"{word}: {count}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def is_valid_subreddit(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-agent': 'myredditapp'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False
        """
