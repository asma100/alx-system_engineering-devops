#!/usr/bin/python3
"""TODO list and export to JSON"""
import json
import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetches TODO list progress for an employee using their ID and exports data to JSON."""

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    try:
        user_data = response.json()
    except json.JSONDecodeError:
        print(f"Error parsing user data from JSON response.")
        return

    username = user_data["username"]
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todo_url)
    try:
        todo_data = response.json()
    except json.JSONDecodeError:
        print(f"Error parsing TODO data from JSON response.")
        return

    # Collect tasks for the user
    tasks = []
    for task in todo_data:
        if task.get('userId') == int(employee_id):
            tasks.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    # Prepare the data in the required format
    output_data = {str(employee_id): tasks}

    # Write data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(output_data, jsonfile)

    print(f'Task data exported to: {filename}')


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except (IndexError, ValueError):
        print("Invalid input: Please enter an integer employee ID as an argument.")
