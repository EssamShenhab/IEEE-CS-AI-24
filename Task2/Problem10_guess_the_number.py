import random

numbers = list(range(1, 101))
random.shuffle(numbers)
cpu_guess = numbers[0]
num_guesses = 0

while True:
    user_guess = input("Enter a numeric value (between 1 and 100): ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if 1 <= user_guess <= 100:
            num_guesses += 1
            if user_guess == cpu_guess:
                print(f"You are right!! You guessed the number in {num_guesses} guesses.")
                break
            elif user_guess < cpu_guess:
                print("Too low. Try again!")
            else:
                print("Too high. Try again!")
        else:
            print("Error: Enter a numeric value between 1 and 100")
    else:
        print("Error: Enter a numeric value between 1 and 100")
