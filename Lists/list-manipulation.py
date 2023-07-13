my_list = ['A', 1, 'B']
my_second_list = [2, 'C', 3]

print('\nextend() method: ')
my_list.extend(my_second_list)
print(my_list)

print('\nappend() method: ')
my_list.append("D")
print(my_list)

print('\ninsert() method: ')
my_list.insert(1, "New item at index 1")
print(my_list)

print('\npop() method: ')
removed_item = my_list.pop(1)
print(removed_item, my_list)

print('\nremove() method: ')
my_list.remove("D")
print(my_list)

print('\nindex() method: ')
print(my_list.index('C'))

print('\ncount() method: ')
print(my_list.count('C'))

print('\nsort() method: ')
list_to_sort = [2, 45, 11, 0, 3, 56, 10, 22, 21, 6, 9]
list_to_sort.sort()
print(list_to_sort)

print('\nreverse() method: ')
list_to_sort.reverse()
print(list_to_sort)

print('\nclear() method: ')
list_to_sort.clear()
print(list_to_sort)