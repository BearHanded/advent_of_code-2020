import helpers.vacation_helpers as vacation_helpers

INPUT = "input.txt"
PLANE_SIZE_H = 127
PLANE_SIZE_W = 7


def get_seat(seat_code):
    # Binary Search Row
    row_code = seat_code[:7]
    lower_bound = 0
    upper_bound = PLANE_SIZE_H
    code_idx = 0
    while lower_bound != upper_bound:
        search_size = (upper_bound - lower_bound + 1) / 2
        if row_code[code_idx] == "F":
            upper_bound -= search_size
        elif row_code[code_idx] == "B":
            lower_bound += search_size
        else:
            raise ValueError("Unsupported Col Code:", row_code[code_idx])
        code_idx += 1

    # Binary Search Col - copy paste cause too lazy to abstract for different codes
    col_code = seat_code[7:]
    left_bound = 0
    right_bound = PLANE_SIZE_W
    code_idx = 0
    while left_bound != right_bound:
        search_size = (right_bound - left_bound + 1) / 2
        if col_code[code_idx] == "L":
            right_bound -= search_size
        elif col_code[code_idx] == "R":
            left_bound += search_size
        else:
            raise ValueError("Unsupported Col Code:", row_code[code_idx])
        code_idx += 1
    return int(lower_bound), int(left_bound);


def get_unique_seat_id(seat):
    (row_num, column) = seat
    return row_num * 8 + column


# RUN - Part 1
boarding_rows = vacation_helpers.file_to_array(INPUT)
highest_id = 0
id_list = []
for boarding_row in boarding_rows:
    row = get_seat(boarding_row)
    uid = get_unique_seat_id(row)
    id_list.append(uid)
    highest_id = max(highest_id, uid)

print("Part 1 - Highest ID", highest_id)

# Part 2
min_id = get_unique_seat_id((0, 0))
max_id = get_unique_seat_id((PLANE_SIZE_H, PLANE_SIZE_W))

missing_seats = [x for x in range(min_id, max_id)
                 if x not in id_list]

# Just eyeball the results for "Not very front" and "Not very back"
print(missing_seats)
