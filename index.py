import os

FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks from the file into a list of dictionaries."""
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if "|" in line:
                    title, completed = line.split("|")
                    tasks.append({"title": title, "completed": completed == "True"})
    return tasks


def save_tasks(tasks):
    """Save all tasks to the file."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(f"{task['title']}|{task['completed']}\n")


def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "!" if task["completed"] else "*"
        print(f"{i}. {task['title']} [{status}]")


def add_task(tasks):
    """Add a new task."""
    title = input("Enter task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(" Task added successfully!")
    else:
        print(" Task cannot be empty.")


def delete_task(tasks):
    """Delete a task by number."""
    display_tasks(tasks)
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f" Deleted task: {removed['title']}")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def mark_completed(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    try:
        num = int(input("\nEnter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            save_tasks(tasks)
            print(f" Task marked as completed: {tasks[num - 1]['title']}")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main program loop."""
    tasks = load_tasks()
    
    while True:
        print("\n====== TO-DO LIST MANAGER ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Exiting... Have a productive day!")
            break
        else:
            print(" Invalid choice, please try again.")


if __name__ == "__main__":
    main()
