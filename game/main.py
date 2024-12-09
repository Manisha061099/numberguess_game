import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 10.")

    
    number_to_guess = random.randint(1, 10)

    attempts = 0
    guessed = False

    while not guessed:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is too high, too low, or correct
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            guessed = True


number_guessing_game()
