import unittest
from week08.primenumber import PrimeNumber

class TestPrimeNumbers(unittest.TestCase):
    
    def test_prime_number(self):

        # if below 2 should return false
        self.assertEqual(PrimeNumber(0).is_prime(),False)
        self.assertEqual(PrimeNumber(1).is_prime(),False)
        self.assertEqual(PrimeNumber(2).is_prime(),False)

        # test examples
        self.assertEqual(PrimeNumber(3).is_prime(),True)
        self.assertEqual(PrimeNumber(4).is_prime(),False)
        self.assertEqual(PrimeNumber(5).is_prime(),True)
        self.assertEqual(PrimeNumber(6).is_prime(),False)
        self.assertEqual(PrimeNumber(7).is_prime(),True)
        self.assertEqual(PrimeNumber(8).is_prime(),False)
        self.assertEqual(PrimeNumber(9).is_prime(),False)
        self.assertEqual(PrimeNumber(10).is_prime(),False)
        self.assertEqual(PrimeNumber(11).is_prime(),True)
        self.assertEqual(PrimeNumber(12).is_prime(),False)
