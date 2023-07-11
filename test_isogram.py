import unittest
from isogram import isogram

class TestIsogram(unittest.TestCase):

    def test_no_letter_repeated(self):
        self.assertEqual(isogram("isogram"), ("isogram", True))

    def test_one_letter_repeated(self):
        self.assertEqual(isogram("elephant"), ("elephant", False))

    def test_input_type(self):
        with self.assertRaises(TypeError):
            isogram(123)

    def test_edge_case(self):
        self.assertEqual(isogram("abcdefghijklmnopqrstuvwxyz"), ("abcdefghijklmnopqrstuvwxyz", True))


if __name__ == '__main__':
    unittest.main()
