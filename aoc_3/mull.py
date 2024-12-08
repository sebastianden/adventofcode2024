import re

# Load imput

with open("input.txt") as f:
    lines = f.readlines()
    input = "".join(lines)

# Part 1
# Regex match all instances of mul(int,int)
matches = re.findall(r"mul\((\d+),(\d+)\)", input)

# Multiply all instances of mul(int,int)
result = 0
for m in matches:
    result += int(m[0]) * int(m[1])
print(result)

# Part 2

# Search indices of all "do()" and "don't()" in string
do_indices = [0] + [m.start() for m in re.finditer("do\(", input)]
dont_indices = [m.start() for m in re.finditer("don't\(", input)]

# For each do index find the closest next dont index and save as interval
intervals = []
for do in do_indices:
    closest_dont = min([dont for dont in dont_indices if dont > do])
    intervals.append((do, closest_dont))

# For every index in the string check if it is in any interval and create a list of all indices that are in any interval
indices = [i for i in range(len(input)) if any([interval[0] <= i <= interval[1] for interval in intervals])]

# Get a new input string with all indices that are in any interval
new_input = "".join([input[i] for i in range(len(input)) if i in indices])

# Regex match all instances of mul(int,int)
matches = re.findall(r"mul\((\d+),(\d+)\)", new_input)

# Multiply all instances of mul(int,int)
result = 0
for m in matches:
    result += int(m[0]) * int(m[1])
print(result)