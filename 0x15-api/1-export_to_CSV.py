#!/usr/bin/python3

"""TODO list and export to CSV"""
import requests
import csv
import sys


def get_employee_todo_progress(employee_id):
    """Fetches TODO list progress for an employee using their ID and exports data to CSV."""

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    try:
        user_data = response.json()
    except json.JSONDecodeError:
        print(f"Error parsing user data from JSON response.")
        return

    name = user_data["username"]
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todo_url)
    try:
        todo_data = response.json()
    except json.JSONDecodeError:
        print(f"Error parsing TODO data from JSON response.")
        return

    total_tasks = 0
    completed = 0

    # Prepare CSV file for writing
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            if task.get('userId') == int(employee_id):
                total_tasks += 1
                completed += 1 if task.get('completed') else 0

                # Write each task data as a row to CSV
                writer.writerow([
                    employee_id,
                    name,
                    task.get('completed'),
                    task.get('title')
                ])

    print(f'Employee {name} is done with tasks({completed}/{total_tasks}):')
    print(f'Task data exported to: {filename}')


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except (IndexError, ValueError):
        print("Invalid input: Please enter an integer employee ID as an argument.")
