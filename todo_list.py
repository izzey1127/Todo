# Todo List - Manage a simple task list

tasks = []

def show_tasks():
    """Display all tasks in the list."""
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(task):
    """Add a task to the list."""
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(index):
    """Remove a task by its index."""
    try:
        removed = tasks.pop(index - 1)
        print(f"Task '{removed}' removed.")
    except IndexError:
        print("Invalid task number.")

def main():
    print("Simple To-Do List Manager")
    while True:
        print("\nChoose an option:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter a task to add: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            try:
                index = int(input("Enter the number of the task to remove: "))
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
