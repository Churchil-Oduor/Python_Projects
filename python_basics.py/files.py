# Python has functions for creating, reading, updating and deleting files.


# Open a file
my_file = open("my_file.txt", "w")

print("Opening Mode: ", my_file.closed)

# Get name of file
print("Name of file is", my_file.name)

# Get opening mode
print("Mode ", my_file.mode)

# write into file
my_file.write("My name is Churchil")
my_file.write(" and I love to code")
my_file.close()

# Append to file
my_file = open("my_file.txt", "a")
my_file.write(" But majorly I like dancing")
my_file.close()


# Reading a file
my_file = open("my_file.txt", "r+")
text = my_file.read();
print(text)
my_file.close()
