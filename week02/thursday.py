#Title
name = "john smith"
print(name.title())
print(name.lower())
print(name.upper())

#Replace
words = "Hello there!"
print(words.replace("!","."))

#Find matches
s = "Look over that way"
print(s.find("over"))

#Strip remove spaces
name = "      john  "
print(name)
print(name.strip( ))
print(name.lstrip( ))
print(name.rstrip( ))

#Split 
s = "These words are separated by spaces"
print(s.split(" "))

exercise01 = "uppercase"
print(exercise01.upper())

exercise02 = "$$John Smith"
print(exercise02.strip("$"))