# A Tuple is a collection which is ordered and unchangeable. Allows duplicate memebrs

# Creating a tuple.
fruits_1 = ("Apples", "Oranges", "Ovacadoes")

# Creating a tuple using the tuple Constructor
fruits_2 = tuple(("Pineapples", "Walnuts"))

# Single value needs trailing comma
fruits_3 = ("Mangoes",)

# Can't change value
# fruits_2[1] = "Chr"

# Delete fruits_2
del fruits_2

# Get length
print(len(fruits_1))


# A set is a collection which is unoredered and unindexed. No duplicate members are allowed.

# Create Set
fruits_set = {"Apples", "Oranges", "Mango"}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("Banana")
print(fruits_set)
# Remove from set
fruits_set.remove("Oranges")

# Clear Set
fruits_set.clear()

# Delete set
del fruits_set

print(fruits_set)
