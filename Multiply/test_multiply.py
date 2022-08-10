"""
Para ejecutar el test haga el siguinete comonado en la terminal: 
    python3 test_multiply.py
"""
from multiply import multiply
import unittest
import math
class TestMultiply(unittest.TestCase):
    
    def test_multiply(self):
        self.assertEqual(10, multiply(5,2))
        self.assertEqual(-16, multiply(8, -2))
        self.assertEqual(-800, multiply(20, -40))
        self.assertEqual(518, multiply(74, 7))
        self.assertEqual(49, multiply(-7, -7))
        self.assertEqual(-630, multiply(-18, 35))
        self.assertEqual(-35, multiply(-1, 35))
        self.assertEqual(-35, multiply(1, -35))
        self.assertEqual(56, multiply(8, 7))
if __name__ == '__main__':
    unittest.main()