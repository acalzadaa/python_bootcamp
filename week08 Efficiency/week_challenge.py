# For this week’s challenge, I’d like you to create a program that asks a user to input a number 
# and tells that user if the number they entered is a prime number or not. 
# Remember that prime numbers are only divisible by one and itself and must be above the number 2. 
# Create a function called “isPrime” that you pass the input into, and return a True or False value. Be 
# sure to keep efficiency in mind when programming the function

from week08.primenumber import PrimeNumber

def main():

    ans = input("Tell me a number: ")
    prime_number = PrimeNumber(int(ans))
    
    if prime_number.is_prime():
        print("is a prime!")
    else:
        print("is not a prime!")

main()