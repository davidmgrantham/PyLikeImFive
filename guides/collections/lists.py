# Define an empty list.
queens = []
print(queens)
# Expected Output:
# []

# Define a list by using equare brackets.
kings = ['Henry VIII', 'George III', 'Edward I', 'William I']

print(kings)
# Expected Output:
# ['Henry VIII', 'George III', 'Edward I', 'William I']

# Access the first item in the list
print(kings[0])
# Expected Output:
# Henry VIII

# Access the second item in the list
print(kings[1])
# Expected Output:
# George III

# Add an item to the list
kings.append('Elizabeth I')
print(kings)
# Expected Output:
# ['Henry VIII', 'George III', 'Edward I', 'William I', 'Elizabeth I']

# Remove an item from the list
kings.remove('George III')
print(kings)
# Expected Output:
# ['Henry VIII', 'Edward I', 'William I', 'Elizabeth I']

# Remove an item from the list by index
kings.pop(1)
print(kings)
# Expected Output:
# ['Henry VIII', 'William I', 'Elizabeth I']

# Sort the list
kings.sort()
print(kings)
# Expected Output:
# ['Elizabeth I', 'Henry VIII', 'William I']

# Loop through the list
for king in kings:
    print(king)

# Expected Output:
# Henry VIII
# George III
# Edward I
# William I

# Del the entire list
del kings
# Expected Output:
# NameError: name 'kings' is not defined

