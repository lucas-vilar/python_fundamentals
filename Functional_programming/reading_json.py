# Reaging JSON files in Python
import json
from collections import namedtuple

students = namedtuple("students", ["name", "phone_number", "email"])

with open("reading_json.json") as json_file:
    data = json.load(json_file)

all_students = map(lambda json_student: students(json_student['name'], json_student['phone_number'], json_student['email']), data['students'])

for student in all_students:
    print(student.name, "    ", student.phone_number, "    ", student.email)