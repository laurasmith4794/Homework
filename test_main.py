import unittest

from main import find_most_common_letters


class TestFindMostCommonLetters(unittest.TestCase):
    def test_valid_sentence(self):
        sentence = "This is a test sentence"
        result = find_most_common_letters(sentence)
        self.assertCountEqual(result, ['t', 's', 'e'])

    def test_invalid_sentence(self):
        sentence = " "
        with self.assertRaises(Exception) as context:
            find_most_common_letters(sentence)
        self.assertEqual(str(context.exception), "Not enough characters")

    def test_edge_case(self):
        sentence = "aaaabbbbccccdddd"
        result = find_most_common_letters(sentence)
        self.assertEqual(result, ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()