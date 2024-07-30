#!/usr/bin/python3
""" JSONPlaceholder API to get information about an employee """
import csv
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

    task_details = []
    for todo in todo_list:
        task_details.append([user_id,
                             username,
                             todo.get('completed'),
                             todo.get('title')])

    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w') as csv_file:
        writer = csv.writer(csv_file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in task_details:
            writer.writerow(task)
