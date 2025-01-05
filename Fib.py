import os

# File where grades will be stored
GRADE_FILE = "grades.txt"

# Function to check if the grade file exists, and create it if necessary
def check_file():
    try:
        # Create the file if it doesn't exist
        if not os.path.exists(GRADE_FILE):
            with open(GRADE_FILE, 'w'):  # Open file in write mode to create it
                pass
        return True
    except PermissionError:
        print("Error: You don't have permission to access the file.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Function to input and store grades
def input_grades():
    grades = []
    while True:
        try:
            subject = input("\nEnter subject name (or type 'done' to finish): ")
            if subject.lower() == 'done':
                break
            grade = input(f"Enter grade for {subject}: ")
            
            # Validate if the grade is a valid numeric input
            grade = float(grade)  # Try converting to a float to ensure it's numeric
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
                continue
            grades.append((subject, grade))
            
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Save grades to file
    try:
        if check_file():
            with open(GRADE_FILE, 'a') as file:
                for subject, grade in grades:
                    file.write(f"{subject}: {grade}\n")
            print("\nGrades saved successfully.")
    except Exception as e:
        print(f"Error saving grades to file: {e}")

# Function to read grades from file and calculate average
def calculate_average():
    try:
        if check_file():
            with open(GRADE_FILE, 'r') as file:
                lines = file.readlines()
                if not lines:
                    print("No grades found in the file.")
                    return
                
                grades = []
                for line in lines:
                    try:
                        subject, grade = line.split(":")
                        grade = float(grade.strip())
                        grades.append(grade)
                    except ValueError:
                        print(f"Skipping invalid entry: {line.strip()}")
                
                if grades:
                    average = sum(grades) / len(grades)
                    print(f"\nYour average grade is: {average:.2f}")
                else:
                    print("No valid grades found to calculate an average.")
    except FileNotFoundError:
        print("Grade file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to show the main menu and interact with the user
def show_menu():
    while True:
        print("\nStudent Grade Tracker")
        print("1. Input and store grades")
        print("2. Calculate and display average grade")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == '1':
            input_grades()
        elif choice == '2':
            calculate_average()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to run the grade tracker application
if __name__ == "__main__":
    show_menu()
