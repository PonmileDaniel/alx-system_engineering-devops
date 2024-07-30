#!/usr/bin/python3
""" Script that uses JSON placeholder API """
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = '{}users/{}'.format(base_url, sys.argv[1])
    res = requests.get(user)
    data = res.json()
    print("Employee {} is done with tasks".format(data.get('name')), end="")

    # Fetch tasks for the user
    todos = '{}todos?userId={}'.format(base_url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    completed_tasks = [task for task in tasks if task.get('completed')]

    print(" ({}/{}):".format(len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
