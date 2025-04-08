import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverterExtra(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(50), "L")
        self.assertEqual(decimal_to_roman(100), "C")
        self.assertEqual(decimal_to_roman(500), "D")
        self.assertEqual(decimal_to_roman(1000), "M")

    def test_various_values(self):
        self.assertEqual(decimal_to_roman(27), "XXVII")
        self.assertEqual(decimal_to_roman(73), "LXXIII")
        self.assertEqual(decimal_to_roman(148), "CXLVIII")
        self.assertEqual(decimal_to_roman(276), "CCLXXVI")
        self.assertEqual(decimal_to_roman(388), "CCCLXXXVIII")

    def test_years(self):
        self.assertEqual(decimal_to_roman(1492), "MCDXCII") 
        self.assertEqual(decimal_to_roman(1776), "MDCCLXXVI") 
        self.assertEqual(decimal_to_roman(1810), "MDCCCX")    
        self.assertEqual(decimal_to_roman(1989), "MCMLXXXIX") 
        self.assertEqual(decimal_to_roman(2024), "MMXXIV") 

    def test_low_values(self):
        self.assertEqual(decimal_to_roman(2), "II")
        self.assertEqual(decimal_to_roman(3), "III")
        self.assertEqual(decimal_to_roman(6), "VI")
        self.assertEqual(decimal_to_roman(7), "VII")
        self.assertEqual(decimal_to_roman(8), "VIII")

if __name__ == '__main__':
    unittest.main()

