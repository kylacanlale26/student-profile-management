# CREATE
students = []

def create_student():
    print("\nCreate Student Profile")
    student_name = input("\nEnter your full name: ")
    student_number = input("Enter your student number (no dash): ")
    year_section = input("Enter your year and section (e.g., 1A): ")
    if any((s["id"]) == student_number for s in students):
        print("\nError! Student ID already exists within the system.")
        return
    student = {
        "name": student_name,
        "id": student_number,
        "yearsection": year_section
    }
    students.append(student)
    print("\nStudent profile added successfully!")

# READ
def view_student():
    student_id = input("\nTo view the student profile card, please enter the student ID number: ") 
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        print("\nError! Student profile not found within the system.")
        return
    print("\n ------- Student Profile Card -------")
    print(f"Student Name: {student['name']}")
    print(f"Student ID: {student['id']}")
    print(f"Year & Section: {student['yearsection']}")
    print("------------------------------------")

# UPDATE
def update_student():
    student_id = int (input("\nEnter the student ID to update: "))
    for student in students:
        if student["id"] == student_id:
            print("\nStudent Information: ")
            print("\nStudent Name: ", student["name"])
            print("\nStudent ID: ", student["id"])
            print("\nYear & Section: ", student["yearsection"])
            command = input("\nType 'edit' to edit the student's info: ")
            if command == "edit":
                while True:
                    print("\nSelect the information to edit: ")
                    print("1. Student's Name.")
                    print("2. Student's Year & Section.")
                    print("3. Finish.")
                    choice = input("\nChoose info to edit: ")
                    if choice == "1":
                        new_name = input("\nEnter new Name: ")
                        student["name"] = new_name
                        print("\nName has been updated!")
                    elif choice == "2":
                        new_yearsection = input("\nEnter new Year & Section: ")
                        student["yearsection"] = new_yearsection
                        print("\nYear & Section has been updated!")
                    elif choice == "3":
                        break
                    else:
                        print("\nInvalid Input!!!")
                while True:
                    confirm = input ("\nType 'update' to confirm: ")
                    if confirm == "update":
                        print("\nStudent info is saved!")
                        break
                    else:
                        print("\nPlease type 'update' to confirm.")
            else:
                print("\nCancelled!")
            return
        print ("\nError! Student Number Cannot be Found!")
    pass

# DELETE


# MENU
def student_menu():
    while True:
        print("\nStudent Profile Management System")
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
            update_student()
        elif choice == "4":
            pass
        elif choice == "5":
            print("\nSee you again!")
            break
student_menu()