#!/usr/bin/python3
""" a Python script that uses a REST API, for a given employee ID,
 and returns information about his/her TODO list progress
"""

import csv
import json
import requests
import sys


def export_todo_data(employee_id, todos_data):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        return

    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            writer.writerow([employee_id, employee_name, task.get("completed"), task.get("title")])
    print(f"Data exported to {filename} successfully.")

def get_todo_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_id} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

    export_todo_data(employee_id, todos_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_data(employee_id)
