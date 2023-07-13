# Generator methods

# Example 1 - send()
print("\n======EXAMPLE 1======")
def generator():
    index = 1
    while True:
        send_variable = yield index
        
        if send_variable is not None:
            index += send_variable
        index +=1
        
my_generator = generator()
print(next(my_generator))
print(next(my_generator))
print(my_generator.send(10))

# Example 2 - send()
print("\n======EXAMPLE 2======")
MAX_STUDENTS = 15

def get_student_ids():
    student_id = 1
    while student_id <= MAX_STUDENTS:
        n = yield student_id

        if n is not None:
            student_id = n
            continue
   
        student_id +=1

student_id_generator = get_student_ids()
for i in student_id_generator:
    if i == 1:
        i = student_id_generator.send(5)
    print(i) 

# Example 3 - throw()
print("\n======EXAMPLE 3======")
def student_id_generator():
    for id in range(1,50):
        yield id

student_generator = student_id_generator()
for id in student_generator:
#    if id == 30:
#        student_generator.throw(ValueError, "Maximum capacity reached!")
    print(id)

# Example 4 - close()
print("\n======EXAMPLE 4======")
def close_generator():
    for i in range(1, 1001):
        yield i
        
my_close_generator = close_generator()
for item in my_close_generator:
    print(item)
    if item == 25:
        my_close_generator.close()