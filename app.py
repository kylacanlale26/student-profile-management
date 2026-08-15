students = []

# CREATE
def create_student():
    student_name = input("Enter your name: ")
    student_number = input("Enter your name: ")
    Year_Section = input("Enter your year and section: ")

    student = {
        name: student_name,
        number: student_number,
        yearsection: Year_Section
    }

    students.append(student)
    print("Student added successfully!")