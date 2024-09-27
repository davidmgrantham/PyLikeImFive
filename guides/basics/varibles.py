# Variables are containers for storing data values. You can assign data types to variables.
x = int(5)
y = "Mark"
print(x)
# Expected Output:
# 5
print(y)
# Expected Output:
# Mark


print(type(x))
# Expected Output:
# <class 'int'>


print(type(y))
# Expected Output:
# <class 'str'>

# You can assign differnt values to multiple variables in one line.
a, b = "David", "John"
print(a)
print(b)
# Expected Output:
# David
# John

# You can assign variables to other variables.
a = b = c = "Hello"
print(a)
print(b)
print(c)
# Expected Output:
# Hello
# Hello
# Hello