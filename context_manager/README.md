# Context managers

## with statement
Using **with()** ensures that the files we are working on will be closed when they are no longer being used.

## Class based context managers
You can implement Class Based context managers through context manager protocol. 

You need to create both __enter __() and __exit __() methods in your classes.

#### __ enter__()
This method handles the setup and is called when entering a new **with** context.
#### __ exit__()
This method handles the teardown logic and is called when the flow of execution leaves the **with**.
This method takes 3 attributes (exc_type, exc_value, traceback)
- exc_type: exception type
- exc_value: exception value
- traceback: traceback

## contextlib
The most pythonic way to create context managers.

Uses the decorator @contextmanager to turn a function into a context manager.

## Nested context managers
Handling multiple files at the same time.

You can create nested context managers using a **with** statement inside another **with** statement.