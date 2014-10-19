password = ""
while password != "secret":
    password = input("Please enter the password: ")
    if password == "secret":
        print("You now have access to the system.")
    else:
        print("Sorry the value entered in incorrect - try again.")
