#!/usr/bin/python3
""""documented"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        documented
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        documented
    """
    user = json.loads(request_employee.text)
    """
        documented
    """
    username = user.get("username")

    """
        documented
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        documented
    """
    tasks = {}
    """
        documented
    """
    user_todos = json.loads(request_todos.text)
    """
        documented
    """
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        documented
    """
    with open('{}.csv'.format(argv[1]), mode='w') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            file_editor.writerow([argv[1], username, v, k])
            