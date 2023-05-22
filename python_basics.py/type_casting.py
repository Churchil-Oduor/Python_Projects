
# type casting
x, y, z = (1.3, 34, 98.55)

# check the type using type() function
print("The type of x, y, and z are ->", type(x), type(y), type(z),"respectively \n")

x = int(x)      # x is type casted into int and the result is 1
y = float(y)    # y is type-casted into float from int
z = complex(z)  # z is type casted into complex from float

print("After type casting, the type of x, y, z are ->", type(x), type(y), type(z),"respectively\n")
