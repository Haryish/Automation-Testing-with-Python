# A string is a sequence of characters enclosed in single, double, or triple quotes.

single_quote = 'Hello'
double_quote = "Hello"
triple_quote = '''Hello'''

# Immutable: Strings in Python cannot be changed after creation.

s = "Python"

# Indexing
print(s[0])  # P
print(s[-1]) # n (last character)

#Slicing
print(s[1:4])  # yth
print(s[:3])   # Pyt (start to index 3, exclusive)
print(s[3:])   # hon (index 3 to end)
print(s[::-1]) # nohtyP (reversed string)

# bAsic Structure: array[initial point: Final Point: Step factor]

# Concatenation
a = "Hello "
b = " World"
print(a + " " + b)  # Hello World
print ("{} + {}".format(a,b))
print("{1} + {0}".format(a,b))
print(f"{a} + {b}")

# Membership operation: 'in' keyword
print("Py" in "Python")  # True
print("Java" not in "Python")  # True

#Common String Methods
print(len(a)) #to get the length
print(a.count('l')) # To get the occurance of the character L
print(a.find("o")) #finds the index of the letter / character/ substring where it starts. Prints -1 if not found
print(a.replace("o","o Python")) # finds and replaces the word - returnable method to assign the new value to new variable
print(" Hello ".strip()) # to trim the spaces around the character
print(" Hello ".lstrip()) # to trim white spaces around left side of chatacter. similar for .rstrip()
r=list("hello")
print(r)
y = [x for x in "hello world".strip()]
z = a+b
cleaned_string = "".join(z.split())
print(cleaned_string)  # Output: "Hello, World!"

# Checking Palindrome
s = "madam"
print(s == s[::-1])  # True


# Checking Anagram
s2 = "roWld"
print(sorted(s2) == sorted(b.strip()))

# Substring
substrings = [a[i:j] for i in range(len(a)) for j in range(i + 1, len(a) + 1)]
print(substrings)  # ['a', 'ab', 'abc', 'b', 'bc', 'c']