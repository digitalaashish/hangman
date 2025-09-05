"""
Game Interface Module

This module handles the user interface and input/output for the Hangman game,
providing console-based interaction functionality.
"""

import os
import sys
import threading
import time


class GameInterface:
    """Handles user interface and input/output for the Hangman game"""

    def __init__(self):
        self.timer_display_active = False
        self.timer_thread = None

    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_welcome(self):
        """Display welcome message and game rules"""
        self.clear_screen()
        print("=" * 50)
        print("           WELCOME TO HANGMAN GAME")
        print("=" * 50)
        print("\nGame Rules:")
        print("• Guess the hidden word/phrase letter by letter")
        print("• You have 6 lives to start with")
        print("• Each wrong guess or timeout costs you a life")
        print("• You have 15 seconds per guess")
        print("• Find the word before your lives run out!")
        print("\nLevels:")
        print("• Basic: Single words")
        print("• Intermediate: Phrases (multiple words)")
        print("=" * 50)

    def get_level_selection(self):
        """Get level selection from user"""
        while True:
            print("\nSelect difficulty level:")
            print("1. Basic (Single words)")
            print("2. Intermediate (Phrases)")
            print("3. Quit game")

            choice = input("\nEnter your choice (1-3): ").strip()

            if choice == "1":
                return "basic"
            if choice == "2":
                return "intermediate"
            if choice == "3":
                return "quit"
            print("Invalid choice! Please enter 1, 2, or 3.")

    def display_game_state(self, game_state, timer_time=None):
        """Display current game state"""
        print("\n" + "=" * 50)
        print(f"Word/Phrase: {game_state['display_word']}")
        print(f"Lives remaining: {'❤️ ' * game_state['lives']}"
              f"({game_state['lives']})")

        if game_state['guessed_letters']:
            guessed = ', '.join(game_state['guessed_letters'])
            print(f"Guessed letters: {guessed}")

        if timer_time is not None:
            print(f"Time remaining: {timer_time:.1f} seconds")

        print("=" * 50)

    def get_letter_input(self):
        """Get letter input from user with validation"""
        while True:
            try:
                letter = input("\nEnter a letter: ").strip().upper()

                if len(letter) != 1:
                    print("Please enter exactly one letter!")
                    continue

                if not letter.isalpha():
                    print("Please enter a valid letter (A-Z)!")
                    continue

                return letter

            except (EOFError, KeyboardInterrupt):
                print("\nGame interrupted by user.")
                return None

    def display_guess_result(self, result, letter):
        """Display result of a guess"""
        if result is True:
            print(f"✅ Great! '{letter}' is in the word!")
        elif result is False:
            print(f"❌ Sorry! '{letter}' is not in the word.")
        elif result is None:
            print(f"⚠️  You already guessed '{letter}'. "
                  f"Try a different letter!")

    def display_timeout_message(self):
        """Display timeout message"""
        print("\n⏰ Time's up! You lose a life.")

    def display_game_over(self, game_state):
        """Display game over message"""
        print("\n" + "=" * 50)
        if game_state['won']:
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"You successfully guessed: {game_state['answer']}")
        else:
            print("💀 GAME OVER! 💀")
            print(f"The answer was: {game_state['answer']}")
        print("=" * 50)

    def ask_play_again(self):
        """Ask if user wants to play again"""
        while True:
            prompt = "\nDo you want to play again? (y/n): "
            choice = input(prompt).strip().lower()
            if choice in ['y', 'yes']:
                return True
            if choice in ['n', 'no']:
                return False
            print("Please enter 'y' for yes or 'n' for no.")

    def display_goodbye(self):
        """Display goodbye message"""
        print("\n" + "=" * 50)
        print("Thanks for playing Hangman!")
        print("Goodbye! 👋")
        print("=" * 50)

    def start_timer_display(self, timer):
        """Start displaying timer in a separate thread"""
        self.timer_display_active = True

        def update_timer_display():
            while self.timer_display_active and timer.is_running:
                # Move cursor up and clear line to update timer
                if hasattr(sys.stdout, 'write'):
                    sys.stdout.write(
                        f"\rTime remaining: {timer.get_formatted_time()}"
                    )
                    sys.stdout.flush()
                time.sleep(0.1)

        self.timer_thread = threading.Thread(target=update_timer_display)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def stop_timer_display(self):
        """Stop timer display"""
        self.timer_display_active = False
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join(timeout=0.5)
        print()  # New line after timer display

    def get_input_with_timeout(self, prompt, timeout_seconds=15):
        """
        Get input from user with timeout
        Returns tuple: (input_string, timed_out)
        """
        result = [None, False]  # [input, timed_out]

        def get_input():
            try:
                result[0] = input(prompt).strip().upper()
            except (EOFError, KeyboardInterrupt):
                result[0] = None

        input_thread = threading.Thread(target=get_input)
        input_thread.daemon = True
        input_thread.start()

        # Wait for input or timeout
        input_thread.join(timeout=timeout_seconds)

        if input_thread.is_alive():
            # Timeout occurred
            result[1] = True
            print("\n⏰ Time's up!")
            return None, True

        return result[0], False
