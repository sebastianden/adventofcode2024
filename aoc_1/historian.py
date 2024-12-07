# Load input data

list1 = []
list2 = []
with open("input.txt") as f:
    data = f.read().splitlines()
    for line in data:
        item1, item2 = line.split()
        list1.append(int(item1))
        list2.append(int(item2))

list1 = sorted(list1)
list2 = sorted(list2)

diff = [abs(a - b) for a, b in zip(list1, list2)]

print(sum(diff))

similarity = 0

for item in list1:
    # Count how often the item appears in list2
    similarity += item * list2.count(item)

print(similarity)
