""" 
A tuple is created by assigning a group of comma-separated values 
enclosed within round brackets to a variable.
"""
# Example
my_tuple = (1, 2, 3)
print(my_tuple) 

# Example 2: Accessing elements by index
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[0])  
print(my_tuple[2])  

# Example 3: Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14)
print(mixed_tuple)

# Example 4: Nested tuple
nested_tuple = (1, (2, 3), ('a', 'b'))
print(nested_tuple) 

# Example 5: Trying to modify a tuple (this will raise an error)
my_tuple = (1, 2, 3)
my_tuple[0] = 10  

# Example 6: Slice animal_tuple from index 1 to index 3
animal_tuple = ("Yellow anaconda", "Reptile", 30.5, 20)
sliced_tuple = animal_tuple[1:4]
print(sliced_tuple)

#Example 7: Return the number of elements in animal_tuple
length_of_tuple = len(animal_tuple)
print(f"No. of attributes: {length_of_tuple}")

# Count the occurrence of the value False in animal_tuple
count_false = animal_tuple.count(False)
print(count_false)

# Assign each element in animal_tuple to individual variables
animal_tuple = ("Yellow anaconda", "Reptile", 30.5, 20)

name, group, av_weight, av_lifespan = animal_tuple
print(f"Name: {name}")
print(f"Group: {group}")

