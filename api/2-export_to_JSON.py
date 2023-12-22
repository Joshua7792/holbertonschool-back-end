#!/usr/bin/python3
import requests
import json
import sys

def fetch_todo_list(employee_id):
    """ Fetches the TODO list and user information for a given employee ID from a REST API. """
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')

    response = requests.get(api_url)
    todos = response.json()

    return employee_id, username, todos

def export_to_json(employee_id):
    """ Exports the TODO list data for the given employee ID to a JSON file. """
    user_id, username, todos = fetch_todo_list(employee_id)

    tasks_data = [
        {"task": task['title'], "completed": task['completed'], "username": username}
        for task in todos
    ]

    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as jsonfile:
        json.dump({str(user_id): tasks_data}, jsonfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        export_to_json(int(sys.argv[1]))
    else:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
