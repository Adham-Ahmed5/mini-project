class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        """Method to display student's information"""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")
    
    def calculate_average(self):
        """Method to calculate and return average grade"""
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0.0


class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grades):
        """Method to add a new student to the database"""
        new_student = Student(name, age, grades)
        self.students.append(new_student)
        print(f"Student {name} added successfully.")

    def display_all_students(self):
        """Display information of all students in the database"""
        if self.students:
            print("\nAll Students in the Database:")
            for student in self.students:
                student.display_info()
                print(f"Average Grade: {student.calculate_average():.2f}\n")
        else:
            print("No students in the database yet.")
    

# Simple scenario of using the system

def main():
    # Create the student database system
    db = StudentDatabase()
    
    # Add a few students to the database
    db.add_student("Alice", 20, [90, 85, 88, 92])
    db.add_student("Bob", 22, [70, 75, 80, 78])
    db.add_student("Charlie", 21, [95, 98, 93, 90])
    
    # Display all students in the database
    db.display_all_students()
    
    # Adding another student
    db.add_student("Diana", 19, [85, 82, 88, 90])
    
    # Display updated student list
    db.display_all_students()

if __name__ == "__main__":
    main()
