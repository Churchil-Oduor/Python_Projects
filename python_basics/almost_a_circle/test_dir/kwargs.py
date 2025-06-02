#!/usr/bin/python3

def passed_items(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("{} == {} ".format(key, value))

passed_items(name="Churchil", country="kenya")

