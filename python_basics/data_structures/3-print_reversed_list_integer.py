#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for item in reversed(my_list):
        print("{}".format(item), end="\n")
