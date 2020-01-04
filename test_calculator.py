import calculator
import unittest

class Test_TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.add(4,3), 7)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5,3), 2)

    def test_multiplication(self):
        self.assertEqual(calculator.multiple(5,5), 25)

    def test_multiplicationEdge(self):
        self.assertEqual(calculator.multiple(0,0), 0)

    def test_division(self):
        self.assertEqual(calculator.divide(10,5), 2)

    def test_square(self):
        self.assertEqual(calculator.square(4), 16)
    
if __name__ == '__main__':
    unittest.main()