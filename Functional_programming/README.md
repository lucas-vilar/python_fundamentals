# Functional Programming
Functional programming is a paradigm in which the code is structured mainly in the form of functions. In functional programming, a function is expected to be “pure”, which means it shouldn't have any side effects, such as do not change the state of an external variable. The function can read an external variable, but must not change it!

In this paradigm we usually work with immutable data, like namedTuple.

## Working with immutable data
In this paradigm we usually work with immutable data due to: 
- Thread-safe manipulation
- Preventing the programmer from accidentaly changing a value
  
## Combining built-in Higher Order Functions

One of the most powerful tools used in functional programming in Python is the combination of map() filter() and reduce() functions to avoid directly iterating our functions.

