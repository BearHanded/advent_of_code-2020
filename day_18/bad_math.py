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


def operate(instructions):
    idx = 0
    rolling_total = 0
    while idx < len(instructions) - 2:
        term_one = instructions[idx]
        operator = instructions[idx + 1]
        term_two = instructions[idx + 2]

        # Convert and operate nested sections
        if isinstance(term_one, list):
            term_one = operate(term_one)
        else:
            term_one = int(term_one)
        if isinstance(term_two, list):
            term_two = operate(term_two)
        else:
            term_two = int(term_two)

        if operator is PLUS:
            rolling_total = term_one + term_two
        else:
            rolling_total = term_one * term_two

        # Save in place and continue
        instructions[idx + 2] = rolling_total
        idx += 2
    return rolling_total


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
