def isPalindrome(word):
    word_temp = word[::-1]
    if word == word_temp:
        return True
    else: 
        return False

def main():
    word = input("Enter a word: ")
    if isPalindrome(word):
        print(f"The word {word} is palindrome!")
    else:
        print(f"The word {word} is not palindrome!")

main()