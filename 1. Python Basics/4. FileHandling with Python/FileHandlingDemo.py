#file = open("SampleFile.txt")

#Reads all the content on te file
#argument : n -> number of charaters oby passsing parameter
#print(file.read())

#Reads one line in the file
#print(file.readline())

#Prints each line in the content
# newline = file.readline()
#
# while newline != "":
#     print(newline)
#     newline = file.readline()

#This will transfer a copy of content in each line to a list indicating each line as an elemnebt in list
#print(file.readlines())
#
# for line in file.readlines():
#     print(line)

# commit_messages= file.readlines()
#
# commit_id= int(input("Enter the commit id: "))
#
# #Split -> (seperator character, number of occurance)
# print(commit_messages[-commit_id].split(":", 1))
#
# file.close()

#TO create the file (x is the mode to create te new file
#commitfile = open('git-commit-file.txt', 'x')

#Now, Read tehe files with all the lines
#Reverse the list
#Write the list back to the file
with open('Files/SampleFile.txt', 'r') as file:
    commit_messages = file.readlines()
    print(reversed(commit_messages))
    with open('Files/git-commit-file.txt', 'w') as commit:
        for line in reversed(commit_messages):
            commit.write(line+"\n")
