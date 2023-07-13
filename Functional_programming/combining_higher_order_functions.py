# Combining built-in Higher Order Functions in functional programming
from collections import namedtuple
from functools import reduce

# Combining map() + filter()
print("\n======EXAMPLE 1======")
# Creating a function that uppercase only names starting with L 
names_list = ['Ronaldo', 'Lucas', 'Julia', 'Lucia', 'Livia', 'Marcia', 'Jonas', 'Laura', 'Gabriel', 'Laerte']

uppercase = map(lambda name: name.upper(), filter(lambda name: name[0] == 'L', names_list))
for name in uppercase:
    print(name)


# Combining reduce() + filter()
print("\n======EXAMPLE 2======")
# Creating a function that returns the most expensive appetizer in the restaurant
meal = namedtuple('meal', ['name', 'price', 'category'])

m1 = meal('Onion Rings', 32.90, 'appetizer')
m2 = meal('Small chicken', 28.50, 'appetizer')
m3 = meal('Brazilian Barbecue', 99.90, 'main_meal')
m4 = meal('Feijoada', 102.90, 'main_meal')
m5 = meal('Lemon Pie', 18.60, 'dessert')
m6 = meal('Pudding', 13.50, 'dessert')
m7 = meal('Green Salad', 22.80, 'appetizer')
m8 = meal('Short Rib', 72.10, 'main_meal')
m9 = meal('Red Velvet', 20.20, 'dessert')

menu = (m1, m2, m3, m4, m5, m6, m7, m8, m9)

most_expensive_appetizer = reduce(lambda meal_1, meal_2: meal_1 if meal_1.price > meal_2.price else meal_2, filter(lambda meal: meal.category == 'appetizer', menu))
print(most_expensive_appetizer)

# Combining reduce() + map() + filter()
print("\n======EXAMPLE 3======")
# creating a function that returns the total value of shirt sales
clothes = namedtuple('clothes', ['item', 'sold_amount', 'unit_price', 'category', 'bar_code'])

c1 = clothes('Green Shirt', 7, 129.9, 'shirt', 2627382)
c2 = clothes('Yellow pants', 2, 49.9, 'pants', 4427382)
c3 = clothes('Jeans Skinny', 10, 99.9, 'jeans', 2607382)
c4 = clothes('Yellow Shirt', 11, 159.9, 'shirt', 2620182)
c5 = clothes('Black Shirt', 2, 169.5, 'shirt', 9627382)
c6 = clothes('Blue pants', 3, 49.9, 'pants', 2007382)
c7 = clothes('Black pants', 10, 89.9, 'pants', 2876082)
c8 = clothes('White Shirt', 2, 109.9, 'shirt', 2627321)

inventory = (c1, c2, c3, c4, c5, c6, c7, c8)

total_value = reduce(lambda sum_clothes1, sum_clothes2: sum_clothes1 + sum_clothes2, map(lambda shirt: shirt.sold_amount * shirt.unit_price, filter(lambda clothes: clothes.category == 'shirt', inventory)))
print(total_value)