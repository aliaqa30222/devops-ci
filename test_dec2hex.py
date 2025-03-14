import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(decimal_to_hex(15), 'F')
        self.assertEqual(decimal_to_hex(255), 'FF')

    def test_zero(self):
        self.assertEqual(decimal_to_hex(0), '0')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex("abc")

    def test_no_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(None)

if __name__ == '__main__':
    unittest.main()

