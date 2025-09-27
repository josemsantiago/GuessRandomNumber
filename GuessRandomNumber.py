#!/usr/bin/env python3
"""
GuessRandomNumber - Number guessing game with multiple algorithms
Includes human guessing, linear search, and binary search implementations
"""

import random
import sys


def guess_random_number(tries=0, start=0, stop=0):
    """Human guessing game - player tries to guess a random number."""
    if tries <= 0 or start >= stop:
        print("Invalid parameters: tries must be > 0 and start < stop")
        return False

    random_number = random.randint(start, stop)
    original_tries = tries

    while tries > 0:
        print(f"Number of tries left: {tries}")
        try:
            guess = int(input(f"Guess a Number between {start} and {stop}: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted!")
            return False

        if random_number == guess:
            print(f"You guessed the correct number in {original_tries - tries + 1} tries!")
            return True
        elif random_number > guess:
            print(f"Guess higher!")
        elif random_number < guess:
            print(f"Guess lower!")
        tries -= 1

    print(f"You have failed to guess the number: {random_number}")
    return False


def guess_random_number_linear_search(tries=0, start=0, stop=0):
    random_number = random.randint(start, stop)
    print(f"The number for the program to guess: {random_number}")
    for i in range(start, stop):
        print(f"Number of tries left {tries}")
        print(f"The program is guessing... {i}")
        if i == random_number:
            print(f"The program guessed the correct Number")
            break
        tries -= 1
        if tries == 0:
            print(f"The Program has failed to guess the correct number")
            break


def guess_random_number_binary_search(tries=0, start=0, stop=0, target_number=None):
    """Binary search implementation to find a target number."""
    if tries <= 0 or start >= stop:
        print("Invalid parameters: tries must be > 0 and start < stop")
        return False

    random_number = target_number if target_number is not None else random.randint(start, stop)
    print(f"Random number to find: {random_number}")
    original_start, original_stop = start, stop

    while start <= stop and tries > 0:
        mid_value = (start + stop) // 2
        print(f"Trying: {mid_value}")
        tries -= 1

        if mid_value == random_number:
            print(f"Found it! {random_number}")
            return True
        elif mid_value < random_number:
            print(f"Guessing higher!")
            start = mid_value + 1
        else:
            print(f"Guessing lower!")
            stop = mid_value - 1

    print(f"The Program has failed to guess the correct number")
    return False

def display_menu():
    """Display the main game menu."""
    print("\n" + "="*40)
    print("GUESS THE NUMBER GAME")
    print("="*40)
    print("1. Human Guessing Game")
    print("2. Linear Search Demo")
    print("3. Binary Search Demo")
    print("4. Exit")
    print("="*40)

def get_game_parameters():
    """Get game parameters from user."""
    try:
        tries = int(input("Enter number of tries: "))
        start = int(input("Enter start number: "))
        stop = int(input("Enter stop number: "))
        return tries, start, stop
    except ValueError:
        print("Please enter valid numbers!")
        return None, None, None
    except (KeyboardInterrupt, EOFError):
        print("\nOperation cancelled!")
        return None, None, None

def main():
    """Main program entry point."""
    print("Welcome to the Number Guessing Game!")

    try:
        while True:
            display_menu()
            try:
                choice = input("Enter your choice (1-4): ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nThanks for playing!")
                break

            if choice == "1":
                print("\n--- Human Guessing Game ---")
                tries, start, stop = get_game_parameters()
                if tries is not None:
                    guess_random_number(tries, start, stop)

            elif choice == "2":
                print("\n--- Linear Search Demo ---")
                tries, start, stop = get_game_parameters()
                if tries is not None:
                    guess_random_number_linear_search(tries, start, stop)

            elif choice == "3":
                print("\n--- Binary Search Demo ---")
                tries, start, stop = get_game_parameters()
                if tries is not None:
                    guess_random_number_binary_search(tries, start, stop)

            elif choice == "4":
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

# Test Cases (uncomment to run)
# guess_random_number(5, 0, 10)
# guess_random_number_linear_search(5, 0, 10)
# guess_random_number_binary_search(5, 0, 100)

