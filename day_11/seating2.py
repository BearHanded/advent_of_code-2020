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


def search_slope(y, x, seats):
    slopes = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1), (1, 0), (1, 1)]
    total = 0
    dimensions = (len(seats), len(seats[0]))
    for slope in slopes:
        y_idx = y + slope[0]
        x_idx = x + slope[1]
        while (0 <= y_idx < dimensions[0]) and (0 <= x_idx < dimensions[1]):
            if seats[y_idx][x_idx] == Seating.OCCUPIED:
                total += 1
                break
            elif seats[y_idx][x_idx] == Seating.EMPTY:
                break
            y_idx += slope[0]
            x_idx += slope[1]
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
            neighbors = search_slope(row, col, seats)
            if (seats[row][col] == Seating.EMPTY) and neighbors == 0:
                new_row += Seating.OCCUPIED
                _unstable = True
            elif (seats[row][col] == Seating.OCCUPIED) and neighbors >= 5:
                new_row += Seating.EMPTY
                _unstable = True
            else:
                new_row += seats[row][col]
        new_seating.append(new_row)
    # pretty_print(new_seating)
    return new_seating, _unstable


# PART 2
print("Initial Seating")
seating_map = [[character for character in row] for row in vacation_helpers.file_to_array(INPUT)]
pretty_print(seating_map)

unstable = True
while unstable:
    seating_map, unstable = apply_rules(seating_map)
print("FINISH --- Total occupied", count_total(seating_map))
