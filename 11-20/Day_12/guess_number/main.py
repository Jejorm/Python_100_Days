from art import logo
from random import randint


def random_number():
    number = randint(1, 100)
    return number


def check_guess(number, guess, attempts):
    if number > guess:
        print("\nToo low.")
        if attempts != 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")

    elif number < guess:
        print("\nToo high.")
        if attempts != 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")

    else:
        print(f"\n\nYou got it! the answer was {number}.")
        win = True
        return win


def game(number, total_attempts):
    while True:
        print(f"\nYou have {total_attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        total_attempts -= 1
        win = check_guess(number, guess, total_attempts)

        if win == True or total_attempts == 0:
            break


continue_game = True

while continue_game:
    number = random_number()
    print(logo)
    print("\n\n\nWelcome to the Number Guessing Game!")
    print("\n\nI'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is: {number}")
    option = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

    if option == "easy":
        game(number, 10)
    elif option == "hard":
        game(number, 5)

    play_again = input("\n\nDo you want to play again? Type something to play or 'n' to exit: \n\n").lower()

    if play_again == 'n':
        print("\n\nGoodbye!")
        continue_game = False
