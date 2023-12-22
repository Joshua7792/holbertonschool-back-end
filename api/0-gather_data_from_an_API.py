#!/usr/bin/python3
import requests
import sys

def fetch_todo_list(employee_id):
    """ Fetches the TODO list for a given employee ID from a REST API. """
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    response = requests.get(api_url)
    todos = response.json()

    total_tasks = len(todos)
    completed_tasks = len([task for task in todos if task['completed']])

    return employee_name, completed_tasks, total_tasks, todos

def display_todo_progress(employee_id):
    """ Displays the TODO list progress for the given employee ID. """
    employee_name, completed_tasks, total_tasks, todos = fetch_todo_list(employee_id)

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    for task in todos:
        if task['completed']:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        display_todo_progress(int(sys.argv[1]))
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
