#!/usr/bin/python3
""" Script that uses JSON placeholder API"""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    user = '{}users/{}'.format(base_url, sys.argv[1])
    res = requests.get(user)
    data = res.json()
    print("Employee {} is done with tasks".format(data.get('name')), end="")

    todos = '{}todos?userId={}'.format(base_url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    last_task = []
    for task in tasks:
        if task.get('completed') is True:
            last_task.append(task)

    print("({}/{}):".format(len(last_task), len(tasks)))
    for task in last_task:
        print("\t {}".format(task.get("title")))
