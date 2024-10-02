"""
Strings in Python
-----------------
Strings are defined by enclosing a sequence of characters within quotes.
You can use either single or double quotes to define strings in Python.
"""

# Defining a string
"""
A string can be created by placing any value within quotes. Here, we define a simple string.
"""
print("William")  # Expected Output: William

# Assigning a string to a variable
"""
You can store strings in variables. In Python, variables do not need to be declared with a specific type.
Here we assign the string "William" to the variable `name`.
"""
name = "William"
print(type(name))  # Outputs the type of the variable `name`
print(name)        # Expected Output: William

# Combining strings
"""
Strings can be concatenated using the `+` operator. This allows you to combine multiple strings into one.
"""
first_name = "William"
last_name = "Wallace"

full_name = first_name + " " + last_name
print(full_name)  # Expected Output: William Wallace

# Using f-strings for string formatting
"""
f-strings (formatted string literals) are a convenient way to include variables within a string.
They are prefixed with an `f` and allow for inline variable substitution.
"""
print(f"Hello, {full_name}")  # Outputs: Hello, William Wallace

