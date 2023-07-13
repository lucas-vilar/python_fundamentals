# Example generator
print("\n======EXAMPLE 1======")
def generator():
    print("First iteration")
    i = 1
    yield i
    print("Second iteration")
    i += 1
    yield i
    print("Third iteration")
    i += 1
    yield i
    print("Fourth iteration")
    i += 1
    yield i

example_generator = generator()
for iteration in example_generator:
    print(iteration)

# Example 2 - using next()
print("\n======EXAMPLE 2======")
second_generator = generator()
print(next(second_generator))
print(next(second_generator))
print(next(second_generator))
print(next(second_generator))

# Example 3
print("\n======EXAMPLE 3======")
my_list = [3,7,11,13,14,20,23]

def third_generator(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield f"{number} is even"
        else:
            yield f"{number} is odd"

new_generator = third_generator(my_list)
for item in new_generator:
    print(item)

# Example 4 - Generator expressions
print("\n======EXAMPLE 4======")
generator_expression = (f'Iteration {i}' for i in range(1,21))

for iteration in generator_expression:
    print(iteration)