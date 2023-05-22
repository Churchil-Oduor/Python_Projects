# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate mambers.

# Create dictionary
person = {

        "first_name" : "Churchil",
        "last_name" : "Basil",
        "age" : 30
}

person_2 = {

        "first_name" : "Allan",
        "last_name" : "Morse",
        "age" : 34
}

# Use Constructor
person_3 = dict(first_name = "AL", last_name = "Bin")

# Get Value
print(person["first_name"])

# Also you can use the get function to get value
print(person_2.get("first_name"))

# Add key/value
person["phone"] = "000-000-000"

# Get dict keys
print(person.keys())

# Get dict values
print(person.values())

# Get dict items
print(person.items())

# Copy dictionary
person_4 = person_2.copy()
print(person_4)

# Remove item using del
del(person_4["age"])

# Remove item using the pop method
person.pop("age")

# Clear
person.clear()
print(person) # returns an empty dict -> {}

# Get Length
print(len(person_3))

# list of dictionaries
people = [

        {
            "name" : "martha",
            "age" : 23
        },

        {
            "name" : "Caleb",
            "age" : 56
            }
]

print(people)

# Get an object in the list
print(people[0])

# Get a specific items components e.g age
print(people[1].get("name"))
print(people[1]["name"])
