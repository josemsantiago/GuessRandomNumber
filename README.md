# Random Number Guessing Game

A comprehensive Python educational project demonstrating different number guessing algorithms and search techniques through interactive and automated implementations.

## Overview

This project implements three distinct approaches to number guessing scenarios, showcasing the differences between human interaction, linear search, and binary search algorithms. It serves as an excellent learning tool for understanding algorithmic efficiency and search strategies.

## Features

### Three Game Modes

1. **Interactive User Guessing (`guess_random_number`)**
   - Traditional number guessing game for human players
   - Configurable range and attempt limits
   - Intelligent feedback system ("Guess higher!" or "Guess lower!")
   - Win/lose conditions with attempt tracking

2. **Linear Search Demonstration (`guess_random_number_linear_search`)**
   - Shows how a computer systematically searches using linear method
   - Displays each guess attempt for educational purposes
   - Reveals the target number for learning transparency
   - Demonstrates O(n) time complexity

3. **Binary Search Algorithm (`guess_random_number_binary_search`)**
   - Efficient divide-and-conquer approach demonstration
   - Shows logarithmic search strategy
   - Much faster than linear search for large ranges
   - Demonstrates O(log n) time complexity

## Technical Implementation

### Programming Concepts Demonstrated
- **Random Number Generation**: Using Python's `random.randint()`
- **Algorithm Comparison**: Linear vs Binary search efficiency
- **User Input Handling**: Interactive gameplay with validation
- **Control Flow**: Loops, conditionals, and function design
- **Search Algorithms**: Fundamental computer science concepts

### Code Structure
```python
import random

def guess_random_number(tries, start, stop):
    # Interactive human guessing game

def guess_random_number_linear_search(tries, start, stop):
    # Computer linear search demonstration

def guess_random_number_binary_search(tries, start, stop):
    # Computer binary search demonstration
```

## Requirements

- Python 3.x
- No external dependencies (uses only Python standard library)

## Usage

1. **Run the program**:
   ```bash
   python GuessRandomNumber.py
   ```

2. **Uncomment test cases** to try different modes:
   ```python
   # Interactive user game
   guess_random_number(5, 0, 10)

   # Linear search demo
   guess_random_number_linear_search(5, 0, 10)

   # Binary search demo
   guess_random_number_binary_search(5, 0, 100)
   ```

## Educational Value

### Algorithm Learning
- **Linear Search**: Step-by-step systematic approach
- **Binary Search**: Efficient divide-and-conquer strategy
- **Complexity Analysis**: Understanding Big O notation through practical examples

### Programming Concepts
- Function parameters and return values
- Loop structures and conditional logic
- Random number generation and manipulation
- User interaction and input validation

## Example Gameplay

### Interactive Mode
```
Number of tries left: 5
Guess a Number between 0 and 10: 5
Guess higher!
Number of tries left: 4
Guess a Number between 0 and 10: 8
You guessed the correct number!
```

### Linear Search Demo
```
The number for the program to guess: 7
Number of tries left 10
The program is guessing... 0
Number of tries left 9
The program is guessing... 1
...
The program guessed the correct Number
```

## Algorithm Efficiency Comparison

- **Linear Search**: O(n) - may need to check every number
- **Binary Search**: O(log n) - eliminates half the possibilities each guess
- **Interactive**: Depends on human strategy and luck

For a range of 1-100:
- Linear Search: Up to 100 guesses
- Binary Search: At most 7 guesses
- Human Player: Variable based on strategy

## Known Issues & Enhancements

### Current Issues
- Binary search function has hardcoded value (71) instead of random generation
- Some test cases are commented out
- Missing input validation for edge cases

### Potential Improvements
- Fix binary search random number generation
- Add input validation and error handling
- Implement GUI version for better user experience
- Add statistics tracking (average guesses, success rate)
- Include more search algorithms (interpolation search, exponential search)
- Add difficulty levels with different ranges

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Educational programming project demonstrating search algorithms and game development in Python.
