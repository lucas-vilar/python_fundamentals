string = "Python"

print('Iterating a string\n')
for letter in string:
    print(f"Letter: {letter}")

print('\nSlicing a string')
print(string[:2])
print(string[::-1])

print("\nlen() method:")
print(len(string))

print("\nlower() method:")
print(string.lower())

print("\nupper() method:")
print(string.upper())

print("\nstrip() method:")
new_string = "             I love python              "
print(new_string)
print(new_string.strip())

print("\nsplit() method:")
split_string = "Python Java C# Ruby PHP"
print(split_string.split(" "))

print("\njoin() method:")
print("-".join(string))

print("\nreplace() method:")
hello_string = "Hello, world!"
print(hello_string.replace("world", "Python"))

print("\nindex() method:")
print(string.index("o"))

print("\ncount() method:")
count_string = "Python Django Flask"
print(count_string.count("o"))

print("\npartition() method:")
partition_string = "Python-Django-Flask"
print(partition_string.partition("-"))