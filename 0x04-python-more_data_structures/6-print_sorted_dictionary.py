def print_sorted_dictionary(a_dictionary):
    new = []
    for x in sorted(a_dictionary):
        print ("{}: {}".format(x, a_dictionary[x]))
