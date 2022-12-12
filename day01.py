# https://adventofcode.com/2022/day/1
import csv

elf, partial = 0, 0
elfs, list_of_values = [], []

with open('input_files/day01_imput.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter='\n')
    for row in csvReader:
        list_of_values.append(row)

for i in list_of_values:
    if len(i) != 0:
        partial += float(i[0])
        if i == len(list_of_values) - 1:
            elfs.append(partial)
    else:
        elfs.append(partial)
        partial = 0
        elf += 1

# First part
print("elfs max calories: ", max(elfs))

# TOP 3
print("TOP 3 max calories: ", sum(sorted(elfs)[-3:]))
