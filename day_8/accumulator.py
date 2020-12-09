import copy

from helpers import vacation_helpers

FILE = "input.txt";


def run_program(instructions):
    accumulator = 0
    idx = 0
    while 0 <= idx < len(instructions):
        instr_tuple = instructions[idx]
        instruction = instr_tuple[0].split(" ")
        instructions[idx][1] += 1
        # Error Check
        if instructions[idx][1] > 1:
            print("INFINITE LOOP DETECTED, TERMINATING")
            print(accumulator)
            return False;

        # run instruct

        if instruction[0] == "nop":
            idx += 1
        elif instruction[0] == "acc":
            accumulator += int(instruction[1])
            idx += 1
        elif instruction[0] == "jmp":
            idx += int(instruction[1])

    if idx == len(instructions):
        print("SUCCESS")
        print(accumulator)
        return True;


accumulator_instructions = vacation_helpers.file_to_array(FILE)
acc_instr = [[instruction, 0] for instruction in accumulator_instructions]
# Part 1
run_program(acc_instr)


# Part 2
print ("Enter part 2")
idx = 0
acc_instr = [[instruction, 0] for instruction in accumulator_instructions]
while 0 <= idx < len(acc_instr):
    # too late at night to de-dupe
    if "nop" in acc_instr[idx][0]:
        temp_set = copy.deepcopy(acc_instr) # Don't care, expensive $$$$$$$$$$$$
        temp_set[idx][0] = temp_set[idx][0].replace("nop", "jmp")
        if run_program(temp_set):
            break
    elif "jmp" in acc_instr[idx][0]:
        temp_set = copy.deepcopy(acc_instr)
        temp_set[idx][0] = temp_set[idx][0].replace("jmp", "nop")
        if run_program(temp_set):
            break
    idx += 1

print("Finished at index", idx)
