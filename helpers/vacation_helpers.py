def file_to_array(filename):
    fp = open(filename, 'r')
    input_iterable = map(lambda x: x.replace("\n", ""), fp.readlines())
    input_array = list(input_iterable)
    return input_array
