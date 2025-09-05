"""
Dictionary Manager Module

This module manages word and phrase dictionaries for the Hangman game,
providing random selection functionality for different difficulty levels.
"""

import random


class DictionaryManager:
    """Manages word and phrase dictionaries for the game"""

    def __init__(self):
        # Basic level words
        self.words = [
            "PYTHON", "COMPUTER", "PROGRAMMING", "ALGORITHM", "FUNCTION",
            "VARIABLE", "LOOP", "CONDITION", "ARRAY", "STRING", "INTEGER",
            "BOOLEAN", "CLASS", "OBJECT", "METHOD", "LIBRARY", "FRAMEWORK",
            "DATABASE", "NETWORK", "SECURITY", "ENCRYPTION", "DEBUGGING",
            "TESTING", "DEVELOPMENT", "SOFTWARE", "HARDWARE", "INTERNET",
            "WEBSITE", "APPLICATION", "INTERFACE", "SYSTEM", "PROTOCOL",
            "SERVER", "CLIENT", "BROWSER", "OPERATING", "MEMORY", "PROCESSOR",
            "KEYBOARD", "MONITOR", "MOUSE", "PRINTER", "SCANNER", "ROUTER",
            "WIRELESS", "BLUETOOTH", "ETHERNET", "FIREWALL", "ANTIVIRUS"
        ]

        # Intermediate level phrases
        self.phrases = [
            "HELLO WORLD", "MACHINE LEARNING", "ARTIFICIAL INTELLIGENCE",
            "DATA STRUCTURE", "SOFTWARE ENGINEERING", "WEB DEVELOPMENT",
            "MOBILE APPLICATION", "CLOUD COMPUTING", "CYBER SECURITY",
            "GAME DEVELOPMENT", "USER INTERFACE", "DATABASE MANAGEMENT",
            "NETWORK ADMINISTRATION", "SYSTEM ANALYSIS", "PROJECT MANAGEMENT",
            "QUALITY ASSURANCE", "VERSION CONTROL", "AGILE METHODOLOGY",
            "OBJECT ORIENTED PROGRAMMING", "FUNCTIONAL PROGRAMMING",
            "RESPONSIVE WEB DESIGN", "FULL STACK DEVELOPMENT",
            "FRONT END DEVELOPMENT", "BACK END DEVELOPMENT",
            "DISTRIBUTED SYSTEMS", "MICROSERVICES ARCHITECTURE",
            "CONTINUOUS INTEGRATION", "CONTINUOUS DEPLOYMENT",
            "AUTOMATED TESTING", "CODE REVIEW PROCESS",
            "TECHNICAL DOCUMENTATION", "SOFTWARE ARCHITECTURE",
            "DESIGN PATTERNS", "ALGORITHM OPTIMIZATION",
            "DATA VISUALIZATION", "BUSINESS INTELLIGENCE"
        ]

    def get_random_word(self, level):
        """
        Get a random word or phrase based on level
        Args:
            level: "basic" for words, "intermediate" for phrases
        Returns:
            Random word or phrase as uppercase string
        """
        if level == "basic":
            return random.choice(self.words)
        if level == "intermediate":
            return random.choice(self.phrases)
        raise ValueError(f"Invalid level: {level}."
                         f"Use 'basic' or 'intermediate'")

    def add_word(self, word, level="basic"):
        """Add a custom word to the dictionary"""
        word = word.upper()
        if level == "basic":
            if word not in self.words:
                self.words.append(word)
        elif level == "intermediate":
            if word not in self.phrases:
                self.phrases.append(word)

    def get_word_count(self, level):
        """Get count of words in specified level"""
        if level == "basic":
            return len(self.words)
        if level == "intermediate":
            return len(self.phrases)
        return 0
