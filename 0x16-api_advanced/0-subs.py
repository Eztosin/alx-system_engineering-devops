#!/usr/bin/python3
"""contains a function that queries the Reddit API"""
import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent":
                                                "YourApp/1.0"})

    if response.status_code == 200:
        content = response.json()
        return int(content["data"]["subscribers"])
    else:
        return (0)
