# https://adventofcode.com/2022/day/3
import csv

message = ""
with open('input_files/day06_input.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        message = row[0]


def get_beggining(msg, size):
    for i in range(size, len(msg) - 1):
        if len(set(msg[i-size:i])) == len(msg[i-size:i]):
            return i
    return 0


print("Part 01: ", get_beggining(message, 4))
print("Part 02: ", get_beggining(message, 14))
