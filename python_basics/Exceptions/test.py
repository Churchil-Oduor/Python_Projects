while True:
    try:
        x = int(input("Enter Number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number")

