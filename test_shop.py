import unittest
from shop import greeting, purchased, retry_purchase, ThreeFailedAttempts

class TestingGreeting(unittest.TestCase):

    def test_invalid_item(self):
        try:
         greeting("Not a valid answer, please return and try again")
        except ValueError as e:
            assert str(e) == "Not a valid answer, please return and try again"

class TestingPurchased(unittest.TestCase):

    def test_purchased_with_enough_money(self):
        self.assertEqual(True, purchased(item="top", balance=100))

    def test_purchased_with_not_enough_money(self):
        self.assertFalse(purchased(item="dress", balance=100))

    def test_purchased_with_negative_money(self):
        self.assertEqual(False, purchased(item="top", balance=-100))

    def test_purchased_with_just_enough_money(self):
        self.assertTrue(purchased(item="dress", balance=150))

class TestingRetryPurchase(unittest.TestCase):

    def test_retrypurchased_too_many_attempts(self):
        with self.assertRaises(ThreeFailedAttempts):
            retry_purchase(item="dress", balance=100, attempts=3),

if __name__ == '__main__':
    unittest.main()
