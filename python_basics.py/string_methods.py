
s = "HelloWorld"
# Python String Methods

# Capitalize string
print(s.capitalize())


# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap Case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace("world", "everyone"))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith("hello"))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split()) # returns a list -> ["hello", "world"]

# Find Position
print(s.find('r')) # returns the index position of r

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
