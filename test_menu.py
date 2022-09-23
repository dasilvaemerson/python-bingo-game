import unittest
from unittest.mock import patch
from menu import Menu
import sys

class Test(unittest.TestCase):
    # @patch('builtins.input', lambda *args: '1')
    # def test_start(self):
    #     self.assertEqual(Menu.start(), True)

# ------ Tests for option 1 -------
    # Test if game Starts if input is equal to "1"
    @patch('game.Game.start')
    @patch('builtins.input', lambda *args: '1')
    def test_game_called(self, mock):
        Menu.start()
        self.assertTrue(mock.called)

# ------ Tests for option 2 -------
    # Test if Bingo Card is generated if input is equal to "2"
    @patch('menu.Menu.new_card')
    @patch('builtins.input', lambda *args: '2')
    def test_card_called(self, mock):
        Menu.start()
        self.assertTrue(mock.called)

# ------ Tests for option 3 -------
    # Test if game is closed if input is equal to "3"
    @patch('builtins.input', lambda *args: '3')
    def test_sys_exit(self):
        with self.assertRaises(SystemExit) as cm:
            Menu.start()
        self.assertEqual(cm.exception.code, 0)

# ------ Tests for invalid Input -------
    # Test if menu restarts if the input is invalid
    @patch('menu.Menu.start')
    @patch('builtins.input', lambda *args: 'g')
    def test_game_invalid(self, mock):
        Menu.start()
        self.assertTrue(mock.called)

# ------ Tests for Generate Bingo Card -------
    # Test if the changes to Main Menu if input is equal to 'N'
    @patch('menu.Menu.start')
    @patch('builtins.input', lambda *args: 'N')
    def test_new_card_deny(self, mock):
        Menu.new_card()
        self.assertTrue(mock.called)


if __name__ == "__main__":
    unittest.main()
