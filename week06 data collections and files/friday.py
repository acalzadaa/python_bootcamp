# Friday: Creating a User Database with CSV Files
import csv
import os

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


# registering a user
def registerUser():
    with open("user.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter = ",")
        print("To register, please enter your info: ")
        email = input("E-mail: ")
        password = input("Password: ")
        password2 = input("Re-type password: ")
        screen_clear()
        if password == password2:
            writer.writerow([email, password])
            print("You are now registered!")
        else: 
            print("Something when wrong. Try again.")
        


# logging a user in

def loginUser():
    print("To login, please enter your info:")
    email = input("E-mail: ")
    password = input("Password: ")
    screen_clear()
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("You are now logged in!")
                return True
    print("Something went wrong, try again!")
    return False




def main():
    active = True
    logged_in = False
    while active:
        if logged_in:
            print("1. (L)ogout \n2. (Q)uit")
            choice = input("what would you like to do? [L/Q]: ").lower()
            screen_clear()
            if choice == "logout" or choice == "l" or choice == "1" and logged_in == True:
                logged_in = False
                print("You are now logged out.") 
            elif choice == "quit" or choice == "q" or choice == "2":
                active = False
                print("Thanks for using our software")
            else:
                print("Sorry, please try again")                
        else:
            print("1. (L)ogin\n2. (R)egister\n3. (Q)uit")
            choice = input("what would you like to do? [L/R/Q]: ").lower()
            screen_clear()            
            if choice == "register" or choice == "r" or choice == "2" and logged_in == False:
                registerUser()
            elif choice == "login" or choice == "l" or choice == "1" and logged_in == False:
                logged_in = loginUser()
            elif choice == "quit" or choice == "q" or choice == "3":
                active = False
                print("Thanks for using our software")
            else:
                print("Sorry, please try again")

main()