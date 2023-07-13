# filter() function in Python

print("\n======EXAMPLE 1======")
number_list = [2, 5, 9, 15, 20, 22, 25]
# Creating a function that filters only even number
even_numbers = filter(lambda number : number % 2 == 0, number_list)
for number in even_numbers:
    print(number)

print("\n======EXAMPLE 2======")
names_list = ['Lucas', 'Maria', 'Julia', 'Laura', 'Leandro', 'Mauro', 'Lucia']
# Creating a function that filters only names that start with L
names_with_l = filter(lambda name : name[0] == 'L', names_list)
for name in names_with_l:
    print(name)