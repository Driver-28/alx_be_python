import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setup(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.addition(3,5),8)
        self.assertEqual(self.calc.addition(5,10),-5)
        self.assertEqual(self.calc.addition(0,0),0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,5),5)
        self.assertEqual(self.calc.subtract(5,10),-5)
        self.assertEqual(self.calc.subtract(0,0),0)
    def  test_multiplication(self):
        self.assertEqual(self.calc.multiply(4,5),20)
        self.assertEqual(self.calc.multiply(0,10),0)
        self.assertEqual(self.calc.multiply(-3,5),-15)
    def test_division(self):
        self.assertEqual(self.calc.divide(10,2),5.0)
        self.assertEqual(self.calc.divide(9,3),3.0)
        self.assertEqual(self.calc.divide(5,0))
if __name__ == "__main__":
    unittest.main()
