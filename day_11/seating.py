from helpers import vacation_helpers

INPUT = "input.txt"


class Seating:
    OCCUPIED = '#'
    FLOOR = '.'
    EMPTY = 'L'


# For printing fun
class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# apply to all seats at once

# Empty && no occupied (direct or diagonal) -> occupied
# Occupied && 4+, empty
# else don't change


def count_adjacent(row, col, seats):
    total = 0
    dimensions = (len(seats), len(seats[0]))
    for row_idx in range(row - 1, min(row + 2, dimensions[0])):
        for col_idx in range(col - 1, min(col + 2, dimensions[1])):
            if row_idx < 0 or col_idx < 0 or (col_idx, row_idx) == (col, row):
                continue
            if seats[row_idx][col_idx] == Seating.OCCUPIED:
                total += 1
    return total


def count_total(seats):
    total = 0
    for row in seats:
        total += row.count(Seating.OCCUPIED)
    return total


def pretty_print(seats):
    print(" ")
    for row in seats:
        out_str = ""
        for character in row:
            if character == Seating.OCCUPIED:
                out_str += BColors.OKCYAN + character + BColors.ENDC
            elif character == Seating.EMPTY:
                out_str += BColors.OKGREEN + character + BColors.ENDC
            else:
                out_str += character
            out_str += " "
        print(out_str)


def apply_rules(seats):
    dimensions = (len(seats), len(seats[0]))
    _unstable = False
    new_seating = []
    for row in range(dimensions[0]):
        new_row = []
        for col in range(dimensions[1]):
            if (seats[row][col] == Seating.EMPTY) and (count_adjacent(row, col, seats) == 0):
                new_row += Seating.OCCUPIED
                _unstable = True
            elif (seats[row][col] == Seating.OCCUPIED) and (count_adjacent(row, col, seats) >= 4):
                new_row += Seating.EMPTY
                _unstable = True
            else:
                new_row += seats[row][col]
        new_seating.append(new_row)
    pretty_print(new_seating)
    return new_seating, _unstable


# PART 1
print("Initial Seating")
seating_map = [[character for character in row] for row in vacation_helpers.file_to_array(INPUT)]
pretty_print(seating_map)

unstable = True
while unstable:
    seating_map, unstable = apply_rules(seating_map)
print("FINISH --- Total occupied", count_total(seating_map))

# Part 2
seating_map = [character for character in vacation_helpers.file_to_array(INPUT)]
