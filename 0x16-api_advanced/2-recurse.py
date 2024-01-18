#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns
 a list containing the titles of all hot articles for a given
 subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches titles of hot articles for a given subreddit.

    Args:
    - subreddit (str): The subreddit to query.
    - hot_list (list): A list to store titles of hot articles.
    - after (str): Identifier for the starting point of the next page.

    Returns:
    - List of titles or None if no results are found.
    """
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0 (by YourUsername)'}
    params = {'limit': 100, 'after': after}

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])

        if not children:
            return hot_list

        hot_list.extend([child['data']['title'] for child in children])

        return recurse(subreddit, hot_list, data['after'])
    elif response.status_code == 404:
        return None
    else:
        return None
