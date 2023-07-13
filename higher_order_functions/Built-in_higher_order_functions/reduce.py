# reduce() function in Python
from functools import reduce

print("\n======EXAMPLE 1======")
numbers_list = [10, 12, 6, 8, 11, 50]
sum_all = reduce(lambda number1, number2: number1 + number2, numbers_list)
print(sum_all)

print("\n======EXAMPLE 2======")
# Returning the most expensive meal in the restaurant
meals = {'Brazilian Barbecue' : 87.90, 'Japanese sushi' : 92.70, 'Italian Pizza' : 66.50, 'Korean chicken' : 70.90}
most_expensive = reduce(lambda meal1, meal2 : meal1 if meals[meal1] > meals[meal2] else meal2, meals)
print(most_expensive) 