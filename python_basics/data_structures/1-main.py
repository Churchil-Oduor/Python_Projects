#!/usr/bin/python3

element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 5]
idx = 5
print("Element at {:d} is {}".format(idx, element_at(my_list, idx)))
