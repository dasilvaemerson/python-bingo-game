import unittest
from card import Card

class TestGenerateCard(unittest.TestCase):

    # Test if the Bingo Card is returned (True)
    def test_card(self):
        self.assertTrue(Card.generate_card())


if __name__ == "__main__":
    unittest.main()

