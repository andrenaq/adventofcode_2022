# https://adventofcode.com/2022/day/3
import csv


def point(c):
    if c.islower():
        return (ord(c) - 96)
    else:
        return (ord(c) - 38)


base = []

with open('input_files/day04_input.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        first_elf = [int(section) for section in row[0].split("-")]
        second_elf = [int(section) for section in row[1].split("-")]
        base.append([first_elf, second_elf])

# Part 1
total = 0
list_of_results = []
for i in base:
    if ((i[0][0] <= i[1][0] and i[0][1] >= i[1][1])
       or (i[1][0] <= i[0][0] and i[1][1] >= i[0][1])):
        total += 1
        # list_of_results.append(i)

print("Fully contained pairs: ", total)
# print("List of fully contained pairs: ", list_of_results)

# Part 2
total2 = 0
# list_of_results = []
for i in base:
    if ((i[0][0] >= i[1][0] and i[0][0] <= i[1][1])
       or (i[0][1] >= i[1][0] and i[0][1] <= i[1][1])) \
     or ((i[0][0] <= i[1][0] and i[0][1] >= i[1][0])
       or (i[0][0] <= i[1][1] and i[0][1] >= i[1][1])):
        total2 += 1
        # list_of_results.append(i)

print("Overlap pairs: ", total2)
# print("List of overlap pairs: ", list_of_results)
