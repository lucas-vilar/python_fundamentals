# Polymorphism in OOP
class Animal:
    def make_noise(self):
        print('AUUUUUUUUUU')

class Robot:
    def make_noise(self):
        print('Bip Bip Bip')

class Airplane:
    def make_noise(self):
        print('VRUUUUMMMMMMMMM')

animal_1, robot_1, airplane_1 = Animal(), Robot(), Airplane()

noises = [animal_1, robot_1, airplane_1]

for noise in noises:
    noise.make_noise()