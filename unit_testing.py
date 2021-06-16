import unittest
from program import *

class TestCurrency(unittest.TestCase):
    def test_currency_atributes(self):
        self.assertEqual(type(var1.curr_unit), str)
        self.assertIn(type(var1.curr_value), [int, float])
        self.assertEqual(type(var2.curr_unit), str)
        self.assertIn(type(var2.curr_value), [int, float])

if __name__ == "__main__":  
    unittest.main()