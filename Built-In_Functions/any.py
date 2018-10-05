# Any

print("The any function can be thought of as a sequence of 'and' opertators.")

print('') # Just for spacing in output :D

print("Returns True if atleast one statement is true")
print("Returns False if all the statements are false or the iterable is empty")

print('') # Just for spacing in output :D

print("=====any Examples=====")

print("""\
officers = ['Picard', 'Data', 'Riker', 'Worf']

x = (any(person in 'Bob Riker Mark Tom' for person in officers)
print(x)
""")

officers = ['Picard', 'Data', 'Riker', 'Worf']

x = any(people in 'Bob Riker Mark Tom' for people in officers)
print("Returns:", x)

print('') # Just for spacing in output :D

print("This is the same as doing this..")

print("""\
officers = ['Picard', 'Data', 'Riker', 'Worf']

for person in officers:
    if person in 'Bob Riker Mark Tom':
        print("True"
        break
""")

officers = ['Picard', 'Data', 'Riker', 'Worf']

for person in officers:
    if person in 'Bob Riker Mark Tom':
        print("Returns: True")
        break

print('') # Just for spacing in output :D

print("=====What about numbers=====")

# Returns a True because atleast one number in the list is not 0 which is always False
print("print(any([0, 0, 0, 0]))")
print(any([0, 0, 2, 0]))

print('') # Just for spacing in output :D

print("=====What about strings=====")
# Thats odd...whitespace is True because it is part of a string.
print("print(any(' '))")
print(any(' '))

print('') # Just for spacing in output :D

print("print(any('This is a string'))")
print(any('This is a string'))