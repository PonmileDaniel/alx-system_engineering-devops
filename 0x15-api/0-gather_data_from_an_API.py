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
    user_url = f"{base_url}users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f"Employee ID {employee_id} not found.")
        sys.exit(1)

    user_data = user_response.json()
    name = user_data.get('name')

    # Get todos
    todos_url = f"{base_url}todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    # Print result
    print(f"Employee {name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
