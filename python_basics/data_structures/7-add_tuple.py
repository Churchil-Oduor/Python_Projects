#!/usr/bin/env python3
names = [8, 6]
age = [2, 5]
a = 0
b = 0


result = tuple(x + y for x, y in zip(names, age))
print(result)


    
    
