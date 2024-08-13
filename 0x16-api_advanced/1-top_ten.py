#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def top_ten(subreddit):
    hearders = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=hearders)

    if res.status_code == 200:
        data = res.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts[:10]:
            print(post.get('data', {}).get('title', 'No title'))
    else:
        print(None)
