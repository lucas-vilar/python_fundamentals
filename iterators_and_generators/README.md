# Iterators and generators in Python
## Iterators
Iterators in Python are objects that allow you to iterate through elements in a collection. To create a new iterator you must follow the **Iterator protocol**:
#### Iterator protocol:
You can create a new iterator using two special methods: __ iter __( ) and __ next __().

#### __ iter__() method:
This method creates a new iterator object. This is required in order to use containers and iterators with the for statement.
 #### __ next __() method:
Used to manually iterate through the items of an iterator. Returns the next item. If no more items are found, throws the StopIteration exception.

## Creating custom iterators
You can also create custom iterators in Python using the iterator protocol (Example 2)

## Built-in iterators in Python
Python has several ready-to-use custom iterators:
#### count()
Count() is an infinite iterator that will repeat an infinite number of times with no trailing period, and no StopIteration exception will be thrown. This interator will count from a first value until we provide some kind of stopping condition. The base syntax of the function looks like this:

count(start_value, intervals) - **Example 1**

#### chain()
Takes one or more iterables and combines them into a single iterator. The base syntax of the function looks like this:

chain(*iterables) -  **Example 2**

#### combinations()
This iterator will produce tuples that contains combinations of all given elements, where the order doesn't matter. The base syntax of the function looks like this:

combinations(iterable, n_elements) - **Example 3**

#### permutations()
This iterator will produce tuples that contains permutations of all given elements, where the order matter. The base syntax of the function looks like this:

permutations(iterable, n_elements) - **Example 4**

## Generators
Generators are functions that return an iterator that produce a sequence of values when iterated over. Instead of use "return", to create a generator you must use the "yield" keyword. Furthermore, generator functions don't finish when return a value.

You can manually iterate over a generator using the next(function) or iterate through a for loop. - **Examples 1 - 4**

## Combining generators
You can combine two or more generators into one using the syntax:

 **yield from generator_name()** - **Example 1**

 ## Generator methods
 #### send()
 This method allows us to send a value to a generator using the yield expression. If you assign yield to a variable, the argument passed to the send() method will be assigned to that variable. Calling send() will also cause the generator to iterate.

**variable = yield index** - **Examples 1 and 2**

#### throw()
Provides the ability to throw an exception within the generator from a certain point. - **Example 3**

#### close()
Finishes a generator early. Once the close() method is called, the generator is finished. - **Example 4**

## Generators pipeline
The output of one generator function have to be the input of another generator function.

In this system you can break down complex operations into smaller parts, where they can be grouped together to achieve the desired result.