# Database operations in Python using SQLite
import sqlite3
from collections import namedtuple

# Creating the database and connection
connection = sqlite3.connect('students.db')
cursor = connection.cursor()

# Creating table if not exists
cursor.execute(''' CREATE TABLE IF NOT EXISTS student(
id INTEGER,
name TEXT,
phone_number TEXT,
email TEXT,
GPA REAL
)''')

students = namedtuple("students", ['id', 'name', 'phone_number', 'email', 'GPA'])

# Inserting one student
student_1 = students(1, "Lucas", "12345678", "lucas@email.com", 3.75)
cursor.execute(f"INSERT INTO student VALUES({student_1.id}, '{student_1.name}', '{student_1.phone_number}', '{student_1.email}', {student_1.GPA})")

# Inserting multiple students
student_2 = students(2, "Julia", "87654321", "julia@email.com", 4.0)
student_3 = students(3, "Fernando", "56781234", "fernando@email.com", 3.80)
student_4 = students(4, "Rita", "67812345", "rita@email.com", 3.96)

student_list = [student_2, student_3, student_4]
cursor.executemany(f"INSERT INTO student VALUES(?,?,?,?,?)", student_list)

connection.commit()

# Retrieving all registers
all_students = cursor.execute("SELECT * FROM student").fetchall()
print("All students: ",all_students)

# Retrieving a unique student
unique_student = cursor.execute("SELECT * FROM student WHERE id = 2").fetchone()
print("\nStudent:", unique_student)

# Updating a register
cursor.execute("UPDATE student SET name = 'Ritinha' WHERE id = 4")
connection.commit()
print("\nAll students: ",all_students)

# Deleting a register
cursor.execute("DELETE FROM student WHERE id = 3")
connection.commit()
print("\nAll students: ",all_students)