
import json
import sys
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({'description': description, 'status': 'not done'})
    save_tasks(tasks)
    print(f"Task added: {description}")

def update_task(index, description):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['description'] = description
        save_tasks(tasks)
        print(f"Task updated: {description}")
    else:
        print(f"Invalid task index. Valid indices are: 0 to {len(tasks)-1}")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task deleted: {removed_task['description']}")
    else:
        print(f"Invalid task index. Valid indices are: 0 to {len(tasks)-1}")

def mark_task(index, status):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['status'] = status
        save_tasks(tasks)
        print(f"Task {status}: {tasks[index]['description']}")
    else:
        print(f"Invalid task index. Valid indices are: 0 to {len(tasks)-1}")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        if filter_status is None or task['status'] == filter_status:
            print(f"{i}. {task['description']} [{task['status']}]")

def main():
    if len(sys.argv) < 2:
        print("Usage: task.py <command> [<args>]")
        return

    command = sys.argv[1]
    if command == 'add':
        description = ' '.join(sys.argv[2:])
        add_task(description)
    elif command == 'update':
        index = int(sys.argv[2])
        description = ' '.join(sys.argv[3:])
        update_task(index, description)
    elif command == 'delete':
        index = int(sys.argv[2])
        delete_task(index)
    elif command == 'mark':
        index = int(sys.argv[2])
        status = sys.argv[3]
        if status in ['not done', 'in progress', 'done']:
            mark_task(index, status)
        else:
            print("Invalid status. Use 'not done', 'in progress', or 'done'.")
    elif command == 'list':
        if len(sys.argv) > 2:
            filter_status = sys.argv[2]
            if filter_status in ['not done', 'in progress', 'done']:
                list_tasks(filter_status)
            else:
                print("Invalid status. Use 'not done', 'in progress', or 'done'.")
        else:
            list_tasks()
    else:
        print("Unknown command")

if __name__ == '__main__':
    main()
