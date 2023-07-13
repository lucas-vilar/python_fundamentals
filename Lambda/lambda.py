# Lambda function in Python
print("\n======EXAMPLE 1======")
first_lambda = lambda n1, n2: n1 + n2
print(first_lambda(3, 5))

print("\n======EXAMPLE 2======")
exclamation_mark = lambda string: string+"!"
print(exclamation_mark('Hello'))

print("\n======EXAMPLE 3======")
higher_than_10 = lambda number: "Is higher than 10" if number > 10 else "Is not higher than 10"
print(higher_than_10(43))