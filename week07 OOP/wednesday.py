class Dog():
    name = ""
    sound = "Bark"
    age = 8

    def happy_birthday(self):
        self.age += 1
    def make_sound(self):
        print(self.sound)
    def print_info(self):
        print("I am dog.")
    def show_age(self, age):
        print(f"I am {age} years old!")

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    def print_info_plus(self):
        if self.get_age() < 10:
            print("Puppy!")
        else:
            print("Dog!")

    def __str__(self):
        return "This is a Dog class"

# understanding which methods are accesible 
# via the class itself and class instances

#Dog.printInfo() # self less method

sam = Dog()
sam.make_sound() # can access self method
sam.show_age(6) # can access self and param method

# adding setters and getters
sam.set_name("Alex")
print(sam.get_name())

# incrementing/decrementing attribute values 
# with methods, best programming practice

print(sam.age)
sam.happy_birthday()
print(sam.age)

# calling a class method from another method
sam.print_info_plus()
sam.happy_birthday()
sam.print_info_plus()

# using magic methods
print(sam)

# Animals: Create a class definition of an animal that has a species attribute and 
# both a setter and getter to change or access the attributes value. Create an 
# instance called “lion,” and call the setter method with an argument of “feline.” 
# Then print out the species by calling the getter method.

class Animal():
    species = ""

    def set_species(self, species):
        self.species = species

    def get_species(self):
        return self.species

lion = Animal()
lion.set_species("feline")
print(lion.get_species())

# User Input: Create a class Person that takes in a name when instantiated but 
# sets an age to 0. Within the class definition setup, a setter and getter that will 
# ask the user to input their age and set the age attribute to the value input. 
# Then output the information in a formatted string as “You are 64 years old.” 
# Assuming the user inputs 64 as their age.

class Person():

    age = 0
    def set_age(self, age):
        self.age = age
    def get_age(self):
        return self.age

age = input("Whats your age?: ")
person = Person()
person.set_age(age)
print(f"You are {person.get_age()} years old")