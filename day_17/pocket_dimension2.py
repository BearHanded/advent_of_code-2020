from helpers import vacation_helpers

FILE = "input.txt"

ACTIVE = "#"
INACTIVE = "."
POTENTIAL_ENERGY = 1
STATE = 0


def cycle_dimension(dimension):
    # Process active and potential
    for x in list(dimension.keys()):
        for y in list(dimension[x].keys()):
            for z in list(dimension[x][y].keys()):
                for w in list(dimension[x][y][z].keys()):
                    if dimension[x][y][z][w][STATE] is ACTIVE:
                        active_neighbors = count_active_neighbors(dimension, x, y, z, w)
                        if not (2 <= active_neighbors <= 3):
                            dimension[x][y][z][w][POTENTIAL_ENERGY] = -1

    # Commit Potential Energy
    for x in dimension:
        for y in dimension[x]:
            for z in dimension[x][y]:
                for w in dimension[x][y][z]:
                    if dimension[x][y][z][w][STATE] is INACTIVE and dimension[x][y][z][w][POTENTIAL_ENERGY] == 3:
                        dimension[x][y][z][w][STATE] = ACTIVE
                    elif dimension[x][y][z][w][STATE] is ACTIVE and dimension[x][y][z][w][POTENTIAL_ENERGY] == -1:
                        dimension[x][y][z][w][STATE] = INACTIVE
                    dimension[x][y][z][w][POTENTIAL_ENERGY] = 0

    return dimension


def count_active_neighbors(dimension, x, y, z, w):
    # Count neighbors AND build potential energy
    # dance around active cell
    # if -1, do not add more potential

    active_neighbors = 0
    x_range = [x - 1, x, x + 1]
    y_range = [y - 1, y, y + 1]
    z_range = [z - 1, z, z + 1]
    w_range = [w - 1, w, w + 1]

    for x_idx in x_range:
        if x_idx not in dimension.keys():
            dimension[x_idx] = {}
        for y_idx in y_range:
            if y_idx not in dimension[x_idx].keys():
                dimension[x_idx][y_idx] = {}
            for z_idx in z_range:
                if z_idx not in dimension[x_idx][y_idx].keys():
                    dimension[x_idx][y_idx][z_idx] = {}
                for w_idx in w_range:
                    if w_idx not in dimension[x_idx][y_idx][z_idx].keys():
                        dimension[x_idx][y_idx][z_idx][w_idx] = [INACTIVE, 0]
                    if x_idx is x and y_idx is y and z_idx is z and w_idx is w:
                        continue
                    # COUNT AND ADD POTENTIAL
                    if dimension[x_idx][y_idx][z_idx][w_idx][STATE] is ACTIVE:
                        active_neighbors += 1
                    elif dimension[x_idx][y_idx][z_idx][w_idx][POTENTIAL_ENERGY] != -1:
                        dimension[x_idx][y_idx][z_idx][w_idx][POTENTIAL_ENERGY] += 1

    return active_neighbors


def print_dimension(dimension):
    # EXPENSIVE. FOR DEBUGGING. MAY NEED TO DISABLE
    x_keys = list(dimension.keys())
    x_keys.sort()
    for x in x_keys:
        print("-- X = ", x, "--")
        y_keys = list(dimension[x].keys())
        y_keys.sort()
        for y in y_keys:
            z_keys = list(dimension[x][y].keys())
            z_keys.sort()
            for z in z_keys:
                w_keys = list(dimension[x][y][z].keys())
                w_keys.sort()
                str_out = "  "
                for w in w_keys:
                    str_out += dimension[x][y][z][w][STATE]
                print(str_out)
    sum_active(pocket_dimension)


def sum_active(dimension):
    total = 0
    for x in dimension:
        for y in dimension[x]:
            for z in dimension[x][y]:
                for w in dimension[x][y][z]:
                    if dimension[x][y][z][w][STATE] is ACTIVE:
                        total += 1
    print("Total Active:", total)


# PART ONE
dimension_start = vacation_helpers.file_to_array(FILE)
print("Starting configuration:")
x_len = range(len(dimension_start))
y_len = range(len(dimension_start[0]))

plane = {i: {j: [dimension_start[i][j], 0] for j in y_len} for i in x_len}
pocket_dimension = {0: {0: plane}}
print_dimension(pocket_dimension)

for cycle in range(1, 7):
    print("---- CYCLE", cycle, "----")
    pocket_dimension = cycle_dimension(pocket_dimension)
    print_dimension(pocket_dimension)
