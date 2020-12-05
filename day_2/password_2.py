fp = open('./input.txt', 'r')
input_iterable = map(lambda x: x, fp.readlines())
password_array = list(input_iterable)

valid_passwords = 0
for password_entry in password_array:
    pass_split = password_entry.split(" ")
    pass_rules = pass_split[0].split("-")
    idx_one = int(pass_rules[0]) - 1
    idx_two = int(pass_rules[1]) - 1
    letter = pass_split[1].replace(":", "")
    password = pass_split[2].replace("\n", "")

    # Check amount in, incr if valid
    occurrences = password.count(letter)

    if password[idx_one] == letter or password[idx_two] == letter:
        if not (password[idx_one] == letter and password[idx_two] == letter):
            valid_passwords += 1


# Results
print("Valid Passwords:", valid_passwords)