# map() function in Python
print("\n======EXAMPLE 1======")
number_list = [2, 5, 9, 15, 20]

number_plus_10 = map(lambda number: number + 10, number_list)
for number in number_plus_10:
    print(number)

print("\n======EXAMPLE 2======")
# Function that doubles odd numbers
odd_numbers = map(lambda number: number * 2 if number % 2 != 0 else number, number_list)
for number in odd_numbers:
    print(number)