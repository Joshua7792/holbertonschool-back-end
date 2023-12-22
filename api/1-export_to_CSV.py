#!/usr/bin/python3
import requests
import sys
import csv

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

def export_to_csv(employee_id):
    """ Exports the TODO list data for the given employee ID to a CSV file. """
    user_id, username, todos = fetch_todo_list(employee_id)

    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task['completed'], task['title']])

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        export_to_csv(int(sys.argv[1]))
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
