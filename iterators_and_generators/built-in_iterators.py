import itertools

# count()
# Example 1 - how many 40kg boxes fit in the truck that supports up to 2500kg?
print("\n======EXAMPLE 1======")
max_capacity = 250
n_boxes = 0

for weight in itertools.count(40, 40):
    if weight > max_capacity:
        print(f"\nThe truck supports {n_boxes} boxes")
        break
    n_boxes += 1

# chain()
# Example 2 - Combining different iterators in one
print("\n======EXAMPLE 2======")
appetizer = ['Green salad', 'Onion rings', 'Mushroom Soup', 'Chicken wings']
main_meal = ['Steak', 'Pork', 'Shrimp fried rice', 'Chicken katsu']
dessert = ('Ice-cream', 'Chocolate', 'Fruit salad')

complete_menu = itertools.chain(appetizer, main_meal, dessert)
for item in complete_menu:
    print(item)
print("")

# combinations()
# Example 3 - Making a combination of different colors
print("\n======EXAMPLE 3======")
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'White', 'Orange']
combinations = itertools.combinations(colors, 3)

for combination in combinations:
    print(combination)

# permutations()
# Example 4 - Creating an anagram with permutations()
print("\n======EXAMPLE 4======")
anagram = itertools.permutations('LOVE', 4)
for item in anagram:
    print(item)