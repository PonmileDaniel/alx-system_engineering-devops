#!/usr/bin/python3
"""information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()

    all_tasks = {}
    for user in users:
        uid = user.get("id")
        username = user.get("username")
        todos = requests.get(base_url + "todos", params={"userId": uid}).json()

        user_tasks = [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        } for todo in todos]

        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
