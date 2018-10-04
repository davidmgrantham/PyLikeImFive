# Namespaces

# Everything in python is a object and you can assign that object a name

# Here 2 is stored in memory and a(the name) is referenced to it.
print("=====Name and Object=====")
a = 2
print("a = 2")

print('') # Just for spacing in output :D

print("=====The Ids are equal=====")
print(id(a) == id(2))

print('') # Just for spacing in output :D

print("=====The type of object=====")
print(type(a))

print('') # Just for spacing in output :D

print('=' * 40)
print(" Listing namespaces in different scopes")
print('=' * 40)

print('') # Just for spacing in output :D

# These are names mapped to the object for a (int type). You can also call these attributes.
# The 'numberator' name listed in the output is a attribute of the int function.
print("=====The namespace for a=====")
print(dir(a))

print('') # Just for spacing in output :D

print("=====The namespace given when the interpreter is started=====")
print(dir())

print('') # Just for spacing in output :D

# This is the namespace that shows on the builtin 
print("=====The namespace for __builtins__=====")
print(dir(__builtins__))

print('') # Just for spacing in output :D

# Notice that a is in the global namespace since we bound 2 to a.
print("=====The namespace for the global namespace=====")
print(dir(globals))

print('') # Just for spacing in output :D

# This will look the name as the global namespace unless used inside a function. See scopes.py
print("=====The namespace for the local namespace=====")
print(dir(locals))