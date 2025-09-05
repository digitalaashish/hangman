"""
Hangman Game Core Logic Module

This module contains the main game logic for the Hangman game,
including word management, guess processing, and game state tracking.
"""


class HangmanGame:
    """Core Hangman game logic"""

    def __init__(self):
        self.lives = 6
        self.guessed_letters = set()
        self.answer = ""
        self.display_word = ""
        self.level = ""
        self.game_over = False
        self.won = False

    def set_word(self, word, level):
        """Set the word/phrase to guess and initialize display"""
        self.answer = word.upper()
        self.level = level
        self.display_word = self._create_display_word()
        self.game_over = False
        self.won = False

    def _create_display_word(self):
        """Create display word with underscores for letters and spaces"""
        display = ""
        for char in self.answer:
            if char == " ":
                display += " "
            elif char.isalpha():
                display += "_"
            else:
                display += char  # For punctuation
        return display

    def guess_letter(self, letter):
        """
        Process a letter guess
        Returns: True if correct, False if incorrect, None if already guessed
        """
        letter = letter.upper()

        # Check if already guessed
        if letter in self.guessed_letters:
            return None

        self.guessed_letters.add(letter)

        # Check if letter is in answer
        if letter in self.answer:
            self._update_display_word(letter)
            self._check_win_condition()
            return True

        self.lives -= 1
        self._check_lose_condition()
        return False

    def _update_display_word(self, letter):
        """Update display word to reveal guessed letter"""
        new_display = ""
        for i, char in enumerate(self.answer):
            if char == letter:
                new_display += char
            else:
                new_display += self.display_word[i]
        self.display_word = new_display

    def _check_win_condition(self):
        """Check if player has won"""
        if "_" not in self.display_word:
            self.won = True
            self.game_over = True

    def _check_lose_condition(self):
        """Check if player has lost"""
        if self.lives <= 0:
            self.game_over = True
            self.won = False

    def handle_timeout(self):
        """Handle when timer runs out"""
        self.lives -= 1
        self._check_lose_condition()

    def get_game_state(self):
        """Get current game state as dictionary"""
        return {
            'display_word': self.display_word,
            'lives': self.lives,
            'guessed_letters': sorted(list(self.guessed_letters)),
            'game_over': self.game_over,
            'won': self.won,
            'answer': self.answer if self.game_over else None
        }

    def reset_game(self):
        """Reset game for new round"""
        self.lives = 6
        self.guessed_letters = set()
        self.answer = ""
        self.display_word = ""
        self.level = ""
        self.game_over = False
        self.won = False
