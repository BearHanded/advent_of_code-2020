target = 2020

fp = open('./input.txt', 'r')
input_iterable = map(lambda x: int(x), fp.readlines())
num_array = list(input_iterable)

idx = 0
match_found = False
for num in num_array:
    second_idx = 0
    for second in num_array:
        third_idx = 0
        for third in num_array:
            if (num + second + third) == 2020 and (idx != second_idx) and (third_idx != second_idx) and (idx != third_idx):
                # Match
                match_found = True
                break
            third_idx += 1
        if match_found:
            break
        second_idx += 1
    if match_found:
        break
    idx += 1

if match_found:
    print("Match:", num, second, third)
    print("Multiplied: ", num * second * third)
else:
    print("No Match")

# Find entries that sum to 2020


# Multiply
