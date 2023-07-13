# Example - All classes have to be halved

def classes_generator():
    yield ('History', 42)
    yield ('Math', 50)
    yield ('Biology', 56)

def halved_classes(classes):
    for _class, students_number in classes:
        yield f"{_class} - A: {int(students_number/2)} students"
        yield f"{_class} - B: {int(students_number/2)} students\n"

my_generator = halved_classes(classes_generator())
for _class in my_generator:
    print(_class)