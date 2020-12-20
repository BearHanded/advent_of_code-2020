from helpers import vacation_helpers

FILE = "input.txt"

# Something easy to switch on
CHARACTER = "CHARACTER"
PATTERN = "PATTERN"
PATTERN_OR = "PATTERN_OR"


def build_rules(input_array):
    _rules = {}
    line_break = input_array.index("")
    for entry in input_array[:line_break]:
        content = entry.split(": ")

        if '\"' in content[1]:
            _rules[int(content[0])] = (CHARACTER, content[1].replace('\"', ''))
        elif '|' in content[1]:
            pattern = [[int(j) for j in i.split(" ")] for i in content[1].split(" | ")]
            _rules[int(content[0])] = (PATTERN_OR, pattern)
        else:
            _rules[int(content[0])] = (PATTERN, [int(i) for i in content[1].split(" ")])
    return _rules


def get_messages(input_array):
    line_break = input_array.index("")
    return input_array[line_break + 1:]


def validate(message, rules, rule_number=0, idx=0, root=True):
    valid_out = False
    if rules[rule_number][0] is CHARACTER:
        a = message[idx]
        r = rules[rule_number][1]
        valid_out = message[idx] == rules[rule_number][1]
        idx += 1  # Shift to next
    elif rules[rule_number][0] is PATTERN:
        is_valid = True
        for rule in rules[rule_number][1]:
            validity, end_idx = validate(message, rules, rule, idx, False)
            is_valid = is_valid and validity
            idx = end_idx
        valid_out = is_valid
    else:
        # PATTERN_OR
        is_valid = False
        for rule_pair in rules[rule_number][1]:
            temp_idx = idx
            temp_valid = True
            for rule in rule_pair:
                validity, end_idx = validate(message, rules, rule, temp_idx, False)
                temp_valid = temp_valid and validity
                temp_idx = end_idx
            is_valid = is_valid or temp_valid
        idx = temp_idx
        valid_out = is_valid
    if root:
        # Check all chars have been processed
        return idx == len(message) and valid_out, idx
    return valid_out, idx


code_input = vacation_helpers.file_to_array(FILE)
rule_set = build_rules(code_input)
messages = get_messages(code_input)

valid_count = 0
for missive in messages:
    result = validate(missive, rule_set)
    valid_count += result[0]
    print(missive, result)

print("Number valid:", valid_count)
# Return string that satisfies the rule?