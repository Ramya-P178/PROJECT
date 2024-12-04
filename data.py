from db import add_student, get_all_students, get_student_by_id, update_student_marks, delete_student


# Function to add a new student and handle the interaction with the DB
def add_new_student(student_name, marks):
    """
    Adds a new student to the database.

    Args:
    student_name (str): The name of the student.
    marks (int): The marks obtained by the student.

    Returns:
    str: A message confirming if the student was successfully added.
    """
    if not student_name or not marks.isdigit():
        return "Invalid input. Please provide a valid student name and marks."

    marks = int(marks)
    if marks < 0 or marks > 100:
        return "Marks must be between 0 and 100."

    add_student(student_name, marks)
    return f"Student {student_name} with marks {marks} added successfully."


# Function to retrieve all students from the database
def fetch_all_students():
    """
    Retrieves all student records from the database.

    Returns:
    list: A list of student tuples (id, student_name, marks).
    """
    students = get_all_students()
    return students


# Function to fetch a specific student by ID
def fetch_student_by_id(student_id):
    """
    Retrieves a student record by their ID.

    Args:
    student_id (int): The ID of the student to fetch.

    Returns:
    tuple: A tuple containing the student record (id, student_name, marks) or None if not found.
    """
    student = get_student_by_id(student_id)
    if student:
        return student
    return "Student not found."


# Function to update the marks of a specific student
def update_student(student_id, new_marks):
    """
    Updates the marks for a given student.

    Args:
    student_id (int): The ID of the student whose marks need to be updated.
    new_marks (int): The new marks to assign to the student.

    Returns:
    str: A message indicating whether the marks were updated successfully or not.
    """
    if new_marks < 0 or new_marks > 100:
        return "Marks must be between 0 and 100."

    update_student_marks(student_id, new_marks)
    return f"Student ID {student_id}'s marks have been updated to {new_marks}."


# Function to delete a student record by ID
def delete_student_by_id(student_id):
    """
    Deletes a student record from the database using the student's ID.

    Args:
    student_id (int): The ID of the student to be deleted.

    Returns:
    str: A message confirming whether the student was deleted or not.
    """
    student = get_student_by_id(student_id)
    if not student:
        return "Student not found, unable to delete."

    delete_student(student_id)
    return f"Student ID {student_id} has been successfully deleted."


# Sample function to demonstrate how these methods can be used
def main():
    # Add a new student
    result = add_new_student('Alice Green', '88')
    print(result)  # Example: Student Alice Green with marks 88 added successfully.

    # Fetch all students
    students = fetch_all_students()
    print("All Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}")

    # Update student marks
    update_result = update_student(1, 95)
    print(update_result)  # Example: Student ID 1's marks have been updated to 95.

    # Delete student by ID
    delete_result = delete_student_by_id(2)
    print(delete_result)  # Example: Student ID 2 has been successfully deleted.


if __name__ == "__main__":
    main()
