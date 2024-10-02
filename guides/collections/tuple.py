"""
Tuples in Python
----------------
A tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets.
They are faster than lists and can be used as keys in dictionaries.
"""

# Define an empty tuple
"""
An empty tuple can be created using empty parentheses.
Tuples are faster than lists and are often used for immutable collections.
"""
kings = ()
print(type(kings))  # Outputs the type of the tuple
print(kings)        # Expected Output: ()

# Define a tuple with three items
"""
We can define tuples with multiple items. These items are ordered and cannot be changed after definition.
"""
kings = ('Henry VIII', 'George III', 'Edward I')
print(kings)  # Expected Output: ('Henry VIII', 'George III', 'Edward I')

# Accessing items
"""
Tuples support indexing to access specific elements. Let's access the first item in the 'kings' tuple.
"""
print(kings[0])  # Expected Output: Henry VIII

# Tuple Methods
"""
Tuples come with a few built-in methods. Two of the most common are count() and index().
"""
# count() - Returns the number of times a value occurs in a tuple
print(kings.count('Henry VIII'))  # Expected Output: 1

# index() - Searches the tuple for a value and returns its index
print(kings.index('Edward I'))  # Expected Output: 2
