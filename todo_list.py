tasks = []

def display_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("Tasks in the to-do list:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    display_tasks()
    if not tasks:
        return
    task_index = int(input("Enter the index of the task to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index.")

def main():
    print("Simple To-Do List Application")

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Thank you for using the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
