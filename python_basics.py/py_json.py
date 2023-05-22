# JSON is commonly used with data APIs. Here how we can parse JSON into a Python dictionary.

import json

user_json = '{"name" : "victor", "age" : 34}'

user_dict = json.loads(user_json)
print(user_dict)

to_json = json.dumps(user_dict)
print(to_json)
