#!/usr/bin/env python3
"""
Hangman Game - Main Entry Point

A console based Hangman game with timer functionality and TDD implementation.
This module contains the main game controller and entry point.
"""

import threading
import time
from hangman_game import HangmanGame
from dictionary import DictionaryManager
from timer import GameTimer
from game_interface import GameInterface


class HangmanGameController:
    """Main game controller that organizes all components"""

    def __init__(self):
        self.game = HangmanGame()
        self.dictionary = DictionaryManager()
        self.interface = GameInterface()
        self.timer = GameTimer(timeout_seconds=15)
        self.input_received = threading.Event()
        self.current_input = None

    def run(self):
        """Main game loop"""
        self.interface.display_welcome()

        while True:
            # Get level selection
            level = self.interface.get_level_selection()

            if level == "quit":
                break

            # Start new game
            self.start_new_game(level)

            # Play the game
            self.play_game()

            # Check if player wants to play again
            if not self.interface.ask_play_again():
                break

        self.interface.display_goodbye()

    def start_new_game(self, level):
        """Initialize a new game with selected level"""
        # Reset game state
        self.game.reset_game()

        # Get random word/phrase
        word = self.dictionary.get_random_word(level)
        self.game.set_word(word, level)

        print(f"\nStarting new {level} level game!")
        letter_count = len([c for c in word if c.isalpha()])
        print(f"Your word/phrase has {letter_count} letters.")

    def play_game(self):
        """Main game play loop"""
        while not self.game.game_over:
            # Display current game state
            game_state = self.game.get_game_state()
            self.interface.display_game_state(game_state)

            # Get letter guess with timer
            letter = self.get_timed_input()

            if letter is None:
                # Timeout occurred
                self.interface.display_timeout_message()
                self.game.handle_timeout()
            else:
                # Process the guess
                result = self.game.guess_letter(letter)
                self.interface.display_guess_result(result, letter)

            # Small delay for better user experience
            time.sleep(1)

        # Display final game state
        final_state = self.game.get_game_state()
        self.interface.display_game_over(final_state)

    def get_timed_input(self):
        """Get user input with 15-second timer"""
        self.input_received.clear()
        self.current_input = None

        # Set up timer callbacks
        def on_timeout():
            self.input_received.set()

        self.timer.set_timeout_callback(on_timeout)

        # Start input thread
        input_thread = threading.Thread(target=self._get_input_thread)
        input_thread.daemon = True
        input_thread.start()

        # Start timer
        self.timer.reset()
        self.timer.start()

        # Display timer countdown
        start_time = time.time()
        while not self.input_received.is_set():
            elapsed = time.time() - start_time
            remaining = max(0, 15 - elapsed)

            if remaining > 0:
                print(
                    f"\rTime remaining: {remaining:.1f}s - "
                    f"Enter a letter: ",
                    end="",
                    flush=True,
                )
                time.sleep(0.1)
            else:
                break

        # Stop timer
        self.timer.stop()

        # Wait for input thread to complete
        input_thread.join(timeout=0.5)

        print()  # New line after timer display

        return self.current_input

    def _get_input_thread(self):
        """Input thread function"""
        try:
            letter = input().strip().upper()

            # Validate input
            if len(letter) == 1 and letter.isalpha():
                self.current_input = letter
            else:
                print("Invalid input! Please enter a single letter.")
                self.current_input = None

        except (EOFError, KeyboardInterrupt):
            self.current_input = None

        finally:
            self.input_received.set()


def main():
    """Entry point of the application"""
    try:
        controller = HangmanGameController()
        controller.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
    except (ValueError, RuntimeError) as exc:
        print(f"\nA game error occurred: {exc}")
        print("Please restart the game.")


if __name__ == "__main__":
    main()
