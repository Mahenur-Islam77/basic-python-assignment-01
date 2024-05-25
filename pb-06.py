# 6. Write a program that determines if a number is even or odd.

# Function to determine if a number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Input: number to be checked
number = int(input("Enter a number: "))

# Determine if the number is even or odd
result = is_even_or_odd(number)

# Output: display the result
print(f"The number {number} is {result}.")
