# How to handle exceptions in context managers
class OpeningFiles:
    def __init__(self, file, mode):
        print("class called!")
        self._file = file
        self._mode = mode

    def __enter__(self):
        print("Opening a real file...")
        self._opened_file = open(self._file, self._mode)
        return self._opened_file
     
    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)
        print(exc_value)
        print(traceback)
        self._opened_file.close()
        # If you don't want the program interrupt execution if an exception appears, return True after .close()
        return True

with OpeningFiles("my_reading_file.txt", "r") as file:
    print(file.any_method())