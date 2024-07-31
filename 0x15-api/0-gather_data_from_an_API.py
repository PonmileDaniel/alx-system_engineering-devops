#!/usr/bin/python3
""" Script that uses JSON placeholder API """
import requests
import sys

if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com/"

    users = requests.get(base + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(base + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get("title") for task in todos if task.get("completed")]

    name = users.get("name")
    count = len(completed)
    total = len(todos)
    print("Employee {} is done with tasks({}/{}):".format(name, count, total))
    for task_title in completed:
        print("\t {}".format(task_title))
