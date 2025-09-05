# Hangman Game - Test-Driven Development Implementation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Code Quality](https://img.shields.io/badge/Pylint-10.00%2F10-brightgreen.svg)](https://pylint.org)
[![Tests](https://img.shields.io/badge/Tests-19%20Passed-brightgreen.svg)](https://docs.python.org/3/library/unittest.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A console-based Hangman game implemented using Test-Driven Development (TDD) methodology with comprehensive unit testing, timer functionality, and perfect code quality standards.

## 🎮 Features

- **Two Difficulty Levels**: Basic (single words) and Intermediate (phrases)
- **Timer System**: 15-second countdown per guess with visual feedback
- **Life System**: 6 lives with emoji indicators
- **Comprehensive Dictionary**: 50+ words and 35+ phrases
- **Input Validation**: Robust error handling and user input validation
- **Clean UI**: Console-based interface with clear game state display
- **Perfect Code Quality**: 100% Pylint score (10.00/10) and zero Flake8 warnings

## 📁 Project Structure

The game follows a modular, object-oriented design with clear separation of concerns:

```
hangman-game/
├── main.py              # Game controller and entry point
├── hangman_game.py      # Core game logic
├── dictionary.py        # Word/phrase management
├── timer.py            # Timer functionality
├── game_interface.py   # User interface handling
├── test_hangman.py     # Comprehensive unit tests
├── requirements.txt    # Project dependencies
├── todo.md            # Implementation plan
└── README.md          # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/digitalaashish/hangman/
cd hangman-game
```

2. Install dependencies (if any):
```bash
pip install -r requirements.txt
```
*Note: This project primarily uses Python's built-in libraries, so requirements.txt may be minimal or empty.*

3. Run the game:
```bash
python main.py
```

### Running Tests

Execute the comprehensive test suite:
```bash
python -m unittest test_hangman.py -v
```

### Code Quality Check

Verify code quality standards:
```bash
# Check with Flake8
flake8 *.py --max-line-length=79

# Check with Pylint
pylint *.py --max-line-length=79
```

## 🎯 How to Play

1. **Start the Game**: Run `python main.py`
2. **Select Difficulty**: Choose between Basic (words) or Intermediate (phrases)
3. **Make Guesses**: Enter letters within the 15-second time limit
4. **Win Condition**: Guess all letters before running out of lives
5. **Lose Condition**: Exhaust all 6 lives through wrong guesses or timeouts

### Game Rules

- ❤️ **6 Lives**: Start with 6 lives, lose one for each wrong guess or timeout
- ⏰ **15-Second Timer**: Each guess must be made within 15 seconds
- 🔤 **Letter Input**: Only single alphabetic characters are accepted
- 🎯 **Two Levels**: Basic (single words) and Intermediate (phrases with spaces)

## 🧪 Test-Driven Development

This project was built using TDD methodology with comprehensive test coverage:

### Test Statistics
- **19 Unit Tests** covering all major functionality
- **4 Test Classes** for different components
- **100% Pass Rate** with robust error handling
- **Edge Case Coverage** including timeouts, invalid inputs, and boundary conditions

### Test Categories
1. **HangmanGame Tests**: Core game logic, win/lose conditions, state management
2. **DictionaryManager Tests**: Word selection, level validation, custom word addition
3. **GameTimer Tests**: Timer functionality, timeout handling, thread safety
4. **GameInterface Tests**: User input validation, display methods, interaction flow

## 📊 Code Quality Metrics

- **Pylint Score**: 10.00/10 (Perfect)
- **Flake8 Warnings**: 0 (Zero warnings)
- **Code Coverage**: Comprehensive unit test coverage
- **Documentation**: 100% docstring coverage for all classes and methods
- **PEP 8 Compliance**: Full adherence to Python style guidelines

## 🏆 Technical Highlights

### Design Patterns
- **MVC Architecture**: Clear separation of Model (game logic), View (interface), Controller (main)
- **Observer Pattern**: Timer callbacks for timeout handling
- **Strategy Pattern**: Different difficulty levels with varying word sources

### Advanced Features
- **Multi-threading**: Non-blocking timer implementation with thread-safe operations
- **Error Handling**: Comprehensive exception handling with graceful degradation
- **Input Validation**: Robust user input sanitization and validation
- **State Management**: Clean game state tracking and reset functionality

### Code Quality Features
- **Modular Design**: Each component has a single responsibility
- **Comprehensive Documentation**: Detailed docstrings for all public methods
- **Type Hints**: Clear parameter and return type documentation
- **Error Messages**: User-friendly error messages and guidance

## 📚 Dependencies

- **Python 3.8+**: Core language requirement
- **unittest**: Built-in testing framework (no external dependencies)
- **threading**: Built-in module for timer functionality
- **random**: Built-in module for word selection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the established code quality standards
4. Run tests and ensure they pass (`python -m unittest test_hangman.py`)
5. Check code quality (`flake8 *.py && pylint *.py`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/digitalaashish/hangman/blob/main/LICENSE) file for details.

## 🔗 Links

- **Repository**: [https://github.com/digitalaashish/hangman](https://github.com/digitalaashish/hangman)
- **Issues**: [https://github.com/digitalaashish/hangman/issues](https://github.com/digitalaashish/hangman/issues)
- **License**: [MIT License](https://github.com/digitalaashish/hangman/blob/main/LICENSE)

## 🙏 Acknowledgments

- Built using Test-Driven Development methodology
- Follows Python PEP 8 style guidelines
- Implements clean code principles
- Uses comprehensive unit testing with Python's unittest framework

---

**Enjoy playing Hangman! 🎮**
