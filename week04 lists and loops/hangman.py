# import additional functions
from random import choice
import os

# declare game variables

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
        
words = ["tree","table","chair","mouse","roof", "apple", "orange", "elephant","sheep", "plane", "airport", "book"]
word = choice(words)
guessed, lives, game_over = 0, 7, False


# create a list of underscores to the length of the word
guesses = list(len(word) * "_")

while not game_over:
    # output game information
    screen_clear()
    hidden_word = " ".join(guesses)
    print(f"Word to guess: {hidden_word}")
    print(f"Lives: {lives}")

    ans = input("Type quit or guess a letter: ").lower()
    if (ans == "quit"):
        print("Thanks for playing")
        game_over = True
    
    elif ans in word:
        print("You guessed correctly!")

        for i in range(len(word)):
            if(word[i] == ans):
                guesses[i] = ans
                guessed += 1
        if(guessed == len(word)):
            print(f"The word was: {word}")
            game_over = True
    else:
        lives -= 1
        print("Incorrect, you lose a life")
        if(lives <= 0):
            print("Game Over!")
            game_over = True

