import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def view_tasks():
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['name']}")


def add_task():
    task_name = input("Enter task: ")

    tasks.append({
        "name": task_name,
        "completed": False
    })

    save_tasks()
    print("Task added!")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks()
            print("Task completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks()
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


tasks = load_tasks()

while True:
    print("\n========================")
    print("       TO-DO LIST")
    print("========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")