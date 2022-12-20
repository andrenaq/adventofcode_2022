# https://adventofcode.com/2022/day/3
import csv

instructions1, instructions2 = [], []

with open('input_files/day09_input.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter='\n')
    for row in csvReader:
        split_row = row[0].split()
        instructions1.append([split_row[0], int(split_row[1])])
        instructions2.append([split_row[0], int(split_row[1])])

positions = []
# Head = 0, nots 1-9
nn = 9  # number of nots
for i in range(nn + 1):
    positions.append([220, 15])

p_h = [500, 500]
p_t = [500, 500]
pt_positions = []
pt_positions.append(str(p_t[0]) + str(p_t[1]))


def check_distances_and_move(p_h, p_t):
    while p_h[0] - p_t[0] >= 2 or \
     p_t[0] - p_h[0] >= 2 or \
     p_h[1] - p_t[1] >= 2 or \
     p_t[1] - p_h[1] >= 2:
        if p_h[0] > p_t[0] and p_h[0] - p_t[0] > 1:
            if p_h[1] != p_t[1]:
                # Moving up
                if p_h[1] > p_t[1]:
                    p_t[1] += 1
                # Moving down
                else:
                    p_t[1] -= 1
            # Move right
            p_t[0] += 1
        # Checking Left distince
        elif p_h[0] < p_t[0] and p_t[0] - p_h[0] > 1:
            if p_h[1] != p_t[1]:
                # Moving up
                if p_h[1] > p_t[1]:
                    p_t[1] += 1
                # Moving down
                else:
                    p_t[1] -= 1
            # Move left
            p_t[0] -= 1
        elif p_h[1] > p_t[1] and p_h[1] - p_t[1] > 1:
            if p_h[0] != p_t[0]:
                # Moving right
                if p_h[0] > p_t[0]:
                    p_t[0] += 1
                # Moving left
                else:
                    p_t[0] -= 1
            p_t[1] += 1
        elif p_h[1] < p_t[1] and p_t[1] - p_h[1] > 1:
            if p_h[0] != p_t[0]:
                # Moving right
                if p_h[0] > p_t[0]:
                    p_t[0] += 1
                # Moving left
                else:
                    p_t[0] -= 1
            p_t[1] -= 1
    return p_t


def execute_instructions(inst):
    if inst[0] == "R":
        jay = True
        multi = 1
    elif inst[0] == "L":
        jay = True
        multi = -1
    elif inst[0] == "U":
        jay = False
        multi = -1
    else:  # i[0] == "D":
        jay = False
        multi = 1
    return [jay, multi]


for i in instructions1:
    jay, multi = execute_instructions(i)
    while i[1] > 0:
        if jay:  # changing on y axis
            p_h[1] += multi
        else:  # changing on x axis
            p_h[0] += multi

        p_t = check_distances_and_move(p_h, p_t)
        pt_positions.append(str(p_t[0]) + str(p_t[1]))
        i[1] -= 1

print("Part 1: ", len(set(pt_positions)))

pt_positions = []
last_position = {}
last_position[str(positions[nn][0]) + "," + str(positions[nn][1])] = 1
for i in instructions2:
    jay, multi = execute_instructions(i)
    while i[1] > 0:
        if jay:
            positions[0][1] += multi
        else:
            positions[0][0] += multi
        for k in range(1, nn + 1):
            positions[k] = check_distances_and_move(
                positions[k-1],
                positions[k]
                )
        pt_positions.append(str(positions[1][0]) + str(positions[1][1]))
        a = str(positions[nn][0])
        b = str(positions[nn][1])
        if (a + "," + b) in last_position:
            last_position[a + "," + b] += 1
        else:
            last_position[a + "," + b] = 1
        i[1] -= 1

print("Part 2: ", len(last_position))
