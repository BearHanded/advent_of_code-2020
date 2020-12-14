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
            if (current_time/bus) % 1 == 0:
                print("MATCH  - at", current_time, bus)
                print("  answer", (current_time-time)*bus)
                return current_time
        current_time += 1

    return int(input[0])


def parse_schedule(input):
    busses = [bus_to_int(x) for x in input[1].split(",")]
    return busses


def find_pattern(busses):
    # sort from largest to smallest to optimize searching, and save the initial idx alongside for matching
    busses_reverse = busses.copy()
    busses_reverse.sort(reverse=True)
    max_bus = max(busses)
    busses_sorted = [[bus_num, busses.index(bus_num) - busses.index(max_bus)] for bus_num in busses_reverse]
    run_number = 0
    run_number_check = 1
    no_match = True
    while no_match:
        run_number += 1
        collision = run_number * max_bus
        if run_number == run_number_check:
            print("Run number", run_number, "Time", collision)
            run_number_check *= 10

        miss_flag = False
        for bus in busses_sorted[1:]:
            if bus[0] == -1:
                continue
            elif ((collision + bus[1]) / bus[0]) % 1 == 0:
                continue
            else:
                miss_flag = True
                break
        if not miss_flag:
            collision_offset = busses.index(max_bus)
            print("MATCH", collision - collision_offset)
            no_match = True
            return collision - (len(busses) - 1)


bus_input = [i for i in vacation_helpers.file_to_array(FILE)]
schedule = parse_schedule(bus_input)
available_time = get_earliest_time(int(bus_input[0]), schedule)
find_pattern(schedule)
