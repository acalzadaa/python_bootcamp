# end of week project
# making a calculator!

# 1. Ask the user for the calculation they would like to perform.
# 2. Ask the user for the numbers they would like to run the operation on.
# 3. Set up try/except clause for mathematical operation.
#    a. Convert numbers input to floats.
#    b. Perform operation and print result.
#    c. If an exception is hit, print error.

# Step 1
operation = input("select an operation [a]dd, [s]ubstract, [m]ultiply, [d]ivide: ")
print(f"you selected: {operation}")
try:
    first = float(input("first number: "))
    second = float(input("second number: "))
    if len(operation) == 1:
        print("listo!")
        if operation.lower() == "a":
            print("seleccionaste Add")
            print(f"{first} + {second} = {(first+second)}")
        elif operation.lower() == "s":
            print("Seleccionaste Substract")
            print(f"{first} - {second} = {(first-second)}")
        elif operation.lower() == "m":
            print("Seleccionaste Multiply")
            print(f"{first} x {second} = {(first*second)}")
        elif operation.lower() == "d":
            print("Seleccionaste Divide")
            print(f"{first} / {second} = {(first/second)}")    
    else:
        print(f"invalid input! {operation}")               
except:
    print("Error!")
