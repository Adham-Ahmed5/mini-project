import os
from datetime import datetime

# File name to store diary entries
DIARY_FILE = "diary.txt"

# Function to handle exceptions and check if file exists
def check_file():
    try:
        if not os.path.exists(DIARY_FILE):
            with open(DIARY_FILE, 'w'):  # Create the file if it doesn't exist
                pass
        return True
    except PermissionError:
        print("Error: You don't have permission to access the file.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Function to add a new diary entry
def add_entry():
    print("Add a new diary entry. Type 'exit' to stop.")
    
    # Get the current timestamp
    timestamp = input("Would you like to add a timestamp to your entry? (y/n): ").strip().lower()
    timestamp_str = ""
    if timestamp == 'y':
        timestamp_str = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - "

    # Start writing the entry
    entry = ""
    while True:
        line = input("Write your entry (type 'exit' to finish): ")
        if line.lower() == 'exit':
            break
        entry += line + "\n"
    
    # Add timestamp and save entry to the file
    try:
        with open(DIARY_FILE, 'a') as file:
            file.write(f"{timestamp_str}{entry}\n")
        print("Your entry has been saved successfully.")
    except Exception as e:
        print(f"Error saving entry: {e}")

# Function to view previous diary entries
def view_entries():
    try:
        if check_file():
            with open(DIARY_FILE, 'r') as file:
                entries = file.read()
                if entries:
                    print("\nYour Diary Entries:\n")
                    print(entries)
                else:
                    print("No entries found.")
    except FileNotFoundError:
        print("No diary file found. You may need to create a new entry first.")
    except Exception as e:
        print(f"Error reading entries: {e}")

# Function to show the main menu
def show_menu():
    while True:
        print("\nPersonal Diary Application")
        print("1. Create a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the diary application
if __name__ == "__main__":
    show_menu()
