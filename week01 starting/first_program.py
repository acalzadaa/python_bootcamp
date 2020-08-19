from random import randint

guessed = False
number = randint(0,100)
guesses = 0
while not guessed:
    ans = input("guess the number from 0 to 100: ")
    guesses += 1
    if int(ans) == number:
        print("yer right!")
        print("you needed {} times to triump! ".format(guesses))
        break
    elif int(ans) > number:
        print("the number is lower! ")
    elif int(ans) < number:
        print("the number is higher! ")
    