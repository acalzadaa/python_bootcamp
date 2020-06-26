# using an else statement
print("1) Using IF ELSE")
name = input("Whats your name?: ")
if name == "Jacob":
    print("Hello Jacob!")
else:
    print(f"Hello {name.upper()}")
    
# writing a full conditional statement with if, elif, else
print("2) Using IF ELIF")
name = "John"
if name[0] == "A":
    print("Name starts with an A")
elif name[0] == "B":
    print("Name starts with a B")
elif name[0] == "J":
    print("Name starts with a J")
else: # covers all other possibilities
    print( f"Name starts with a {name}")
    
# exercise 1... fix the bug! output Hello John
name = "John"
if name == "Jack":
    print("Hello Jack")
elif name=="John":
    print("Hello John")

# exercise 2... receive the time in military time... output 
# Good Morning if less than 1200
# Good Afternoon if between 1200 and 1700 
# Good Evening if equal or above 1700
    
print("Exercise 2: input an hour in military time")
try:
    time = input("What time is it (0000-2359)?: ")

    #is 4 characters?
    if len(time) == 4:
        hour = int(time[0:2])
        minutes = int(time[2:4])
        print(f"hour {hour}, minutes {minutes}")
        
        if hour <= 12:
            print("Good Morning!")
        elif hour > 12 and hour <= 17:
            print("Good Afternoon!")
        elif hour > 17 and hour < 24:
            print("Good Evening!")
        else:
            print(f"Error: bad time! {time}")
    else:
        print(f"Error, {time} no es una hora valida")

except:
    print("Only numbers from 0000 to 2359 are valid")

