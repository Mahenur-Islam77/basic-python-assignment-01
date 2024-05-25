# 19. Write a program that generates a random number and allows the user to guess it.

import random

# Function to generate a random number within a specified range
def generate_random_number(start, end):
    return random.randint(start, end)

# Define the range for the random number
start_range = int(input("Enter a starting range: "))
end_range = int(input("Enter an end range: "))
    
# Generate the random number
random_number = generate_random_number(start_range, end_range)
    
# Prompt the user to guess the number
print(f"Guess the number between {start_range} and {end_range}: ")
guess = None
attempts = 0
    
# Loop until the correct number is guessed
while guess != random_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < random_number:
        print("Too low, try again!")
    elif guess > random_number:
        print("Too high, try again!")
    else:
        print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")
