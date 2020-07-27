# Prime numbers are only divisible by one and itself and must be above the number 2
class PrimeNumber():
    def __init__(self, number):
        self.number = number

    def is_prime(self):

        #is more than 2?
        if self.number <= 2:
            return False

        for num in range(2, self.number):
            if self.number % num == 0:
                print(f"found a divisor! {num}:{self.number}")
                return False

        return True