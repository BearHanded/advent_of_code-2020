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


def number_of_configs(sorted_joltage):
    jolts = [0]
    jolts += sorted_joltage.copy()
    jolts.append(sorted_joltage[-1] + 3)

    voltage_paths = {0: 1}
    # Build a map like  {0: 1, 1: 1, 4: 1, 5: 1, 6: 2, 7: 4...} listing the number of ways to each number
    for jolt in jolts[1:]:
        # sum the last 3 ways to reach this number
        voltage_paths[jolt] = \
            voltage_paths.get(jolt-1, 0) + voltage_paths.get(jolt-2, 0) + voltage_paths.get(jolt-3, 0)

    return voltage_paths


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

results = number_of_configs(joltage_sorted)
print("Results", results)
print("Total ", results[max(results.keys())])

