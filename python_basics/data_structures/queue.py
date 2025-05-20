#!/usr/bin/env python3
 
from collections import deque

_list = ["Churchil", "Basil", "Okech", "Oduor"]
my_queue = deque(_list)
print(my_queue.popleft())
