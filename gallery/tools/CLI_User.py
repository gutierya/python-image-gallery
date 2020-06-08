import psycopg2

# Menu options to user
def printOptions():
    print(" ")
    print("1)  List users")
    print("2)  Add user")
    print("3)  Edit user")
    print("4)  Delete user")
    print("5)  Quit")

# Listing user
def listUsers():
    print(" ")


# Adding  user
def addUser():
    print(" ")
    adduser_name = input("Username ")
    adduser_pass = input("Password ")
    adduser_fullname = input("Full name ")


# Editing user
def editUser():
    print(" ")
    edit_username = input("Edit user")
    else:
        print('That user doesnt exist sadly')


# Deleting user
def deleteUser():
    print(" ")
    delete_username = input("Enter user to delete ")
    delete_choice = input("Sure you want to delete?? ")
        if delete_choice == 'y':
        #delete
    else:
        print("User no exist ")


# Main
def main():
    print("1) List Users\n2) Add user\n3) Edit user\n4) Delete user\n5) Quit")
    c = int(input("Enter command"))
    if c == 1:
        listUser()
    elif c == 2:
        addUser()
        listUser()
    elif c == 3:
        editUser()
        listUser()
    elif c == 4:
        deleteUser()
        listUser()
    elif c == 5:
        quit()

if __name__ == '__main__':
    main()
