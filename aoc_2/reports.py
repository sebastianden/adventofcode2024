# Read input data

reports = []
with open("input.txt") as f:
    data = f.read().splitlines()
    for line in data:
        reports.append([int(item) for item in line.split()])


def is_safe(report):
    diff = [a - b for a, b in zip(report, report[1:])]
    # If all negative or all positive
    if all(x > 0 for x in diff) or all(x < 0 for x in diff):
        # If no abs(item) larger than 3
        if all(abs(x) < 4 for x in diff):
            return True
    return False


count = 0
for report in reports:
    if is_safe(report):
        count += 1


# Part 2

count = 0
for report in reports:
    # Check if report is already safe
    if is_safe(report):
        count += 1
        continue
    # Check if report would be safe without the first item or the second item or etc.
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            count += 1
            break

print(count)
