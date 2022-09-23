import unittest
from unittest.mock import patch
from game import Game
import threading

class Test(unittest.TestCase):
    # Test if number is drawed when the user presses a key.

    # Test if number is inside the numbers list
    def test_number_in_range(self):
        a = 4
        b = Game.numbers_list
        self.assertIn(a, b)

    # Test if number is outside of the numbers range (1 - 75)
    def test_number_not_in_range(self):
        a = 76
        b = Game.numbers_list
        self.assertNotIn(a, b)
    
    # Test if numbers list range is a string
    def test_number_not_string(self):
        a = '1'
        b = Game.numbers_list[0]
        self.assertIsNot(a, b)
    
    # Test if numbers list range is a string
    def test_number_is_int(self):
        a = 1
        b = Game.numbers_list[0]
        self.assertIs(a, b)

    # Test if game Function is called if input is equal to "B"
    @patch('builtins.input')
    def test_bingo_call(self, input_mock):
        input_mock.side_effect=['B','S']
        with patch.object(Game, "bingo_call") as mock:
            game_thread = threading.Thread(target=self._game_thread)
            game_thread.start()
            mock.assert_called_once()

    # Test if game is closed when the input is equal to "S"
    @patch('builtins.input')
    def test_exit(self, input_mock):
        input_mock.side_effect=['S']
        with patch.object(Game, "bingo_call") as mock:
            game_thread = threading.Thread(target=self._game_thread)
            game_thread.start()
            mock.assert_not_called()
            
    # Creates thread as workaround the While(True) loop
    def _game_thread(self):
        Game.start()

if __name__ == "__main__":
    unittest.main()
