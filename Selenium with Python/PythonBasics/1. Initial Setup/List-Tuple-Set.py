# For More content: https://www.digitalocean.com/community/tutorials/python-data-types

# from FirstDemo import d, e
# you can use import as above, but while calling the class, it will utilize all the print statements available there
# b, c, d, e = fa.b, fa.c, fa.d, fa.e

# List, Set, Tuples
# visit

values = [1, 2, "a", 4, 5.0]
print("Multiple values can be done in a single variable called 'values' = " + str(values))
print("Values in middle: " + values[2])  # prints "a"

ptr = 3
print("First {} values are : ".format(ptr), values[:ptr])
print("Middle Value: ", values[int((len(values)) / 2)])
print("Last {} values are : ".format(ptr), values[-ptr:len(values)])

# List Manipulation
'''Lets add variable b,c,d and e to list, modify values[2] with value of variable a and remove the value of a,d,
e from the list '''
values.append("d")
print("After insertion: Value = " + str(values))
values.append(["e"])
print("After insertion: Value = " + str(values))
values[len(values) - 1] = "e"
# print("After Modification: Value = " + str(values))
# values[5:7] = d, e
print("After Modification: Value = " + str(values))
values.pop()
print("After Deletion of last element: Value = " + str(values))
values.remove(values[2])
print("After Deletion of '2'nd element: Value = " + str(values))
# values.remove(fa.d)  # won't change anything as there has no value exist
values.pop()
values.remove(5.0)
print("After Deletion of Last two values: Value = {0}".format(str(values)))
