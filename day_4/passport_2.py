import helpers.vacation_helpers as vacation_helpers
import day_4.validation as validation

INPUT = "input.txt"
REQ_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


# Return a line as tuples of key values
def line_to_fields(line):
    fields = []
    passport_content = line.split(" ")
    for pair in passport_content:
        pair_split = pair.split(":")
        fields.append((pair_split[0], pair_split[1]))

    return fields


def validate(passport):
    valid_fields = 0
    missing_cid = False
    for req_field in REQ_FIELDS:
        not_found = True
        for pair in passport:
            if pair[0] == req_field:
                validator = validation.validation_rules.get(pair[0])
                isValid = validator(pair[1])

                if isValid:
                    valid_fields += 1

                not_found = False
                break
        if req_field == "cid" and not_found:
            missing_cid = True

    return valid_fields == len(REQ_FIELDS) or (valid_fields == len(REQ_FIELDS) - 1 and missing_cid)


passports_lines = vacation_helpers.file_to_array(INPUT)

passport_idx = 0
passports = [[]] * len(passports_lines)
passport_buffer = []
for passports_line in passports_lines:
    if len(passports_line) > 0:
        pairs = line_to_fields(passports_line)
        passport_buffer += pairs
    else:
        passports.append(passport_buffer)
        passport_idx += 1
        passport_buffer = []
passports.append(passport_buffer)

valid_passports = 0
for passport_entry in passports:
    if validate(passport_entry):
        valid_passports += 1

print("Valid Passport Count", valid_passports)