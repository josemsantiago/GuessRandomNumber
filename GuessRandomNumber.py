import random


def guess_random_number(tries=0, start=0, stop=0):
    random_number = random.randint(start, stop)
    while tries > 0:
        print(f"Number of tries left: {tries}")
        guess = int(input(f"Guess a Number between {start} and {stop}: "))
        if random_number == guess:
            print(f"You guessed the correct number!")
            break
        elif random_number > guess:
            print(f"Guess higher!")
        elif random_number < guess:
            print(f"Guess lower!")
        tries -= 1
        if tries == 0:
            print(f"You have failed to guess the number: {random_number}")


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


def guess_random_number_binary_search(tries=0, start=0, stop=0):
    random_number =71
    print(f"Random number to find: {random_number}")
    while start <= stop and tries > 0:
        mid_value = (start + stop) // 2
        tries -= 1
        if mid_value == random_number:
            print(f"Found it! {random_number}")
            break
        elif mid_value < random_number:
            print(f"Guessing higher!")
            start = mid_value + 1
        else:
            print(f"Guessing lower!")
            stop = mid_value - 1
        if tries == 0:
            print(f"The Program has failed to guess the correct number")
            break

## Test Cases
##guess_random_number(5,0,10)
##guess_random_number_linear_search(5,0,10)
##guess_random_number_binary_search(5,0,100)

