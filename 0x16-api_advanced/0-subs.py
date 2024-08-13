#!/usr/bin/python3
"""FUnction that queries the
Reddit APi and return no of
subscribers"""
import sys
import requests


def number_of_subscribers(subreddit):
    """Query to reddit Api"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
