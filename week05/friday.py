# Friday: Creating a Shopping Cart



# declare game variables
import os
# global list variables
cart = []

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
        
# create functions to add items to cart
def addItems(item):
    screen_clear()
    cart.append(item)
    print(f"{item} has been added")

# create function to remove items from cart
def removeItems(item):
    screen_clear()
    try:
        cart.remove(item)
        print(f"{item} has been removed")
    except:
        print(f"{item} not in the list")

# create a function to show items in cart
def showCart():
    screen_clear()
    if cart:
        print("Here is your cart:")
        for item in cart:
            print(f"- {item}")
    else:
        print("Cart is empty.")

# create function to clear items from cart
def clearCart():
    screen_clear()
    cart.clear()
    print("Cart is empty.")
    
# create main function that loops until the user quits
def main():
    done = False
    while not done:
        ans = input("Quit/Add/Remove/Show/Clear: ").lower()
        # Base Case
        if ans == "quit":
            print("Goodbye!")
            showCart()
            done = True
        elif ans == "add":
            item = input("Enter item to add: ")
            addItems(item)
        elif ans == "remove":
            showCart()
            item = input("Enter item to remove: ")
            removeItems(item)
        elif ans == "show":
            showCart()
        elif ans == "clear":
            clearCart()
        else: 
            print("Invalid option")
        

main()