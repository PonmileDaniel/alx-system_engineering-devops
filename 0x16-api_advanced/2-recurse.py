#!/usr/bin/python3
"""
Function that queries the Reddit Api and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def recurse(subreddit, hot=[], after=None):
    """Recursive query"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    res = requests.get(url, headers=headers, params=params)

    if res.status_code != 200:
        return (None)

    data = res.json().get('data', {})
    posts = data.get('children', [])
    if not posts:
        return (hot if hot else None)

    hot.extend(post.get('data', {}).get('title') for post in posts)
    after = data.get('after')
    if after:
        return recurse(subreddit, hot, after)
    else:
        return (hot)
