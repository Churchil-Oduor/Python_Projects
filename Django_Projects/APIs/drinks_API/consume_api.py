#!/usr/bin/env python3
import requests

response = requests.get("http://127.0.0.1:8000/drinks")
data = response.json()
print(data)
#list_data = data["drinks"]

#for x in range(len(list_data)):
 #   print(list_data[x]["name"])

