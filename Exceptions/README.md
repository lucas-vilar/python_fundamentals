# Exceptions in Python
Syntax to handle exceptions in Python:

    try:
        block of code to be tested
    except Exception:
        how to handle the exception
    else:
        what to do when there is no error
    finally:
        this code will be executed regardless of the result of the try and except blocks

## Raising exceptions in Python
You can raise exceptions if a condition occurs in your code.

To do this, use the **raise** keyword

## Creating custom exceptions in Python
In python, you can create your custom exceptions.

You must create a class extending from **Exception**. When the condition occurs, you can raise your custom exception like a standard one.