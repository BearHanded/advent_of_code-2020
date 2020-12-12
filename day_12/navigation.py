from enum import Enum

from helpers import vacation_helpers

FILE = "input.txt"


class Directions:
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"


CARDINAL = [Directions.NORTH, Directions.EAST, Directions.SOUTH, Directions.WEST]


def navigate(instruction, starting_dir, location):
    command = instruction[0]
    magnitude = int(instruction[1:])

    # PROCESS TURNS
    if command == Directions.LEFT:
        idx = CARDINAL.index(starting_dir) - int(magnitude / 90)
        if idx < 0:
            idx += len(CARDINAL)
        starting_dir = CARDINAL[idx]
    elif command == Directions.RIGHT:
        idx = CARDINAL.index(starting_dir) + int(magnitude / 90)
        if idx >= len(CARDINAL):
            idx -= len(CARDINAL)
        starting_dir = CARDINAL[idx]
    elif command == Directions.FORWARD:
        # Convert direction to command
        command = starting_dir

    # DIRECTIONS
    if command == Directions.NORTH:
        location[1] += magnitude
    elif command == Directions.EAST:
        location[0] += magnitude
    elif command == Directions.SOUTH:
        location[1] -= magnitude
    elif command == Directions.WEST:
        location[0] -= magnitude
    print("  - ", command, magnitude, " => ", coords, starting_dir)

    return location, starting_dir


nav_instructs = [i for i in vacation_helpers.file_to_array(FILE)]

# Part 1
print("BEGIN 1, ", FILE)
direction = Directions.EAST
coords = [0, 0]
for instruct in nav_instructs:
    coords, direction = navigate(instruct, direction, coords)

print("END", coords, direction)
print("Manhattan Distance, ", abs(coords[0]) + abs(coords[1]))
