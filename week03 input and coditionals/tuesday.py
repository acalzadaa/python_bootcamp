# using an if statement to only runcode if the condition is met
print("keyword IF/THEN: ")

x, y = 5, 10
if x < y:
    print("x is less than y")

# checking user input
print("keyword INPUT: ")

try:
    ans = int(input("What is 5 + 5? "))
    if ans == 10:
        print("you got it right!")
except:
    print("Hey! only numbers!")

# using the keyword 'not' within an 'if statement'
print("keyword NOT: ")

flag = False
if not flag:
    print("Flag is False")

# using the keyword 'in' within and 'if statement'
print("keyword IN: ")

word = "Baseball"
if "b" in word:
    print(f"{word} contains the character b")

if "x" in word:
    print(f"{word} doesn't contain the character x")

# exercise part1
print("exercise part1: does it contains ES?")
try:
    ans = input("write a word: ")
    if "es" in ans:
        print("hurray!")
    else:
        print("buuu")
except:
    print("only words!")

# exercise part2
print("exercise part2: does it end with ING?")
try:
    ans = input("write a word: ")
    if len(ans) > 3:
        if ans.endswith("ing"):
            print("yeah!")
        else:
            print("buu")
    else:
        print("cheater!")
except:
    print("only words!")

# exercise check equality
print("exercise equality: are the two words equal?")

word1 = input("write the first word: ").lower()
word2 = input("write the second word: ").lower()




