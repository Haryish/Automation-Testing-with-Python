# ---- Dictionaries in Python ----

# A dictionary in Python is an unordered collection of data in key-value pairs.
# It allows for fast lookups based on keys, and each key must be unique.

# Key Features of Dictionaries:
# - Unordered: The elements are stored as key-value pairs, but there is no defined order.
# - Mutable: You can change, add, or remove elements.
# - Keys must be unique and hashable (e.g., strings, integers, tuples).
# - Values can be of any data type (e.g., strings, lists, other dictionaries).

# ---- Creating Dictionaries ----

# Using curly braces {} to define a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Dictionary using {}:", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using the dict() constructor to create a dictionary
my_dict = dict(name="Alice", age=30, city="New York")
print("Dictionary using dict():", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Creating an empty dictionary
empty_dict = {}
print("Empty Dictionary:", empty_dict)  # Output: {}

# ---- Dictionary Operations ----

# Accessing values by keys
print("Value associated with key 'name':", my_dict['name'])  # Output: Alice

# Using .get() method to access values (returns None if key does not exist, instead of throwing an error)
print("Value associated with key 'age':", my_dict.get('age'))  # Output: 30
print("Value associated with key 'gender':", my_dict.get('gender'))  # Output: None

# Modifying values in a dictionary
my_dict['age'] = 31  # Modify existing value
print("Dictionary after modifying 'age':", my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Adding new key-value pairs
my_dict['gender'] = 'Female'
print("Dictionary after adding a new key-value pair:", my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'gender': 'Female'}

# Removing items from a dictionary
del my_dict['city']  # Removes the key 'city' and its associated value
print("Dictionary after removing 'city':", my_dict)  # Output: {'name': 'Alice', 'age': 31, 'gender': 'Female'}

# Using pop() to remove an item and return its value
removed_item = my_dict.pop('gender')
print("Removed item:", removed_item)  # Output: Female
print("Dictionary after pop():", my_dict)  # Output: {'name': 'Alice', 'age': 31}

# Using popitem() to remove and return a random key-value pair
random_item = my_dict.popitem()
print("Randomly removed item:", random_item)  # Output: ('age', 31)
print("Dictionary after popitem():", my_dict)  # Output: {'name': 'Alice'}

# Clearing the entire dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)  # Output: {}

# ---- Dictionary Methods ----

# Accessing all keys in a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Keys in the dictionary:", my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# Accessing all values in a dictionary
print("Values in the dictionary:", my_dict.values())  # Output: dict_values(['Alice', 30, 'New York'])

# Accessing all key-value pairs in a dictionary
print("Items in the dictionary:", my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Checking if a key exists in the dictionary
print("Is 'name' a key in the dictionary?", 'name' in my_dict)  # Output: True
print("Is 'address' a key in the dictionary?", 'address' in my_dict)  # Output: False

# ---- Dictionary Comprehensions ----

# Creating a dictionary using dictionary comprehension
squares = {x: x**2 for x in range(5)}
print("Dictionary of squares:", squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ---- Nested Dictionaries ----

# A dictionary can contain another dictionary as a value.
nested_dict = {'person': {'name': 'Alice', 'age': 30}, 'city': 'New York'}
print("Nested Dictionary:", nested_dict)  # Output: {'person': {'name': 'Alice', 'age': 30}, 'city': 'New York'}

# Accessing values in a nested dictionary
print("Name from nested dictionary:", nested_dict['person']['name'])  # Output: Alice

# ---- Advantages of Dictionaries ----

# - Fast lookups: Retrieving a value by key is very efficient.
# - Mutable: You can add, remove, or update items in the dictionary.
# - Allows for different data types as keys and values (strings, integers, lists, etc.).
# - Keys must be unique, so there is no duplication of keys.

# ---- Limitations of Dictionaries ----

# - Unordered: Dictionaries do not maintain the order of insertion (Python 3.6+ maintains insertion order, but this is an implementation detail, not a language feature).
# - Mutable Keys: Keys must be hashable, so mutable data types (like lists) cannot be used as keys.
# - Memory consumption: Dictionaries can be memory-intensive due to storing keys and values.

# ---- Examples ----

# Mapping keys to values (e.g., mapping student IDs to names)
student_dict = {101: "John", 102: "Alice", 103: "Bob"}
print("Student Dictionary:", student_dict)  # Output: {101: 'John', 102: 'Alice', 103: 'Bob'}

# Reversing a dictionary (swap keys and values)
reversed_dict = {v: k for k, v in student_dict.items()}
print("Reversed Dictionary (values as keys):", reversed_dict)  # Output: {'John': 101, 'Alice': 102, 'Bob': 103}

# ---- Conclusion ----

# Dictionaries are highly efficient data structures for associating keys to values. They are widely used for fast lookups and when you need to associate unique keys with specific data.
# The key features include fast access, mutability, and flexibility in the types of data they can store.
