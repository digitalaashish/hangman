"""
Test Module for Hangman Game

This module contains comprehensive unit tests for all components
of the Hangman game using Test-Driven Development principles.
"""

import unittest
from unittest.mock import patch
import threading
from hangman_game import HangmanGame
from dictionary import DictionaryManager
from timer import GameTimer
from game_interface import GameInterface


class TestHangmanGame(unittest.TestCase):
    """Test cases for HangmanGame class"""

    def setUp(self):
        self.game = HangmanGame()

    def test_game_initialization(self):
        """Test game initializes with correct default values"""
        self.assertEqual(self.game.lives, 6)
        self.assertEqual(self.game.guessed_letters, set())
        self.assertFalse(self.game.game_over)
        self.assertFalse(self.game.won)

    def test_set_word_basic_level(self):
        """Test setting word for basic level"""
        self.game.set_word("PYTHON", "basic")
        self.assertEqual(self.game.answer, "PYTHON")
        self.assertEqual(self.game.level, "basic")
        self.assertEqual(self.game.display_word, "______")

    def test_set_phrase_intermediate_level(self):
        """Test setting phrase for intermediate level"""
        self.game.set_word("HELLO WORLD", "intermediate")
        self.assertEqual(self.game.answer, "HELLO WORLD")
        self.assertEqual(self.game.level, "intermediate")
        self.assertEqual(self.game.display_word, "_____ _____")

    def test_correct_guess(self):
        """Test correct letter guess"""
        self.game.set_word("PYTHON", "basic")
        result = self.game.guess_letter("P")
        self.assertTrue(result)
        self.assertIn("P", self.game.guessed_letters)
        self.assertEqual(self.game.display_word, "P_____")
        self.assertEqual(self.game.lives, 6)  # Lives should not decrease

    def test_incorrect_guess(self):
        """Test incorrect letter guess"""
        self.game.set_word("PYTHON", "basic")
        result = self.game.guess_letter("Z")
        self.assertFalse(result)
        self.assertIn("Z", self.game.guessed_letters)
        self.assertEqual(self.game.display_word, "______")
        self.assertEqual(self.game.lives, 5)  # Lives should decrease

    def test_duplicate_guess(self):
        """Test guessing same letter twice"""
        self.game.set_word("PYTHON", "basic")
        self.game.guess_letter("P")
        result = self.game.guess_letter("P")
        self.assertIsNone(result)  # Should return None for duplicate
        self.assertEqual(self.game.lives, 6)  # Lives should not decrease

    def test_win_condition(self):
        """Test winning the game"""
        self.game.set_word("CAT", "basic")
        self.game.guess_letter("C")
        self.game.guess_letter("A")
        self.game.guess_letter("T")
        self.assertTrue(self.game.won)
        self.assertTrue(self.game.game_over)

    def test_lose_condition(self):
        """Test losing the game"""
        self.game.set_word("CAT", "basic")
        # Make 6 wrong guesses
        wrong_letters = ["X", "Y", "Z", "Q", "W", "R"]
        for letter in wrong_letters:
            self.game.guess_letter(letter)
        self.assertFalse(self.game.won)
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.lives, 0)

    def test_timeout_deducts_life(self):
        """Test that timeout deducts a life"""
        self.game.set_word("PYTHON", "basic")
        initial_lives = self.game.lives
        self.game.handle_timeout()
        self.assertEqual(self.game.lives, initial_lives - 1)


class TestDictionaryManager(unittest.TestCase):
    """Test cases for DictionaryManager class"""

    def setUp(self):
        self.dict_manager = DictionaryManager()

    def test_get_random_word(self):
        """Test getting random word for basic level"""
        word = self.dict_manager.get_random_word("basic")
        self.assertIsInstance(word, str)
        self.assertTrue(word.isupper())
        self.assertNotIn(" ", word)

    def test_get_random_phrase(self):
        """Test getting random phrase for intermediate level"""
        phrase = self.dict_manager.get_random_word("intermediate")
        self.assertIsInstance(phrase, str)
        self.assertTrue(phrase.isupper())

    def test_invalid_level(self):
        """Test invalid level raises exception"""
        with self.assertRaises(ValueError):
            self.dict_manager.get_random_word("invalid")


class TestGameTimer(unittest.TestCase):
    """Test cases for GameTimer class"""

    def setUp(self):
        self.timer = GameTimer(timeout_seconds=1)  # Short timeout for testing

    def test_timer_initialization(self):
        """Test timer initializes correctly"""
        self.assertEqual(self.timer.timeout_seconds, 1)
        self.assertFalse(self.timer.is_running)
        self.assertFalse(self.timer.timed_out)

    def test_timer_start_and_stop(self):
        """Test timer start and stop functionality"""
        self.timer.start()
        self.assertTrue(self.timer.is_running)
        self.timer.stop()
        self.assertFalse(self.timer.is_running)

    def test_timer_timeout(self):
        """Test timer timeout functionality"""
        callback_called = threading.Event()

        def timeout_callback():
            callback_called.set()

        self.timer.timeout_callback = timeout_callback
        self.timer.start()

        # Wait for timeout
        callback_called.wait(timeout=2)
        self.assertTrue(callback_called.is_set())
        self.assertTrue(self.timer.timed_out)


class TestGameInterface(unittest.TestCase):
    """Test cases for GameInterface class"""

    def setUp(self):
        self.interface = GameInterface()

    @patch('builtins.input', return_value='1')
    def test_get_level_selection_basic(self, _):
        """Test level selection for basic"""
        level = self.interface.get_level_selection()
        self.assertEqual(level, "basic")

    @patch('builtins.input', return_value='2')
    def test_get_level_selection_intermediate(self, _):
        """Test level selection for intermediate"""
        level = self.interface.get_level_selection()
        self.assertEqual(level, "intermediate")

    @patch('builtins.input', return_value='A')
    def test_get_letter_input_valid(self, _):
        """Test valid letter input"""
        letter = self.interface.get_letter_input()
        self.assertEqual(letter, 'A')

    @patch('builtins.input', side_effect=['1', 'A'])
    def test_get_letter_input_invalid_then_valid(self, _):
        """Test invalid input followed by valid input"""
        letter = self.interface.get_letter_input()
        self.assertEqual(letter, 'A')


if __name__ == '__main__':
    unittest.main()
