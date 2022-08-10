"""
Para ejecutar el test haga el siguinete comonado en la terminal: 
    python3 testest_perfect_number.py
"""
from perfect_number import its_perfect_number
import unittest

class TestPerfectNumber(unittest.TestCase):
    
    def test_perfect_number(self):
        num_perfect = "It is a Perfect Number"
        num_not_perfect = "It is not a Perfect Number"
        self.assertEquals(its_perfect_number(3), num_not_perfect)
        self.assertEquals(its_perfect_number(6), num_perfect)
        self.assertEquals(its_perfect_number(5), num_not_perfect)
        self.assertEquals(its_perfect_number(28), num_perfect)
        self.assertEquals(its_perfect_number(496), num_perfect)
        self.assertEquals(its_perfect_number(57), num_not_perfect)
        self.assertEquals(its_perfect_number(8128), num_perfect)
if __name__ == '__main__':
    unittest.main()