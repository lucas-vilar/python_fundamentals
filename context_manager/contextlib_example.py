# Example
from contextlib import contextmanager

@contextmanager
def opening_file_contextlib(file, mode):
    opened_file = open(file, mode)
    try:
        yield opened_file
    except Exception:
        print("Error ocurred!")
    finally:
        opened_file.close()

with opening_file_contextlib("my_reading_file.txt", "r") as my_file:
    print(my_file.read())