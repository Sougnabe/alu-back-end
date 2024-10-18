#!/usr/bin/python3
#module is documented
import requests
import sys
#module is documented

def fetch_employee_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        return

    employee = user_response.json()
    employee_name = employee.get("name")

    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")#!/usr/bin/python3
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        return

    employee = user_response.json()
    employee_name = employee.get("name")

    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")