# Example - Creating a function that does math operations from another function

def math_operations(func, number1, number2):
    return func(number1, number2)

def my_sum(number1, number2):
    return number1 + number2

def my_sub(number1, number2):
    return number1 - number2

def my_div(number1, number2):
    return number1 / number2

number1 = 12
number2 = 3

print(f"{number1} + {number2} = {math_operations(my_sum, number1, number2)}")
print(f"{number1} - {number2} = {math_operations(my_sub, number1, number2)}")
print(f"{number1} / {number2} = {math_operations(my_div, number1, number2)}")
