# Dictionaries
# They have a few rules...
# 1. Unlike a sequenced object like a list dictionaries are a hash and there NOT guaranteed order. Adding a element CAN change the order for example
# 2. Operations like slice, indexing, etc are not avialbe bcause they are dependent on a sequenced order.

# Two different ways to create dictionaries
the_dict = {"Captain": "Picard", "Military": "Starfleet", "Ship": "USS Enterprise-D", "Stardate": 41254.7}

# This one uses the dict() built-in method
same_dict = dict(Captain = "Picard", Military = "Starfleet", Ship = "USS Enterprise-D", Stardate = 41254.7)

print("=====Directory Dictionary Object=====")
print(dir(the_dict))

print('') # Just for spacing in output :D

print("=====Directory dict method=====")
print(dir(dict))

print('') # Just for spacing in output :D

# Both dictionaries
print("=====Both the_dict and same_dict are dictionary types=====")
print(type(the_dict))
print(type(same_dict))

print('') # Just for spacing in output :D

# Differnt ids
print("=====Differnt ids even though they have the same values=====")
print(id(the_dict))
print(id(same_dict))

print('') # Just for spacing in output :D

# They have the same values but different ids meaning they are two differnt objects in memory. 
print("Dictionary Compare the_dict and same_dict: ", the_dict == same_dict)

print('') # Just for spacing in output :D

print('=' * 15)
print("Getting Values")
print('=' * 15)

print('') # Just for spacing in output :D

# This executes the __getitem method automatically within the dictionary object. This does what the below __getitem__ method does without typing it.
print("=====Get a value from a dictionary=====")
print(the_dict["Captain"])

# This executes the __getitem by using it in your code - This is NOT recommended as __getitem__ is intended for internal use to the dictionary object. 
print("=====Get a value from dictionary using the default __getitem__ method=====")
print(the_dict.__getitem__("Captain"))

# Use the .get method provided by the dictionay object. This gets the value from a key. 
print("=====Get a value from using .get method=====")
print(the_dict.get("Captain"))

# Use the dict().get method that is built-in to python. This gets the value from a key. 
print("=====Get a value from dictionary using dict().get built-in method=====")
print(dict(the_dict).get("Captain"))

print('') # Just for spacing in output :D

print('=' * 15)
print("Adding Key/Values")
print('=' * 15)

print('') # Just for spacing in output :D

# Add a key and value to a dictionary
print("=====Add a value to a dictionary=====")
the_dict["First Officer"] = "Riker"
print(the_dict)

print('') # Just for spacing in output :D

print('=====Add a value to your dictionary using the default __setitem__ method=====')
the_dict.__setitem__("COO", "Data")
print(the_dict)

# Needed infomration #
# Updating key/values
# Clearing dictionary
# Deleting things in dictionary
