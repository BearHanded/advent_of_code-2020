from itertools import product

from helpers import vacation_helpers

FILE = "input.txt"


def apply_mask(value, mask):
    binary = str(bin(value))[2:]
    binary = '{message:{fill}{align}{width}}'.format(
        message=binary,
        fill='0',
        align='>',
        width=36,
    )
    new_str = ""
    for i in range(len(mask)):
        if mask[i] == 'X' or mask[i] == '1':
            new_str += mask[i]
        else:
            new_str += binary[i]
    return new_str


def assign_to_masked_address(value, address, mem):
    x_pos = [index for index, val in enumerate(address) if val == 'X']
    combinations = [x for x in product('01', repeat=len(x_pos))]
    valid_addresses = []
    for possibility in combinations:
        for pos, val in zip(x_pos, possibility):
            address = address[:pos] + val + address[pos + 1:]
        valid_addresses.append(address)
    for valid in valid_addresses:
        mem[int(valid, 2)] = value
    return mem


def run_init(data, mem):
    mask = ""
    for line in data:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            address = line[line.index('[')+1:line.index(']')]
            value = int(line.split(' = ')[1])
            address = apply_mask(int(address), mask)
            mem = assign_to_masked_address(value, address, mem)
    return mem


ferry_data = vacation_helpers.file_to_array(FILE)

memory = {}
memory = run_init(ferry_data, memory)
print("memory", memory)
print("Sum of values in memory", sum(memory.values()))


# Part 2