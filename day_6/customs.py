from helpers import vacation_helpers
from collections import Counter

INPUT = "input.txt"


customs_rows = vacation_helpers.file_to_array(INPUT)

# Part 1
group_results = []
group_idx = 0
buffer = []
for row in customs_rows:
    buffer += row

    if not row:
        # get the set of unique keys e.g. ["a", "c", "x"]
        group_results.append(len(Counter(buffer).keys()))
        buffer = []

# Get last item out of buffer if necessary
if len(buffer) > 0:
    group_results.append(len(Counter(buffer).keys()))

print("All unique entries", sum(group_results))

# Part 2
group_results = []
group_idx = 0
group_size = 0
buffer = []
for row in customs_rows:
    buffer += row
    if not row:
        # get the total of unique keys e.g. [3, 1, 4]
        counts = Counter(buffer).values()
        matching_results = Counter(counts)[group_size]
        group_results.append(matching_results)
        group_size = 0
        buffer = []
    else:
        group_size += 1

# Get last item out of buffer if necessary
if len(buffer) > 0:
    counts = Counter(buffer).values()
    matching_results = Counter(counts)[group_size]
    group_results.append(matching_results)
print("All matching entries", sum(group_results))

