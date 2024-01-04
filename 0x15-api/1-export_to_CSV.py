#!/usr/bin/python3
""" a Python script that uses a REST API, for a given employee ID,
 and returns information about his/her TODO list progress
"""

import csv
import json
import requests
import sys


def get_todo_data(employee_id):
    """Uses a REST API, for a given employee ID,
    and returns information about his/her TODO list progress
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        return

    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        return

    todos_data = todos_response.json()

    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, "w", newline="") as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            csv_writer.writerow([
                task["userId"],
                employee_name,
                str(task["completed"]),
                task["title"]
            ])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_data(employee_id)
