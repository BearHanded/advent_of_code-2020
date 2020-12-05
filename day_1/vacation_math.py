target = 2020

fp = open('./input.txt', 'r')
input_iterable = map(lambda x: int(x), fp.readlines())
num_array = list(input_iterable)

idx = 0
match_found = False
for num in num_array:
    comparison_idx = 0
    for other_num in num_array:
        if (num + other_num) == 2020 and (idx != comparison_idx):
            # Match
            match_found = True
            break
        comparison_idx += 1
    if match_found:
        break
    idx += 1

if match_found:
    print("Match: ", num, " ", other_num)
    print("Multiplied: ", num * other_num)
else:
    print("No Match")

# Find entries that sum to 2020


# Multiply
