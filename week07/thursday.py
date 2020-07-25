# inheriting a class and accessing the inherited method

class Animal():
    def __init__(self, species):
        self.species = species
        
    def makeSound(self):
        print("Roar")

class Dog(Animal):
    def __init__(self, species, name):
        self.name = name
        super().__init__(species)

    def makeSound(self):
        print("Bark")

sam = Dog("Canine", "Sammi")
lion = Animal("Feline")
sam.makeSound()
print(sam.species)

sam.makeSound()
lion.makeSound()


class Physics():
    gravity = 9.8

class Automobile():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Ford(Physics, Automobile):
    def __init__(self, model, year):
        Automobile.__init__(self, "Ford", model, year)

truck = Ford("F-150", 2018)
print(truck.gravity, truck.make, truck.model, truck.year)

# Good Guys/Bad Guys: Create three classes, a superclass called “Characters” 
# that will be defined with the following attributes and methods: 
# a. Attributes: name, team, height, weight 
# b. Methods: sayHello

class Characters():
    def __init__(self, name, team, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.team = team

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm with {self.team} ")

class GoodGuys(Characters):
    def __init__(self, name, height, weight):
        Characters.__init__(self, name, "The Good Guys", height, weight)

class BadGuys(Characters):
    def __init__(self, name, height, weight):
        Characters.__init__(self, name, "The Bad Guys", height, weight)

goodguy = GoodGuys("Max", 1.8, 60)
goodguy.say_hello()

badguy = BadGuys("Sin-bad", 1.8, 60)
badguy.say_hello()
