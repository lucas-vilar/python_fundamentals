# Getters and setter in Python
class Student:
    def __init__(self, name, email, phone_number):
        self._name = name
        self._email = email
        self._phone_number = phone_number

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        print("Name updated!")

    @name.deleter
    def name(self):
        try:
            del self._name
        except Exception as e:
            print(f"Error: Unable to delete name {self.name}")
    