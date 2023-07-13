# Creating a function that returns another function

def math_operation(operator):
    def my_sum(number1, number2):
        return number1 + number2
    
    def my_sub(number1, number2):
        return number1 - number2
    
    if operator == "+":
        return my_sum
    if operator == "-":
        return my_sub
    
sum_function = math_operation("+")
print(sum_function(4, 9))
sub_function = math_operation("-")
print(sub_function(10, 2))