# CREATE

students = []

def create_student():
    print("\nCreate Student Profile")
    student_name = input("\nEnter your full name: ")
    student_number = int(input("Enter your student number (no dash): "))
    Year_Section = input("Enter your year and section (e.g., 1A): ")

    student = {
        "name": student_name,
        "id": student_number,
        "yearsection": Year_Section
    }

    students.append(student)
    print("\nStudent added successfully!\n")

# READ
def view_student():
    student_id = int(input("\nTo view the student profile card, please enter the student ID number: "))
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        print("\nError! Student profile not found within the management system.\n")
        return
    print(f"\n ------- Student Profile Card -------")
    print(f"Student Name: {student['name']}")
    print(f"Student ID: {student['id']}")

# UPDATE

# DELETE

# MENU
def student_menu():
    while True:

        print("Student Profile")

        while True:
            print("\nOptions:")
            print("""1. Create New Student Profile
2. View Student Profile
3. Update Student Profile
4. Delete Student Profile
5. Exit
            """)

            choice = input("Choose from the following options (number only): ")

            if choice not in ["1", "2", "3", "4", "5"]:
                print("\nInvalid Choice. Please choose only from the following.")
            else:
                break

        if choice == "1":
            create_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            print("See you again!")
            break

student_menu()