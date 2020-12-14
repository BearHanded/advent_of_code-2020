import math

from helpers import vacation_helpers

FILE = "input.txt"


def bus_to_int(str):
    try:
        out = int(str)
        return out
    except ValueError:
        return -1


def get_earliest_time(time, busses):
    print("Searching at", time)
    no_bus = True
    current_time = time
    filtered_busses = [x for x in busses if x != -1]
    while no_bus:
        for bus in filtered_busses:
            if (current_time / bus) % 1 == 0:
                print("MATCH  - at", current_time, bus)
                print("  answer", (current_time - time) * bus)
                return current_time
        current_time += 1

    return int(input[0])


def parse_schedule(input):
    busses = [bus_to_int(x) for x in input[1].split(",")]
    return busses


def find_pattern(buses):
    buses = [(n, int(x)) for n, x in enumerate(buses) if x != -1]
    lcm = buses[0][1] # least common muliplier so far
    timestamp = - buses[0][0]

    # Solve for each bus at a time, building up the next delay input, thus finding a pattern
    for delay, bus in buses[1:]:
        delay = -delay % bus
        k = (delay - timestamp) * pow(lcm, -1, bus) % bus
        lcm_new = abs(lcm * bus) // math.gcd(lcm, bus)
        timestamp = (lcm * k + timestamp) % lcm_new
        lcm = lcm_new
        print("With bus", bus, "-", timestamp)


bus_input = [i for i in vacation_helpers.file_to_array(FILE)]
schedule = parse_schedule(bus_input)
available_time = get_earliest_time(int(bus_input[0]), schedule)
find_pattern(schedule)
