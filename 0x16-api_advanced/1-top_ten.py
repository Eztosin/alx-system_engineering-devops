#!/usr/bin/python3
"""contains a function that queries the Reddit API and prints
 the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first
    10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers={"User-Agent":
                                          "YourApp/1.0"})

    if response.status_code == 200:
        content = response.json()
        hot_posts = content["data"]["children"])
        for post in hot_posts:
            print(post["data"]["title"]
    else:
        print("None")
