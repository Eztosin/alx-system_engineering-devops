#!/usr/bin/python3
"""A Python script that retrieves data for all employees' TODO lists
and exports the data in a single JSON file.
"""

import json
import requests


def get_all_todo_data():
    """Retrieves TODO list data for all employees."""
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users".format(base_url)

    user_response = requests.get(users_url)
    if user_response.status_code != 200:
        print("Failed to fetch user data")
        return

    user_data = user_response.json()

    all_data = {}
    for user in user_data:
        user_id = str(user.get("id"))
        username = user.get("username")

        todos_url = "{}/todos?userId={}".format(base_url, user_id)
        todo_response = requests.get(todos_url)

        if todo_response.status_code == 200:
            todo_data = todo_response.json()
            all_data[user_id] = []
            for task in todo_data:
                all_data[user_id].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    json_file = "todo_all_employees.json"
    with open(json_file, "w", encoding="utf-8") as jsonfile:
        json.dump(all_data, jsonfile)

    print("Data exported to", json_file)


if __name__ == "__main__":
    get_all_todo_data()
