# https://adventofcode.com/2022/day/2
import csv

list_of_values = []

with open('day02_input.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter='\n')
    for row in csvReader:
        list_of_values.append(row[0].split())
# A -> ROCK
# B -> PAPER
# C -> SCISSORS

# Part 1
total = 0
mapping = {"Y": "B", "X": "A", "Z": "C"}
shape_pointing = {"A": 1, "B": 2, "C": 3}
outcome_pointing = {
    "AB": 6,
    "AC": 0,
    "BA": 0,
    "BC": 6,
    "CA": 6,
    "CB": 0
}

total = 0
for play in list_of_values:
    final_play = mapping[play[1]]
    shape = shape_pointing[final_play]
    if str(play[0]) == final_play:
        total += shape + 3
    else:
        out_come = outcome_pointing[str(play[0]) + final_play]
        total += shape + out_come

print("Part 1 total: ", total)

# Part 2
mapping = {
    "AY": [3, 1], "AX": [0, 3], "AZ": [6, 2],
    "BY": [3, 2], "BX": [0, 1], "BZ": [6, 3],
    "CY": [3, 3], "CX": [0, 2], "CZ": [6, 1]
    }
total = 0
for play in list_of_values:
    total += sum(mapping[play[0] + play[1]])

print("Part 2 total: ", total)
