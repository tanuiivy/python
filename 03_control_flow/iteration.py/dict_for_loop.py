# Creating a dictionary 'person' to store information about an individual
person = {
    "name": "Ivy",  # Name of the person
    "age": 20,  # Age of the person
    "is_student": False,  # Boolean value indicating if the person is a student
    "address": {  # Nested dictionary to store address details
        "street": "123 Main Street",  # Street address
        "city": "New York"  # City name
    }
}

# Printing the value associated with the key 'name' from the 'person' dictionary
print(person["name"])  # Output: John

# Looping through the dictionary items (key-value pairs)
for dkeys, dvalues in person.items():
    # Printing each key and its corresponding value in the 'person' dictionary
    print(f"The key is {dkeys} and the value is {dvalues}")
