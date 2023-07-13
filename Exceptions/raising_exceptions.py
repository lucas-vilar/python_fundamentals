# Raising exceptions in Python

def age(age):
    if age > 0:
        print("Valid age")
    else:
        raise Exception(f"{age} is not a valid age!")
    
age(int(input("Type your age: ")))