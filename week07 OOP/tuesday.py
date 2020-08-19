class Car():
    sound = "Beep"
    color = "Red"

ford = Car()
print(ford.sound)

ford.sound = 'Boing'
print(ford.sound)

class OtherCar():
    def __init__(self, color):
        self.color = color

chevy = OtherCar("blue")
print(chevy.color)

class AnotherCar():
    def __init__(self, color, year):
        self.color = color
        self.year = year

kia = AnotherCar("red", "2020")
print(kia.color)
print(kia.year)

class Vehicle():
    sound = "boing"
    def __init__(self, color, year):
        self.color = color
        self.year = year
        
print(Vehicle.sound)
v = Vehicle("yellow", 1999)
print(v.color)
print(v.year)
print(v.sound)


# Dogs: Create a Dog class that has one global attribute and two instance level 
# attributes. The global attribute should be “species” with a value of “Canine.” 
# The two instance attributes should be “name” and “breed.” 
# Then instantiate two dog objects, a Husky named Sammi and a Chocolate Lab named Casey.

class Dog: 
    species = "Canine"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Sammi", "Husky")
dog2 = Dog("Casey", "Chocolate Lab")


# User Input: Create a Person class that has a single instance level attribute of 
# “name.” Ask the user to input their name, and create an instance of the Person 
# class with the name they typed in. Then print out their name.

class Person:
    def __init__(self, name):
        self.name = name
        
ans = input("Whats your name?: ")
who = Person(ans)
print(f"Hello {who.name}")