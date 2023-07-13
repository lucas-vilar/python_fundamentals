# Class based context managers
print("\n======EXAMPLE 1======")
# Opening a hypothetical file
class OpeningFiles:
    def __init__(self):
        print("class called!")

    def __enter__(self):
        print("File opened!")

    def __exit__(self, *exc):
        print("File closed!")

with OpeningFiles() as open_file:
    print("Hypothetical file!")

print("\n======EXAMPLE 2======")
# Opening a real file
class OpeningRealFiles:
    def __init__(self, file, mode):
        print("class called!")
        self._file = file
        self._mode = mode

    def __enter__(self):
        print("Opening a real file...")
        self._opened_file = open(self._file, self._mode)
        return self._opened_file
     
    def __exit__(self, *exc):
        print("File closed!")
        self._opened_file.close()

with OpeningRealFiles("class_based_context_manager.txt", "r") as real_file:
    print(real_file.read())