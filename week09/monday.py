# Monday: Generators and Iterators

# Generators and Iterators

print("\nIterator\n")

# creating a basic iterator from an iterable
sports = ["baseball", "soccer", "football", "hockey", "basketball"]
my_iter = iter(sports)
print(next(my_iter))
print(next(my_iter))

# va a seguir donde se quedo!!!

for item in my_iter:
    print(item)

# creating our own iterator

print("\nCustom Iterator\n")

class Alphabet:
    def __iter__(self):
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.index = 0
        return self

    def __next__(self):
        if self.index <= 25:
            char = self.letters[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration


for char in Alphabet():
    print(char)

# generators

# creating our own range generator with start, stop, and step parameters
print("\nRange Generator\n")


def my_range(stop, start=0, step=1):
    while start < stop:
        print(f"Generator Start Value: {start}")
        yield start
        start += step

for x in my_range(5):
    print(f"For Loop X Value: {x}")

# Power of Two: Create an iterator that takes in a integer, and when iterated over,
# it returns the power of two of each element.
#
# >>> for i in powtwo( [ 1,2,3,4 ] ):
print("\nExercise 1: power of two\n")

class PowTwo:
    def __init__(self, max = 0):
      self.max = max

    def __iter__(self):
      self.index = 0
      return self

    def __next__(self):
        if self.index <= self.max:
            result = 2 ** self.index
            self.index += 1
            return result
        else:
            raise StopIteration

numbers = PowTwo(2)
for i in numbers:
    print(i)

for i in  PowTwo(2):
    print(i)

# Squares: Create a generator that acts like the range function, except it
# yields a squared number every time. The result of the following call should
# be “0, 1, 4, 16”.
#
# >>> for i in range(4):
print("\nExercise 2: generator\n")
def my_range2(stop, start=0, step=1):
    
    while start < stop:
        print(f"Generator Start Value: {start}")
        yield start*start
        start += step

for x in my_range2(4):
    print(f"For Loop X Value: {x}")