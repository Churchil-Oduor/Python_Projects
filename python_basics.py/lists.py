# A list is a collection which is ordered and changeable. Allows duplicate members

# create a list 
numbers = [1, 2, 3, 4, 5]

fruits = ["Apples", "mangoes", "ovacados"]

# create a list using the list constructor
# numbers_2 = list((1, 3, 6, 8))

# list methods

# Insert into list
fruits.insert(2, "Oranges")

# Remove from list
fruits.remove("mangoes")

# Remove with Pop
fruits.pop(2)

# Append into list
fruits.append("Tomatoes")

# Get length
print(len(fruits))

# Reverse list
fruits.reverse()

# Sort list alphabetically
fruits.sort()

# Reverse Sort
fruits.sort(reverse = True)

# Change value
fruits[0] = "Blueberries"

print(fruits)
