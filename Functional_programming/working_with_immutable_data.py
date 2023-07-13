# Working with immutable data
from collections import namedtuple

student = namedtuple("student", ["name", "email", "phone_number"])

student1 = student("Lucas", "lucas@email.com", "12345678")
student2 = student("Julia", "julia@email.com", "87654312")
student3 = student("Fernando", "fernando@email.com", "13245768")

_class = (student1, student2, student3)

for student in _class:
    print(student.name)