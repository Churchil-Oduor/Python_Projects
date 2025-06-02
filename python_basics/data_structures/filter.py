#!/usr/bin/env python3

numbers = [1, 2,3 ,4, 5,6 ,7, 8]
even_no = filter(lambda x: x % 2 == 0, numbers)
res = list(even_no)
print(res)
