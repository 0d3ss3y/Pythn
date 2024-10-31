import unittest
from unittest.mock import patch
from io import StringIO
from bagel import *
import random

# Assume the code above is in a module named bagels_game
# from bagels_game import main, generate_random_number, play_game, clear_screen, rules

class TestBagelsGame(unittest.TestCase):

    @patch('random.randint')
    def test_generate_random_number(self, mock_randint):
        mock_randint.return_value = 123
        self.assertEqual(generate_random_number(), 123)

    @patch('builtins.input', side_effect=['123', '456', '789'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_correct_guess(self, mock_stdout, mock_input):
        # Test a successful guess
        with patch('bagels_game.generate_random_number', return_value=123):
            play_game(123)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Congratulations! You guessed the number!", output)

    @patch('builtins.input', side_effect=['234', '123'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_incorrect_guess_with_clues(self, mock_stdout, mock_input):
        # Test incorrect guess with clues
        with patch('bagels_game.generate_random_number', return_value=123):
            play_game(123)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Pico", output)  # Incorrect digit in the wrong position
            self.assertIn("Fermi", output)  # Correct digit in the right position

    @patch('builtins.input', side_effect=['999', '888', '777', '666', '555', '444', '333', '222', '111', '000'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_exceeding_guesses(self, mock_stdout, mock_input):
        # Test when all guesses are wrong
        with patch('bagels_game.generate_random_number', return_value=123):
            play_game(123)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Sorry, you lost!", output)

    @patch('builtins.input', side_effect=['y', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_continue_game(self, mock_stdout, mock_input):
        with patch('bagels_game.main') as mock_main:
            continueGame()
            self.assertIn("Would you like to play again? (y/n)", mock_stdout.getvalue())
            mock_main.assert_called_once()  # Check if main is called after 'y'

    @patch('sys.stdout', new_callable=StringIO)
    def test_rules(self, mock_stdout):
        rules()
        output = mock_stdout.getvalue().strip()
        self.assertIn("I am thinking of a 3-digit number.", output)
        self.assertIn("Pico", output)  # Check presence of clues in rules

    @patch('sys.stdout', new_callable=StringIO)
    def test_heading(self, mock_stdout):
        heading()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Bagels, a deductive logic game.")

if __name__ == '__main__':
    unittest.main()
