# Hangman Game - TDD Implementation Plan

## MVP Features to Implement:
1. **Game Core Logic** (`hangman_game.py`)
   - Word/phrase selection from dictionary
   - Game state management (lives, guessed letters, current state)
   - Letter guessing logic
   - Win/lose conditions

2. **Dictionary Manager** (`dictionary.py`)
   - Load words and phrases from predefined lists
   - Random selection for basic (words) and intermediate (phrases) levels

3. **Timer System** (`timer.py`)
   - 15-second countdown timer
   - Timer display and timeout handling

4. **Game Interface** (`game_interface.py`)
   - Console-based user interface
   - Display game state, timer, and user prompts
   - Input handling

5. **Main Game Loop** (`main.py`)
   - Game initialization and main loop
   - Level selection and game flow control

6. **Test Suite** (`test_hangman.py`)
   - Unit tests for all components using TDD approach
   - Test game logic, timer, dictionary, and interface

## File Structure:
- `main.py` - Entry point and main game loop
- `hangman_game.py` - Core game logic
- `dictionary.py` - Word/phrase management
- `timer.py` - Timer functionality
- `game_interface.py` - User interface
- `test_hangman.py` - Comprehensive test suite
- `requirements.txt` - Dependencies

## Implementation Priority:
1. Start with tests for core game logic
2. Implement basic word guessing mechanics
3. Add timer functionality
4. Create user interface
5. Integrate all components in main loop