# Encapsulation in OOP

class Animal:
    def __init__(self, name, color):
# is a convention to put a _ in private attributes
        self._name = name
        self._color = color