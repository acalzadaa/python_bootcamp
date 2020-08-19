# Prime numbers are only divisible by one and itself and must be above the number 2
class PrimeNumber:
    def __init__(self, number):
        self.number = number

    def is_prime(self):

        if (self.number > 2 and len([prime for prime in range(1, self.number + 1) if self.number % prime == 0]) == 2):
            return True
        else:
            return False
