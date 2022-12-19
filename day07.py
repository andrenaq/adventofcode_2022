# https://adventofcode.com/2022/day/3
import csv

input = []
with open('input_files/day07_input.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        input.append(row[0].split())

# good candidate to use classes
def total_dir(folder, all_files):
    total = 0
    if len(all_files[folder]["dir_list"]) == 0:
        total += sum(all_files[folder]["files"].values())
    else:
        for i in all_files[folder]["dir_list"]:
            total += total_dir(i, all_files)
        total += sum(all_files[folder]["files"].values())
    return total

dir = {}
current_dir = []
for cmd in input:
    if cmd[0] == "$":
        if cmd[1] == "cd" and cmd[2] != "..":
            current_dir.append(cmd[2])
            dir["/".join(current_dir)] = {"dir_list": [], "files": {}}
        elif cmd[1] == "cd" and cmd[2] == "..":
            current_dir.pop()
        else:  # ls ->  do nothing
            continue
    elif cmd[0].isnumeric():
        dir["/".join(current_dir)]["files"][cmd[1]] = int(cmd[0])
    elif cmd[0] == "dir":
        dir["/".join(current_dir)]["dir_list"].append("/".join(current_dir) +
         "/" + cmd[1])

list_dir = []
total = []
space_needed = 30000000 - (70000000 - total_dir("/base", dir))
print(space_needed)
for key in dir.keys():
    # 26363334
    # 2810068
    total_size = total_dir(key, dir)
    print(total_size, key)
    if total_size > space_needed:
        print(key,  dir[key]["dir_list"], dir[key]["files"])
        list_dir.append(key)
        total.append(total_size)
print("============================")
print(total)
print("============================")
print(min(total))

# di = "ftj"
# print(dir[di]["dir_list"], dir[di]["files"])
# print(",".join(list_dir))