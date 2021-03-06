import collections

from helpers import vacation_helpers

FILE = "input.txt"
VALID_KEYS = [1, 2, 3]

def is_valid_joltage(sorted_joltage):
    jolts = [0]
    jolts += sorted_joltage.copy()
    jolts.append(sorted_joltage[-1] + 3)

    joltage_map = {1: 0, 2: 0, 3: 0}
    for idx in range(0, len(jolts) - 1):
        diff = jolts[idx + 1] - jolts[idx]
        if diff in VALID_KEYS:
            joltage_map[diff] += 1
        else:
            return {}
    return joltage_map


def number_of_configs(sorted_joltage, valid_map=[]):
    print("Working...", len(valid_map), "solution", end='\r')

    # Naive
    # Check if checked
    for elem in valid_map:
        if collections.Counter(elem) == collections.Counter(sorted_joltage):
            return 0
    if not is_valid_joltage(sorted_joltage):
        return 0
    valid_map.append(sorted_joltage)

    total = 1
    for idx in range(1, len(sorted_joltage) - 1):  # first and last are fixtures
        sub_list = sorted_joltage.copy()
        sub_list.pop(idx)
        total += number_of_configs(sub_list, valid_map)
    return total


joltage_array = [int(i) for i in vacation_helpers.file_to_array(FILE)]
joltage_sorted = joltage_array.copy()
joltage_sorted.sort()

# Part One:
highest_rating = joltage_sorted[-1] + 3

print("Rated For: ", highest_rating)
jolt_map = is_valid_joltage(joltage_sorted.copy())
print("jolt types", jolt_map)
print("Answer: ", jolt_map[1] * jolt_map[3])

# PART 2
# Always preserve 0 and max in array
# Any diff < 3 can be tested without
# Build

validity = []
print(number_of_configs(joltage_sorted, validity))
print(validity, len(validity))

