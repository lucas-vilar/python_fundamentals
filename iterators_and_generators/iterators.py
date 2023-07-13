# Iterators in Python

# Methods iter() and next()
dogs = ['Pinscher', 'Bulldog', 'Poodle', 'Vira-Lata']
# converts dog to an interable list
iterable_list = dogs.__iter__()
# __next__() returns the next element
print(iterable_list.__next__())
print(iterable_list.__next__())
print(iterable_list.__next__())
print(iterable_list.__next__())
# if __next__() is called again it will raise a StopIteration Exception
#print(iterable_list.__next__())

print("\n============Creating a custom iterator============")
class CustomCustomer:
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        #defines the iterator limits
        if self.index > 20:
            raise StopIteration
        else:
            self.index +=1
            return f"Customer {self.index}"

customers = CustomCustomer()
for customer in customers:
    print(customer)