global usernames
usernames = []
global passwords
passwords = {}
buttons = ""



def signupUser():
    global usernames
    createusername = input("School ID#: ")
    if createusername in usernames:
        print("\n That username is already been used \n")
    else:
        usernames.append(createusername)
        createpassword=input("Create a password (Try to use caps or numbers or symbols to strengthen your password. i.e.:K, 1, !): ")
        passwords[createusername] = createpassword
        print("\n Congratulations, your account has been created \n")
        openMenu()

def loginUser():
    urusername = input("School ID#: ")
    urpassword = input("Password: ")
    if urusername in usernames and passwords[urusername] == urpassword:
        print ("\n Login successful, welcome", urusername)
        openMenu()
    else:

        print ("\n Login Unsuccessful, you will be redirected to the home page")
        openMenu()


def openMenu():

    buttons = input("Hello \n Press '1' to Login, '2' to Sign Up, and '3' to Quit")

    if buttons == "1":
        loginUser()
    elif buttons == "2":
        signupUser()

while buttons == "3":
    print("See you again soon")
    openMenu()

openMenu()






