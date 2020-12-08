from helpers import vacation_helpers

FILE = "input.txt";


def get_name(rule):
    return rule.split(' bag')[0]


def get_contents(rule):
    content_str = rule.split('contain ')[1]  # 1 wavy lime bag, 1 vibrant green bag, 3 light yellow bags.
    bags = content_str.split(', ')  # [1 wavy lime bag, 1 vibrant green bag, 3 light yellow bags.]
    split_by_space = [item.split(" ") for item in bags]

    contents = {}
    for parsed_rule in split_by_space:
        if parsed_rule[0] == "no":
            continue
        contents[parsed_rule[1] + " " + parsed_rule[2]] = int(parsed_rule[0])
    return contents


def build_rules(rule_input):
    return {get_name(rule): get_contents(rule) for rule in rule_input}


def flatten_bags(rules):
    return [];


############
# Count number of bags containing one type of bag
def total_bags_containing(bag_type, bags):
    del bags[bag_type]  # Ignore real bag
    totalled = 0
    for bag in bags:
        totalled += total_bags_containing_nested(bag_type, bags[bag], bags)
    return totalled


def total_bags_containing_nested(bag_type, bag_rule, all_rules):
    if len(bag_rule) == 0:
        return 0
    else:
        if bag_type in bag_rule:
            return 1
        else:
            # If any of subrules contain 1, return
            for bag in bag_rule:
                if total_bags_containing_nested(bag_type, all_rules[bag], all_rules):
                    return 1
            return 0


############
# Count all bags in one bag
def total_bags(bag_type, bags):
    bag = bags[bag_type]  # Ignore real bag
    totalled = 0
    for bag_key in bag:
        result = total_bags_nested(bags[bag_key], bags)
        totalled += bag[bag_key] + bag[bag_key] * result
    return totalled


def total_bags_nested(bag_rule, bags):
    if len(bag_rule) == 0:
        return 0
    else:
        totalled = 0
        for bag_key in bag_rule:
            totalled += bag_rule[bag_key] + bag_rule[bag_key] * total_bags_nested(bags[bag_key], bags)
        return totalled


bag_rules_input = vacation_helpers.file_to_array(FILE)

# Part 1
target_bag = "shiny gold"
bag_rules = build_rules(bag_rules_input)
print(bag_rules);
total = total_bags_containing(target_bag, bag_rules.copy())
print("Bags containing shiny gold", total)

total_in_gold = total_bags(target_bag, bag_rules)
print("Shiny gold contains", total_in_gold)
