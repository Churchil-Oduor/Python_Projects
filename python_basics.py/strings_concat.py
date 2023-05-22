
#  string concatenation
name = "Churchil"
age = 12

# concatenating using the + operator
print("My name is ", name, "and I am ", str(age), "years old")

#concatenating using the .format() function
print("My name is {name} and I {age} years old".format(name = name, age = age))


# concatenation using the f-string
print(f"My name is {name} and I am {age} years old")
