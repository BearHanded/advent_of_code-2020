import string


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def validate_birth_year(str_in):
    valid = represents_int(str_in) and len(str_in) == 4 and 1920 <= int(str_in) <= 2002
    return valid


def validate_issuer_year(str_in):
    valid = represents_int(str_in) and len(str_in) == 4 and 2010 <= int(str_in) <= 2020
    return valid


def validate_expiration_year(str_in):
    valid = represents_int(str_in) and len(str_in) == 4 and 2020 <= int(str_in) <= 2030
    return valid


def validate_height(str_in):
    if len(str_in) <= 3:
        return False;

    # Parse
    last_chars = str_in[-2:]
    num = str_in[:-2]

    if last_chars == "cm":
        return represents_int(num) and 150 <= int(num) <= 193
    elif last_chars == "in":
        return represents_int(num) and 59 <= int(num) <= 76
    else:
        return False;


def validate_hair_color(str_in):
    if len(str_in) != 7:
        return False

        # Parse
    prefix = str_in[0]
    hex_code = str_in[1:]

    if prefix == "#":
        return all(c in string.hexdigits for c in hex_code)
    else:
        return False;


def validate_eye_color(str_in):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return valid_colors.count(str_in) == 1


def validate_passport_id(str_in):
    if len(str_in) != 9:
        return False
    return represents_int(str_in)


def validate_country_id(str_in):
    return True;


validation_rules = {
    "byr": validate_birth_year,
    "iyr": validate_issuer_year,
    "eyr": validate_expiration_year,
    "hgt": validate_height,
    "hcl": validate_hair_color,
    "ecl": validate_eye_color,
    "pid": validate_passport_id,
    "cid": validate_country_id,
}
