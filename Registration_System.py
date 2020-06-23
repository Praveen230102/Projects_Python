# here we have to work on a project
# the project is simple
# It's on registering
# we have to make a program in which we can register if our name is not there
# now here is the overview of the project
# -------------------------------------------------------------------------------------------------------------
#                     WELCOME
#
#         If you have registered ID then login
#         If you are new here then register


#           WHEN WE WANT TO LOGIN -------
#           INPUT THE USER NAME
#            INPUT THE PASSWORD
#           IF THE PASSWORD IS INCORRECT THEN ASK FOR TRY AGAIN
#            ELSE
#           THANKS FOR COMING


#           WHEN WE WANT TO REGISTER
#           INPUT THE USER NAME
#           INPUT THE EMAIL ID
#           INPUT THE PASSWORD
#           INPUT PASSWORD AGAIN TO CONFIRM
#
#           NOW HERE COMES MORE CONDITIONS -------------
#
#           FIRST CONDITION ----------------
#           IF THE USER NAME IS ALREADY PRESENT THEN ASK USER TO ENTER ANOTHER USER NAME
#
#           SECOND CONDITION ---------------
#           IF THE USER NAME IS VALID BUT THE CONFIRM PASSWORD IS INCORRECT THEN ASK USER TO ENTER PASSWORD AGAIN
#           TILL PASSWORD AND CONFIRM PASSWORD IS SAME

#           IF BOTH USER NAME AND CONFIRM PASSWORD IS SATISFIED THEN PRINT
#           YOU HAVE BEEN REGISTERED SUCCESSFULLY

#         --------------------------------- THANKS FOR REGISTERING --------------------------

#   WE HAVE TO MAKE FUNCTIONS FOR EVERY THING
#   > INPUT THE USER NAME PASSWORD FOR LOGIN
#   > INPUT THE EMAIL, USER NAME, PASSWORD, CONFIRM PASSWORD FOR REGISTERING
#   > CHECK FOR PASSWORD AND CONFIRM PASSWORD
#   > CHECK FOR USER NAME IN DICTIONARY
#   > THAT DICTIONARY WILL BE GLOBAL AND ANY FUNCTION CAN HAVE ACCESS TO THIS DICTIONARY

#   ---------------------------------------------------------------------------------------------
from _collections import OrderedDict
database = OrderedDict()
# Coder used this ordered dict because it takes care of the order user is providing but normal dictionary don't
# keep track of that


def user_name_check(x):
    if x in database:
        return 0
    else:
        return 1


def intro():
    # register the user
    # input the name of user
    name = input("Enter your name > ")
    # input the user name
    username = input("Enter your user name > ")
    # input email ID of user
    email = input("Enter your email ID > ")
    # input password of user
    password = input("Enter your password > ")
    # input password again
    con_pass = input("Enter your password again > ")
    return name, username, email, password, con_pass

def check_pass(x, y):
    if x == y:
        return True
    else:
        return False


print("""                              _ _ _                   _ _ _     _ _  _ _                    _ _ _     _ _ _
  |  |\   |  |\    |     |   |        |\       /|   |       |       |       |              |         |       |    |\      /|
  |  | \  |  | \   |     |   |_ _ _   | \     / |   |_ _ _  |       |       |              |         |       |    | \    / |
  |  |  \ |  | /   |     |        |   |  \   /  |   |       |       |       |              |         |       |    |  \  /  |
  |  |   \|  |/    |_ _ _|   _ _ _|   |   \/    |   |       |   _ _ | _ _    _ _ _    ()   |_ _ _    | _ _ _ |    |   \/   |
                                        """)
# print("------------------------------WELCOME ------------------------------")
print("If you want to login then type 1 else type 0 !")
temp = int(input())
# now check if user wants to login then use login input function else logout input function
# calling login_input function for input user name and password
if temp == 1:
    uname1 = input("Enter your User Name > ")
    password1 = input("Enter your password > ")
    if uname1 not in database:
        print("The user name and password you entered is not found !!")
        print("Please try again !!")
    elif uname1 in database and password1 != database[uname1]:
        print("You entered wrong password !!")
        print("Please try again with correct password !!")
    elif uname1 in database and database[uname1] == password1:
        print("Thanks for login !!")
        print("Enjoy Your Day. ")
# now here comes the another important work
# what if user wants to register
else:
    name, username, email, password, con_pass = intro()
    # let's say the user name is invalid that means that user name is already taken
    if user_name_check(username) == 0:
        # so in that case we will print this msg
        print("This user name is not valid.")
        print("Please try again with another user name !! ")
        # now check if the user name is present in data base or not
        # if user name is already present in data base then user a while until user enter valid user name
        while user_name_check(username) != 1:
            # after that we will use this loop which goes until user input the valid user name
            # this will again ask for the same detail
            name, username, email, password, con_pass = intro()
            if user_name_check(username) == 1:
                # now we have checked user name now we have to check for password
                break
            else:
                print("This user name is not valid.")
                print("Please try again with another user name !! ")
                continue
        # after getting checked for user name now its time to check the password
        # so check_pass is a function which get both password as well confirm password and return true or false on
        # the basis that password is same or not
        if check_pass(password, con_pass):
            # in this case the password and confirm password is same
            # so the user registered successfully
            # this means we have been entered user name correctly and now we have been entered the password correctly
            print("Registering ..........")
            print("You have been registered successfully.")
        else:
            # if not
            # now we have to user the same technique which we have been used while checking user name
            # firstly we will print this msg
            print("You have entered wrong password!!")
            print("Please try again with another password.")
            # after that we will ask for the same set of information again until password and confirm password wil be
            # same
            # but the main thing which I am considering is that the user again inputs valid user name
            # I am thinking that user is not dumb
            # hold on the code is updated and if user is dumb he is not able to register
            # coder have been updated that code
            while not check_pass(password, con_pass) or user_name_check(username) == 0:
                name, username, email, password, con_pass = intro()
                if check_pass(password, con_pass) and user_name_check(username) == 1:
                    print("Registering ..........")
                    print("You have been registered successfully.")
                    print("Thanks for coming .")
                    # when we get that user have been entered valid user name and password then we will break this loop
                    break
                else:
                    print("You entered the wrong info !!")
                    print("Either your username or your password is invalid !!")
                    print("Please check it and try again !!")
                    continue
    else:
        # this means the user name we entered is correct user name and now we have to check for password and confirm
        # password
        if check_pass(password, con_pass):
            # this means we have been entered user name correctly and now we have been entered the password correctly
            print("Registering ..........")
            print("You have been registered successfully.")
        else:
            # now we have to user the same technique which we have been used while checking user name
            print("You have entered wrong password!!")
            print("Please try again with another password.")
            # this is the same thing we have been done above user will enter the set of information until every thing
            # is correct
            while not check_pass(password, con_pass) or user_name_check(username) == 0:
                name, username, email, password, con_pass = intro()
                if check_pass(password, con_pass) and user_name_check(username) == 1:
                    print("Registering ..........")
                    print("You have been registered successfully.")
                    print("Thanks for coming .")
                    break
                else:
                    print("You entered the wrong info !!")
                    print("Either your username or your password is invalid !!")
                    print("Please check it and try again !!")
                    continue
