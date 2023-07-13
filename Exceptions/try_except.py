# Handling exceptions in Python

# Examples about how to handle exceptions
#Example 1
try:
    3 / 0
except ZeroDivisionError as e:
    print("Error:",e)
    print("You can't divide by zero")

#Example 2
colors = {'Blue' : '#128172', 'Green' : '#19280F', 'Red' : '#F5436FF0'}
def hexadecimal_code(color):
    try:
        print(f"\nThe hexadecimal code for {color} is {colors[color]}")
    except Exception as e:
        print("\nError:",e,"not registered")
    else:
        print('\ntry block successfully executed')
    finally:
        print('\nend of try block')

hexadecimal_code(input("\nType a color name to find the hexadecimal code: "))