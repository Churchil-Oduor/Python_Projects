
# A function is a block of code which only runs when it is called. In python, curly braces are not used, instead indentation with tabs or spaces is used.

# Create function
def hello(name = "Nameless"):
    print(f"Hello {name}")

# Return a value
def get_sum(num1, num2):
    return (num1 + num2)

print(get_sum(2, 5))
