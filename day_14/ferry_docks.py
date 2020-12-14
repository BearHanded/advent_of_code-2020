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
        if mask[i] == '0' or mask[i] == '1':
            new_str += mask[i]
        else:
            new_str += binary[i]
    return int(new_str, 2)


def run_init(data, mem):
    mask = ""
    for line in data:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            address = line[line.index('[')+1:line.index(']')]
            value = int(line.split(' = ')[1])
            mem[address] = apply_mask(value, mask)
    return mem


ferry_data = vacation_helpers.file_to_array(FILE)

memory = {}
memory = run_init(ferry_data, memory)
print("memory", memory)
print("Sum of values in memory", sum(memory.values()))


# Part 2