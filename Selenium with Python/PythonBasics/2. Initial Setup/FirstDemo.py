# Kickstart with testing the interpreter with Hello world program
print("hello world")

# Variables and datatypes available
a = "Hello"
b, c = 12, 12.3
e = 100 + 3j
d = True

# Printing and concatenation
print("The value of each value (a,b,c,d) are {}, {}, {}, {}".format(a, b, c, d))
print("The type of variables are {} for a, {} for b, {} for c, {} for d".format(type(a), type(b), type(c), type(d)))

'''Since the Print Function allows string values, to avoid warnings, we use str() with the variables as parameters to 
print them as string '''

print("Value of e allows complex data type " + str(type(e)) + " with value" + str(e))

