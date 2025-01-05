import os

# File where tasks will be stored
TASKS_FILE = "tasks.txt"

# Function to check if the task file exists, create if it doesn't
def check_file():
    try:
        # Create the file if it doesn't exist
        if not os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'w'):  # Open file in write mode to create it
                pass
        return True
    except PermissionError:
        print("Error: You don't have permission to access the file.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Function to add a task to the list
def add_task(task):
    try:
        if check_file():
            with open(TASKS_FILE, 'a') as file:
                file.write(f"{task}\n")
            print(f"Task '{task}' added successfully.")
    except Exception as e:
        print(f"Error saving task to file: {e}")

# Function to remove a completed task from the list
def remove_task(task):
    try:
        if check_file():
            with open(TASKS_FILE, 'r') as file:
                lines = file.readlines()
            
            if task + "\n" in lines:
                lines.remove(task + "\n")
                with open(TASKS_FILE, 'w') as file:
                    file.writelines(lines)
                print(f"Task '{task}' removed successfully.")
            else:
                print(f"Task '{task}' not found in the list.")
    except FileNotFoundError:
        print("Task file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to view the current task list
def view_tasks():
    try:
        if check_file():
            with open(TASKS_FILE, 'r') as file:
                tasks = file.readlines()
                if tasks:
                    print("\nCurrent Task List:")
                    for task in tasks:
                        print(f"- {task.strip()}")
                else:
                    print("No tasks in the list.")
    except FileNotFoundError:
        print("Task file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to load tasks from the file
def load_tasks():
    tasks = []
    try:
        if check_file():
            with open(TASKS_FILE, 'r') as file:
                tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        print("Task file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return tasks

# Main function to run the task manager
def main():
    while True:
        print("\nTask List Manager")
        print("1. Add a new task")
        print("2. Remove a completed task")
        print("3. View current task list")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ").strip()
        
        if choice == '1':
            task = input("Enter the task to add: ").strip()
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ").strip()
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting Task List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
