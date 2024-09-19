"""
A list is a flexible data structure in Python. 
It can contain elements of different data types, which are enclosed within square brackets.

lists are also ordered, starting with an index of 0, 
making it possible for us to access items through their indexes.

Their ordered nature also allows for duplicated items.

Lists are mutable and elements can be modified, added, or removed as required.
"""

# Create an empty list called "mammals"
animals = []

# Create a list, defined within square brackets
animals = ["Lion", "Elephant", "Dolphin"]
print(animals)

# Create a list from a tuple using the list constructor
birds = list(("Eagle", "Penguin", "Parrot"))
print(birds)

"""
We can use the range() function to generate a sequence of numbers based on a given start and end point.
Syntax: range(start, stop, step)
start: An integer number specifying the start point (included).
stop: An integer number specifying the end point (not included).
step: An integer number specifying the incrementation. The default is 1.
We then pass the result of the range function to the list() constructor to convert it to a list.
"""

# Generate a sequence of numbers starting from 0 to 4
range_list = list(range(0,5))
print(range_list)

# Check the type of the variable
type(birds)

# Combine the mammals and birds lists
animals_combined = animals + birds
print(animals_combined)

# Create a copy of the mammals list
animals_copy = animals.copy()

print(animals, animals_copy)

# nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)

# Access the first element of the nested list
print(nested_list[0])
access_nested = nested_list[0][2]

# slicing
# Access the first two elements of the mammals list 
print(animals[:2])

# modification
# Modify the first element of the mammals list
animals[0] = "Tiger"
print(animals)

append_animal = animals.append("Giraffe")
print(animals)

extend_animal = animals.extend(["Zebra", "Kangaroo"])
print(animals)

insert_animal = animals.insert(2, "Cheetah")
print(animals)

remove_animal = animals.remove("Elephant")
print(animals)

pop_animal = animals.pop(2)
print(animals)

clear_animal = animals.clear()
print(animals)


# order
# Reverse the order of the mammals list
animals.reverse()
print(animals)

# order
# Sort the mammals list in ascending order
animals.sort()


# len
# Find the number of elements in the mammals list
print(len(animals))

# count
# Count the number of times "Lion" appears in the mammals list
print(animals.count("Lion"))