"""
String Methods in Python
-------------------------
Python provides a variety of built-in methods to manipulate and work with strings. These methods can help in
tasks like transforming, searching, and formatting strings. Below are some of the most commonly used string methods.
"""

# capitalize() - Converts the first character to upper case
"""
capitalize() converts the first character of the string to uppercase, and the rest to lowercase.
"""
example = "hello world"
print(example.capitalize())  # Expected Output: Hello world

# upper() - Converts the entire string to upper case
"""
upper() converts all characters in the string to uppercase.
"""
print(example.upper())  # Expected Output: HELLO WORLD

# lower() - Converts the entire string to lower case
"""
lower() converts all characters in the string to lowercase.
"""
print(example.lower())  # Expected Output: hello world

# title() - Converts the first character of each word to upper case
"""
title() converts the first character of each word to uppercase and the rest to lowercase.
"""
print(example.title())  # Expected Output: Hello World

# strip() - Removes whitespace from the beginning and end of a string
"""
strip() removes any leading and trailing spaces (or other specified characters) from the string.
"""
example_with_spaces = "   hello world   "
print(example_with_spaces.strip())  # Expected Output: hello world

# replace() - Replaces a string with another string
"""
replace() searches for a specified substring in the string and replaces it with another substring.
"""
print(example.replace("world", "everyone"))  # Expected Output: hello everyone

# split() - Splits a string into a list based on a separator
"""
split() divides a string into a list based on the separator provided (default is any whitespace).
"""
split_example = "hello world, how are you?"
print(split_example.split())  # Expected Output: ['hello', 'world,', 'how', 'are', 'you?']

# join() - Joins a list of strings into a single string, with a specified separator
"""
join() takes an iterable (like a list) of strings and joins them into one string, separated by the given string.
"""
words = ["hello", "world"]
print(" ".join(words))  # Expected Output: hello world

# find() - Searches the string for a specified value and returns the index where it is found
"""
find() returns the index of the first occurrence of a substring within the string. If not found, it returns -1.
"""
print(example.find("world"))  # Expected Output: 6

# count() - Returns the number of times a specified value appears in a string
"""
count() returns the number of occurrences of a specified substring within the string.
"""
print(example.count("l"))  # Expected Output: 3

# startswith() - Checks if the string starts with a specified value
"""
startswith() returns True if the string starts with the specified value, otherwise it returns False.
"""
print(example.startswith("hello"))  # Expected Output: True

# endswith() - Checks if the string ends with a specified value
"""
endswith() returns True if the string ends with the specified value, otherwise it returns False.
"""
print(example.endswith("world"))  # Expected Output: True

# isdigit() - Returns True if all characters in the string are digits
"""
isdigit() checks if all the characters in the string are digits (0-9).
"""
digit_example = "12345"
print(digit_example.isdigit())  # Expected Output: True

# isalpha() - Returns True if all characters in the string are alphabetic
"""
isalpha() checks if all the characters in the string are alphabetic (A-Z, a-z).
"""
alpha_example = "Hello"
print(alpha_example.isalpha())  # Expected Output: True

# isnumeric() - Returns True if all characters in the string are numeric
"""
isnumeric() checks if all characters in the string are numeric, including integers and other numeric characters.
"""
numeric_example = "Ⅳ"  # Roman numeral four
print(numeric_example.isnumeric())  # Expected Output: True

# len() - Returns the length of the string (number of characters)
"""
len() is a built-in function that returns the length of the string.
"""
print(len(example))  # Expected Output: 11

