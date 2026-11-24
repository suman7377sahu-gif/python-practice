# We are going to write a program that generates a random number and asks the user to guess it. If the player’s guess is higher than the actual number, the program displays “Lower number please” . Similarly, if the user’s guess is too low, the program prints “Higher number please” . When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.


import random

target_number = random.randint(1, 100)
guess = 0
no_of_guesses = 0

print("------ Welcome to the Number Guessing Game ------")

while guess != target_number:

    try:
        guess = int(input("Guess a number (1-100): "))

        if guess < 1 or guess > 100:
            raise ValueError("Please enter a number between 1 and 100!")

    except ValueError as e:
        print("Invalid input:", e)
        continue

    no_of_guesses += 1

    if guess > target_number:
        print("Lower number please!")

    elif guess < target_number:
        print("Higher number please!")

    else:
        print(f"Congratulations! You guessed the number in {no_of_guesses} attempts!")
