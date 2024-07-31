#!/usr/bin/python3
"""JSONPlaceholder API to get information about an employee."""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user_url = '{}users/{}'.format(base_url, user_id)
    response = requests.get(user_url)
    user_data = response.json()
    username = user_data.get('username')

    todos_url = '{}todos?userId={}'.format(base_url, user_id)
    response = requests.get(todos_url)
    todo_list = response.json()

    task_list = []
    for todo in todo_list:
        task_info = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        task_list.append(task_info)

    user_tasks = {str(user_id): task_list}
    filename = '{}.json'.format(user_id)
    with open(filename, mode='w') as json_file:
        json.dump(user_tasks, json_file)
