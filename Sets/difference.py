# The difference returns all elements which belong to A but not to B

bookstore_books = {'Harry Potter', 'Game of thrones', 'Lord of the rings', '1984', 'Pride and Prejudice', 'American Gods', 'it', 'Carrie'}
my_books =  {'Harry Potter', 'Lord of the rings', '1984', 'Carrie'}

books_to_buy = bookstore_books.difference(my_books)
print(books_to_buy)