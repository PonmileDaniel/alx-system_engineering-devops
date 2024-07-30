#!/usr/bin/python3
""" JSON placeholder API to get TODO list progress of an employee """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_url = "{}users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Get employee name
    name = user_data.get('name')

    # Fetch tasks for the user
    todos_url = "{}todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Separate completed and total tasks
    completed_tasks = [task for task in todos_data if task.get('completed')]
    tasks = len(todos_data)
    done = len(completed_tasks)

    # Display employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(name, done, tasks))

    # Print titles of completed tasks
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
