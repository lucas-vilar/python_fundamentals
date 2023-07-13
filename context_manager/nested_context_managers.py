# Nested context managers
# Working with multiple files at the same time
from contextlib import contextmanager

@contextmanager
def file_handling(file, mode):
    opened_file = open(file, mode)
    try:
        yield opened_file
    except Exception as e:
        print(e)
    finally:
        opened_file.close()

name = 'Lucas'
with file_handling("default_message.txt", "r") as reading_file:
    with file_handling(f"{name}_message.txt", "w") as writing_file:
        writing_file.write(f"Dear, {name}\n")
        writing_file.write(reading_file.read())
