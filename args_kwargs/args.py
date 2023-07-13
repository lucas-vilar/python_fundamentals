# Creating a function with *args"
def sum_n_numbers(*args):
    return f"The sum is {sum(args)}"

print(sum_n_numbers(1, 2, 3, 90, 67, 91, 23))

# Manipulating the data in *args"
def is_string(*args):
    for arg in args:
        if type(arg) == str:
            print(arg.upper())
        else:
            print(f"{arg} is not a string")

is_string('a', 56, ['a', 'b'], 'c', 0, 'e', 'y', 5)

#Using *args in range function
start_end = [0,20]
print("\n",list(range(*start_end)))