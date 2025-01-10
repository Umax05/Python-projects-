# todo.py

def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    if not tasks:
        print("\nYour to-do list is empty! Nothing to remove.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(filename, tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(filename, tasks)
        elif choice == '4':
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()