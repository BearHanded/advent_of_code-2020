from enum import Enum
from math import sin, cos

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


def pivot_waypoint(waypoint_location, angle):
    magnitude = int(angle/90)
    # baby transform

    for transform_count in range(abs(magnitude)):
        # Clockwise
        if(angle > 0):
            waypoint_location = [waypoint_location[1], -1 * waypoint_location[0]]
        # CounterClockwise
        else:
            waypoint_location = [-1 * waypoint_location[1], waypoint_location[0]]
    return waypoint_location;


def navigate(instruction, waypoint_location, ship_location):
    command = instruction[0]
    magnitude = int(instruction[1:])

    # PROCESS TURNS
    if command == Directions.LEFT:
        waypoint_location = pivot_waypoint(waypoint_location, -1 * magnitude)
    elif command == Directions.RIGHT:
        waypoint_location = pivot_waypoint(waypoint_location, magnitude)
    # DIRECTIONS - Move waypoint
    elif command == Directions.NORTH:
        waypoint_location[1] += magnitude
    elif command == Directions.EAST:
        waypoint_location[0] += magnitude
    elif command == Directions.SOUTH:
        waypoint_location[1] -= magnitude
    elif command == Directions.WEST:
        waypoint_location[0] -= magnitude
    # COMMIT TO WAYPOINT
    elif command == Directions.FORWARD:
        # Ship += waypoint coords, keep waypoint location relative to ship
        ship_location[0] += magnitude * waypoint[0]
        ship_location[1] += magnitude * waypoint[1]
    print("  - ", command, magnitude, " => ", ship_location, waypoint_location)

    return waypoint_location, ship_location


nav_instructs = [i for i in vacation_helpers.file_to_array(FILE)]

# Part 1
print("BEGIN 1, ", FILE)
direction = Directions.EAST
waypoint = [10, 1]
ship = [0, 0]
for instruct in nav_instructs:
    waypoint, ship = navigate(instruct, waypoint, ship)

print("END", ship, waypoint)
print("Manhattan Distance, ", abs(ship[0]) + abs(ship[1]))
