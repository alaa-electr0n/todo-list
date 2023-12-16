# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed successfully!")
    else:
        print("Task not found!")

# Function to view tasks
def view_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks yet!")

# Function to delete all tasks
def delete_all_tasks():
    global tasks
    tasks = []
    print("All tasks deleted!")

# Menu for user interaction
while True:
    print("\n*** To-Do List ***")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Delete all tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        delete_all_tasks()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
