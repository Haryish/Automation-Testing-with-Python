
# Tuples
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
my_tuple = 1, 2, 3
print(my_tuple)  # Output: (1, 2, 3)
single_tuple = (5,)  # or 5,
print(single_tuple)  # Output: (5,)
empty_tuple = ()
print(empty_tuple)  # Output: ()
my_tuple = (10, 20, 30, 40)
print(my_tuple[1])  # Output: 20
print(my_tuple[1:3])  # Output: (20, 30)
print(my_tuple[::-1]) # Reverse
print(my_tuple[1::2]) # Step factor = 2

# Operations:
# Concatenation:
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4)

# Repetition:
t = (5, 10)
print(t * 3)  # Output: (5, 10, 5, 10, 5, 10)

# Membership Testing:
t = (1, 2, 3)
print(2 in t)  # Output: True
print(4 in t)  # Output: False

# Length:
print(len((1, 2, 3)))  # Output: 3

# Max and Min:
t = (5, 10, 15)
print(max(t))  # Output: 15
print(min(t))  # Output: 5

# Count Occurrences of an Element:
t = (1, 2, 2, 3, 3, 3)
print(t.count(3))  # Output: 3

# Index of an Element:
print(t.index(2))  # Output: 1 (first occurrence of 2)

# Packing
packed = 1, 2, "hello"  # Tuple packed without parentheses
print(packed)  # Output: (1, 2, 'hello')
a, b, c = packed
print(a,b,c) # Unpacking