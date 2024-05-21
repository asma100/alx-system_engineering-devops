#!/usr/bin/python3
"""Fetches TODO list progress for all employees and saves data as JSON."""
import json
import requests


def fetch_all_employees_tasks():
    """Fetches TODO list progress for all employees and returns a dictionary."""

    # URLs for the API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users
    users_response = requests.get(users_url)
    users = users_response.json()

    # Fetch all tasks
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Structure to hold the data
    all_tasks = {}

    # Populate the structure
    for user in users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                task_list.append(task_dict)

        all_tasks[user.get('id')] = task_list

    return all_tasks  # Return the dictionary containing all employee data


if __name__ == "__main__":
    try:
        # Fetch data for all employees
        all_employee_data = fetch_all_employees_tasks()

        # Save data to JSON file
        with open('todo_all_employees.json', mode='w') as f:
            json.dump(all_employee_data, f)

       # print("Successfully saved TODO data for all employees to 'todo_all_employees.json'.")
    except requests.exceptions.RequestException as e:
        #print(f"Error fetching data: {e}")

