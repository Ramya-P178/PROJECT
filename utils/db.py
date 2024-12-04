import sqlite3


# Create a connection to the SQLite database
def create_connection():
    """Create a connection to the SQLite database"""
    conn = sqlite3.connect('student_performance.db')  # This creates the DB file if it doesn't exist
    return conn


# Create the students table if it doesn't already exist
def create_table():
    """Create the 'students' table in the database if it doesn't exist"""
    conn = create_connection()
    cursor = conn.cursor()

    # Create the table for student performance
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        marks INTEGER NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


# Function to add a new student
def add_student(student_name, marks):
    """Add a new student to the students table"""
    conn = create_connection()
    cursor = conn.cursor()

    # Insert the student data into the table
    cursor.execute('''
    INSERT INTO students (student_name, marks)
    VALUES (?, ?)
    ''', (student_name, marks))

    conn.commit()
    conn.close()


# Function to retrieve all students from the database
def get_all_students():
    """Fetch all student records from the database"""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()  # Fetch all records

    conn.close()
    return students


# Function to retrieve a specific student by ID
def get_student_by_id(student_id):
    """Fetch a student record by ID"""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()  # Fetch a single record based on the ID

    conn.close()
    return student


# Function to update a student's marks
def update_student_marks(student_id, new_marks):
    """Update the marks for an existing student"""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE students
    SET marks = ?
    WHERE id = ?
    ''', (new_marks, student_id))

    conn.commit()
    conn.close()


# Function to delete a student by ID
def delete_student(student_id):
    """Delete a student record from the database"""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))

    conn.commit()
    conn.close()


# Function to drop the 'students' table (for testing or resetting)
def drop_table():
    """Drop the 'students' table (optional)"""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS students')

    conn.commit()
    conn.close()


# Main function to test the database operations
if __name__ == '__main__':
    create_table()  # Create the table if it doesn't exist

    # Add some sample students (uncomment these lines to add data)
    # add_student('John Doe', 85)
    # add_student('Jane Smith', 92)
    # add_student('Alice Green', 76)

    # Fetch all students
    students = get_all_students()
    print("All Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}")

    # Update student marks (uncomment to update)
    # update_student_marks(1, 95)  # Update marks for student with ID 1

    # Fetch and print the student with ID 1
    student = get_student_by_id(1)
    print("\nUpdated Student (ID: 1):")
    print(f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}")

    # Delete a student (uncomment to delete)
    # delete_student(3)  # Delete student with ID 3

    # Fetch all students after deletion
    students = get_all_students()
    print("\nStudents after deletion:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}")
