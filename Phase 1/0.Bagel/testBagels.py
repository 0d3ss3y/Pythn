import unittest
import 
from unittest.mock import patch

class TestBagelsGame(unittest.TestCase):

    def test_generate_random_number(self):
        """Test if the random number is within the correct range."""
        number = generate_random_number()
        self.assertGreaterEqual(number, 100)
        self.assertLessEqual(number, 999)

    def test_evaluate_guess(self):
        """Test the evaluate_guess function."""
        number = 123
        self.assertEqual(evaluate_guess('123', number), (3, 0))  # All digits correct, in correct position
        self.assertEqual(evaluate_guess('231', number), (1, 2))  # 1 digit correct in position, 2 in wrong position
        self.assertEqual(evaluate_guess('456', number), (0, 0))  # No digits correct

    @patch('builtins.input', side_effect=['123', '456', '789'])
    def test_play_game_win(self, mock_input):
        """Test playing the game and winning."""
        with patch('random.randint', return_value=123):
            result = play_game(123)
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['456', '789', '000'])
    def test_play_game_loss(self, mock_input):
        """Test playing the game and losing."""
        with patch('random.randint', return_value=123):
            result = play_game(123)
            self.assertFalse(result)

    @patch('builtins.input', side_effect=['abc', '12', '456'])
    def test_input_validation(self, mock_input):
        """Test input validation for guesses."""
        with patch('random.randint', return_value=123):
            with self.assertRaises(SystemExit):  # Expecting to exit due to invalid input
                play_game(123)

if __name__ == '__main__':
    unittest.main()