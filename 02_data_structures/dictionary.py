"""
They store a collection of key-based items, of any data type, defined within curly brackets.
The key difference between dictionaries and previous 
data structures is that they are stored in pairs; 
that is, the key and the value itself, separated by a colon.

The key is used to identify the value. 
Therefore, we can access an item in a dictionary using its respective key.

Since the keys act as identifiers, they must be unique and no duplicates are allowed.

Dictionaries are mutable in that we can modify the value associated with a particular key. 
It is also possible for us to add or remove key: value pairs from an existing dictionary.
"""
# Create an empty dictionary called "person"
person = {}

# Create a dictionary with key-value pairs
person = {
    "name": "John",
    "age": 30,
    "is_student": False
}
print(person)

# Create a dictionary from a list of tuples
person_list = [("name", "John"), ("age", 30), ("is_student", False)]
person = dict(person_list)
print(person)

# Create a dictionary from two lists
keys = ["name", "age", "is_student"]
values = ["John", 30, False]
person = dict(zip(keys, values))
print(person)

# Create a dictionary from two tuples
keys = ("name", "age", "is_student")
values = ("John", 30, False)
person = dict(zip(keys, values))
print(person)

# Access the value of a key in the dictionary
print(person["name"])

# Access the value of a key using the get() method
print(person.get("age"))

# Access the value of a key using the get() method with a default value
print(person.get("address", "Unknown"))

# Add a new key-value pair to the dictionary
person["address"] = "123 Main Street"
print(person)

# Modify the value of a key in the dictionary
person["name"] = "Jane"
print(person)

# Remove a key-value pair from the dictionary
del person["is_student"]
print(person)

# Check if a key is in the dictionary
print("name" in person)

# Check if a value is in the dictionary
print("Jane" in person.values())

# Get the number of key-value pairs in the dictionary
print(len(person))

# Get all the keys in the dictionary
print(person.keys())

# Get all the values in the dictionary
print(person.values())

# Get all the key-value pairs in the dictionary
print(person.items())

# Copy a dictionary
person_copy = person.copy()
print(person_copy)

# Clear a dictionary
person.clear()
print(person)

# Delete a dictionary
del person

# Create a dictionary with mixed data types
person = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "grades": [90, 85, 88]
}
print(person)

# Access a value within a list in the dictionary
print(person["grades"][0])

# Access a value within a dictionary in the dictionary
person["address"] = {"street": "123 Main Street", "city": "New York"}
print(person["address"]["city"])

# Create a dictionary with nested dictionaries
person = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "address": {
        "street": "123 Main Street",
        "city": "New York"
    }
}
print(person)

# Access a value within a nested dictionary
print(person["address"]["city"])

# Create a dictionary with a dictionary as a key
person = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "address": {
        "street": "123 Main Street",
        "city": "New York"
    },
    "contact": {
        "email": "  [email protected]", "phone": "123-456-7890" }
}
print(person)

# Access a value within a nested dictionary
print(person["contact"]["email"])

# Create a dictionary with a dictionary as a value
person = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "address": {
        "street": "123 Main Street",
        "city": "New York"
    },
    "contact": {
        "email": "  [email protected]", "phone": "123-456-7890" }
}
print(person)

# Access a value within a nested dictionary
print(person["contact"]["email"])
