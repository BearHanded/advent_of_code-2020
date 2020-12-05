import helpers.vacation_helpers as vacation_helpers

# CONSTANTS
INPUT = "input.txt"
TREE = "#"
OPEN = "."
SLOPE = (3, 1)


def navigate(location, slope_x, slope_y, width):
    x_wrapped = location[0] + slope_x
    x_wrapped = x_wrapped % width
    return x_wrapped, location[1] + slope_y


def tree_search(slope, landscape):
    landscape_width = len(landscape[0])
    landscape_height = len(landscape)

    location = (0, 0)
    trees_count = 0
    while location[1] < landscape_height:
        if landscape[location[1]][location[0]] == TREE:
            trees_count += 1
        location = navigate(location, slope[0], slope[1], landscape_width)

    print("TREES HIT:", trees_count)
    return trees_count


# Read in
landscape = vacation_helpers.file_to_array(INPUT)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

out = 1
for slope in slopes:
    out = out * tree_search(slope, landscape)

print("MULTIPLIED: ", out)
