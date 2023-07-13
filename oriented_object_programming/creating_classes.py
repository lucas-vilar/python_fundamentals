#Creating a new class
class student:
    def __init__(self, name, phone_number, email):
        self.name =  name
        self.phone_number = phone_number
        self.email = email

    def __str__(self) -> str:
        return f"Name: {self.name}    Phone number: {self.phone_number}    E-mail: {self.email}"

student_1 = student('Lucas', '12345678', 'lucas@email.com')
student_2 = student('Julia', '87654321', 'julia@email.com')
print(student_1)
print(student_2)