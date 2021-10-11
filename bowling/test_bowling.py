import unittest
from bowling import *

class BowlingTests(unittest.TestCase):
    def test_example(self):
       self.assertEqual(bowling('8/9-X_X_6/4/X_8-X_XXX'), 194) 


if __name__ == '__main__':
    unittest.main()
