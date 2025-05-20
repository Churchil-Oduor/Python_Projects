#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    count = sum(1 for item in matrix if isinstance(item, list))
    
    if count == 1:
        tin = matrix[0]
        print_list(tin)
    else:
        for i in range(count):
            tin = matrix[i]
            print_list(tin)



def print_list(tin):
    for i in range(len(tin)):
        if i == (len(tin) - 1):
            print("{}".format(tin[i]), end="\n")
        else:
            print("{}".format(tin[i]), end=" ")
