#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for index in range(x):
            val = my_list[index]
            if type(val) is int:
                print("{:d}".format(val), end="")
                count += 1
        print()
        return count
    except IndexError("list index out of range"):
        raise IndexError from None
