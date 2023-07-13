# Creating a first function with **kwargs
def student_info(**kwargs):
    print(kwargs)

student_info(name = "Lucas Vilar", email = "lucas@email.com", phone = '12345678', favorite_subject = "Math")

# Getting all values from kwargs
def my_car(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

my_car(color="Red", year=2020, number_wheels = 4, price = 500.0)

#Unpacking kwargs in a function
my_dict = {"number1" : 1, "number2" : 5, "number3" : 10}

def sum_3_numbers(number1, number2, number3):
    return number1 + number2 + number3

print(sum_3_numbers(**my_dict))