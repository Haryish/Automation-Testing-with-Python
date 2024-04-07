import os
'''
Objective:
 Create the CRUD operation that can create, read the content, update / append, delete the file
 Thereby renaming the file, listing out the available files in the folder
'''


def create():
    try:
        newfile = input("Enter the file name with proper standards: ")
        with open("Files/"+newfile, "x") as cfile:
            print("\n Enter your content now...")
            print("\n----------------------------------------------------------------------\n")
            cfile.write(input(""))
            print("\n----------------------------------------------------------------------\n")
    except IOError:
        print("Couldn't able to enter the content, Try Again!! ")
    return "File Created successfully"


def read():
    try:
        print("Enter the file name as per below available files")
        print(os.listdir("./Files"))
        newfile = input("\n")
        if os.path.isfile("./Files"):
            with open(newfile, "x") as rfile:
                print("\n The content you entered are...")
                print("\n----------------------------------------------------------------------\n")
                rfile.read(input(""))
                print("\n----------------------------------------------------------------------\n")
    except IOError:
        print("Couldn't able to enter the content, Try Again!! ")
    return "File Content Read successfully"


def update():

    return "File has appended successfully"


def delete():

    return "File deleted successfully"


def rename():

    return "File renamed successfully"


class FileManagement:
    pass


if __name__ == '__main__':
    file = 'Files/CRUD.txt'
    new_file = 'Files/Sample.txt'
    print("File Handling and management")
    print("Basic Crud Operation")

    crud = FileManagement()
    while True:
        print("\n 1. Create \n 2. Read \n 3. Append \n 4. Delete \n 5. Rename file \n 0. Quit")
        options = int(input("Option: "))
        if options == 1:
            operationCommand = create()
        elif options == 2:
            operationCommand = read()
        elif options == 3:
            operationCommand = update()
        elif options == 4:
            operationCommand = delete()
        elif options == 5:
            operationCommand = rename()
        elif options == 0:
            operationCommand = "See you again!! "
            pass
        else:
            print("\n Invalid Option Number, Please enter again")

        print( operationCommand )