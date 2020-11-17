"""
You can use this code to read countries data from countries.csv file,
then you can rewrite them back to another file with a new format.
"""

import csv

my_file = open("my_file.txt", "w")

with open('countries.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_reader.next()
    for row in csv_reader:
        for column in row:
            my_file.write(column + ",")
        my_file.write("\n")

my_file.close()