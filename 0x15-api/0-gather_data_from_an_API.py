#!/usr/bin/python3
""" JSONPlaceholder API to fetch an employee's TODO list progress """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/"

    # Get user information
    user_url = "{}users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Employee ID {} not found.".format(employee_id))
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Get todos
    todos_url = "{}todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    # Print result
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
