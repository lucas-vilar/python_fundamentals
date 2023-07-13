# Example 1
def even_numbers():
    even = [2,4,6,8,10,12,14,16,18,20]
    for number in even:
        yield number

def odd_numbers():
    odd = [1,3,5,7,9,11,13,15,17,19]
    for number in odd:
        yield number

def all_numbers():
    yield "\nEven numbers:"
    yield from even_numbers()
    yield "\nOdd numbers:"
    yield from odd_numbers()

numbers_generator = all_numbers()
for number in numbers_generator:
    print(number)