#Creating a function with different kinds of arguments

def student_info(name, *subjects, school_name, **student_contacts):
    print(name)
    print(subjects)
    print(school_name)
    print(student_contacts)

student_info('Lucas', 'History', 'Math', 'Biology', school_name='Rio de Janeiro School', phone_number = '12345678', email = 'lucas@email.com')