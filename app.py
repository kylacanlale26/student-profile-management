# CREATE
students = []
# READ
def view_student():
    student_id = int(input("To view the student profile card, please enter the student ID number: "))
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        print("Error! Student profile not found within the management system.")
        return
    print(f"\n ------- Student Profile Card -------")
    print(f"Student Name: {student['name']}")
    print(f"Student ID: {student['id']}")
# UPDATE

# DELETE