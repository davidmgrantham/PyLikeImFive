# Define an empty dictionary.
kings = {}
print(kings)
# Expected Output:
# {}

# A dictionary is a collection of key-value pairs. Each key is unique and is used to access the corresponding value.
kings = {"Henry VIII": "Tudor", "George III": "Hanover", "Edward I": "Plantagenet", "William I": "Norman"}
print(kings)
# Expected Output:
# {'Henry VIII': 'Tudor', 'George III': 'Hanover', 'Edward I': 'Plantagenet', 'William I': 'Norman'}

# Access the value by key
print(kings["Henry VIII"])
# Expected Output:
# Tudor

# loop over the dictionary
for king, dynasty in kings.items():
    print(f"{king} was a {dynasty} king.")
# Expected Output:
# Henry VIII was a Tudor king.
# George III was a Hanover king.
# Edward I was a Plantagenet king.
# William I was a Norman king.

# Add a key-value pair to the dictionary
kings["Elizabeth I"] = "Tudor"
print(kings)
# Expected Output:
# {'Henry VIII': 'Tudor', 'George III': 'Hanover', 'Edward I': 'Plantagenet', 'William I': 'Norman', 'Elizabeth I': 'Tudor'}