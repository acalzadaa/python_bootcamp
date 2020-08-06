import unittest
from week09.insertsort import insert_sort
class TestInsertSort(unittest.TestCase):
    
    def test_insertsort(self):
        self.assertEqual(insert_sort([4,3,2,1]),[1,2,3,4])
