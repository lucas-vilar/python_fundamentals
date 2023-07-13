# Abstraction in OOP
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def make_noise(self):
        pass

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)
# The Cat class needs to implement the make_noise method, as it is abstract in Animal()
    def make_noise(self):
        return "Miau Miau"
    
cat_1 = Cat('Garfield', 'Orange')
print(cat_1.make_noise())
