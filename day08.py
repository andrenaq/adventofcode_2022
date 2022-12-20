# https://adventofcode.com/2022/day/3
import csv

horizontal = []
vertical = []
with open('input_files/day08_input.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter='\n')
    for row in csvReader:
        horizontal.append(row[0])
        vertical.append([])

# Creating the vertical list
for i in range(len(horizontal)):
    for k in range(len(horizontal[i])):
        vertical[k].append(horizontal[i][k])

total = 0
total += 2 * len(horizontal[0])
total += 2 * (len(horizontal) - 2)
view_total = 0
for i in range(1, len(vertical)-1):
    for k in range(1, len(horizontal[i]) - 1):
        # print(vertical[k][i], max(vertical[k][:i]), max(vertical[k][i + 1:]),
        #     max(horizontal[i][:k]), max(horizontal[i][k + 1:]))
        if max(vertical[k][:i]) < vertical[k][i] or \
         max(vertical[k][i + 1:]) < vertical[k][i] or \
         max(horizontal[i][:k]) < vertical[k][i] or \
         max(horizontal[i][k + 1:]) < vertical[k][i]:
            total += 1
        left, right = k - 1, k + 1
        left_total, right_total = 0, 0
        while left >= 0:
            left_total += 1
            if horizontal[i][left] >= horizontal[i][k]:
                break
            left -= 1
        while right < len(horizontal[i]):
            right_total += 1
            if horizontal[i][right] >= horizontal[i][k]:
                break
            right += 1

        up, down = i - 1, i + 1
        up_total, down_total = 0, 0
        while up >= 0:
            up_total += 1
            if vertical[k][up] >= vertical[k][i]:
                break
            up -= 1
        while down < len(vertical[i]):
            down_total += 1
            if vertical[k][down] >= vertical[k][i]:
                break
            down += 1

        view_total = max(
            view_total,
            left_total * right_total * up_total * down_total)

print("Part 1: ", total)
print("Part 2: ", view_total)
