from helpers import vacation_helpers

FILE = "input.txt"

test_preamble = [x + 1 for x in range(25)];


def sum_is_contained(number, num_array, window_size=25, starting_index=0):
    array = num_array[starting_index:starting_index + 1 + window_size]
    for x in array:
        for y in array:
            if x == y:
                continue
            if x + y == number:
                return x, y
    return ()


def get_invalid_sum_subarray(number, num_array):
    for x_idx in range(len(num_array)):
        for y_idx in range(len(num_array)):
            array_slice = num_array[x_idx:y_idx]
            if x_idx == y_idx:
                continue
            if sum(array_slice) == number:
                return array_slice
    return []


# TEST
# print("26", sum_is_contained(26, test_preamble))
# print("49", sum_is_contained(49, test_preamble))
# print("100", sum_is_contained(100, test_preamble))
# print("50", sum_is_contained(50, test_preamble))

# Init
encoding_numbers = [int(i) for i in vacation_helpers.file_to_array(FILE)]
invalid_number = 0;

# Part One
sliding_window = 25
for idx in range(sliding_window, len(encoding_numbers)):
    if not sum_is_contained(encoding_numbers[idx], encoding_numbers,
                            starting_index=idx - sliding_window, window_size=sliding_window):
        invalid_number = encoding_numbers[idx]
        print("Invalid entry:", encoding_numbers[idx])
        break

# Part Two
sliding_window = 25
invalid_array = get_invalid_sum_subarray(invalid_number, encoding_numbers)

print("invalid array", invalid_array)
print("key ", max(invalid_array) + min(invalid_array))
