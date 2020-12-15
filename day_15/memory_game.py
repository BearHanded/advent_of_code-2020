import time

from helpers import vacation_helpers

INPUT = "input.txt"
start_time = time.time()


def play_game(rules, end_turn=2020):
    idx = 1
    previous = int(rules[-1])
    last_seen = {}
    for rule in rules:
        last_seen[int(rule)] = (-1, idx)
        idx += 1

    print_idx = idx  # for fun
    print("Rules:", rules)
    while idx <= end_turn:
        if print_idx == idx:
            print_idx *= 10
            print("Running...", idx, "@", time.time() - start_time)

        # Don't add the previous to the last_seen cache until we've processed
        current = 0
        previous_assigned_at = -1
        if previous in last_seen:
            previous_assigned_at = last_seen[previous][0]
            current = 0 if (previous_assigned_at == -1) else last_seen[previous][1] - previous_assigned_at
        new_last_seen = -1 if current not in last_seen else last_seen[current][1]
        last_seen[current] = (new_last_seen, idx)  # (previous_assigned_at, assigned_at)

        idx += 1
        previous = current
    return current


rules = vacation_helpers.file_as_string(INPUT).split(",")
result = play_game(rules, 30000000)
print("Turn 2020 result:", result)
