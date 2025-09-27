#!/usr/bin/env python3
"""
Simple test suite for GuessRandomNumber
Tests basic functionality of number guessing algorithms
"""

import unittest
from unittest.mock import patch
import GuessRandomNumber


class TestGuessRandomNumber(unittest.TestCase):
    """Test cases for GuessRandomNumber functionality."""

    def test_guess_random_number_invalid_params(self):
        """Test invalid parameters handling."""
        result = GuessRandomNumber.guess_random_number(0, 1, 10)
        self.assertFalse(result)

        result = GuessRandomNumber.guess_random_number(5, 10, 1)
        self.assertFalse(result)

    def test_binary_search_invalid_params(self):
        """Test binary search with invalid parameters."""
        result = GuessRandomNumber.guess_random_number_binary_search(0, 1, 10)
        self.assertFalse(result)

        result = GuessRandomNumber.guess_random_number_binary_search(5, 10, 1)
        self.assertFalse(result)

    def test_binary_search_success(self):
        """Test successful binary search."""
        result = GuessRandomNumber.guess_random_number_binary_search(10, 1, 100, target_number=50)
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['5'])
    def test_guess_random_number_correct_guess(self, mock_input):
        """Test correct guess scenario."""
        with patch('GuessRandomNumber.random.randint', return_value=5):
            result = GuessRandomNumber.guess_random_number(3, 1, 10)
            self.assertTrue(result)

    def test_main_function_exists(self):
        """Test that main function exists and is callable."""
        self.assertTrue(callable(GuessRandomNumber.main))


if __name__ == '__main__':
    unittest.main()