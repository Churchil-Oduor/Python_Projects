# for loop

people = ["John", "Paul", "Sara"]

# simple for loop
for person in people:
    print(f"Current Person: {person}")

# Break

for person in people:
    if person == "Sara":
        break
    print(f"Current Person: {person}")

# range
for i in range(len(people)):
    print(people[i])
