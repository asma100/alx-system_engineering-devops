#!/usr/bin/env bash

"""TODO list """
import json
import requests


def fetch_all_employees_tasks():
    """Fetches TODO list progress for an employee using their ID."""

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
        user_id = user['id']
        username = user['username']
        user_tasks = []
        
        for task in todos:
            if task['userId'] == user_id:
                user_tasks.append({
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                })

        all_tasks[user_id] = user_tasks

    # Export to JSON in a compact format
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, separators=(',', ':'))

    print("Data has been exported to todo_all_employees.json")

# Run the function to fetch and export the tasks
fetch_all_employees_tasks()
