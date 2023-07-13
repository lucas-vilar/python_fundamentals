# Inheritance in OOP
class Animal:
    def __init__(self, name, color, number_eyes, can_fly):
        self.name = name
        self.color = color
        self.number_eyes =  number_eyes
        self.can_fly = can_fly

    def is_animal(self):
        return f"{self.name} is an animal!"
    
class Dog(Animal):
    def __init__(self, name, color, number_eyes, can_fly, favorite_toy, ):
        super().__init__(name, color, number_eyes, can_fly)
        self.favorite_toy = favorite_toy

    def fav_toy(self):
        return f"{self.name} favorite toy is {self.favorite_toy}"
    
class Cat(Animal):
    def __init__(self, name, color, number_eyes, can_fly, like_lasagna):
        super().__init__(name, color, number_eyes, can_fly)
        self.like_lasagna =  like_lasagna

    def lasagna(self):
        return f"Like lasagna: {self.like_lasagna}"
    
animal_1 = Dog('Quico', 'Black', 2, False, 'Ball')
animal_2 = Cat('Garfield', 'Orange', 2, False, True)

print("\n",animal_1.is_animal())
print("\n",animal_2.is_animal())
print("\n",animal_1.fav_toy())
print("\n",animal_2.lasagna())

print("\n======MULTIPLE INHERITANCE======")
print("Example 1: \n")
class Student:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"Name: {self.name} E-mail: {self.email}"
    
class CollegeStudent(Student):
    def __init__(self, name, email, phone_number, university_name):
        super().__init__(name, email, phone_number)
        self.university_name = university_name
    
    def my_college(self):
        return f"{self.name} university is {self.university_name}"
    
class MicrobiologyStudent(CollegeStudent):
    def __init__(self, name, email, phone_number, university_name, favorite_bacteria):
        super().__init__(name, email, phone_number, university_name)
        self.favorite_bacteria = favorite_bacteria

    def bacteria(self):
        return f"{self.name} favorite bacteria is {self.favorite_bacteria}"
    
student_1 = MicrobiologyStudent('Lucas', 'lucas@email.com', '12345678', 'Federal University of Rio de Janeiro', 'Escherichia coli')
print(student_1)
print(student_1.my_college())
print(student_1.bacteria())
print("")


print("Example 2: \n")
class Mammalian(Animal):
    def __init__(self, name, color, number_eyes, can_fly):
        super().__init__(name, color, number_eyes, can_fly)

    def is_mammalian(self):
        return f"I am a mammalian!"

class FlyingAnimal(Animal):
    def __init__(self, name, color, number_eyes, can_fly):
        super().__init__(name, color, number_eyes, can_fly)

    def fly(self):
        return f"Yes, I can fly: {self.can_fly}"
    
class Bat(Mammalian, FlyingAnimal):
    def __init__(self, name, color, number_eyes, can_fly):
        super().__init__(name, color, number_eyes, can_fly)

    def batman(self):
        return f"I'm Batman!"
    
bat1 = Bat('Batman', 'Black', 2, True)
print(bat1.is_mammalian())
print(bat1.fly())
print(bat1.batman())