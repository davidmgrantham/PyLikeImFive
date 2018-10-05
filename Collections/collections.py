# Formating
ftm = "{0:<5} {1:<10}"
ftm2 = "{0:^5} {1:^10}"

# Collection Types
the_string = "This is a string"
the_bytes =  bytearray(the_string, encoding = 'UTf-8')
the_list = list(range(10))
the_tuple = tuple(range(10))
the_dict = {"Captain": "Picard", "Military": "Starfleet", "Ship": "USS Enterprise-D" }
the_set = set(range(10))

# Other ways to create these objects....

another_list = ["Mercury", "Mars", "Saturn", "Earth"]
another_dict = {"Team": "Alabama", "City": "Tuscaloosa", "Couch": "Nick Saban"}
another_tuple = ("Alabama", "Auburn", "Montgomery", "Huntsville", "Chelsea")
another_set = {"A", "B", "C"}

# Type of object
print("=====Collection Types=====")
print(ftm.format("   Type", "Output"))
print(ftm.format("=" * 5, "=" * 5))
print('') # Just for spacing in output :D
print('the_string = "This is a string"')
print(type(the_string))
print('') # Just for spacing in output :D
print("the_bytes =  bytearray(the_string, encoding = 'UTf-8')")
print(type(the_bytes))
print('') # Just for spacing in output :D
print('the_list = list(range(10))')
print(type(the_list))
print('') # Just for spacing in output :D
print('the_tuple = tuple(range(10))')
print(type(the_tuple))
print('') # Just for spacing in output :D
print('the_dict = {"Captain": "Picard", "Military": "Starfleet", "Ship": "USS Enterprise-D" }')
print(type(the_dict))
print('') # Just for spacing in output :D
print('the_set = set(range(10))')
print(type(the_set))

print('') # Just for spacing in output :D

print("=====More Collection Types=====")
print(ftm.format("Type   ", "Output"))
print(ftm.format("=" * 5, "=" * 5))
print('') # Just for spacing in output :D
print('another_list = ["Mercury", "Mars", "Saturn", "Earth"]')
print(type(another_list))
print('') # Just for spacing in output :D
print('another_dict = {"Team": "Alabama", "City": "Tuscaloosa", "Couch": "Nick Saban"}')
print(type(another_dict))
print('') # Just for spacing in output :D
print('another_tuple = ("Alabama", "Auburn", "Montgomery", "Huntsville", "Chelsea")')
print(type(another_tuple))
print('') # Just for spacing in output :D
print('another_set = {"A", "B", "C"}')
print(type(another_set))

print('') # Just for spacing in output :D

# Response from various collection types
print("=====Collection Example=====")
print(ftm.format("Type   ", "Output"))
print(ftm.format("==" * 5, "==" * 5))
print('') # Just for spacing in output :D
print('the_string = "This is a string"')
print("String: ", the_string)
print('') # Just for spacing in output :D
print("the_bytes =  bytearray(the_string, encoding = 'UTf-8')")
print("Bytes: ", the_bytes)
print('') # Just for spacing in output :D
print('the_list = list(range(10))')
print("Range: ", the_list)
print('') # Just for spacing in output :D
print('the_tuple = tuple(range(10))')
print("Tuple: ", the_tuple)
print('') # Just for spacing in output :D
print('the_dict = {"Captain": "Picard", "Military": "Starfleet", "Ship": "USS Enterprise-D" }')
print("Dictionary ", the_dict)
print('') # Just for spacing in output :D
print('the_set = set(range(10))')
print("Set ", the_set)

print('') # Just for spacing in output :D

# Enumerate Method
# You don't need to get index values for your loop, but you can get some with the enumerate method
print("=====Enumerate Method=====")
print(ftm2.format("Index   ", "Value"))
print(ftm2.format("=" * 2, "=" * 10))
for city_and_index in enumerate(another_tuple):
    print(city_and_index)

print('') # Just for spacing in output :D

# Unpacking a tuple
# The names index and city are associated with values contained with the tuple provided by the enumerate method
# The names are "recycled" with each iteration
# start_at is provided to give a starting index point. Without it 0 would be assumed.
print("=====Enumerate Method With Index Values=====")
print(ftm.format("Index   ", "Value"))
print(ftm.format("=" * 5, "=" * 10))
start_at = 1
for index, city in enumerate(another_tuple, start_at):
    print("City #{} is {}".format(index, city))

print('') # Just for spacing in output :D

# Slicing
print("=====Slicing=====")
print(the_list)
# <Iterable>[<start>:<stop>:<stride>]
print("<Iterable>[<start>:<stop>:<stride>]")
print(the_list[0:6:2])
print(the_list[0:10:3])

print('') # Just for spacing in output :D

# Slicing Continued
# Python has a built-in class for slice as well
print("=====Slicer class=====")
slicer = slice(0,6,2)
print("slicer = slice(0,6,2)")
print(type(slice))
print(type(slicer))

print(the_list[slicer])

print('') # Just for spacing in output :D

print("=====Alernative Syntax=====")
print("the_list.__getitem__(slicer)")
print(the_list.__getitem__(slicer))

print('') # Just for spacing in output :D

# Slicing Strings
print("=====Slicing a string=====")
print('the_string = "This is a string"')
print("Slice a string: ", the_string[3:10])

print('') # Just for spacing in output :D

# Copy a list
print("=====Copy a list=====")
print("the_list= ", the_list)
print("The the_list id is: ", id(the_list))
# This is one way to copy a list
new_list = the_list[:]
print("new_list= ",new_list)
print("The new_list id is: ", id(new_list))

print('') # Just for spacing in output :D

# I recommend using this way to copy lists as it is more readable
print("=====Alernative Copy Option=====")
another_new_list = the_list.copy()
print("another_new_list= ",another_new_list)

