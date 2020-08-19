import unittest
from week09.bubblesort import bubble_sort
class TestBubbleSort(unittest.TestCase):
    
    def test_bubblesort(self):
        self.assertEqual(bubble_sort([4,3,2,1]),[1,2,3,4])
