#!/usr/bin/python3
import requests
import json

def fetch_all_users():
    """ Fetches all users from the REST API. """
    users_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users_url)
    return response.json()

def fetch_user_tasks(user_id):
    """ Fetches tasks for a specific user from the REST API. """
    tasks_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(tasks_url)
    return response.json()

def export_all_tasks():
    """ Exports all tasks of all users to a JSON file. """
    users = fetch_all_users()
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        tasks = fetch_user_tasks(user_id)

        all_tasks[user_id] = [
            {"username": username, "task": task['title'], "completed": task['completed']}
            for task in tasks
        ]

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)

if __name__ == "__main__":
    export_all_tasks()
