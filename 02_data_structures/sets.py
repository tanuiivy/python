"""
Another common data structure in Python is a set which is a collection of unique items. 
Sets can contain elements of different data types and are defined using curly brackets.
"""
# Create an empty set called "unique_numbers"
unique_numbers = set()

# Create a set with unique numbers
unique_numbers = {1, 2, 3, 4, 5}

# Create a set from a list
numbers = [1, 2, 3, 4, 5]
numbers_set = set(numbers)

# Create a set from a tuple
numbers_tuple = (1, 2, 3, 4, 5)
numbers_set = set(numbers_tuple)

# Create a set from a string
numbers_string = "12345"
numbers_set = set(numbers_string)

# Create a set from a range
numbers_range = range(1, 6)
numbers_set = set(numbers_range)

# Check the type of the variable
type(numbers_set)

# Add an element to the set
numbers_set.add(6)
print(numbers_set)

# Remove an element from the set
numbers_set.remove(6)
print(numbers_set)

# Check if an element is in the set
print(1 in numbers_set)

# Combine two sets
numbers_set2 = {6, 7, 8, 9, 10}
numbers_combined = numbers_set.union(numbers_set2)
print(numbers_combined)

# Find the intersection of two sets
numbers_intersection = numbers_set.intersection(numbers_set2)
print(numbers_intersection)

# Find the difference between two sets                      
numbers_difference = numbers_set.difference(numbers_set2)
print(numbers_difference)

# Find the symmetric difference between two sets
numbers_symmetric_difference = numbers_set.symmetric_difference(numbers_set2)
print(numbers_symmetric_difference)

# Check if a set is a subset of another set
numbers_subset = {1, 2, 3}
print(numbers_subset.issubset(numbers_set))

# Check if a set is a superset of another set
numbers_superset = {1, 2, 3}
print(numbers_set.issuperset(numbers_superset))

# Check if two sets are disjoint
numbers_disjoint = numbers_set.isdisjoint(numbers_set2)
print(numbers_disjoint)

# Clear the set
numbers_set.clear()
print(numbers_set)

# Delete the set
del numbers_set
print(numbers_set)




