#!/usr/bin/python3
"""A Python script that uses a REST API, for a given employee ID,
and returns information about his/her TODO list progress and
 exports data in CSV and JSON formats.
"""

import csv
import json
import requests
import sys


def get_todo_data(employee_id):
    """Uses a REST API for a given employee ID
    and returns information about his/her TODO list progress.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    user_response = requests.get(employee_url)
    if user_response.status_code != 200:
        print("Failed to fetch user data")
        return

    user_data = user_response.json()
    username = user_data.get("username")

    todo_response = requests.get(todos_url)
    if todo_response.status_code != 200:
        print("Failed to fetch TODO list data")
        return

    todo_data = todo_response.json()

    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            csv_writer.writerow([
                task["userId"],
                username,
                str(task.get("completed")),
                task.get("title")
            ])

    json_file = "{}.json".format(employee_id)
    json_data = {employee_id: []}
    for task in todo_data:
        json_data[employee_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open(json_file, "w", encoding="utf-8") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_data(employee_id)
