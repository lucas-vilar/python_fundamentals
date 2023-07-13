# Reading csv files in Python
import csv
from collections import namedtuple

students = namedtuple("students", ["id", "name", "phone_number", "email"])

# Opening the csv file
with open('reading_csv.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=";", quotechar="|")
    next(reader) # Since the first line is the header

    mapper  = tuple(map(lambda student: students(int(student[0]), student[1], student[2], student[3]), reader))
    _class = tuple(mapper)

print(_class)