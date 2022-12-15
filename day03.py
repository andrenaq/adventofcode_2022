# https://adventofcode.com/2022/day/3
import csv


def point(c):
    if c.islower():
        return (ord(c) - 96)
    else:
        return (ord(c) - 38)


base = []

with open('adventofcode_2022/input_files/day03_input.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter='\n')
    for row in csvReader:
        base.append(row[0])

rucksacks = []
for i in base:
    middle = int(len(i) / 2)
    rucksacks.append([i[:middle], i[middle:]])

wrong_items = {}

for rucksack in rucksacks:
    all_items = {}
    for i in range(len(rucksack[0])):
        if rucksack[0][i] not in all_items:
            all_items[rucksack[0][i]] = i

    for k in rucksack[1]:
        if k in all_items:          
            if k in wrong_items:
                wrong_items[k] += 1
            else:  
                wrong_items[k] = 1
            break
total = []
for i in wrong_items.keys():
    total.append(point(i) * wrong_items[i])

# Part 1
print("Total part 1: ", sum(total))


# Part 2
rucksacks = base

badges = {}
for i in range(0, len(rucksacks), 3):
    dict_01 = dict.fromkeys(list(rucksacks[i]), 1)
    dict_02 = dict.fromkeys(list(rucksacks[i+1]), 1)
    for k in list(rucksacks[i+2]):
        if (k in dict_01) and (k in dict_02):
            if k in badges:
                badges[k] += 1
            else:  
                badges[k] = 1
            break

total_2 = []
for i in badges.keys():
    total_2.append(point(i) * badges[i])

print("Total part 2: ", sum(total_2))
