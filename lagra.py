users = {"felix":"1234", "marcus":"££££££"}
items = {"felix":["en måne","en swimmingpool","apelsinkrokant"],"marcus":["kanelbulle","elskåp","röd tröja"]}

def welcome():
    print("Welcome to Lagra (TM)");
    answer = options(False)
    if (answer == "q"):
        True
    elif (answer == "l"):
        goToLogin()    
    else:
        print("Invalid command");
        welcome()

def options(retry):
    if retry:
        print("	r) Retry")
    else:
        print("	l) Log in")
    print("	q) quit")
    return input("Option: ")

def goToLogin():
    user = input("	User: ")
    if user in users.keys():
        password = input("    Password: ")
        if password == users[user]:      
            print(f"Welcome {user}")   
            while loggedIn(user):
                True
            welcome()
        else:
            print("Wrong password")
            answer = options(True)
            if (answer == "q"):
                True
                #break
            elif (answer == "r"):
                goToLogin()
    else:
        print("Invalid user")
        answer = options(True)
        if (answer == "q"):
            True
        elif (answer == "r"):
            goToLogin()
    
def loggedIn(user):
    print("")
    print("Select an action")
    print("	a) Add item")
    print("	l) List items")
    print("	q) Log out")
    
    answer = input("Option: ")
    if answer == "q":
        return False
    elif answer == "a":
        addItem(user)
    elif answer == "l":
        printItems(user)
    else:
        print("Invalid command")
    return True
    
    
def printItems(user):
    print("These are your items")
    index = 1
    for item in items[user]:
        print(f"{index}: {item}")
        index += 1

def addItem(user):
    items[user].append(input("Add item: "))

welcome()
