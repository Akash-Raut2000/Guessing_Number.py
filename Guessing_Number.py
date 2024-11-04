import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Try a higher number.")
        elif guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")

print("Thank you for playing!")