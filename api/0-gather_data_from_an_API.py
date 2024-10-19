#!/usr/bin/python3
"""
documented
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    """
        take user Id
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        convert json to dictionary
    """
    employee = json.loads(request_employee.text)
    """
        takes employee name
    """
    employee_name = employee.get("name")

    """
        request the TODO list of user
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
    employee_todos = json.loads(request_todos.text)
    """
        documented
    """
    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        documented
    """
    EMPLOYEE_NAME = employee_name
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))         