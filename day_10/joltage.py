from helpers import vacation_helpers

FILE = "input.txt"

joltage_array = [int(i) for i in vacation_helpers.file_to_array(FILE)]
joltage_sorted = joltage_array.copy()
joltage_sorted.append(0) # ADD IN OUTLET (0)
joltage_sorted.sort()

highest_rating = joltage_sorted[-1] + 3
joltage_sorted.append(highest_rating) # ADD IN HIGHEST RATING FOR DEVICE

print("Rated For: ", highest_rating)

jolt_map = {1: 0, 2: 0, 3: 0}
for idx in range(0, len(joltage_sorted)-1):
    print("pair", joltage_sorted[idx], joltage_sorted[idx + 1])
    diff = joltage_sorted[idx + 1] - joltage_sorted[idx]
    if jolt_map[diff] >= 0:
        jolt_map[diff] += 1
    else:
        print("INVALID JOLTAGE ", joltage_sorted[idx + 1], " AND ", joltage_sorted[idx])

print("jolt types", jolt_map)
print("Answer: ", jolt_map[1] * jolt_map[3])



# PART 2
# Always preserve 0 and max in array
# Any diff < 3 can be tested without
# Build 