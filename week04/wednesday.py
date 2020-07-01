# writing your first while loop
print("Test 1 Exercise ---------------------")

health = 10
while health > 0:
    print(health)
    health -= 1
print("sali!")

# using two or more loops together is called a nested loop
print("Test 2 Exercise ---------------------")

for i in range(2):
    for j in range(3):
        print(i, j)

# exercise 1
# User Input: Write a while loop that continues to ask for user input and runs 
# until they type “quit”.
print("Exercise 1 ---------------------")

exitWord = "quit"
exit = False
while not exit:
    word = input("Echo chamber... to quit write quit: ")
    if(word.lower() == exitWord):
        exit = True

# exercise 2 Double Loop: Write a for loop within a while loop that will count from 0 to 5, 
# but when it reaches 3, it sets a game_over variable to True and breaks out of
# the loop. The while loop should continue to loop until game_over is True. The
# output should only be 0, 1, 2.
print("Exercise 2 ---------------------")

game_over = False
while not game_over:
    for count in range(6):
        if(count > 2):
            game_over = True
            break
        print(count)