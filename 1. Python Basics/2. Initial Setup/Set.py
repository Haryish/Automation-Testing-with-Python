# ---- Sets in Python ----

# A set in Python is an unordered collection of unique elements.
# Sets are useful when you want to store distinct values and perform set operations like union, intersection, and difference.

# Key Features of Sets:
# - Unordered: The elements have no defined order.
# - Unique Elements: Duplicates are automatically removed.
# - Mutable: You can add or remove elements from a set.
# - Immutable Elements: Set elements must be hashable, so mutable objects like lists cannot be added.

# ---- Creating Sets ----

# Using curly braces {} to create a set
my_set = {1, 2, 3}
print("Set using {}:", my_set)  # Output: {1, 2, 3}

# Using set() constructor to create a set from an iterable
my_set = set([1, 2, 3, 3])  # Converts list to set (duplicates removed)
print("Set using set() constructor:", my_set)  # Output: {1, 2, 3}

# Creating an empty set
empty_set = set()  # Use set(), not {} which creates an empty dictionary
print("Empty set:", empty_set)  # Output: set()

# ---- Common Set Operations ----

# Adding elements to a set
my_set = {1, 2}
my_set.add(3)  # Adds a single element
print("Set after adding an element:", my_set)  # Output: {1, 2, 3}

# Updating set with multiple elements
my_set.update([4, 5])  # Adds multiple elements
print("Set after updating with multiple elements:", my_set)  # Output: {1, 2, 3, 4, 5}

# Removing elements from a set
my_set.remove(2)  # Removes 2 (raises error if element not found)
my_set.discard(4)  # Removes 4 (does nothing if element not found)
print("Set after remove and discard operations:", my_set)  # Output: {1, 3, 5}

# Popping an element (removes and returns an arbitrary element)
popped = my_set.pop()
print("Popped element:", popped)
print("Set after pop:", my_set)  # Output: The set without the popped element

# Clearing all elements from the set
my_set.clear()
print("Set after clearing all elements:", my_set)  # Output: set()

# ---- Set Operations ----

# Union of sets (combines elements from both sets)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union of sets:", set1 | set2)  # Output: {1, 2, 3, 4, 5}
print("Union using .union():", set1.union(set2))  # Output: {1, 2, 3, 4, 5}

# Intersection of sets (common elements between sets)
print("Intersection of sets:", set1 & set2)  # Output: {3}
print("Intersection using .intersection():", set1.intersection(set2))  # Output: {3}

# Difference of sets (elements in set1 but not in set2)
print("Difference of sets:", set1 - set2)  # Output: {1, 2}
print("Difference using .difference():", set1.difference(set2))  # Output: {1, 2}

# Symmetric Difference (elements in either set, but not both)
print("Symmetric Difference of sets:", set1 ^ set2)  # Output: {1, 2, 4, 5}
print("Symmetric Difference using .symmetric_difference():", set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

# ---- Set Methods ----

# Membership Testing (check if an element is in the set)
print("Is 2 in set1?", 2 in set1)  # Output: True
print("Is 4 in set1?", 4 in set1)  # Output: False

# Subset and Superset Testing (check relationships between sets)
set3 = {1, 2}
print("Is set3 a subset of set1?", set3.issubset(set1))  # Output: True
print("Is set1 a superset of set3?", set1.issuperset(set3))  # Output: True

# Disjoint Testing (check if two sets have no elements in common)
set4 = {4, 5}
print("Are set1 and set4 disjoint?", set1.isdisjoint(set4))  # Output: True

# ---- Frozen Sets ----

# A frozen set is an immutable version of a set. Once created, it cannot be modified.

# Creating a frozen set
frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)  # Output: frozenset({1, 2, 3})

# Operations on frozen sets (union, intersection, difference) are supported
print("Frozen set union:", frozen | {4, 5})  # Output: frozenset({1, 2, 3, 4, 5})

# Frozen sets do not support add() or remove() methods
# frozen.add(4)  # This will raise an AttributeError

# ---- Examples ----

# Removing duplicates from a list using set
my_list = [1, 2, 2, 3, 3, 3]
unique = set(my_list)
print("Unique elements from list:", unique)  # Output: {1, 2, 3}

# Finding common elements between two lists using sets
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print("Common elements between list1 and list2:", common)  # Output: {3, 4}

# ---- Advantages of Sets ----
# - Fast membership testing: Checking x in set is faster than in a list.
# - Automatic duplicate removal: Sets inherently maintain unique elements.
# - Support for mathematical operations: Built-in support for union, intersection, etc.

# ---- Limitations of Sets ----
# - Unordered: You can’t rely on the order of elements.
# - Unhashable elements: Sets cannot contain mutable types like lists or dictionaries.

# ---- Conclusion ----
# Sets are a powerful data structure for storing unique elements and performing mathematical set operations like union, intersection, and difference.
# Their unordered nature makes them perfect for use cases like removing duplicates and fast membership testing.
