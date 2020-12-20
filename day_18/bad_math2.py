import pyparsing
from helpers import vacation_helpers

FILE = "input.txt"
PLUS = "+"
TIMES = "*"
# Init pyparsing
math_content = pyparsing.Word(pyparsing.alphanums) | '+' | '*'
parens = pyparsing.nestedExpr('(', ')', content=math_content)


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def solve(math_str):
    # Start on the left, solve until index 2 hits a parenthesis , then start solving from there
    # If hit a closing parenthesis, collapse most recent string to number and return to previous cursor
    print(math_str)
    parsed = parse_problem(math_str)
    return operate(parsed)


def parse_term(term):
    if isinstance(term, list):
        term = operate(term)
    else:
        term = int(term)
    return term


def operate(instructions):
    idx = 0
    rolling_total = 0

    # Reduce parens
    while len(instructions) > 1:
        idx = 0
        max_len = len(instructions)
        changed_flag = False

        if max_len == 1 and isinstance(instructions[0], list):
            instructions[0] = parse_term(instructions[0])

        # ADDITION
        for idx in range(0, max_len):
            if instructions[idx] is PLUS:
                term_one = parse_term(instructions[idx - 1])
                term_two = parse_term(instructions[idx + 1])
                out = term_one + term_two
                new_instructions = instructions[:idx-1]
                new_instructions.append(out)
                if (idx + 2) < max_len:
                    new_instructions += instructions[idx+2:]
                instructions = new_instructions
                changed_flag = True
                break  # Just start over, array size changed

        if changed_flag:
            continue

        # MULTIPLICATION
        for idx in range(0, max_len):
            if instructions[idx] is TIMES:
                term_one = parse_term(instructions[idx-1])
                term_two = parse_term(instructions[idx+1])
                out = term_one * term_two
                new_instructions = instructions[:idx-1]
                new_instructions.append(out)
                if (idx + 2) < max_len:
                    new_instructions += instructions[idx+2:]
                instructions = new_instructions
                changed_flag = True
                break # Just start over, array size changed

    return instructions[0]


def parse_problem(math_str):
    common_root = '(' + math_str + ')'  # Limitation of parser
    res = parens.parseString(common_root)

    return res.asList()[0]


# PART ONE
homework = vacation_helpers.file_to_array(FILE)
total = 0
for problem in homework:
    result = solve(problem)
    print(result)
    print("")
    total += result

print("Total", total)
