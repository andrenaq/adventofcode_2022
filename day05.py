# https://adventofcode.com/2022/day/3
import csv
import copy
# PARSING THE DAATA =========================================================
base, instructions = [], []
with open('input_files/day05_input.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        if len(row) > 0:
            if row[0][0] == "m":
                instructions.append(row[0].split(" "))
            else:
                r = []
                k = row[0].replace("    [", "# [").replace("]    ", "] # ") \
                    .replace("#    ", "# # ").replace("    #", " # # ") \
                    .replace("[", "").replace("    ", " #") \
                    .replace("]", "").split()
                base.insert(0, k)
base.pop(0)
crates_part1 = []
for i in range(len(base[0])):
    crates_part1.append([])
    for k in range(len(base)):
        if base[k][i] != "#":
            crates_part1[i].append(base[k][i])
crates_part2 = copy.deepcopy(crates_part1)
# END OF # PARSING  =========================================================


# PART 1
def execute_orders_part_1(inst, crates):
    for i in range(int(inst[1])):
        crates[int(inst[5]) - 1] \
            .append((crates[int(inst[3]) - 1].pop()))
    return crates


for i in instructions:
    crates_part1 = execute_orders_part_1(i, crates_part1)

top_of_crates = []
for i in crates_part1:
    top_of_crates.append(i.pop())
print("".join(top_of_crates))


# PART 2
def execute_orders_part_2(inst, crates):
    crates[int(inst[5]) - 1].extend(crates[int(inst[3]) - 1][-int(inst[1]):])
    crates[int(inst[3]) - 1] = crates[int(inst[3]) - 1][:-int(inst[1])]
    return crates


for i in instructions:
    crates_part2 = execute_orders_part_2(i, crates_part2)
top_of_crates = []
for i in crates_part2:
    if len(i) > 0:
        top_of_crates.append(i.pop())
print("".join(top_of_crates))
